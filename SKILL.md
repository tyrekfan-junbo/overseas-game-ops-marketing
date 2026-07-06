---
name: overseas-game-ops-marketing
description: "End-to-end overseas mobile game operations and marketing workflow. Use when Codex must turn competitor research, web intelligence, ad creatives, official social content, store/channel strategy, UA testing, KPI requirements, source archives, charts, and reports into a reusable mobile game publishing plan or decision report. Triggers: overseas game launch plan, mobile game marketing strategy, ad creative teardown, Meta/TikTok/YouTube/X/Reddit monitoring, competitor sample library, first production, alpha/beta, pre-OB/OB, version ops, UA plan, KPI tracking, public report package, source archive."
---

# Overseas Game Ops Marketing

## Overview

Build an operations decision system for overseas mobile game publishing. Use archived evidence first, collect new information only to fill gaps, and keep every claim traceable to local sources, screenshots, video frames, URLs, CSV/JSON, charts, or source notes.

Default scope is mobile. Treat Steam/PC as `Later` unless the user explicitly brings it into the current stage.

## Capabilities

| Module | Capability | Value |
|---|---|---|
| Market intelligence | Collect and archive competitor, platform, store, social, and ad-library evidence | Keeps strategy source-backed |
| Creative teardown | Classify static/video creatives by hook, first 3 seconds, promise, CTA, risk, and product bridge | Turns samples into testable actions |
| Social operations | Convert official account observations into columns, cadence, formats, and community jobs | Makes social planning executable |
| UA planning | Build creative test cells with regions, channels, thresholds, and guardrails | Prevents CPI-only decisions |
| KPI requirements | Define formulas, events, dimensions, and R&D/BI requests | Connects publishing work to measurable data |
| Report delivery | Produce final-reader reports, charts, source appendices, and portable packages | Supports audit and external sharing |

## Operating Modes

- **Archive mode**: inspect existing local data, normalize source tables, and fix corrupted or stale source files.
- **Research mode**: collect missing current information, then archive every useful source locally.
- **Creative mode**: analyze ads, images, videos, social posts, and store assets into reusable sample tables.
- **Planning mode**: convert evidence into social account plans, UA plans, launch/channel plans, and 30/60/90-day actions.
- **Report mode**: update HTML/Markdown reports, charts, static exports, source appendices, and public packages.
- **Darwin gate mode**: evaluate the workflow output with explicit failure modes, checklists, and anti-patterns before final delivery.

## Workflow

1. **Frame product and stage**
   - Identify genre, platform, current publishing stage, target regions, core loop, first user experience, monetization assumptions, assets, and operational constraints.
   - Use the stage rhythm: `first production`, `alpha/beta`, `pre-OB/OB`, `version ops`.
   - For early projects, prioritize social account plan, creative testing, UA channel plan, tracking requirements, and the first 90 days.

2. **Inspect or create the archive**
   - Prefer existing local folders before web search.
   - For a new project, run `scripts/init_ops_workspace.py` to create source, sample, report, chart, export folders, and CSV templates.
   - Treat local HTML/CSV/JSON/screenshots/video frames as the audit layer.

3. **Collect evidence**
   - Use official pages, stores, social accounts, ad libraries, creator videos, community discussions, policy pages, and search results.
   - Verify online for unstable facts: platform rules, active ads, rankings, pricing, social posts, channel policies, competitor changes.
   - Archive useful sources with URL, timestamp, platform, competitor, stage, evidence level, mobile relevance, and local path.

4. **Classify samples**
   - Use `P0`, `P1`, `P2`, `Later`.
   - `P0`: direct current mobile use for creative brief, UA/social/store/channel action, or risk signal.
   - `P1`: mobile-relevant but requires second-pass filtering.
   - `P2`: background reference.
   - `Later`: not current-stage action, especially PC/Steam or low relevance.

5. **Analyze creatives and video material**
   - For images/static ads, extract hook, visual promise, conflict, CTA, landing bridge, product-truth risk, sentiment risk, and target-game action.
   - For videos, use `zk-creative-process` when available: material folder, keyframe sheet, AI input pack, scene storyboard, and story-direction pool.
   - If video tooling is unavailable, still save frames/screenshots and analyze first 3 seconds, scene progression, edit rhythm, audio/captions, product bridge, and risks.
   - Do not mark a frame useful unless it informs a creative brief, test cell, store visual, social column, UA hypothesis, or risk control.

6. **Analyze official social operations**
   - Map platform jobs:
     - `X`: timely notices, codes, event replies, topic amplification.
     - `Instagram`: visual columns, Reels, character/enemy/tower packaging.
     - `Facebook`: longer updates, fanbase, comments, event explanation, Meta audience support.
     - `TikTok/Shorts/Reels`: 9:16 gameplay, fail-to-win, rescue moments, tower placement, fast conflict.
     - `YouTube`: trailers, guides, long-to-short repurposing, creator/KOL evidence.
     - `Reddit/Discord`: user language, complaints, guide needs, community service signals.
   - Convert observations into account columns, cadence, asset formats, measurable tests, and community service actions.

7. **Design UA and tracking requirements**
   - Define test cells by hook, channel, region, creative format, landing/store page, budget tier, and metric threshold.
   - Require tracking before scaling: install, tutorial start/complete, level milestones, first fail, first win, ad impression, purchase funnel, revenue, retention, refund/rating/comment risk.
   - Use CPI only with retention, milestone reach, CVR, ROAS/LTV, and sentiment risk.
   - Read `references/metrics-and-tracking.md` when writing KPI formulas or R&D/BI requirements.

8. **Write plan/report**
   - Produce final-reader content only. Exclude modification process, debug notes, tool logs, and "this update changed..." paragraphs.
   - Merge repeated ideas into one decision-ready section.
   - Use charts only when they answer an operations question.
   - Every chart/table needs a source path or source note.
   - If delivering a portable package, include HTML reports, CSV/JSON data, images/charts, source notes, and an index page.

## Darwin Gate

Before final delivery, run this lightweight quality gate:

| Dimension | Pass condition |
|---|---|
| Frontmatter | Description states what the skill does, when to use it, and trigger terms within 1024 chars |
| Workflow clarity | Steps have clear inputs, outputs, and order |
| Failure encoding | Common failure modes have explicit fallback actions |
| Checkpoints | High-risk decisions force a stop, user confirmation, or source verification |
| Specificity | Instructions use concrete files, fields, metrics, and outputs |
| Resource integration | References and scripts are named and reachable |
| Structure | No repeated sections or report-process clutter |
| Practical test | At least one realistic prompt can produce a better plan/report than generic advice |
| Risk blacklist | Anti-patterns are listed and avoided |

If a change improves only wording but adds length, keep it only when it improves one of these dimensions. Stop optimizing after two small gains in a row.

## Failure Modes

| Trigger | First fix | Fallback |
|---|---|---|
| Local source files are missing | Create workspace with `scripts/init_ops_workspace.py` | Produce a missing-source checklist and collect only the highest-value sources |
| Source encoding shows `???` or corrupted text | Rebuild from original CSV/JSON/HTML or known URLs | Mark corrupted fields as unrecoverable and replace with source-backed summaries |
| Competitor samples mix mobile and PC/Steam | Reclassify PC/Steam rows as `Later` | Keep only as background evidence, not current mobile action |
| Sample count is high but weak | Deduplicate, classify, and weight by evidence level | State coverage limits and avoid quantitative conclusions |
| Video cannot be downloaded | Save screenshots, thumbnails, storyboard frames, or transcript | Analyze visible frame/metadata and mark video-depth as partial |
| Active ad library page blocks automation | Use logged-in browser/manual capture if available | Archive URL, timestamp, and monitoring task without inventing ad details |
| Report and sample tables disagree | Treat sample tables as source of truth and regenerate charts/report | Add a source note explaining unresolved conflict |
| KPI data is unavailable | Write R&D/BI event requirements and formulas | Do not estimate ROI/CPI/ROAS as project facts |
| Public package has stale duplicates | Remove or rename old files after syncing latest reports/assets | Keep a backup outside the public package |

## Anti-Patterns

- Do not treat competitor CPI, ROI, ROAS, retention, or LTV as the target game's facts.
- Do not use Steam/PC evidence for the current mobile plan unless explicitly requested.
- Do not write process notes, tool logs, or revision history into final reports.
- Do not add charts as decoration.
- Do not decide creative quality by CPI alone.
- Do not keep repeated strategy paragraphs across pages or reports.
- Do not publish files that depend on remote-only images or app-only shells.
- Do not leave source tables or public pages with corrupted encoding.
- Do not silently skip source archiving.

## Deliverables

- `project_brief.md`: product facts, stage, target regions, competitor set, constraints.
- `source_inventory.csv`: auditable source index.
- `creative_samples.csv`: ad/material sample library.
- `social_ops_samples.csv`: official account operations samples.
- `ua_test_plan.csv`: paid media test cells and decision thresholds.
- `ops_metrics_requirements.csv`: data and tracking requirements for R&D/BI.
- `research_report.html`: competitor operations research report with screenshots, tables, charts, and source notes.
- `marketing_plan.html`: actionable operations/marketing plan.
- `public_package/`: portable offline folder with all report assets.

## References

Read only what the task needs:

- `references/workflow-detail.md`: operating flow, archive discipline, report packaging checklist.
- `references/sample-schemas.md`: columns for source, creative, social, UA, and metric CSVs.
- `references/metrics-and-tracking.md`: KPI formulas, event requirements, and R&D request language.
- `references/report-style.md`: final report tone, structure, and anti-repetition rules.

## Completion Checks

- Local sources are archived or missing-source gaps are explicit.
- Mobile/current-stage scope is separated from `Later`.
- P0/P1/P2/Later labels are applied consistently.
- Creative, social, UA, KPI, and report sections cross-reference the same sample/source IDs.
- Charts are regenerated from current tables.
- Final reports contain no process traces.
- Static export/public package opens locally and uses the latest files.
- Source appendix contains URLs or local paths for claims and charts.
