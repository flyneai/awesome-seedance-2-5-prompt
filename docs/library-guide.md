# Seedance 2.5 recipe guide

[Home](../README.md) · [Video cases](community-videos.md)

> **Check the available mode first:** these are general Seedance creative workflows, not a promise that Flyne supports every reference, editing or extension feature. Use the [recipe-to-platform guide](flyne-ai-guide.md#match-the-recipe-to-the-available-mode) before choosing an advanced recipe.

## Find the right prompt in under a minute

| If you need… | Start here |
|---|---|
| A video example with its original X post and published prompt | [Community video showcase](community-videos.md) |
| One complete prompt to customize | [120-prompt master index](../prompts/README.md) |
| A product, ad, UGC, or creator-video recipe | [Foundation prompts 04–09](../prompts/prompt-library.md) |
| UI, education, real estate, mobility, pet, or industry content | [Extended prompts 37–60](../prompts/extended-scenarios.md) |
| SaaS, creator, jewelry, culture, clean-energy, accessibility, or game content | [Advanced English workflows 61–72](../prompts/advanced-workflows.en.md) |
| Match cuts, one-takes, tutorials, video edits, batch SKUs, digital presenters, extension, or previs | [Creative techniques 73–100](../prompts/creative-techniques.en.md) |
| Genre films, safe vehicle shots, social comedy, audio sync, original animation, dynamic posters, or material morphs | [Genre, social & visual experiments 101–120](../prompts/genre-social-experiments.en.md) |
| A prompt in your preferred language | [15-language prompt directory](../prompts/i18n/README.md) |
| Help choosing by business goal or available asset | [English use-case matrix](use-case-matrix.en.md) |
| Better camera, timing, sound, continuity, or negative constraints | [Advanced prompting guide](prompting-guide.md) |
| A Flyne AI text-to-video vs image-to-video decision | [Flyne AI creation workflow](flyne-ai-guide.md) |

### What is included

- **120 full recipes**, not one-line prompt fragments: each includes mode, references, timeline, camera, sound, continuity, and exclusions. The core 60-scene catalog is in Simplified Chinese, with 60 additional professional, creative-technique, genre, social, and visual-experiment workflows in English.
- **15-language support**, including 14 independent localized prompt files with six complete shared test scenes in each language.
- **20+ practical categories** for brand, ecommerce, UGC, travel, food, fashion, beauty, cinematic, animation, sports, fantasy, VFX, UI, social, education, architecture, mobility, nature, industry, and hospitality workflows.
- **Production guidance** for prompt debugging, aspect-ratio planning, reference ownership, final-frame design, rights review, and iteration records.

## New Seedance 2.5 prompts for genre films, social video, and visual experiments

Prompts 101–120 turn popular creative patterns into production-safe, original briefs: closed-course motorsport, analog drama, orbital science, fantasy flight, natural-history reconstruction, percussion sync, vertical comedy, accessible fashion, motion-reference transfer, original animation, workplace short drama, and material morphing.

![Original nine-panel night garden storyboard for Prompt 115](../assets/night-garden-storyboard.png)

The image above was generated specifically for [Prompt 115: Night Garden Dynamic Event Poster](../prompts/genre-social-experiments.en.md#115-night-garden-dynamic-event-poster). Its nine panels are cumulative keyframes rather than copied frames, and the full reusable generation brief is documented in [Original Image Prompt Notes](../assets/IMAGE_PROMPTS.md).

## What makes a strong Seedance 2.5 prompt?

The official Seedance 2.5 page highlights video generation up to 30 seconds in one pass, two extensions, more precise interpretation of reference videos, broader audio-visual editing, professional camera movement, performance blocking, white-model control, and green-screen editing. A useful prompt should therefore read like a compact directing brief, not a pile of style adjectives.

```text
[Mode] Text-to-video / Image-to-video / Reference-to-video / Edit
[Goal] Use, audience, emotion, duration, aspect ratio
[Reference roles] Image 1 locks identity; Video 1 provides camera path only
[Visual anchors] Subject, wardrobe, product geometry, set, time, palette
[Timeline] Establishment -> action -> turn -> final frame
[Camera] Shot size, height, path, speed, focus, stopping point
[Performance and physics] Gaze, hands, weight, inertia, contact, cloth, water
[Audio] Dialogue, ambience, foley, music, synchronization cues
[Continuity] What must never change
[Avoid] Morphing, duplicates, extra limbs, fake text, logos, watermarks
```

For the full method, see [Seedance 2.5 Prompting Guide: From Brief to Usable Video](prompting-guide.md).

## Three copy-ready Seedance 2.5 prompts

### Cinematic storm rescue training

```text
Use the input image as the first frame and only visual anchor. Preserve the identities and orange rain gear of the two adult volunteers, the rescue boat geometry, the number of people, the lighthouse position, and the cold storm lighting.

00:00-00:07: Track steadily from water level behind the boat. The hull rises and falls with real weight; spray briefly crosses the lens guard; the lighthouse beam sweeps through rain.
00:07-00:15: Slide forward along the side to the volunteers' shoulders. The front volunteer points toward the safe channel while the rear volunteer adjusts the throttle.
00:15-00:23: A side wave pushes the boat left. Both lower their center of gravity and correct course. Raise the camera slightly to reveal the passage through the rocks; water inertia and body balance must be physically plausible.
00:23-00:30: Enter calmer harbor water. Push past the volunteers toward the lighthouse and stop on a wide, hopeful final frame.

Audio: stereo rain, waves, engine, two short safety calls, and a very soft low string tone at the end. No casualties, added people, altered boat parts, teleporting camera, text, logos, or watermark.
```

### Premium unbranded sparkling-tea ad

```text
Use the bottle in the input image as the only product anchor. Preserve its silhouette, cap, blank-label proportions, amber liquid level, and lighting. Generate no text.

00:00-00:05: Macro focus on condensation, then rack focus to fine bubbles rising in the liquid.
00:05-00:11: Orbit clockwise by about 35 degrees while slowly pulling back. The ice pedestal refracts accurately; two tea leaves travel in the opposite direction for layered motion. The bottle remains stable.
00:11-00:17: A warm backlight passes behind the bottle. The cap lifts only slightly with a clean click and releases a natural mist, not an explosion.
00:17-00:24: Lower to a subtle hero angle. Droplets fall naturally, then stop on a clean front view with negative space above for post-production copy.

Audio: cap click, fine carbonation, light ice sound, minimal fresh rhythm. No fake text, extra bottles, label drift, melting glass, trademarks, or watermark.
```

### Paper fox leaves a sketchbook

```text
Use the input image as the art and character anchor. Preserve the red paper fox's triangular ears, pointed nose, folds, pencil texture, and proportions; preserve the café table, sketchbook, lamp, rainy window, and cup layout.

00:00-00:07: Pencil lines tremble slightly. The fox blinks and raises one front paw as the camera makes a macro push-in.
00:07-00:14: The fox steps over the page edge, transitioning naturally from flat graphite lines to dimensional folded paper with correct contact shadows.
00:14-00:21: Track parallel as it walks around pencil shavings and studies the steam above the cup.
00:21-00:27: Steam forms a brief path toward the rainy window. The fox trots after it while tiny tabletop droplets react to its steps.
00:27-00:30: It stops at the window with a consistent reflection. Raise the camera and finish on an open-ended sense of departure.

Audio: rain, paper folds, wood contact, and minimal glockenspiel. No extra animals, redesign, franchise resemblance, text, logos, or watermark.
```

## Full prompt library

Open the [120-prompt master index](../prompts/README.md), the [24-scene foundation library](../prompts/prompt-library.md), the [36-scene extended library](../prompts/extended-scenarios.md), the [12 advanced English workflows](../prompts/advanced-workflows.en.md), the [28 creative-technique prompts](../prompts/creative-techniques.en.md), or the [20 genre, social, and visual-experiment prompts](../prompts/genre-social-experiments.en.md). Use the [English use-case matrix](use-case-matrix.en.md) to filter by goal and input asset. Together they cover:

- cinematic drama and science fiction;
- product, skincare, beverage, and wearable ads;
- vertical UGC, travel diaries, and food reviews;
- paper craft, clay animation, and living murals;
- climbing, tennis, and street dance;
- jazz, bakery ASMR, and radio drama;
- portrait micro-expressions, architectural parallax, and start/end frames;
- green screen, white-model previs, reference camera paths, and precise editing.
- SaaS launches, creator courses, assembly proof, jewelry, museums, clean energy, telehealth onboarding, podcasts, logistics UI, accessibility, and original game concepts.
- object-centered match cuts, continuous room transitions, multi-reference tutorials, local edits, SKU batches, multilingual presenters, motion transfer, long-form chaining, extension, region editing, and white-model-to-final rendering.
- safe genre filmmaking, analog memory shorts, space and archaeology explainers, social mockumentaries, dialogue memes, accessible fashion transitions, dynamic posters, original duel and mecha animation, and controlled material morphs.

### Complete prompt files in more languages

- [English](../prompts/i18n/prompt-library.en.md), [Traditional Chinese](../prompts/i18n/prompt-library.zh-TW.md), [Japanese](../prompts/i18n/prompt-library.ja.md), and [Korean](../prompts/i18n/prompt-library.ko.md);
- [Spanish](../prompts/i18n/prompt-library.es.md), [French](../prompts/i18n/prompt-library.fr.md), [German](../prompts/i18n/prompt-library.de.md), and [Brazilian Portuguese](../prompts/i18n/prompt-library.pt-BR.md);
- [Arabic](../prompts/i18n/prompt-library.ar.md), [Russian](../prompts/i18n/prompt-library.ru.md), and [Bahasa Indonesia](../prompts/i18n/prompt-library.id.md).
- [Italian](../prompts/i18n/prompt-library.it.md), [Thai](../prompts/i18n/prompt-library.th.md), and [Vietnamese](../prompts/i18n/prompt-library.vi.md).

Each language file contains six complete, copy-ready recipes rather than translated titles alone. See the [localization rules and language matrix](../prompts/i18n/README.md).

## Image-to-video checklist

- Lock identity, wardrobe, product shape, object count, composition, and key-light direction.
- Separate subject motion, environmental motion, and camera motion.
- Give each reference file one job; never say “use everything from all references.”
- Describe the camera's start, path, speed, and final stopping point.
- Reserve the final 4–6 seconds for deceleration and a deliberate end frame.
- Add dialogue, ambience, foley, and music as separate audio layers.
- Use original or properly licensed people, music, products, and visual assets.

## Seedance 2.5 prompt FAQ

### What is a Seedance 2.5 prompt?

A Seedance 2.5 prompt is a directing brief for a generated video. Strong prompts define the goal, reference roles, visual anchors, timed actions, camera path, physical behavior, sound, continuity, and concrete failure conditions.

### Should I use Text-to-Video or Image-to-Video?

Use [Text-to-Video](https://flyne.ai/model/seedance-2-5/) when you are exploring from a concept or script. Use [Image-to-Video](https://flyne.ai/model/seedance-2-5/) when a product, person, illustration, composition, or starting image must remain recognizable. Supplying a required end frame needs a dedicated end-frame input supported by the selected platform; ordinary image-to-video does not by itself confirm that control.

### How do I keep a person or product consistent?

Name one primary identity or product anchor, list its invariant properties before describing motion, assign one job to every other reference, and reject redesign, part-count changes, label drift, or identity drift explicitly. Test this anchor before adding elaborate effects.

### Can Seedance 2.5 prompts be written in different languages?

This repository supports 15 languages. The shared multilingual set keeps the same six scene IDs so teams can compare instruction following, UI text, speech, audio, and cultural localization without changing the production brief.

### Are these prompts free to use?

The repository is released under the [MIT License](../LICENSE). Generated output may still involve separate rights for source images, people, voices, music, trademarks, locations, claims, and the platform or model used to create it.
