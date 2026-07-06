# Sample Schemas

## source_inventory.csv

Recommended columns:

`source_id, collected_at, platform, source_type, competitor, stage, url, local_path, title, summary, evidence_level, mobile_relevance, notes`

## creative_samples.csv

Recommended columns:

`sample_id, collected_at, competitor, platform, channel, stage, priority, source_url, local_asset_path, format, hook_type, first_3_seconds, visual_promise, conflict, cta, landing_bridge, product_truth_risk, user_sentiment_risk, yeeyo_action, metric_to_watch, evidence_level`

Priority:

- `P0`: immediate current mobile use.
- `P1`: relevant but needs filtering.
- `P2`: background reference.
- `Later`: not current-stage use.

## social_ops_samples.csv

Recommended columns:

`sample_id, collected_at, competitor, platform, account, post_url, local_asset_path, post_type, content_column, operation_job, user_action, cta, reusable_pattern, yeeyo_column, evidence_level`

Content columns can include: code/welfare, event notice, guide, creator prompt, UGC challenge, gameplay moment, hero/tower/enemy spotlight, update announcement, community service, complaint response.

## ua_test_plan.csv

Recommended columns:

`test_id, stage, region, channel, platform, creative_id, hook_type, format, landing_page, budget_tier, hypothesis, success_metric, guardrail_metric, stop_condition, scale_condition, source_sample_ids`

## ops_metrics_requirements.csv

Recommended columns:

`requirement_id, metric, formula, events_needed, dimensions_needed, owner, priority, why_needed, decision_supported, validation_method`

## report_sources.csv

Recommended columns:

`report_section, claim_or_chart, source_ids, local_paths, generated_at, notes`
