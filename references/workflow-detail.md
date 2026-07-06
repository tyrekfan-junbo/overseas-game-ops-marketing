# Workflow Detail

## Intake

Capture:

- Game name and local project path.
- Current stage: first production, alpha/beta, pre-OB/OB, version ops.
- Current work goal: market strategy, social account plan, creative testing, UA plan, channel launch, data requirements, report refresh, or public package.
- Platform scope: mobile by default; list Android/iOS/TapTap Global/other stores if relevant.
- Competitor baseline: direct competitor first, then genre and method references.

## Evidence Collection Order

1. Existing local archive.
2. Official competitor channels and store pages.
3. Ad libraries and creative intelligence sources.
4. YouTube/short video/creator content and video frames.
5. X/Reddit/Facebook/Instagram/TikTok community and official posts.
6. Market/channel/platform policy pages.
7. Secondary articles and trend reports.

Store each source with URL, access date, platform, competitor, stage, evidence type, evidence level, and local file path.

## Archive Discipline

Create or maintain:

- `sources/` for raw source files, converted markdown, screenshots, video frames, and source notes.
- `samples/` for normalized CSV/JSON sample tables.
- `charts/` for chart images and chart source tables.
- `reports/` for HTML/Markdown reports.
- `public_package/` for portable delivery.

Do not let public reports depend on remote-only images or app-only UI shells. Public packages should open locally.

## Report Refresh Checklist

When new sources or samples are added:

- Recompute headline sample counts.
- Rebuild charts from the latest CSV/JSON.
- Update related conclusions in the research report and marketing plan.
- Regenerate static export if one exists.
- Sync public package.
- Remove old duplicate filenames that could confuse the reader.
- Verify that HTML pages are readable and not corrupted by encoding.

## Source Quality

Use `primary` for official pages, stores, ad libraries, direct screenshots, local video frames, and first-party platform pages.

Use `secondary` for media articles, market reports, social discussions, and creator analysis.

Use `derived` for AI summaries, charts, or conclusions based on archived sources. Derived outputs must point back to primary/secondary source rows.
