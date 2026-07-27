"""Metamorphic tests for source transformations and fingerprint stability."""

import tempfile
from pathlib import Path

from bbt.adapters.git_source_state import GitSourceStateProvider


def test_line_ending_transformation_preserves_fingerprint():
    """Verify that CRLF vs LF line endings produce identical project_fingerprint."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        projects_dir = tmp_path / "projects"
        projects_dir.mkdir(parents=True)

        narrative_file = projects_dir / "math.md"

        # LF content
        narrative_file.write_bytes(b"# Math Project\n\n**Purpose:** Rigorous calculus.\n")
        provider_lf = GitSourceStateProvider(tmp_path)
        fp_lf = provider_lf.calculate_project_fingerprint()

        # CRLF content
        narrative_file.write_bytes(b"# Math Project\r\n\r\n**Purpose:** Rigorous calculus.\r\n")
        provider_crlf = GitSourceStateProvider(tmp_path)
        fp_crlf = provider_crlf.calculate_project_fingerprint()

        # Metamorphic Property: Fingerprint must be invariant under line ending transformation
        assert fp_lf == fp_crlf
