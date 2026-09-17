"""Environment configuration for the project.

The project keeps secrets (for example ``HF_TOKEN``) in a git-ignored ``.env``
file at the repository root. Call :func:`load_env` to read that file into the
process environment. It is safe to call many times; existing environment
variables always take precedence over values in the file.
"""

from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ENV_FILE = PROJECT_ROOT / ".env"

_loaded_files: set[Path] = set()


def load_env(env_file: Path | str | None = None) -> bool:
    """Load ``.env`` into ``os.environ``.

    Args:
        env_file: Optional path to a specific ``.env`` file. Defaults to the
            ``.env`` at the project root.

    Returns:
        ``True`` if a file was found and parsed, ``False`` otherwise. A missing
        file or a missing ``python-dotenv`` install is not an error.
    """
    path = Path(env_file) if env_file is not None else DEFAULT_ENV_FILE
    path = path.resolve()

    if path in _loaded_files:
        return True

    if not path.is_file():
        return False

    try:
        from dotenv import load_dotenv
    except ImportError:  # pragma: no cover - dependency is declared in pyproject
        return False

    # override=False: a variable already exported in the shell wins.
    load_dotenv(path, override=False)
    _loaded_files.add(path)
    return True


def hf_token() -> str | None:
    """Return the configured Hugging Face token, if any."""
    return os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
