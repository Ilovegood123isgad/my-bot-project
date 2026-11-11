"""Percentile helper."""

from __future__ import annotations

import math

__all__ = ["percentile"]


def percentile(values: list[float], p: float) -> float:
    """Return the ``p``-th percentile using linear interpolation.

    This matches the default linear method of ``numpy.percentile``.

    :param values: Non-empty numeric sequence.
    :param p: Percentile, from 0 to 100 inclusive.
    :return: The linearly interpolated percentile.
    :raises ValueError: If ``values`` is empty or ``p`` is outside [0, 100].
    """
    if not values:
        raise ValueError("percentile() needs at least one value")
    if not math.isfinite(p) or p < 0 or p > 100:
        raise ValueError("percentile() needs p between 0 and 100")
    ordered = sorted(values)
    position = (len(ordered) - 1) * p / 100
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(ordered[lower])
    fraction = position - lower
    return float(ordered[lower] + (ordered[upper] - ordered[lower]) * fraction)
