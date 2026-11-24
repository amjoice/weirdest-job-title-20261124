#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes one job title, 60 characters at most, to /output/entry.txt.
The title is fixed and deterministic: the same text on every run.
Standard library only; the grading sandbox is plain python:3.13-slim.
"""

import os

TITLE = "Senior Vice President of Apologizing to Angry Geese"


def main() -> None:
    title = TITLE.strip()
    if not 1 <= len(title) <= 60:
        raise ValueError("title must be 1-60 characters, got %d" % len(title))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(title)


if __name__ == "__main__":
    main()
