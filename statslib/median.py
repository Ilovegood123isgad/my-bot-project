"""Median helper."""

from __future__ import annotations

__all__ = ["median"]


def median(values: list[float]) -> float:
    """Return the middle value of a non-empty sequence.

    For an even number of values the result is the average of the two middle
    values.

    :param values: Non-empty numeric sequence.
    :return: The median of ``values``.
    :raises ValueError: If ``values`` is empty.
    """
    if not values:
        raise ValueError("median() needs at least one value")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2
