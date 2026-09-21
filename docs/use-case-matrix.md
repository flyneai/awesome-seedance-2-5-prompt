# Seedance 2.5 使用场景选择矩阵

[English Guide](../README.md) · [中文指南](../README_ZH.md) · [120 个提示词索引](../prompts/README.md) · [多语言 prompts](../prompts/i18n/README.md) · [在线使用](https://flyne.ai/model/seedance-2-5/)

> **先确认平台功能：** 本文包含通用 Seedance 创作流程，不代表 Flyne 当前支持全部多参考、编辑或延长功能。按[配方与平台功能对照](flyne-ai-guide.md#配方与平台功能怎么对应)选择可执行的路线。

不知道应该从哪个提示词开始时，先按目标选择场景，再根据输入素材、画幅、时长和验收重点筛选。具体参数以平台实时页面为准。

最新的 [101–120 类型片、社媒与视觉实验 Prompt](../prompts/genre-social-experiments.en.md) 补充了封闭赛道、太空与考古科普、声音同步、竖屏喜剧、无障碍换装、动态海报、原创动画及材质变形。

## 按业务目标选择

| 目标 | 推荐场景 | 首选模式 | 常用画幅 | 首轮重点检查 |
|---|---|---|---|---|
| 品牌认知 | [25](../prompts/extended-scenarios.md#25-深夜图书馆会员季开场片) 图书馆会员季、[26](../prompts/extended-scenarios.md#26-城市修补节公益宣传) 修补节、[27](../prompts/extended-scenarios.md#27-同一活动的三画幅适配) 三画幅适配 | 参考生视频 | 16:9 + 9:16 | 情绪统一、人物自然、跨画幅一致 |
| 电商转化 | [04](../prompts/prompt-library.md#04-无品牌气泡茶揭晓) 气泡茶、[28](../prompts/extended-scenarios.md#28-折叠旅行水壶三步演示) 折叠水壶、[30](../prompts/extended-scenarios.md#30-360-度商品旋转稳定性测试) 360 度旋转 | 图生视频 | 1:1 / 9:16 | 产品几何、标签、卖点动作 |
| 产品教育 | [06](../prompts/prompt-library.md#06-模块化运动手环功能演示) 运动手环、[29](../prompts/extended-scenarios.md#29-人体工学坐垫材质剖面) 坐垫剖面、[37](../prompts/extended-scenarios.md#37-专注计时器真实操作演示) 计时器 | 图生视频 | 16:9 | 步骤正确、结构稳定、文字准确 |
| UGC 广告 | [07](../prompts/prompt-library.md#07-城市通勤背包实测) 通勤背包、[08](../prompts/prompt-library.md#08-雨天老城一小时旅行日记) 旅行日记、[09](../prompts/prompt-library.md#09-小餐馆开放式厨房探店) 餐馆探店 | 人像参考 | 9:16 | 口型、手持感、台词可信度 |
| 时尚美妆 | [31](../prompts/extended-scenarios.md#31-防雨风衣的城市风场测试) 风衣、[32](../prompts/extended-scenarios.md#32-三种围巾系法的连续换装) 围巾、[33](../prompts/extended-scenarios.md#33-口红材质与肤色真实呈现) 口红、[114](../prompts/genre-social-experiments.en.md#114-six-look-accessible-capsule-wardrobe-transition) 无障碍换装 | 人物 + 单品 | 9:16 / 4:5 | 身份、布料、肤色、单品结构 |
| 电影叙事 | [01](../prompts/prompt-library.md#01-暴雨海岸救援演练) 救援、[02](../prompts/prompt-library.md#02-末班列车后的重逢) 重逢、[03](../prompts/prompt-library.md#03-沙海气象站的信号) 气象站、[101](../prompts/genre-social-experiments.en.md#101-closed-course-rain-strategy-film)–[105](../prompts/genre-social-experiments.en.md#105-floating-orchard-courier-glide) 类型短片 | 文生 / 图生 | 16:9 | 时间轴、表演、空间连续性 |
| 动画 IP 原型 | [10](../prompts/prompt-library.md#10-纸狐狸走出速写本) 纸狐狸、[11](../prompts/prompt-library.md#11-黏土机器人修理月亮灯) 黏土机器人、[36](../prompts/extended-scenarios.md#36-布料生物穿过工作室) 布料生物、[117](../prompts/genre-social-experiments.en.md#117-ember-and-frost-staff-duel)–[118](../prompts/genre-social-experiments.en.md#118-tiny-moss-mecha-garden-repair) 原创动画 | 图生 / 文生 | 16:9 / 1:1 | 角色轮廓、材质、肢体数量 |
| 运动内容 | [13](../prompts/prompt-library.md#13-室内攀岩最后一步) 攀岩、[14](../prompts/prompt-library.md#14-红土球场的长回合) 网球、[15](../prompts/prompt-library.md#15-地铁出口的即兴街舞接力) 街舞 | 文生 / 动作参考 | 16:9 / 9:16 | 真实物理、动作顺序、安全性 |
| 音乐与 ASMR | [16](../prompts/prompt-library.md#16-屋顶爵士三重奏) 爵士、[17](../prompts/prompt-library.md#17-清晨面包坊-asmr) 面包坊、[18](../prompts/prompt-library.md#18-雨夜社区电台的一封来信) 电台、[110](../prompts/genre-social-experiments.en.md#110-percussion-led-rehearsal-light-sync) 打击乐同步 | 音画联合 | 16:9 | 动作与声音同步、音量层级 |
| 社交创意 | [40](../prompts/extended-scenarios.md#40-一颗柠檬穿过三间厨房) 柠檬转场、[41](../prompts/extended-scenarios.md#41-办公椅偷偷参加晨会) 办公椅、[42](../prompts/extended-scenarios.md#42-洗衣房里的错袜侦探) 错袜侦探、[111](../prompts/genre-social-experiments.en.md#111-mirror-delay-morning-micro-comedy)–[113](../prompts/genre-social-experiments.en.md#113-neighborhood-bakery-debate-meme) 社媒短片 | 文生 / 多场景 | 9:16 | 节奏、道具连续、笑点清楚 |
| 教育科普 | [43](../prompts/extended-scenarios.md#43-城市湿地如何减缓暴雨) 湿地、[44](../prompts/extended-scenarios.md#44-安全使用台钻的四步演示) 台钻、[45](../prompts/extended-scenarios.md#45-从露珠进入微观世界) 微观世界、[104](../prompts/genre-social-experiments.en.md#104-orbital-repair-debris-avoidance-study)、[106](../prompts/genre-social-experiments.en.md#106-controlled-wet-road-brake-demonstration)–[109](../prompts/genre-social-experiments.en.md#109-mars-sample-collection-procedure) 科学演示 | 图表 / 人物参考 | 16:9 | 科学准确、免责声明、标签可读 |
| 房地产 | [20](../prompts/prompt-library.md#20-建筑外观的日落视差展示) 建筑视差、[46](../prompts/extended-scenarios.md#46-真实小户型无广角欺骗导览) 小户型、[48](../prompts/extended-scenarios.md#48-同一庭院的晨昏光线研究) 庭院光线 | 建筑图生视频 | 16:9 | 尺度诚实、几何、门窗和家具 |
| 无障碍预演 | [38](../prompts/extended-scenarios.md#38-无障碍路线规划应用) 路线应用、[47](../prompts/extended-scenarios.md#47-无障碍咖啡馆动线验证) 咖啡馆动线、[57](../prompts/extended-scenarios.md#57-包容性紧急出口提醒) 紧急出口 | UI / 白模 | 16:9 / 9:16 | 路径可行、不虚构合规声明 |
| 交通出行 | [49](../prompts/extended-scenarios.md#49-载货电助力自行车雨天测试) 载货自行车、[50](../prompts/extended-scenarios.md#50-夜行列车卧铺服务导览) 夜行列车、[51](../prompts/extended-scenarios.md#51-人行道配送机器人交接) 配送机器人 | 产品 + 动作参考 | 16:9 | 结构、道路安全、运动物理 |
| 自然宠物 | [52](../prompts/extended-scenarios.md#52-老年犬雨衣合身检查) 老年犬、[53](../prompts/extended-scenarios.md#53-阳台夜蛾观察日志) 夜蛾、[54](../prompts/extended-scenarios.md#54-阳台番茄七日成长日记) 番茄成长 | 图生 / 多日参考 | 16:9 / 9:16 | 物种与身份、福利、时间连续 |
| 工业流程 | [55](../prompts/extended-scenarios.md#55-小批量收音机组装流程) 收音机、[56](../prompts/extended-scenarios.md#56-冷藏食品包裹的全程追踪) 冷链包裹 | 多步骤参考 | 16:9 | 零件数量、步骤、安全操作 |
| 公共服务 | [57](../prompts/extended-scenarios.md#57-包容性紧急出口提醒) 紧急出口、[26](../prompts/extended-scenarios.md#26-城市修补节公益宣传) 修补节 | 人物 + 场景 | 16:9 / 9:16 | 包容性、语气、事实与风险 |
| 酒店会展 | [23](../prompts/prompt-library.md#23-白模空间预演酒店大堂一镜到底) 大堂白模、[58](../prompts/extended-scenarios.md#58-山谷木屋诚实入住导览) 木屋、[59](../prompts/extended-scenarios.md#59-小型展位从空场到开门) 展位、[60](../prompts/extended-scenarios.md#60-无声耳机舞会入场体验) 舞会 | 白模 / 场景图 | 16:9 / 9:16 | 空间诚实、设施不虚构、动线 |

## 按输入素材选择

英文专业场景 61–72 另见 [Advanced Workflows](../prompts/advanced-workflows.en.md)，覆盖 SaaS、创作者课程、家具组装、珠宝、餐饮、博物馆、清洁能源、远程问诊入口、播客、物流 UI、无障碍活动和独立游戏。

| 你拥有的素材 | 推荐模式 | 适合场景 | 写法 |
|---|---|---|---|
| 只有文字想法 | 文生视频 | 02、03、11、13、15、34、41、45 | 把角色、环境、动作和镜头全部写清 |
| 一张产品图 | 图生视频 | 04、05、06、28、29、30 | 先锁定几何、标签、材质和液面 |
| 一张人物图 | 人像图生视频 | 07、19、31、32 | 先锁定脸、发型、衣服、体型和表情范围 |
| 多张角色与场景图 | 参考生视频 | 01、12、23、31、58 | 每张素材只指定一个职责 |
| 一段动作视频 | 动作参考 | 14、15、36、49 | 只参考步态、路径或节奏，不复制人物 |
| 白模或预演视频 | 白模控制 | 23、47、59 | 固定空间、走位、遮挡和相机路径 |
| UI 截图 | UI 图生视频 | 37、38、39 | 保留文字、状态和交互顺序 |
| 首帧与尾帧 | 首尾帧 | 21 | 描述中间过渡和终帧到达条件 |
| 已有视频需要修改 | 视频编辑 | 24 | 只修改一个维度并重复所有不变量 |
| 音频或节奏参考 | 音画联合 | 16、17、18、60 | 明确只参考节奏、声音或声场 |

## 按渠道选择画幅

| 渠道或用途 | 推荐画幅 | 构图重点 |
|---|---|---|
| 短视频信息流 | 9:16 | 主体处于中央安全区，顶部和底部避开 UI |
| 社交动态与商城 | 4:5 | 产品和脸部同时可见，减少极端横向运动 |
| 商品详情页 | 1:1 / 4:5 | 几何稳定、背景干净、首尾可截帧 |
| 官网横幅 | 16:9 | 留出文案区，运动不要穿过主要按钮区域 |
| 电影感叙事 | 16:9 / 2.39:1 | 强调空间层次、调度和声音环境 |
| 教育与演示 | 16:9 | 标签足够大，流程从左到右或从上到下明确 |

## 首轮生成验收

1. **身份与产品：** 脸、服装、产品轮廓、标签和物品数量是否稳定。
2. **空间：** 人物是否穿墙，门窗、家具和前后遮挡是否正确。
3. **动作：** 每个动作是否由前一个动作触发，重量和惯性是否可信。
4. **摄影：** 镜头是否按单一路径到达明确的停止位置。
5. **音频：** 对白、环境声、拟音和音乐是否分层，关键声音是否同步。
6. **文字：** 只出现被明确提供和允许的文字，拼写、数字和方向正确。
7. **权利与安全：** 素材授权、人物同意、商标、音乐、健康及安全表述已复核。

## 快速入口

- [基础 24 个提示词](../prompts/prompt-library.md)
- [扩展 36 个提示词](../prompts/extended-scenarios.md)
- [14 份独立外语 prompts（共 15 种语言）](../prompts/i18n/README.md)
- [Seedance 2.5 在线页面](https://flyne.ai/model/seedance-2-5/)
