"""Command line entry point."""

from __future__ import annotations

import sys

from .summarize import summarize

__version__ = "1.0.0"

__all__ = ["main"]


def main(argv: list[str]) -> int:
    """Run the command line interface.

    :param argv: Command line arguments, without the program name.
    :return: Process exit status: 0 on success or for ``--version``, 2 on
        usage errors.
    """
    if argv == ["--version"]:
        print(f"stats {__version__}")
        return 0
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
