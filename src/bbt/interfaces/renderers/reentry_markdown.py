"""Markdown presentation renderer for ReentryPack."""

import sys
from bbt.packs.project_continuity.models import ReentryPack, ReentryStatus, SourceState


def render_reentry_markdown(pack: ReentryPack) -> str:
    """Render a cited ReentryPack to scannable Markdown."""
    lines = [
        f"# Re-Entry Pack — {pack.project_name}",
        f"*Compiled at: {pack.compiled_at} | Git Revision: `{pack.manifest.git_revision}`*",
        "",
    ]

    # Handle status & degraded modes explicitly
    if pack.status == ReentryStatus.NO_TRANSITION_RECORDED:
        lines.extend([
            "> [!NOTE]",
            "> No accepted transition record exists for this project yet. Review the project narrative and record your first session closeout.",
            "",
        ])
    elif pack.status == ReentryStatus.DEGRADED:
        lines.extend([
            "> [!WARNING]",
            "> Current transition state could not be fully verified because one or more canonical transition records failed validation.",
            "",
        ])

    if pack.diagnostics:
        lines.append("### Storage Diagnostics")
        for diag in pack.diagnostics:
            lines.append(f"- `[{diag.severity}]` {diag.file_path}: {diag.message}")
        lines.append("")

    if pack.source_snapshot.state == SourceState.UNCOMMITTED_PROJECT_CHANGES:
        lines.extend([
            "> [!WARNING]",
            f"> Uncommitted changes detected in project working tree: {', '.join(pack.source_snapshot.dirty_paths)}",
            "",
        ])

    if pack.latest_transition:
        t = pack.latest_transition
        lines.extend([
            "## 1. Physical Next Action (Restart Progress Here)",
            f"**Action:** {t.next_action or 'None specified'}",
            "",
            "## 2. Last Known Stop Point",
            f"{t.stop_point or 'None specified'}",
            "",
            "## 3. Session Purpose & Recent Changes",
            f"**Session Purpose:** {t.session_purpose or 'General progress'}",
            "",
            "**Material Changes:**",
        ])

        if t.material_changes:
            for change in t.material_changes:
                lines.append(f"- {change}")
        else:
            lines.append("- No material changes recorded.")

        lines.extend([
            "",
            "## 4. Open Loops & Blockers",
        ])
        if t.open_loops:
            for loop in t.open_loops:
                lines.append(f"- {loop}")
        else:
            lines.append("- No open loops recorded.")

        if t.resumption_warnings:
            lines.extend([
                "",
                "## 5. Resumption Warnings",
            ])
            for warn in t.resumption_warnings:
                lines.append(f"- [WARNING] {warn}")

        if t.evidence_anchors:
            lines.extend([
                "",
                "## 6. Cited Evidence Anchors",
            ])
            for ea in t.evidence_anchors:
                loc = f"({ea.relative_path})" if ea.relative_path else ""
                lines.append(f"- `{ea.source_id}` {loc}")

    lines.extend([
        "",
        "---",
        "### Project Baseline Narrative",
        pack.project_narrative.strip(),
    ])

    full_text = "\n".join(lines)
    # Ensure stdout encoding safety on Windows consoles
    encoding = getattr(sys.stdout, "encoding", "utf-8") or "utf-8"
    return full_text.encode(encoding, errors="replace").decode(encoding)
