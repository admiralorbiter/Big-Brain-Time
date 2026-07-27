"""Deterministic Re-entry Pack compiler using domain ports."""

from typing import Optional
from bbt.ports.ports import (
    ProjectTransitionRepository,
    ProjectNarrativeRepository,
    SourceStateProvider,
    Clock,
)
from bbt.packs.project_continuity.models import (
    ReentryPack,
    ReentryStatus,
    ReentryManifest,
    SourceState,
)


class ReentryCompiler:
    """Compiles deterministic, cited Re-entry Packs via injected ports."""

    def __init__(
        self,
        project_id: str,
        transitions: ProjectTransitionRepository,
        narratives: ProjectNarrativeRepository,
        source_state: SourceStateProvider,
        clock: Clock,
    ):
        self.project_id = project_id
        self.transitions = transitions
        self.narratives = narratives
        self.source_state = source_state
        self.clock = clock

    def compile(self) -> ReentryPack:
        """Compile a cited Re-entry Pack artifact."""
        narrative_doc = self.narratives.get_canonical_narrative(self.project_id)
        read_result = self.transitions.read_current(self.project_id)
        snapshot = self.source_state.snapshot(self.project_id)
        now_dt = self.clock.now()
        now_iso = now_dt.isoformat().replace("+00:00", "Z")

        latest_t = read_result.latest

        # Determine ReentryStatus
        if read_result.degraded:
            status = ReentryStatus.DEGRADED
        elif not latest_t:
            status = ReentryStatus.NO_TRANSITION_RECORDED
        elif snapshot.state in (SourceState.PROJECT_CHANGED, SourceState.UNCOMMITTED_PROJECT_CHANGES):
            status = ReentryStatus.STALE
        else:
            status = ReentryStatus.READY

        manifest = ReentryManifest(
            compiler="bbt.reentry-compiler/v0.1",
            compiled_at=now_iso,
            project_id=self.project_id,
            git_revision=snapshot.repository_head or "git:uncommitted-or-none",
            project_fingerprint=snapshot.project_fingerprint,
            latest_transition_id=latest_t.id if latest_t else None,
            transition_recorded_at=latest_t.recorded_at if latest_t else None,
        )

        return ReentryPack(
            status=status,
            project_name=narrative_doc.title,
            compiled_at=now_iso,
            project_narrative=narrative_doc.content,
            latest_transition=latest_t,
            source_snapshot=snapshot,
            manifest=manifest,
            diagnostics=read_result.diagnostics,
        )
