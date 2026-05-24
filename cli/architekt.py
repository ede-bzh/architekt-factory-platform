#!/usr/bin/env python3
"""architekt — alias for sf (ADR-001).

Thin wrapper that imports and runs main from cli/sf.py (same argparse).
"""

import os
import sys

_cli_dir = os.path.dirname(os.path.abspath(__file__))
_sf_dir = os.path.dirname(_cli_dir)
if _sf_dir not in sys.path:
    sys.path.insert(0, _sf_dir)

from cli.sf import main

if __name__ == "__main__":
    main()
