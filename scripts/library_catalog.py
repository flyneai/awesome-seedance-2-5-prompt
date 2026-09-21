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
                               anchor=slug(m[1]+'. '+m[2]),prompt=blocks[0].strip(),
                               settings=section.split('```text', 1)[0].strip()))
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
    index = '# Library prompt downloads / 主库提示词下载\n\n[Master index / 总目录](../README.md) · [Source and license / 来源与许可](../../docs/PROVENANCE.md)\n\n120 inherited recipes: 60 Chinese and 60 English. TXT files contain prompt text only. Each Guide file preserves the recipe settings and source link; save it with the TXT when sharing. These are not verified Flyne AI render results. Use **Raw** or **Download raw file** to save a text file.\n\n120 条继承自主库的配方：60 条中文、60 条英文。TXT 只含提示词；每条配方另附说明文件，保留参数和来源链接，转发时建议一起保存。这些不是已验证的 Flyne AI 生成结果。打开文件后使用 **Raw** 或 **Download raw file** 保存。\n\n| ID | Recipe / 场景 | Language / 语言 | Download / 下载 |\n|---|---|---|---|\n'
    for r in recipes():
        name=f"{r['id']:03d}.{r['language']}.txt"
        files['prompts/downloads/'+name]=r['prompt']+'\n'
        guide=f"{r['id']:03d}.{r['language']}.md"
        source=f"../{r['file']}#{r['anchor']}"
        public=f"https://github.com/flyneai/awesome-seedance-2-5-prompt/blob/main/prompts/{r['file']}#{r['anchor']}"
        settings=re.sub(r'\]\((?![a-z]+:|#)([^)]+)\)', lambda m: '](../'+m[1]+')', r['settings'])
        files['prompts/downloads/'+guide]=f'''# {r['id']:03d} · {r['title']}

[Prompt TXT / 提示词正文]({name}) · [Recipe / 场景原页]({source}) · [Online source / 在线来源]({public})

## Recipe settings / 配方参数

{settings}

These are the recipe's creative targets, not verified account settings or render results. Read the prompt's opening instructions for required input files and their roles. Replace project-specific assets and text before use; check that your provider supports every required input and mode. No input assets are bundled with this text file unless the recipe links them explicitly.

以上是配方的创作目标，不是已验证的账号设置或生成结果。所需素材及其作用见提示词开头；使用前替换为自己的素材与文字，并确认平台支持所需输入和模式。除非场景原页明确附有链接，否则下载文本不包含输入素材。

[Platform mode guide / 平台功能对照](../../docs/flyne-ai-guide.md#match-the-recipe-to-the-available-mode) · [Source and license / 来源与许可](../../docs/PROVENANCE.md)

Keep this note with the TXT when sharing. 转发 TXT 时，请同时保留本说明。
'''
        language = '中文' if r['language']=='zh' else 'English'
        index+=f"| {r['id']:03d} | [{r['title']}](../{r['file']}#{r['anchor']}) | {language} | [TXT]({name}) · [说明 / Guide]({guide}) |\n"
    files['prompts/downloads/README.md']=index
    return files
