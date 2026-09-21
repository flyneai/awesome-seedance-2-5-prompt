# Flyne AI · Seedance 2.5 视频提示词库

[English](README.md) · [简体中文](README_ZH.md) · [其他语言](prompts/i18n/README.md)

[![Flyne AI：产品、人物与故事](assets/flyne-seedance-banner.jpg)](https://flyne.ai/model/seedance-2-5/)

**选一个场景，复制提示词，在 Flyne AI 做出自己的版本。**

基于 [FLAQ 开源项目](docs/PROVENANCE.md) 改编，保留 120 条完整配方，适合商品展示、人物短片、社交视频和剧情创作。上图为品牌宣传插画，不是 Seedance 生成的视频截图。

[**前往 Flyne AI →**](https://flyne.ai/model/seedance-2-5/) · [120 条提示词目录](prompts/README.md) · [视频案例](docs/community-videos.md) · [提交提示词](https://github.com/flyneai/awesome-seedance-2-5-prompt/issues/new?template=prompt.yml)

## 第一次使用

1. **先选简单场景。** 例如产品缓慢转动、人物一个动作或一个简短情节。
2. **换成自己的内容。** 替换主体、场景和动作；需要固定外观时，上传自己的产品图或已获授权的人物照片。
3. **打开生成页面。** 文生视频和图生视频都在 [Flyne AI 的同一个 Seedance 2.5 页面](https://flyne.ai/model/seedance-2-5/)使用，在页面内选择实际支持的模式和素材。
4. **确认参数再生成。** 检查时长、比例、清晰度、声音和费用。长提示词可以拆成几个短镜头。
5. **检查结果。** 先看人物与产品有没有变形、物体数量是否正确、动作和声音是否自然，每次只改一个问题。

[详细操作说明](docs/flyne-ai-guide.md)

## 按用途选择

| 想做什么 | 从哪里开始 | 准备什么 |
|---|---|---|
| 商品广告、上新短片 | [基础场景库](prompts/prompt-library.md) | 清楚的产品图、不能改变的产品细节 |
| 人物介绍、社交短片 | [扩展场景库](prompts/extended-scenarios.md) | 已获授权的人像或虚构人物描述 |
| 剧情、动画、奇幻短片 | [类型片与视觉实验](prompts/genre-social-experiments.en.md) | 一个核心情节、固定角色、明确结尾 |
| 教程、转场、系列视频 | [创作技巧库](prompts/creative-techniques.en.md) | 分镜安排及用途清楚的参考素材 |

## 社区视频与提示词

<!-- BEGIN ZH CASES -->
共 **18 个 X 视频案例**，其中 **6 个新增案例**已提供中文说明和中文练习提示词。

[查看全部视频](docs/community-videos.md) · [阅读新增案例中文提示词](docs/community-videos.zh.md)

| 新增案例 | 中文说明与练习提示词 |
|---|---|
| 五人舞蹈与队形变化 | [查看](docs/community-videos.zh.md#x13-dance-formation) |
| 狐狸与雪鸮的雪地冒险 | [查看](docs/community-videos.zh.md#x14-fox-sled) |
| 从备料到装盘的天妇罗 | [查看](docs/community-videos.zh.md#x15-tempura-process) |
| 双人夜间公路旅行 | [查看](docs/community-videos.zh.md#x16-night-road-trip) |
| 开往太空的列车 | [查看](docs/community-videos.zh.md#x17-lunar-train) |
| 小狗闯入镜子自拍 | [查看](docs/community-videos.zh.md#x18-dog-mirror) |
<!-- END ZH CASES -->

**请区分两种提示词：** 作者原提示词在 X 原帖；仓库里的可复制版本是改写练习，未实测生成，不能当成原视频的生成参数。X 可能要求登录，模型名称来自发布者自述。

[完整来源记录](docs/x-showcase-sources.md)

## 收录范围

- **120 条主库配方**：60 个中文通用场景，加 60 个英文专业及创作场景。
- **15 种语言入口**：围绕同一组六个练习场景提供多语言版本，并非 120 条配方全部翻译成 15 种语言。
- **完整教程**：[中文详细指南](docs/library-guide.zh.md)、[用途对照表](docs/use-case-matrix.md)、[参考图与插画说明](assets/IMAGE_PROMPTS.md)。

## 开发者接口

推荐 [FLAQ Seedance 2.5 文生视频接口](https://flaq.ai/models/bytedance/seedance-2-5-text-to-video/)，使用方法见 [接口指南](docs/flaq-ai-api-guide.md)。Flyne AI 与 FLAQ 的账户、参数和计费分别以各自页面为准。本仓库没有进行服务稳定性测试。

## 参与维护

欢迎提交有实际输出的原创提示词，或提供能找到完整提示词的 X 视频案例。后续优先补充不同作者的商品、美妆、服装和室内空间案例。

[贡献说明](CONTRIBUTING.md) · [维护方法](docs/maintenance.md) · [实测清单](docs/render-testing.md) · [更新记录](CHANGELOG.md)

目前尚无已验证的 Flyne AI 实测案例。仓库文字与原创素材按 [MIT 许可](LICENSE) 提供；外链视频、缩略图和引用仍归原权利人所有，不属于本仓库的 MIT 授权范围。
