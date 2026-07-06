#!/usr/bin/env python3
"""Create a reusable overseas mobile game operations research workspace."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path


TABLES = {
    "source_inventory.csv": [
        "source_id",
        "collected_at",
        "platform",
        "source_type",
        "competitor",
        "stage",
        "url",
        "local_path",
        "title",
        "summary",
        "evidence_level",
        "mobile_relevance",
        "notes",
    ],
    "creative_samples.csv": [
        "sample_id",
        "collected_at",
        "competitor",
        "platform",
        "channel",
        "stage",
        "priority",
        "source_url",
        "local_asset_path",
        "format",
        "hook_type",
        "first_3_seconds",
        "visual_promise",
        "conflict",
        "cta",
        "landing_bridge",
        "product_truth_risk",
        "user_sentiment_risk",
        "yeeyo_action",
        "metric_to_watch",
        "evidence_level",
    ],
    "social_ops_samples.csv": [
        "sample_id",
        "collected_at",
        "competitor",
        "platform",
        "account",
        "post_url",
        "local_asset_path",
        "post_type",
        "content_column",
        "operation_job",
        "user_action",
        "cta",
        "reusable_pattern",
        "yeeyo_column",
        "evidence_level",
    ],
    "ua_test_plan.csv": [
        "test_id",
        "stage",
        "region",
        "channel",
        "platform",
        "creative_id",
        "hook_type",
        "format",
        "landing_page",
        "budget_tier",
        "hypothesis",
        "success_metric",
        "guardrail_metric",
        "stop_condition",
        "scale_condition",
        "source_sample_ids",
    ],
    "ops_metrics_requirements.csv": [
        "requirement_id",
        "metric",
        "formula",
        "events_needed",
        "dimensions_needed",
        "owner",
        "priority",
        "why_needed",
        "decision_supported",
        "validation_method",
    ],
    "report_sources.csv": [
        "report_section",
        "claim_or_chart",
        "source_ids",
        "local_paths",
        "generated_at",
        "notes",
    ],
}


def write_csv(path: Path, header: list[str]) -> None:
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerow(header)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_name", help="Game or publishing project name")
    parser.add_argument("--out", default=".", help="Output parent directory")
    parser.add_argument("--stage", default="first production")
    parser.add_argument("--competitors", default="", help="Comma-separated competitors")
    parser.add_argument("--regions", default="", help="Comma-separated target regions")
    args = parser.parse_args()

    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in args.project_name).strip("-")
    root = Path(args.out).resolve() / slug
    dirs = [
        "sources/raw",
        "sources/screenshots",
        "sources/video_frames",
        "samples",
        "charts",
        "reports",
        "exports/public_package",
        "working",
    ]
    for d in dirs:
        (root / d).mkdir(parents=True, exist_ok=True)

    for filename, header in TABLES.items():
        write_csv(root / "samples" / filename, header)

    brief = root / "project_brief.md"
    if not brief.exists():
        brief.write_text(
            "\n".join(
                [
                    f"# {args.project_name} Overseas Operations Brief",
                    "",
                    f"- Stage: {args.stage}",
                    f"- Competitors: {args.competitors or 'TBD'}",
                    f"- Target regions: {args.regions or 'TBD'}",
                    "- Platforms: Android, iOS, TapTap Global, other mobile channels as needed",
                    "- Current goal: define social account plan, creative test plan, UA channels, tracking requirements, and launch report",
                    "",
                    "## Product Facts",
                    "",
                    "- Genre/core loop:",
                    "- First 10-minute player experience:",
                    "- Monetization:",
                    "- Available assets:",
                    "- Must show:",
                    "- Must avoid:",
                    "",
                    "## Open Questions",
                    "",
                    "- What gameplay can honestly bridge from ad hook to in-game experience?",
                    "- What events are already tracked?",
                    "- Which regions and channels are available for first tests?",
                ]
            ),
            encoding="utf-8",
        )

    manifest = {
        "project_name": args.project_name,
        "stage": args.stage,
        "competitors": [x.strip() for x in args.competitors.split(",") if x.strip()],
        "regions": [x.strip() for x in args.regions.split(",") if x.strip()],
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "folders": dirs,
        "tables": list(TABLES),
    }
    (root / "workspace_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
