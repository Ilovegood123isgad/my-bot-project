#!/usr/bin/env python3
"""Small statistics helpers used by the sample project.

Run `python3 stats.py 1 2 3 4` to print a summary of the numbers.
"""

from __future__ import annotations

import sys


def mean(values: list[float]) -> float:
    """Arithmetic mean of a non-empty sequence."""
    if not values:
        raise ValueError("mean() needs at least one value")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Middle value of a non-empty sequence.

    For an even number of values this is the average of the two middle ones.
    """
    if not values:
        raise ValueError("median() needs at least one value")
    ordered = sorted(values)
    middle = len(ordered) // 2
    return ordered[middle]


def spread(values: list[float]) -> float:
    """Difference between the largest and the smallest value."""
    if not values:
        raise ValueError("spread() needs at least one value")
    return max(values) - min(values)


def summarize(values: list[float]) -> str:
    """One-line human readable summary."""
    return (
        f"count={len(values)} "
        f"mean={mean(values):.2f} "
        f"median={median(values):.2f} "
        f"spread={spread(values):.2f}"
    )


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: python3 stats.py <number> [<number> ...]", file=sys.stderr)
        return 2
    try:
        values = [float(item) for item in argv]
    except ValueError:
        print("every argument must be a number", file=sys.stderr)
        return 2
    print(summarize(values))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
