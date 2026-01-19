"""
Machine identification logic.

This module provides a deterministic, non-secret identifier
used ONLY for version selection logic.

Security note:
- This is NOT authentication
- This value is not transmitted
"""

import socket
import uuid


def get_machine_id() -> str:
    """
    Generate a stable identifier for the current machine.

    Combines:
    - Hostname
    - Hardware node identifier

    Returns:
        str: deterministic machine identifier
    """
    hostname = socket.gethostname()
    node_id = uuid.getnode()
    return f"{hostname}-{node_id}"
