# X video showcase: sources and verification

[Watch all 18 cases](../README.md#seedance-25-videos-from-x--watch-inspect-remix) · [Structured records](x-showcase-sources.json) · [Upstream attribution](PROVENANCE.md)

The collection contains **18 public X posts**. X01–X12 were inherited from the pinned FLAQ collection; their original post-body checks are dated 2026-09-20. X13–X18 were added on 2026-09-21 after reading the public post text and video metadata. All 18 video and thumbnail URLs were checked again on 2026-09-21; all returned HTTP 200 with the expected video or image content type using curl. Exact results are recorded per entry, alongside the inherited checks. Python urllib initially returned 403 for these hosts; those failed attempts are also noted.

## New cases

| ID | Subject | What to study |
|---|---|---|
| X13 | Five-person dance | Performer count, formation changes, grounded footwork |
| X14 | Fox and owl sled adventure | Cause and effect, recurring props, animal count |
| X15 | Tempura preparation | Ingredient state changes and contact sounds |
| X16 | Night road trip | Two-character continuity across locations |
| X17 | Lunar train | Reference identity and large scene transitions |
| X18 | Dog mirror selfie | Continuous viewpoint and reflection consistency |

## Retrieval method

X search redirected to login in the research browser. Search-engine discovery and the [community gallery](https://cheerselfai.com/en/demo/seedance-2-5) supplied candidate status links. The six new entries were checked against each post's public text and media metadata through [FxTwitter](https://github.com/FixTweet/FxTwitter), not accepted solely from a gallery label. Each source body explicitly names Seedance 2.5 and contains a complete prompt. Entries saying only “prompt in replies” were excluded when the prompt was not recovered.

Source attribution is the poster's claim, not independent model authentication. HTTP HEAD checks establish link availability and reported media type only; they do not establish playback quality or successful reproduction. No paid generation or end-to-end playback test was performed. The source text was read during curation; complete third-party posts are not mirrored in this repository.

## Reading a case

Click the thumbnail or **Watch video** for the original-hosted MP4. GitHub Markdown does not reliably embed arbitrary external video players. Open the X source for the author's full prompt; X may require login. The copyable block is a newly written editorial adaptation that did not produce the linked video.

The 18 cases are separate from the 120 numbered recipes. Durations are creative briefs. X14 requests portrait 8K, while the upload is landscape 720p; X18 also requests portrait but uploads landscape. The records preserve these differences without guessing whether cropping, padding or re-encoding occurred.

## Maintenance

Keep each X status ID unique. Record the author, original URL, prompt location, model evidence, video URL, thumbnail, uploaded dimensions, duration and check date. If media fails, retain the original post as a fallback and mark the failure. If the source no longer supports the entry, mark it unavailable or remove it with a changelog note. Do not silently relabel a Seedance 2.0 example as 2.5.

Videos, thumbnails and quotations remain third-party material excluded from MIT. Creator corrections and removal requests are welcome via the repository's issues.
