# Seedance 2.5 Use-Case and Prompt Finder

[Home](../README.md) · [120 prompt recipes](../prompts/README.md) · [Prompting guide](prompting-guide.md) · [Flyne AI workflow](flyne-ai-guide.md)

> **Check the available mode first:** these are general Seedance creative workflows, not a promise that Flyne supports every reference, editing or extension feature. Use the [recipe-to-platform guide](flyne-ai-guide.md#match-the-recipe-to-the-available-mode) before choosing an advanced recipe.

Choose a business goal first, then narrow the prompt by available assets, delivery format, and first-pass quality checks.

## Find a prompt by goal

| Goal | Recommended recipe IDs | Preferred starting mode | First review priority |
|---|---|---|---|
| Brand awareness | [25](../prompts/extended-scenarios.md#25-深夜图书馆会员季开场片) library membership, [26](../prompts/extended-scenarios.md#26-城市修补节公益宣传) repair festival, [27](../prompts/extended-scenarios.md#27-同一活动的三画幅适配) multi-format campaign | Reference-to-video | Mood, natural performance, format continuity |
| Ecommerce conversion | [04](../prompts/prompt-library.md#04-无品牌气泡茶揭晓) sparkling tea, [28](../prompts/extended-scenarios.md#28-折叠旅行水壶三步演示) folding bottle, [30](../prompts/extended-scenarios.md#30-360-度商品旋转稳定性测试) product rotation | Image-to-video | Product geometry, labels, feature action |
| Product education | [06](../prompts/prompt-library.md#06-模块化运动手环功能演示) wearable, [29](../prompts/extended-scenarios.md#29-人体工学坐垫材质剖面) cushion cutaway, [37](../prompts/extended-scenarios.md#37-专注计时器真实操作演示) focus timer | Image-to-video | Correct steps, stable structure, accurate UI |
| Vertical UGC | [07](../prompts/prompt-library.md#07-城市通勤背包实测) commuter bag, [08](../prompts/prompt-library.md#08-雨天老城一小时旅行日记) travel diary, [09](../prompts/prompt-library.md#09-小餐馆开放式厨房探店) restaurant review | Portrait reference | Speech, handheld feel, credible reactions |
| Fashion and beauty | [31](../prompts/extended-scenarios.md#31-防雨风衣的城市风场测试) raincoat, [32](../prompts/extended-scenarios.md#32-三种围巾系法的连续换装) scarf styling, [33](../prompts/extended-scenarios.md#33-口红材质与肤色真实呈现) lipstick material, [114](../prompts/genre-social-experiments.en.md#114-six-look-accessible-capsule-wardrobe-transition) capsule wardrobe | Person + product | Identity, cloth physics, skin tone, item structure |
| Cinematic storytelling | [01](../prompts/prompt-library.md#01-暴雨海岸救援演练) rescue, [02](../prompts/prompt-library.md#02-末班列车后的重逢) reunion, [03](../prompts/prompt-library.md#03-沙海气象站的信号) weather station, [101](../prompts/genre-social-experiments.en.md#101-closed-course-rain-strategy-film)–[105](../prompts/genre-social-experiments.en.md#105-floating-orchard-courier-glide) genre shorts | Text- or image-to-video | Timeline, blocking, spatial continuity |
| Animation prototype | [10](../prompts/prompt-library.md#10-纸狐狸走出速写本) paper fox, [11](../prompts/prompt-library.md#11-黏土机器人修理月亮灯) clay robot, [36](../prompts/extended-scenarios.md#36-布料生物穿过工作室) fabric creature, [117](../prompts/genre-social-experiments.en.md#117-ember-and-frost-staff-duel)–[118](../prompts/genre-social-experiments.en.md#118-tiny-moss-mecha-garden-repair) original animation | Image- or text-to-video | Silhouette, material, limb count |
| Sports and movement | [13](../prompts/prompt-library.md#13-室内攀岩最后一步) climbing, [14](../prompts/prompt-library.md#14-红土球场的长回合) tennis, [15](../prompts/prompt-library.md#15-地铁出口的即兴街舞接力) dance | Text + action reference | Plausible physics, action order, safety |
| Music and ASMR | [16](../prompts/prompt-library.md#16-屋顶爵士三重奏) jazz, [17](../prompts/prompt-library.md#17-清晨面包坊-asmr) bakery, [18](../prompts/prompt-library.md#18-雨夜社区电台的一封来信) radio, [110](../prompts/genre-social-experiments.en.md#110-percussion-led-rehearsal-light-sync) percussion sync | Audio-visual | Action sync and layer balance |
| Social creative | [40](../prompts/extended-scenarios.md#40-一颗柠檬穿过三间厨房) lemon transition, [41](../prompts/extended-scenarios.md#41-办公椅偷偷参加晨会) office-chair comedy, [42](../prompts/extended-scenarios.md#42-洗衣房里的错袜侦探) sock detective, [111](../prompts/genre-social-experiments.en.md#111-mirror-delay-morning-micro-comedy)–[113](../prompts/genre-social-experiments.en.md#113-neighborhood-bakery-debate-meme) social shorts | Text / multi-scene | Rhythm, prop continuity, clear payoff |
| Education and training | [43](../prompts/extended-scenarios.md#43-城市湿地如何减缓暴雨) wetland, [44](../prompts/extended-scenarios.md#44-安全使用台钻的四步演示) drill press, [45](../prompts/extended-scenarios.md#45-从露珠进入微观世界) micro-world, [104](../prompts/genre-social-experiments.en.md#104-orbital-repair-debris-avoidance-study) and [106](../prompts/genre-social-experiments.en.md#106-controlled-wet-road-brake-demonstration)–[109](../prompts/genre-social-experiments.en.md#109-mars-sample-collection-procedure) science studies | Diagram / person reference | Factual accuracy, disclaimer, readable labels |
| Real estate and architecture | [20](../prompts/prompt-library.md#20-建筑外观的日落视差展示) parallax, [46](../prompts/extended-scenarios.md#46-真实小户型无广角欺骗导览) apartment, [48](../prompts/extended-scenarios.md#48-同一庭院的晨昏光线研究) courtyard | Image-to-video | Honest scale, geometry, doors and furniture |
| Accessibility prototype | [38](../prompts/extended-scenarios.md#38-无障碍路线规划应用) route app, [47](../prompts/extended-scenarios.md#47-无障碍咖啡馆动线验证) café circulation, [57](../prompts/extended-scenarios.md#57-包容性紧急出口提醒) exit reminder | UI / white model | Viable path, inclusive framing, no invented compliance claim |
| Mobility and robotics | [49](../prompts/extended-scenarios.md#49-载货电助力自行车雨天测试) cargo bike, [50](../prompts/extended-scenarios.md#50-夜行列车卧铺服务导览) sleeper train, [51](../prompts/extended-scenarios.md#51-人行道配送机器人交接) delivery robot | Product + action | Structure, road safety, motion physics |
| Nature and pets | [52](../prompts/extended-scenarios.md#52-老年犬雨衣合身检查) senior dog, [53](../prompts/extended-scenarios.md#53-阳台夜蛾观察日志) moth, [54](../prompts/extended-scenarios.md#54-阳台番茄七日成长日记) tomato growth | Image / multi-day reference | Species or identity, welfare, time continuity |
| Industry and logistics | [55](../prompts/extended-scenarios.md#55-小批量收音机组装流程) radio assembly, [56](../prompts/extended-scenarios.md#56-冷藏食品包裹的全程追踪) cold parcel | Multi-step reference | Part count, process order, safe operation |
| Hospitality and events | [23](../prompts/prompt-library.md#23-白模空间预演酒店大堂一镜到底) lobby previs, [58](../prompts/extended-scenarios.md#58-山谷木屋诚实入住导览) cabin, [59](../prompts/extended-scenarios.md#59-小型展位从空场到开门) booth, [60](../prompts/extended-scenarios.md#60-无声耳机舞会入场体验) silent disco | White model / location | Honest space, no invented amenities, circulation |
| Posters and visual experiments | [115](../prompts/genre-social-experiments.en.md#115-night-garden-dynamic-event-poster) dynamic poster, [120](../prompts/genre-social-experiments.en.md#120-four-material-fluid-morph-study) material morph | Storyboard / multi-image | Keyframe order, silhouette, material separation, clean copy space |

## Advanced English workflow shortcuts

| Need | Recipe IDs | What the prompt protects |
|---|---|---|
| SaaS and service onboarding | [61](../prompts/advanced-workflows.en.md#61-calm-saas-launch-film-without-invented-metrics) launch film, [68](../prompts/advanced-workflows.en.md#68-accessible-telehealth-appointment-onboarding) telehealth onboarding, [70](../prompts/advanced-workflows.en.md#70-parcel-tracking-status-walkthrough) parcel tracking | Approved UI states, exact copy, no invented metrics or personal data |
| Creator and audio promotion | [62](../prompts/advanced-workflows.en.md#62-creator-course-vertical-ad-with-credible-delivery) creator course, [69](../prompts/advanced-workflows.en.md#69-multilingual-independent-podcast-trailer) multilingual podcast | Authorized identity and voice, credible delivery, no testimonials or voice cloning |
| Ecommerce and hospitality detail | [63](../prompts/advanced-workflows.en.md#63-flat-pack-side-table-assembly-proof) furniture assembly, [64](../prompts/advanced-workflows.en.md#64-recycled-silver-ring-macro-study) silver ring, [65](../prompts/advanced-workflows.en.md#65-seasonal-restaurant-menu-film-with-honest-ingredients) seasonal menu | Part count, geometry, material, ingredients, honest product behavior |
| Culture and public education | [66](../prompts/advanced-workflows.en.md#66-community-museum-exhibition-teaser) museum teaser, [67](../prompts/advanced-workflows.en.md#67-neighborhood-solar-and-storage-explainer) energy explainer | Artwork integrity, accurate labels, no implied endorsement or unsupported claims |
| Accessibility and inclusive events | [71](../prompts/advanced-workflows.en.md#71-accessible-live-event-welcome-film) live-event welcome | Real routes and features, respectful agency, no fabricated compliance claim |
| Original entertainment concept | [72](../prompts/advanced-workflows.en.md#72-original-indie-game-world-reveal) indie game reveal | Character silhouette, level geography, reference separation, no franchise resemblance |

## Choose by available input

For match cuts, multi-reference tutorials, local edits, batch SKU generation, digital presenters, long-form chaining, video extension, region edits, and white-model rendering, browse [Creative Techniques 73–100](../prompts/creative-techniques.en.md).

For controlled genre filmmaking, social comedy, audio synchronization, dynamic posters, original animation, and material morphing, browse [Genre, Social & Visual Experiments 101–120](../prompts/genre-social-experiments.en.md).

| What you have | Start with | Prompt strategy |
|---|---|---|
| Text idea only | [Text-to-Video](https://flyne.ai/model/seedance-2-5/) | Fully define subject, world, timeline, camera, sound, and final frame |
| One product image | [Image-to-Video](https://flyne.ai/model/seedance-2-5/) | Lock geometry, label region, material, part count, and liquid level |
| One portrait | Image-to-video | Lock face, hair, age, body proportions, wardrobe, and expression range |
| Several character and location images | Reference-to-video | Give every asset one job and state priority when references conflict |
| UI screenshots | UI image-to-video | Preserve approved text, state, controls, and interaction order |
| First and end frames | Image-to-video | Define each frame's role and the physical transition between them |
| Existing clip to modify | Video editing workflow | Change one dimension and repeat every invariant |
| Audio or rhythm reference | Audio-visual workflow | State whether it controls timing, ambience, dialogue, or music only |

## First-pass acceptance test

1. Identity, wardrobe, product shape, labels, and object count remain stable.
2. Doors, walls, furniture, foreground occlusion, and travel direction remain coherent.
3. Actions have plausible weight, contact, inertia, and recovery.
4. The camera follows one understandable path and reaches a deliberate stop.
5. Dialogue, ambience, foley, and music are separated and synchronized.
6. Only approved, legible text appears; no invented claims, logos, or prices.
7. Likeness, asset, music, trademark, safety, and advertising rights are reviewed.
