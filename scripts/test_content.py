"""Regression checks for catalog integrity and generated artifacts."""
import contextlib
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

import build_showcase
import check_content
from library_catalog import ROOT, recipes, validate_languages, download_outputs


class ContentRegressionTests(unittest.TestCase):
    def test_companion_notes_preserve_settings_and_rebase_links(self):
        files = download_outputs()
        self.assertIn('**Duration:** 20 seconds', files['prompts/downloads/061.en.md'])
        self.assertIn('../../assets/modular-lamp/README.md', files['prompts/downloads/100.en.md'])
        self.assertIn('https://github.com/flyneai/', files['prompts/downloads/061.en.md'])
        self.assertNotIn('Recipe settings', files['prompts/downloads/061.en.txt'])

    def test_ratio_values_are_not_recipe_links(self):
        text = '| 用途 | 推荐画幅 |\n|---|---|\n| 短片 | [9](../prompts/a.md):[16](../prompts/b.md) |'
        self.assertEqual(len(check_content.linked_ratios(text)), 1)
        valid = '| 场景 | 常用画幅 |\n|---|---|\n| [09](../prompts/a.md) | 9:16 / 2.39:1 |'
        self.assertEqual(check_content.linked_ratios(valid), [])

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT/'prompts', self.root/'prompts')

    def test_duplicate_recipe_id_is_rejected(self):
        path = self.root/'prompts/prompt-library.md'
        path.write_text(path.read_text().replace('### 02.', '### 01.', 1))
        with self.assertRaisesRegex(ValueError, 'unique ordered recipe IDs'):
            recipes(self.root)

    def test_missing_prompt_block_is_rejected(self):
        path = self.root/'prompts/advanced-workflows.en.md'
        path.write_text(path.read_text().replace('```text', '```', 1))
        with self.assertRaisesRegex(ValueError, 'complete text prompt'):
            recipes(self.root)

    def test_missing_language_scene_is_rejected(self):
        path = self.root/'prompts/i18n/prompt-library.en.md'
        path.write_text(path.read_text().replace('## I18N-06', '## Removed-06', 1))
        with self.assertRaisesRegex(ValueError, 'scene IDs'):
            validate_languages(self.root)

    def test_removed_case_download_is_reported(self):
        # Full temporary copy makes the real checker exercise its stale-file path.
        for name in ['docs', 'assets']:
            shutil.copytree(ROOT/name, self.root/name)
        for path in ROOT.glob('*.md'):
            shutil.copy(path,self.root/path.name)
        shutil.copy(ROOT/'LICENSE',self.root/'LICENSE')
        extra=self.root/'prompts/community/removed-case.en.txt'
        extra.write_text('Former case text\n')
        err=io.StringIO()
        with patch.object(check_content,'ROOT',self.root), patch.object(sys,'argv',['check_content.py']), contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            result=check_content.main()
        self.assertEqual(result,1)
        self.assertIn('removed-case.en.txt: unexpected generated file',err.getvalue())

    def test_tested_case_gets_report_links_and_count(self):
        shutil.copytree(ROOT/'docs',self.root/'docs')
        for name in ['README.md','README_ZH.md']:
            shutil.copy(ROOT/name,self.root/name)
        path=self.root/'docs/x-showcase-sources.json'
        data=json.loads(path.read_text())
        data['entries'][0].update(render_test_status='tested',render_test_report='docs/tests/example.md')
        path.write_text(json.dumps(data))
        with patch.object(build_showcase,'ROOT',self.root):
            pages=build_showcase.outputs()
        self.assertIn('[Read report](../docs/tests/example.md)',pages['docs/community-videos.md'])
        self.assertIn('[查看报告](../docs/tests/example.md)',pages['docs/community-videos.zh.md'])
        self.assertIn('**1/19**',pages['README.md'])
        self.assertIn('**1/19**',pages['README_ZH.md'])
        self.assertIn('Not render-tested',pages['docs/community-videos.md'])


if __name__=='__main__':
    unittest.main()
