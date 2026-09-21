#!/usr/bin/env python3
"""Check local Markdown links, showcase records and optional public media headers."""
import argparse
import concurrent.futures
import json
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def linked_ratios(text):
    """Return table rows where an aspect-ratio value became a recipe link."""
    columns = []
    bad = []
    for line in text.splitlines():
        if not line.startswith('|'):
            columns = []
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        header = [i for i,c in enumerate(cells) if c in ('推荐画幅', '常用画幅', 'Aspect ratio', 'Ratio')]
        if header:
            columns = header
        elif any(i < len(cells) and re.search(r'\[\d+(?:\.\d+)?\]\([^)]*prompts/', cells[i]) for i in columns):
            bad.append(line)
    return bad

def anchors(path):
    text = path.read_text()
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    seen = {}
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug + (f'-{count}' if count else ''))
    return result

def media_header(url):
    try:
        result = subprocess.run(['curl', '--head', '--location', '--silent', '--show-error',
                             '--max-time', '25', '--output', '/dev/null',
                             '--write-out', '%{http_code}\t%{content_type}', url],
                                capture_output=True, text=True, timeout=30)
    except (subprocess.TimeoutExpired, OSError) as exc:
        return {'http_status': 0, 'content_type': '', 'error': str(exc)}
    code, _, content_type = result.stdout.strip().partition('\t')
    return {'http_status': int(code or 0), 'content_type': content_type,
            'error': result.stderr.strip() if result.returncode else None}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check-media', action='store_true', help='Read live headers; does not rewrite historical records.')
    parser.add_argument('--media-report', type=Path, help='Write live media results as JSON; requires --check-media.')
    args = parser.parse_args()
    if args.media_report and not args.check_media:
        parser.error('--media-report requires --check-media')
    errors = []
    from library_catalog import recipes, validate_languages
    try:
        recipes()
        validate_languages()
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = re.sub(r'```[\s\S]*?```', '', path.read_text())
        if linked_ratios(text):
            errors.append(f'{path.relative_to(ROOT)}: aspect-ratio numbers must not link to recipes')
        for target in re.findall(r'\]\(([^\s)]+)', text):
            parts = urlsplit(target)
            if parts.scheme or target.startswith('//'):
                continue
            local = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not local.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing {target}')
            elif parts.fragment and local.suffix == '.md' and unquote(parts.fragment) not in anchors(local):
                errors.append(f'{path.relative_to(ROOT)}: missing anchor {target}')
    data = json.loads((ROOT/'docs/x-showcase-sources.json').read_text())
    entries = data['entries']
    from build_showcase import GROUPS, outputs
    readme = (ROOT/'README.md').read_text()
    gallery = (ROOT/'docs/community-videos.md').read_text()
    if data.get('schema_version') != 2:
        errors.append('Expected case schema_version 2')
    if len({e['id'] for e in entries}) != len(entries):
        errors.append('Duplicate case IDs')
    if len({e['post_id'] for e in entries}) != len(entries):
        errors.append('Duplicate X status IDs')
    for e in entries:
        if e.get('browse_group') not in GROUPS:
            errors.append(f"{e.get('id')}: invalid browse_group")
        for key in ('id','title','title_zh','category','inputs','lesson','adaptation','source_checked_on','retrieval_url','case_path','render_test_status','posted_by','original_post','full_prompt_url','prompt_location','model_label','model_evidence','video_url','thumbnail_url','published_media','media_check'):
            if not e.get(key):
                errors.append(f"{e.get('id')}: missing {key}")
        if e['original_post'] != f"https://x.com/{e['posted_by']}/status/{e['post_id']}":
            errors.append(f"{e['id']}: inconsistent author/status URL")
        for key in ('adaptation_zh','lesson_zh','inputs_zh','format_note_zh','source_excerpt','featured'):
            if key not in e:
                errors.append(f"{e['id']}: missing shared field {key}")
        if e.get('adaptation_zh') and not all(e.get(k) for k in ('lesson_zh','inputs_zh','format_note_zh')):
            errors.append(f"{e['id']}: incomplete Chinese case")
        if e.get('render_test_status') not in ('not_tested', 'tested'):
            errors.append(f"{e['id']}: invalid render_test_status")
        if e.get('render_test_status') == 'tested':
            report=e.get('render_test_report')
            if not report or not (ROOT/report).is_file():
                errors.append(f"{e['id']}: tested cases require a local render report for human review")
        if e['id'] not in anchors(ROOT/'docs/community-videos.md'):
            errors.append(f"{e['id']}: missing showcase anchor")
        for key in ('video_url','thumbnail_url','original_post'):
            if e[key] not in gallery:
                errors.append(f"{e['id']}: {key} absent from gallery")
    if f'X_video_examples-{len(entries)}-' not in readme:
        errors.append('README badge count differs from source records')
    generated = outputs()
    for folder in ('prompts/community', 'prompts/downloads'):
        for path in (ROOT/folder).rglob('*'):
            if path.is_file() and str(path.relative_to(ROOT)) not in generated:
                errors.append(f'{path.relative_to(ROOT)}: unexpected generated file; review and remove stale downloads')
    for name, expected in generated.items():
        if not (ROOT/name).is_file() or (ROOT/name).read_text() != expected:
            errors.append(f'{name}: generated content is stale; run scripts/build_showcase.py')
    if args.check_media:
        jobs = [(e['id'],kind,e[kind+'_url']) for e in entries for kind in ('video','thumbnail')]
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(media_header,[job[2] for job in jobs]))
        for (case,kind,_), result in zip(jobs,results):
            expected = 'video/' if kind == 'video' else 'image/'
            if result['http_status'] != 200 or not result['content_type'].startswith(expected):
                errors.append(f'{case} {kind}: {result}')
        if args.media_report:
            args.media_report.parent.mkdir(parents=True, exist_ok=True)
            report={'checked_at': datetime.now(timezone.utc).isoformat(), 'method':'curl HTTP HEAD',
                    'results':[{'case':case,'kind':kind,'url':url,**result} for (case,kind,url),result in zip(jobs,results)]}
            args.media_report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        print(f'Checked {len(jobs)} live media headers; historical records unchanged.')
    if errors:
        print('\n'.join(errors),file=sys.stderr)
        return 1
    print(f'PASS: 120 recipe IDs and prompt blocks, 14 six-scene language files, local links, generated files and {len(entries)} unique X cases.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
