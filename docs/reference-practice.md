# 两组带参考图的练习 / Two practices with reference images

[中文首页](../README_ZH.md) · [English home](../README.md) · [主库下载 / Library downloads](../prompts/downloads/README.md)

这里使用仓库已有、继承自 FLAQ 源库的参考图，配上与画面对应的短练习。它们是输入图片，不是生成结果；以下提示词均未实测，不计入主库的 120 条配方。图片来源及许可见 [来源说明](PROVENANCE.md) 与 [图片制作记录](../assets/IMAGE_PROMPTS.md)。

These existing reference images come from the upstream FLAQ collection. They are inputs, not generated-video results. The short practice prompts below have not been render-tested and are separate from the 120 numbered recipes. See the source and image notes linked above.

1. 点击图片链接，保存原图；在 Flyne AI 的图生视频模式中上传为第一张参考图。
2. 选择下面的中文或英文提示词。八秒、横屏是练习目标，请按账户实际选项调整。
3. 生成后检查固定细节；有问题时每次只改一个动作或镜头要求。

Save an original image through its link, upload it as the first image in Flyne AI's image-to-video mode, and copy either language below. Eight seconds and landscape framing are targets, subject to available settings. Review the listed details after generation.

<a id="bottle"></a>

## 1. 饮品静物 / Bottle still life

[下载参考图 / Download image](../assets/product-sparkling-tea-reference.png) · [中文主库配方 04](../prompts/prompt-library.md#04-无品牌气泡茶揭晓) · [English full recipe](../prompts/i18n/prompt-library.en.md#i18n-01-unbranded-sparkling-tea-reveal)

![琥珀色饮品瓶、空白标签、冰台和茶叶 / Amber bottle, blank label, ice pedestal and tea leaves](../assets/product-sparkling-tea-reference.png)

**观察重点：** 瓶盖是否保持闭合、标签有没有凭空长出文字、瓶子和冰台是否变形。原图中的悬浮茶叶和水滴属于插画设计；这个练习将它们固定，不要求真实自由落体。

**Review:** closed cap, blank label, stable bottle and ice geometry. The floating leaves and droplets are part of the stylized input; this practice holds them still rather than asking for realistic free fall.

### 中文提示词

```text
以输入图作为首帧，制作八秒横屏产品短片。保持同一只琥珀色饮品瓶、金色闭合瓶盖、空白标签、冰台、背景颜色和光线方向。瓶子、冰台、悬浮茶叶和水滴都保持原位，不增加任何物体。

0–5 秒：镜头极缓慢地向瓶身推进，保持瓶盖和瓶底都在画面内。玻璃与冰的高光只随镜头位置轻微变化。
5–8 秒：镜头缓缓停止，保持清楚稳定的产品构图。

只保留轻微环境声。不打开瓶盖，不旋转瓶子，不改变液面，不让冰台融化，不生成标签文字或新增标志。
```

### English prompt

```text
Use the input image as the first frame for an eight-second landscape product film. Preserve the same amber drink bottle, closed gold cap, blank label, ice pedestal, background colors and lighting direction. Keep the bottle, ice, suspended tea leaves and droplets in their original positions. Add no objects.

0–5s: push very slowly toward the bottle while keeping both cap and bottle base in frame. Reflections on glass and ice change only slightly with camera position.
5–8s: ease the camera to a stop and hold a clear, stable product composition.

Use only faint ambience. Do not open the cap, rotate the bottle, change the liquid level, melt the ice, generate label text or add logos.
```

<a id="fox"></a>

## 2. 纸狐狸看雨 / Paper fox watches the rain

[下载参考图 / Download image](../assets/paper-fox-story-reference.png) · [中文主库配方 10](../prompts/prompt-library.md#10-纸狐狸走出速写本) · [English longer story](library-guide.md#paper-fox-leaves-a-sketchbook)

![雨窗前的红色折纸狐狸 / Red paper fox beside a rainy window](../assets/paper-fox-story-reference.png)

**观察重点：** 耳朵、鼻尖和折痕是否一致，脚是否仍接触纸面，杯子与灯具是否移位。原图中的狐狸已是立体纸艺，因此练习直接从立体狐狸开始，不要求从平面图案变身。

**Review:** consistent ears, nose and folds; feet touching the page; cup and lamp staying in place. The input already shows a dimensional paper fox, so this practice does not ask it to transform from a flat drawing.

### 中文提示词

```text
以输入图作为首帧，制作八秒横屏纸艺短片。保持红色折纸狐狸的耳朵、尖鼻、折痕、纸张纹理和身体比例。速写本、桌面、杯碟、灯具与雨窗布局不变。

0–4 秒：固定机位。狐狸的脚保持接触纸面，头部缓慢转向雨窗，身体与尾巴不移动。
4–8 秒：狐狸安静地看雨；窗上的雨滴向下滑动，杯口升起少量蒸汽。保持最后的构图。

使用轻微雨声和纸张折动声。只有一只狐狸，不走路，不展开纸张，不变成真实动物，不增加文字、物体或角色。
```

### English prompt

```text
Use the input image as the first frame for an eight-second landscape paper-craft film. Preserve the red fox's ears, pointed nose, folds, paper texture and proportions. Keep the sketchbook, tabletop, cup, saucer, lamp and rainy-window layout unchanged.

0–4s: use a locked camera. The fox keeps its feet touching the page and slowly turns its head toward the rainy window; its body and tail stay still.
4–8s: the fox quietly watches the rain. Drops slide down the glass and a little steam rises above the cup. Hold the final composition.

Use faint rain and paper-fold sounds. Exactly one fox. No walking, unfolding paper, transformation into a real animal, added text, objects or characters.
```
