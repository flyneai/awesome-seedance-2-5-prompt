#!/usr/bin/env python3
"""Render showcase pages and homepage selections from the source records."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    'products': ('Products and brands', '商品与品牌'),
    'people': ('People and everyday life', '人物与日常'),
    'tutorials': ('Tutorials and processes', '教程与制作过程'),
    'stories': ('Stories and visual effects', '故事与视觉特效'),
}

def category_index(entries, prefix='', chinese=False):
    text = '| 用途 | 案例 |\n|---|---|\n' if chinese else '| Browse by use | Cases |\n|---|---|\n'
    for group, labels in GROUPS.items():
        cases = [e for e in entries if e.get('browse_group') == group]
        if not cases:
            continue
        links = ' · '.join(f"[{e['id'].split('-')[0].upper()} · {e['title_zh'] if chinese else e['title']}]({prefix}#{e['id']})" for e in cases)
        text += f'| {labels[chinese]} | {links} |\n'
    return text

def replace_block(text, name, value):
    pattern = rf'<!-- BEGIN {name} -->[\s\S]*?<!-- END {name} -->'
    if len(re.findall(pattern, text)) != 1:
        raise ValueError(f'Expected exactly one {name} block')
    return re.sub(pattern, lambda _: f'<!-- BEGIN {name} -->\n{value}\n<!-- END {name} -->', text)

def starter_prompts(language):
    chinese = language == 'zh'
    text = ('## 直接复制：三个新手练习\n\n这些中英双语练习未实测，不计入主库的 120 条配方。时长和画幅是创作目标，请按页面实际选项调整。\n' if chinese else '## Copy a starter prompt\n\nThree bilingual practice briefs, not render-tested and not counted among the 120 library recipes. Duration and ratio are creative targets; adapt them to the options available in your account.\n')
    for e in json.loads((ROOT/'docs/starter-prompts.json').read_text()):
        title = e['title_zh'] if chinese else e['title']
        inputs = e['inputs_zh'] if chinese else e['inputs']
        format_note = e['format_zh'] if chinese else e['format']
        other = 'README.md' if chinese else 'README_ZH.md'
        label = 'English version' if chinese else '中文版'
        text += f'\n<a id="{e["id"]}"></a>\n\n<details>\n<summary>{title} · {inputs}</summary>\n\n**{format_note}** · [{label}]({other}#{e["id"]})\n\n```text\n{e[language]}\n```\n\n</details>\n'
    return text.rstrip()

def outputs():
    entries = json.loads((ROOT/'docs/x-showcase-sources.json').read_text())['entries']
    page = '# Seedance 2.5 community video gallery\n\n[Home](../README.md) · [来源说明 / Source notes](x-showcase-sources.md) · [新增案例中文说明](community-videos.zh.md)\n\n'
    page += f'{len(entries)} source-linked examples. **Author prompts are on X; the copyable blocks below are untested editorial adaptations, not the prompts that produced these videos.** Model attribution is the posting account\'s claim. Uploaded dimensions are not generation settings.\n\n'
    page += category_index(entries) + '\n[Download individual practice prompts](../prompts/community/README.md). These are separate from the 120 numbered recipes.\n\n'
    page += '| Case | Category | Author prompt |\n|---|---|---|\n'
    for e in entries:
        page += f"| [{e['id'].split('-')[0].upper()} · {e['title']}](#{e['id']}) | {e['category']} | [@{e['posted_by']}]({e['full_prompt_url']}) |\n"
    for e in entries:
        media=e['published_media'];check=e['media_check']
        page += f'''\n<a id="{e['id']}"></a>

## {e['id'].split('-')[0].upper()} · {e['title']}

[![{e['title']} — @{e['posted_by']}]({e['thumbnail_url']})]({e['video_url']})

[▶ Watch video]({e['video_url']}) · [Author's full source prompt on X]({e['full_prompt_url']}) · **@{e['posted_by']}**, {e['post_date']}

**What to study:** {e['lesson']}

**Inputs:** {e['inputs']}

**Source format:** {e['format_note']} Uploaded duration: {media['duration_seconds']} seconds.

Source text checked: {e['source_checked_on']}. Media headers checked: {check['checked_on']}; video HTTP {check.get('video_http_status', 'unknown')}, thumbnail HTTP {check.get('thumbnail_http_status','unknown')}. Header checks are not playback tests. [Verification method](x-showcase-sources.md).
'''
        if e['source_excerpt']:page+=f"\n**Short source excerpt:** {e['source_excerpt']}\n"
        page+=f'''\n<details>
<summary>Copy editorial practice prompt — not render-tested</summary>

This variant did not produce the linked video. Adapt the duration to your provider or split it into shots.

[Open plain-text practice prompt](../prompts/community/{e['id']}.en.txt) — use GitHub's **Raw** or **Download raw file** control to save it.

```text
{e['adaptation']}
```

</details>
'''
    page+='\nVideos and thumbnails stay on the original host and are excluded from MIT. If a media link fails, use the author\'s source post. See [source notes](x-showcase-sources.md) for attribution corrections and removal requests.\n'
    translated=[e for e in entries if e['adaptation_zh']]
    chinese='# 新增 X 视频案例：中文说明与练习提示词\n\n[中文首页](../README_ZH.md) · [全部案例](community-videos.md) · [来源记录](x-showcase-sources.md)\n\n以下中文提示词翻译自本仓库的英文改写版，不是作者原提示词，也未实测生成。视频仍为作者发布的版本，完整原提示词请查看 X 原帖。\n'
    chinese += '\n' + category_index(translated, chinese=True)
    for e in translated:
        chinese+=f'''\n<a id="{e['id']}"></a>

## {e['id'].split('-')[0].upper()} · {e['title_zh']}

[![{e['title_zh']}]({e['thumbnail_url']})]({e['video_url']})

[观看视频]({e['video_url']}) · [作者原帖及原提示词]({e['original_post']}) · [英文说明](community-videos.md#{e['id']})

**值得学习：** {e['lesson_zh']}

**需要的素材：** {e['inputs_zh']}

**画幅与时长：** {e['format_note_zh']}

<details>
<summary>复制中文练习提示词（未实测）</summary>

[打开纯文本提示词](../prompts/community/{e['id']}.zh.txt)，可使用 GitHub 的 **Raw** 或 **Download raw file** 保存。

```text
{e['adaptation_zh']}
```

</details>
'''
    featured=f'Browse [all {len(entries)} cases](docs/community-videos.md). These three are starting points for different creative tasks.\n\n| Example | Preview | Study |\n|---|---|---|\n'
    for e in entries:
        if e['featured']:
            featured+=f"| [{e['title']}](docs/community-videos.md#{e['id']}) | [![{e['title']}]({e['thumbnail_url']})]({e['video_url']}) | {e['category']} |\n"
    # Keep old inbound README anchors functional after moving full cases.
    featured+='\n<details>\n<summary>Case index — including links from earlier versions</summary>\n\n'
    for e in entries:featured+=f'<a id="{e["id"]}"></a>\n\n[{e["id"].split("-")[0].upper()} · {e["title"]}](docs/community-videos.md#{e["id"]})\n\n'
    featured+='</details>'
    readme=(ROOT/'README.md').read_text()
    readme=replace_block(readme,'CASE BADGE',f'[![Prompts](https://img.shields.io/badge/Prompts-120-blue.svg)](prompts/README.md) [![X video examples](https://img.shields.io/badge/X_video_examples-{len(entries)}-black.svg)](docs/community-videos.md) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)')
    readme=replace_block(readme,'FEATURED CASES',featured)
    readme=replace_block(readme,'STARTER PROMPTS',starter_prompts('en'))
    zh_summary=f'共 **{len(entries)} 个 X 视频案例**，其中 **{len(translated)} 个新增案例**已提供中文说明和中文练习提示词。\n\n[查看全部视频（英文说明）](docs/community-videos.md) · [阅读新增案例中文提示词](docs/community-videos.zh.md)\n\n| 新增案例 | 中文说明与练习提示词 |\n|---|---|\n'
    for e in translated:
        zh_summary+=f"| {e['title_zh']} | [查看](docs/community-videos.zh.md#{e['id']}) |\n"
    zh_readme=replace_block((ROOT/'README_ZH.md').read_text(),'ZH CASES',zh_summary.rstrip())
    zh_readme=replace_block(zh_readme,'STARTER PROMPTS',starter_prompts('zh'))
    files = {'docs/community-videos.md':page,'docs/community-videos.zh.md':chinese,'README.md':readme,'README_ZH.md':zh_readme}
    downloads = '# Community practice prompts / 社区案例练习提示词\n\n[Video gallery / 视频案例](../../docs/community-videos.md) · [120 recipes / 主提示词库](../README.md)\n\nThese files contain only our editorial practice text, not the source video prompts. None has been render-tested. Open a file, then use **Raw** or **Download raw file** to copy or save it. Attribution and source links stay in the gallery.\n\n这些文件只含本仓库改写的练习提示词，不是生成原视频的提示词，均未实测。打开文件后，可用 **Raw** 或 **Download raw file** 复制或保存。作者和原帖链接见视频案例页。\n\n| Case / 案例 | English | 中文 |\n|---|---|---|\n'
    for e in entries:
        stem = e['id']
        files[f'prompts/community/{stem}.en.txt'] = e['adaptation'].strip() + '\n'
        zh_link = '—'
        if e['adaptation_zh']:
            files[f'prompts/community/{stem}.zh.txt'] = e['adaptation_zh'].strip() + '\n'
            zh_link = f'[TXT]({stem}.zh.txt)'
        downloads += f"| [{stem.split('-')[0].upper()} · {e['title']}](../../docs/community-videos.md#{stem}) | [TXT]({stem}.en.txt) | {zh_link} |\n"
    files['prompts/community/README.md'] = downloads
    return files

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    stale=[]
    for name,text in outputs().items():
        path=ROOT/name
        if args.check:
            if not path.exists() or path.read_text()!=text:stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
    if stale:raise SystemExit('Generated content is stale: '+', '.join(stale))
    print('Showcase pages are current.' if args.check else 'Showcase pages generated.')

if __name__=='__main__':main()
