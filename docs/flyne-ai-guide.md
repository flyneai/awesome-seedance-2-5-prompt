# Create Seedance 2.5 videos with Flyne AI

[Home](../README.md) · [中文首页](../README_ZH.md) · [120 recipes](../prompts/README.md)

## Start with a small scene

Open [Seedance 2.5 on Flyne AI](https://flyne.ai/model/seedance-2-5/). Choose a scene from this collection, replace the subject and setting, and state one main action. If appearance matters, attach your product image or an authorized character reference and explain what it should preserve.

Select the duration, aspect ratio, resolution and audio options available in your account. Check the displayed cost before generating. Start with a short test; if a recipe exceeds the available duration, split it at a natural shot boundary. A prompt requesting 4K or 30 seconds does not override the provider's settings.

Review the output for character identity, object count, motion, reflections, sound timing and the final frame. Change one instruction at a time. Keep the successful prompt, settings, input roles and output together when contributing a tested example.

The public Flyne AI model page was checked on **2026-09-21**. It describes text, image and reference workflows. No paid generation, account-specific option check or uptime measurement was performed for this repository update.

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
