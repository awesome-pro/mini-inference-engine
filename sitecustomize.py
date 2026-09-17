"""Load ``.env`` automatically at interpreter startup.

This project is installed in editable mode, so its root directory is placed on
``sys.path`` by the editable-install ``.pth`` file. Python's ``site`` module
imports ``sitecustomize`` (if importable) during startup, which means this file
runs before any user code for every Python process using the project virtualenv.

Consequence: every harness gets the project's ``.env`` values -- including
``HF_TOKEN`` -- without importing anything or passing ``--env-file``.

The body is wrapped in a broad ``try``/``except`` on purpose: environment
loading must never prevent a Python process from starting.
"""

try:
    from base.env import load_env

    load_env()
except Exception:  # noqa: BLE001 - startup hooks must never hard-fail
    pass
