"""Read numbered recipes without treating translated practice sets as new recipes."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LIBRARIES = (
    ('prompt-library.md', 1, 24, 'zh'),
    ('extended-scenarios.md', 25, 60, 'zh'),
    ('advanced-workflows.en.md', 61, 72, 'en'),
    ('creative-techniques.en.md', 73, 100, 'en'),
    ('genre-social-experiments.en.md', 101, 120, 'en'),
)

def slug(title):
    return re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')

def recipes(root=ROOT):
    result = []
    for filename, first, last, language in LIBRARIES:
        text = (root/'prompts'/filename).read_text()
        headings = list(re.finditer(r'^#{2,3} (\d+)\. (.+)$', text, re.M))
        ids = [int(m[1]) for m in headings]
        if ids != list(range(first, last+1)):
            raise ValueError(f'{filename}: expected unique ordered recipe IDs {first}–{last}; found {ids}')
        for i, m in enumerate(headings):
            section = text[m.end():headings[i+1].start() if i+1<len(headings) else len(text)]
            blocks = re.findall(r'^```text\n([\s\S]*?)\n```', section, re.M)
            if len(blocks) != 1 or not blocks[0].strip():
                raise ValueError(f'{filename}: recipe {m[1]} needs one complete text prompt')
            result.append(dict(id=int(m[1]),title=m[2],language=language,file=filename,
                               anchor=slug(m[1]+'. '+m[2]),prompt=blocks[0].strip()))
    return result

def validate_languages(root=ROOT):
    files = list((root/'prompts/i18n').glob('prompt-library.*.md'))
    if len(files) != 14:
        raise ValueError(f'Expected 14 language files, found {len(files)}')
    for path in files:
        text = path.read_text()
        headings = list(re.finditer(r'^## I18N-(\d+)\b.*$', text, re.M))
        if [int(m[1]) for m in headings] != list(range(1,7)):
            raise ValueError(f'{path.name}: expected shared scene IDs 01–06 once each')
        for i,m in enumerate(headings):
            section = text[m.end():headings[i+1].start() if i+1<len(headings) else len(text)]
            if not re.search(r'^```text\n\S[\s\S]*?\n```',section,re.M):
                raise ValueError(f'{path.name}: scene {m[1]} has no complete text prompt')

def download_outputs():
    files = {}
    index = '# Library prompt downloads / 主库提示词下载\n\n[Master index / 总目录](../README.md) · [Source and license / 来源与许可](../../docs/PROVENANCE.md)\n\n120 inherited recipes: 60 Chinese and 60 English. Files contain prompt text only; open the linked recipe for input requirements and settings. These are not verified Flyne AI render results. Use **Raw** or **Download raw file** to save a text file.\n\n120 条继承自主库的配方：60 条中文、60 条英文。文本文件只含提示词，素材和参数说明请查看对应场景。这些不是已验证的 Flyne AI 生成结果。打开文件后使用 **Raw** 或 **Download raw file** 保存。\n\n| ID | Recipe / 场景 | Language / 语言 | Download / 下载 |\n|---|---|---|---|\n'
    for r in recipes():
        name=f"{r['id']:03d}.{r['language']}.txt"
        files['prompts/downloads/'+name]=r['prompt']+'\n'
        language = '中文' if r['language']=='zh' else 'English'
        index+=f"| {r['id']:03d} | [{r['title']}](../{r['file']}#{r['anchor']}) | {language} | [TXT]({name}) |\n"
    files['prompts/downloads/README.md']=index
    return files
