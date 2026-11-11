#!/usr/bin/env python3
"""Compatibility layer for the statslib package.

Run `python3 stats.py 1 2 3 4` to print a summary of the numbers.
"""

from __future__ import annotations

import sys

from statslib import main, mean, median, percentile, spread, summarize
# Re-exported for compatibility with the previous stats.py.
from statslib.main import __version__

__all__ = ["main", "mean", "median", "percentile", "spread", "summarize"]


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
