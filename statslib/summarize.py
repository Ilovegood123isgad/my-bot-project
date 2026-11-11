"""One-line summary helper."""

from __future__ import annotations

from .mean import mean
from .median import median
from .spread import spread

__all__ = ["summarize"]


def summarize(values: list[float]) -> str:
    """Return a one-line human readable summary of ``values``.

    :param values: Non-empty numeric sequence.
    :return: Text of the form ``count=<n> mean=<m> median=<d> spread=<s>``.
    :raises ValueError: If ``values`` is empty.
    """
    return (
        f"count={len(values)} "
        f"mean={mean(values):.2f} "
        f"median={median(values):.2f} "
        f"spread={spread(values):.2f}"
    )
