# Maintain the collection / 维护方法

[Home](../README.md) · [Contribution guide](../CONTRIBUTING.md)

## One source for community cases

Edit `docs/x-showcase-sources.json`, then run:

```sh
python3 scripts/build_showcase.py
python3 scripts/check_content.py
python3 scripts/build_showcase.py --check
```

The JSON records generate the complete gallery, Chinese adaptations, category navigation, plain-text downloads, homepage selections, case counts and Chinese case table. Set `browse_group` to `products`, `people`, `tutorials` or `stories`; the generation script holds their English and Chinese display names. Files under `prompts/community/` are generated, not independently maintained. Do not edit generated sections by hand. Keep original source IDs and dates. Every case uses the same fields; leave a translation empty until it is actually written. `featured` selects homepage cards. `render_test_status` stays `not_tested` until a documented reproduction exists.

The `readme_anchor` field retains the original ID for old links; `case_path` identifies the current full case. README compatibility links remain available in the collapsed case index.

## Homepage starter prompts

Edit `docs/starter-prompts.json` to update the three bilingual beginner exercises. The same generation command updates their English and Chinese homepage blocks; content checks detect stale copies. These exercises are separate from the 120 inherited recipes and remain untested until actual render evidence is supplied. Keep input requirements and timing aligned across languages.

## Library downloads and structural checks

The five numbered library files remain the source for all 120 recipe downloads under `prompts/downloads/`. Run the same generator after editing a recipe. Each TXT has a companion Markdown note containing the recipe’s pre-prompt instructions, settings and an online source link; share both files when context matters. The checker requires IDs 01–120 exactly once and in order across their assigned files, a complete prompt block for each recipe, and six shared scenes in each of the 14 language files. These structural checks do not certify translation accuracy or render quality.

The checker also flags files under the generated download directories that no longer appear in the source records. Review and remove those obsolete files explicitly; generation never silently deletes them. Per-case test labels and homepage test counts follow `render_test_status`, with a report link for tested entries. Reports still need human review.

## Separate media checks

```sh
python3 scripts/check_content.py --check-media --media-report /tmp/flyne-media-report.json
```

The **Media link checks** GitHub workflow runs when source records change and can also be started manually from Actions. It uploads a dated report even when links fail. It does not rewrite historical verification dates or delete entries automatically. Network failures, rate limits and expired links need human review; use the original X URL as the fallback.

The content check runs separately, so an external host outage does not masquerade as a broken repository structure. It validates local links, shared case fields, counts and generated-page consistency. Neither check proves that a video plays correctly or that a prompt reproduces it.

## Review before adding a case

- Require an explicit Seedance 2.5 statement, a video and a recoverable prompt.
- Compare the original prompt's requested format with the uploaded file metadata.
- Preserve credits and distinguish author wording from an editorial adaptation.
- Favor a new practical use or creator over another near-duplicate scene.
- Record changed or removed entries in the changelog.

## 中文维护步骤

1. 在 JSON 来源文件中新增或更新案例，填写作者、原帖、视频、缩略图、分类、素材要求和检查日期。
2. 运行上面的生成命令，英文案例页、中文改写页和首页数量会一起更新。
3. 运行内容检查；需要检查视频是否还能访问时，单独运行媒体检查。
4. 媒体异常报告只表示这次访问结果。核实原因后再修改历史记录，不要因一次失败就删除案例。
5. 有实际生成记录后，按 [实测清单](render-testing.md) 提交证据；不能只把状态改成“已测试”。

## Repository sidebar

The current repository description still advertises “600+”. An administrator should replace it with:

> Seedance 2.5 prompts by Flyne AI: 120 recipes, source-linked X video examples, multilingual starter prompts, and practical creation guides.

The maintainers' content workflow cannot change repository settings without the necessary GitHub permission. Update the sidebar count when the collection grows.
