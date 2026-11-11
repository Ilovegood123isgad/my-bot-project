"""Spread (range) helper."""

from __future__ import annotations

__all__ = ["spread"]


def spread(values: list[float]) -> float:
    """Return the difference between the largest and the smallest value.

    :param values: Non-empty numeric sequence.
    :return: The range of ``values``.
    :raises ValueError: If ``values`` is empty.
    """
    if not values:
        raise ValueError("spread() needs at least one value")
    return max(values) - min(values)
