#!/usr/bin/env python3
"""Tests for the stats.py --version flag. Run with `python3 test_cli_version.py`."""

import contextlib
import io
import subprocess
import sys
import unittest
from pathlib import Path

from stats import main

STATS_SCRIPT = Path(__file__).with_name("stats.py")


class VersionFlagTests(unittest.TestCase):
    def test_prints_version_and_succeeds(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            status = main(["--version"])
        self.assertEqual(status, 0)
        self.assertEqual(stdout.getvalue(), "stats 1.0.0\n")

    def test_command_prints_version_and_exits_zero(self):
        result = subprocess.run(
            [sys.executable, str(STATS_SCRIPT), "--version"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "stats 1.0.0\n")
        self.assertEqual(result.stderr, "")


class ExistingBehaviorTests(unittest.TestCase):
    def test_numbers_still_print_summary(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            status = main(["1", "2", "3", "4"])
        self.assertEqual(status, 0)
        self.assertEqual(
            stdout.getvalue(),
            "count=4 mean=2.50 median=2.50 spread=3.00\n",
        )

    def test_no_arguments_still_prints_usage(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            status = main([])
        self.assertEqual(status, 2)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(
            stderr.getvalue(),
            "usage: python3 stats.py <number> [<number> ...]\n",
        )

    def test_bad_argument_still_exits_two(self):
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            status = main(["3", "oops"])
        self.assertEqual(status, 2)
        self.assertEqual(stdout.getvalue(), "")
        self.assertEqual(stderr.getvalue(), "every argument must be a number\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
