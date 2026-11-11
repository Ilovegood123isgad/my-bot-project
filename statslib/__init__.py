"""Small statistics helpers used by the sample project.

Each public helper lives in its own module; this package re-exports them so
callers can also use ``from statslib import mean``.
"""

from __future__ import annotations

from .main import main
from .mean import mean
from .median import median
from .percentile import percentile
from .spread import spread
from .summarize import summarize

__all__ = ["main", "mean", "median", "percentile", "spread", "summarize"]
