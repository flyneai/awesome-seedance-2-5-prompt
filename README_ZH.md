# Flyne AI · Seedance 2.5 视频提示词库

[English](README.md) · [简体中文](README_ZH.md) · [其他语言](prompts/i18n/README.md)

[![Flyne AI：产品、人物与故事](assets/flyne-seedance-banner.jpg)](https://flyne.ai/model/seedance-2-5/)

**选一个场景，复制提示词，在 Flyne AI 做出自己的版本。**

基于 [FLAQ 开源项目](docs/PROVENANCE.md) 改编，保留 120 条完整配方，适合商品展示、人物短片、社交视频和剧情创作。上图为品牌宣传插画，不是 Seedance 生成的视频截图。

[**前往 Flyne AI →**](https://flyne.ai/model/seedance-2-5/) · [120 条提示词目录](prompts/README.md) · [视频案例（中文）](docs/community-videos.zh.md) · [提交提示词](https://github.com/flyneai/awesome-seedance-2-5-prompt/issues/new?template=prompt.yml)

## 第一次使用

1. **先选简单场景。** 例如产品缓慢转动、人物一个动作或一个简短情节。
2. **换成自己的内容。** 替换主体、场景和动作；需要固定外观时，上传自己的产品图或已获授权的人物照片。
3. **打开生成页面。** 文生视频和图生视频都在 [Flyne AI 的同一个 Seedance 2.5 页面](https://flyne.ai/model/seedance-2-5/)使用，在页面内选择实际支持的模式和素材。
4. **确认参数再生成。** 检查时长、比例、清晰度、声音和费用。长提示词可以拆成几个短镜头。
5. **检查结果。** 先看人物与产品有没有变形、物体数量是否正确、动作和声音是否自然，每次只改一个问题。

[详细操作说明](docs/flyne-ai-guide.md)

<!-- BEGIN STARTER PROMPTS -->
## 直接复制：三个新手练习

这些中英双语练习未实测，不计入主库的 120 条配方。时长和画幅是创作目标，请按页面实际选项调整。

<a id="starter-product"></a>

<details>
<summary>商品展示 · 一张清晰的产品图</summary>

**8 秒 · 竖屏 9:16** · [English version](README.md#starter-product)

```text
以提供的产品照片为唯一参考，保持产品形状、颜色、瓶盖、标签布局和材质不变。纯色背景前，一件产品静置在奶油色哑光桌面上。

0–3 秒：从产品表面近景开始，镜头缓慢拉远。
3–6 秒：镜头小幅向右移动，展示侧面，产品始终静止。光线柔和，方向不变。
6–8 秒：停在清楚的正面偏侧构图，产品上方留白，供后期添加文案。

保留安静的室内环境声。不打开、旋转或复制产品。不出现手、新文字、液体特效或包装变化。
```

</details>

<a id="starter-person"></a>

<details>
<summary>人物短片 · 一张有使用授权的成年人照片</summary>

**8 秒 · 竖屏 9:16** · [English version](README.md#starter-person)

```text
以提供的成年人照片固定面容、发型、服装和身体比例。人物坐在窗边，采用胸部以上构图，双手不入镜，背景保持静止。

0–3 秒：人物看向窗外，自然呼吸。
3–6 秒：视线和头部缓慢转向镜头，然后露出轻松的微笑。
6–8 秒：保持表情和构图。全程固定机位，柔和日光始终从同一侧照入。

只保留安静的室内环境声，没有对白或音乐。不增加人物、不改变脸型或服装、不添加配饰、文字或突然的镜头运动。
```

</details>

<a id="starter-story"></a>

<details>
<summary>纸船靠岸的小故事 · 只需文字，无需图片</summary>

**8 秒 · 横屏 16:9** · [English version](README.md#starter-story)

```text
用一个连续镜头制作八秒的微缩小故事。一只黄色小纸船漂在浅浅的雨水洼中，旁边有一块光滑的石头。采用原创手工定格动画质感，光线柔和阴沉，纸张折痕清晰可见。

0–3 秒：细小波纹把纸船缓缓推向石头。镜头贴近水面，从侧面跟随。
3–6 秒：纸船轻轻碰到石头，随水流略微转动，保持形状和黄色不变。
6–8 秒：纸船停在石头后方的平静水面。镜头停止，最后几滴雨在周围泛起小圆圈。

只用轻柔的雨声和水声。全片只有一只纸船。没有人物、沉没、纸张展开、文字或切镜。
```

</details>
<!-- END STARTER PROMPTS -->

## 按用途选择

| 想做什么 | 直接复制中文练习 | 更多场景 | 准备什么 |
|---|---|---|---|
| 商品广告、上新短片 | [商品展示](#starter-product) | [基础场景库（中文）](prompts/prompt-library.md) | 一张清晰产品图 |
| 人物介绍、社交短片 | [人物短片](#starter-person) | [扩展场景库（中文）](prompts/extended-scenarios.md) | 一张有使用授权的人像 |
| 剧情、动画、奇幻短片 | [纸船小故事](#starter-story) | [类型片与视觉实验（英文）](prompts/genre-social-experiments.en.md) | 新手练习无需图片；进阶场景按说明准备 |
| 教程、制作过程 | [天妇罗制作（中文）](docs/community-videos.zh.md#x15-tempura-process) | [创作技巧库（英文）](prompts/creative-techniques.en.md) | 分镜安排及所选场景要求的素材 |

## 社区视频与提示词

<!-- BEGIN ZH CASES -->
共 **19 个 X 视频案例**，其中 **7 个新增案例**已提供中文说明和中文练习提示词。

[查看全部视频（英文说明）](docs/community-videos.md) · [阅读新增案例中文提示词](docs/community-videos.zh.md)

| 新增案例 | 中文说明与练习提示词 |
|---|---|
| 五人舞蹈与队形变化 | [查看](docs/community-videos.zh.md#x13-dance-formation) |
| 狐狸与雪鸮的雪地冒险 | [查看](docs/community-videos.zh.md#x14-fox-sled) |
| 从备料到装盘的天妇罗 | [查看](docs/community-videos.zh.md#x15-tempura-process) |
| 双人夜间公路旅行 | [查看](docs/community-videos.zh.md#x16-night-road-trip) |
| 开往太空的列车 | [查看](docs/community-videos.zh.md#x17-lunar-train) |
| 小狗闯入镜子自拍 | [查看](docs/community-videos.zh.md#x18-dog-mirror) |
| 用动作衔接场景的音乐品牌短片 | [查看](docs/community-videos.zh.md#x19-music-brand-film) |
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
