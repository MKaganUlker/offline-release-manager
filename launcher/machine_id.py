"""
Machine identification logic.

Purpose:
- Provide a deterministic, non-secret identifier
- Used only for version selection
"""

import socket
import uuid


def get_machine_id() -> str:
    hostname = socket.gethostname()
    node = uuid.getnode()
    return f"{hostname}-{node}"
