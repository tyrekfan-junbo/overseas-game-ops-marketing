# Metrics And Tracking

## Core Formulas

- `CTR = clicks / impressions`
- `CVR_install = installs / clicks`
- `CPI = spend / installs`
- `CPA_target = spend / target_actions`
- `D1 retention = users active on day 1 / installs`
- `D3 retention = users active on day 3 / installs`
- `D7 retention = users active on day 7 / installs`
- `ARPDAU = daily revenue / daily active users`
- `ARPU = total revenue / users`
- `ARPPU = total revenue / paying users`
- `Pay rate = paying users / active users`
- `LTV_N = cumulative revenue through day N / acquired users`
- `ROI = revenue / spend`
- `ROAS_N = attributed revenue through day N / ad spend`
- `Refund rate = refunded orders / paid orders`
- `Ad engagement rate = rewarded ad impressions or completed ad views / eligible users`

## Minimum Event Requirements

Ask R&D/BI for:

- Acquisition identifiers: install source, campaign, ad group, creative ID, country, platform, device.
- Funnel events: install, first open, tutorial start, tutorial complete, level/mission start, level/mission win, level/mission fail.
- Gameplay progress: tower placement, hero unlock/use, skill use, level reach, first loss point, retry.
- Monetization: purchase view, purchase click, purchase success, SKU, amount, currency, refund, ad impression, ad revenue.
- Retention: daily active by install cohort and campaign.
- Store/community risk: rating, review text, complaint tags, refund/support tickets when available.

## Decision Rules

Do not decide creative quality by CPI alone. Pair:

- Acquisition: CTR, CVR, CPI.
- Product fit: D1/D3/D7 retention, first milestone reach, fail/retry behavior.
- Monetization: ROAS, LTV, ARPU/ARPPU, pay rate, ad revenue.
- Risk: negative reviews, fake-ad complaints, refund/support signals.

## R&D Request Language

Use direct requests:

- Add a stable `creative_id` and `campaign_id` from ad click to game events.
- Export cohort tables by install date, region, platform, channel, campaign, ad group, and creative.
- Record the first 10-minute progression funnel so UA hooks can be matched against real playable content.
- Add review/complaint tags for “ad mismatch”, “paywall”, “crash”, “balance”, “fake gameplay”, and “localization”.
