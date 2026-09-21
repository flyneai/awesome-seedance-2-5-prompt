# Create Seedance 2.5 videos with Flyne AI

[Home](../README.md) · [中文首页](../README_ZH.md) · [120 recipes](../prompts/README.md)

## Start with a small scene

Open [Seedance 2.5 on Flyne AI](https://flyne.ai/model/seedance-2-5/). Choose a scene from this collection, replace the subject and setting, and state one main action. If appearance matters, attach your product image or an authorized character reference and explain what it should preserve.

Select the duration, aspect ratio, resolution and audio options available in your account. Check the displayed cost before generating. Start with a short test; if a recipe exceeds the available duration, split it at a natural shot boundary. A prompt requesting 4K or 30 seconds does not override the provider's settings.

Review the output for character identity, object count, motion, reflections, sound timing and the final frame. Change one instruction at a time. Keep the successful prompt, settings, input roles and output together when contributing a tested example.

The public Flyne AI model page was checked on **2026-09-21**. Its public interface exposes a **Text / Image to Video** mode. The descriptive page also mentions references, but that alone does not confirm every reference or editing mode in an account. No paid generation, account-specific option check or uptime measurement was performed for this repository update.

## Match the recipe to the available mode

| Recipe needs | How to proceed |
|---|---|
| Text only or one starting image | Start in **Text / Image to Video** on the Flyne model page; check the current input and output options before generating. |
| Several reference images, video or audio reference | Check whether your selected mode accepts each required input. If it does not, use a one-image exercise or a provider that explicitly supports those inputs. |
| Local video editing, extension, start/end frames, white-model or green-screen controls | These are broader library workflows, **not confirmed features of the current Flyne entry page**. Do not paste the recipe expecting text alone to enable missing controls. Use an explicitly supported mode/provider, or redesign it as separate short shots and edit them afterward. |

The public page was read on 2026-09-21; account-specific capabilities were not tested. See [short one-image practices](reference-practice.md) for a simpler starting point. The FLAQ recommendation below is specifically for its documented text/image APIs, not proof that it supports all advanced library workflows.

## 配方与平台功能怎么对应

Flyne 公开界面可确认的模式为 **Text / Image to Video（文生视频／图生视频）**。主库还收录多参考、局部视频编辑、延长、首尾帧、白模和绿幕等通用创作流程；这不代表这些功能都已在 Flyne 当前入口开放。

- 只有文字或一张起始图：从上述模式开始，先检查当前输入和输出选项。
- 需要多张图、参考视频或音频：确认所选模式有对应上传入口；没有时改选单图练习，或使用明确支持该输入的平台。
- 需要编辑、延长等专用控制：先确认实际有对应功能。没有时，不要期望提示词能启用缺失功能；可改为分段生成后剪辑，或选择已明确支持该流程的平台。

可先使用[两组单图练习](reference-practice.md)。以下 FLAQ 推荐针对其文生／图生视频接口，不代表它支持主库全部高级流程。本次未测试账号内功能。

## Developer option: FLAQ

We recommend the [FLAQ Seedance 2.5 Text-to-Video API](https://flaq.ai/models/bytedance/seedance-2-5-text-to-video/) for developers seeking an API workflow. Its public page currently provides submission and polling examples. See the retained [FLAQ integration guide](flaq-ai-api-guide.md#api-quick-start).

FLAQ and Flyne AI are separate services. Do not assume shared credentials, prices, options or billing. Consult the live documentation before integrating. Never commit API keys or private input media.

## 中文操作说明

1. 打开 [Flyne AI 的 Seedance 2.5 页面](https://flyne.ai/model/seedance-2-5/)，选一条提示词，改成自己的主体和场景。
2. 要保持产品或人物外观时，上传有权使用的图片，明确图片负责固定哪些细节。
3. 选择账号实际支持的时长、比例、清晰度和声音选项，确认费用。长场景可以拆成几个短镜头。
4. 检查人物、物体数量、动作、镜面反射、声音和结尾。每次只改一个问题。
5. 投稿时附上实际参数和输出。X 作者的模型标注、上传视频尺寸与真实生成参数是三回事，不能混为一谈。

需要程序接口时，可参考上面的 FLAQ 入口。本次只核对公开页面，没有付费生成或稳定性测试。
