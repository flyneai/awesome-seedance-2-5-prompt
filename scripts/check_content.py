#!/usr/bin/env python3
"""Check local Markdown links, showcase records and optional public media headers."""
import argparse
import concurrent.futures
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

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
    result = subprocess.run(['curl', '--head', '--location', '--silent', '--show-error',
                             '--max-time', '25', '--output', '/dev/null',
                             '--write-out', '%{http_code}\t%{content_type}', url],
                            capture_output=True, text=True, timeout=30)
    code, _, content_type = result.stdout.strip().partition('\t')
    return {'http_status': int(code or 0), 'content_type': content_type,
            'error': result.stderr.strip() if result.returncode else None}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check-media', action='store_true', help='Read live headers; does not rewrite historical records.')
    args = parser.parse_args()
    errors = []
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = re.sub(r'```[\s\S]*?```', '', path.read_text())
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
    readme = (ROOT/'README.md').read_text()
    if len({e['post_id'] for e in entries}) != len(entries):
        errors.append('Duplicate X status IDs')
    for e in entries:
        for key in ('id','posted_by','original_post','full_prompt_url','prompt_location','model_label','model_evidence','video_url','thumbnail_url','published_media','media_check'):
            if not e.get(key):
                errors.append(f"{e.get('id')}: missing {key}")
        if e['original_post'] != f"https://x.com/{e['posted_by']}/status/{e['post_id']}":
            errors.append(f"{e['id']}: inconsistent author/status URL")
        if e['id'] not in anchors(ROOT/'README.md'):
            errors.append(f"{e['id']}: missing showcase anchor")
        for key in ('video_url','thumbnail_url','original_post'):
            if e[key] not in readme:
                errors.append(f"{e['id']}: {key} absent from README")
    if f'X_video_examples-{len(entries)}-' not in readme:
        errors.append('README badge count differs from source records')
    if args.check_media:
        jobs = [(e['id'],kind,e[kind+'_url']) for e in entries for kind in ('video','thumbnail')]
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(media_header,[job[2] for job in jobs]))
        for (case,kind,_), result in zip(jobs,results):
            expected = 'video/' if kind == 'video' else 'image/'
            if result['http_status'] != 200 or not result['content_type'].startswith(expected):
                errors.append(f'{case} {kind}: {result}')
        print(f'Checked {len(jobs)} live media headers; historical records unchanged.')
    if errors:
        print('\n'.join(errors),file=sys.stderr)
        return 1
    print(f'PASS: local links, anchors and {len(entries)} unique X cases.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
