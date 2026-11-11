"""Arithmetic mean helper."""

from __future__ import annotations

__all__ = ["mean"]


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty sequence.

    :param values: Non-empty numeric sequence.
    :return: The arithmetic mean of ``values``.
    :raises ValueError: If ``values`` is empty.
    """
    if not values:
        raise ValueError("mean() needs at least one value")
    return sum(values) / len(values)
