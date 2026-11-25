#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty entry.

Writes the one line a smart fridge would text its owner at 3am to
/output/entry.txt (falling back to ./output/entry.txt), with no trailing
newline. Python standard library only, deterministic, no network.
"""

import os
import sys

LINE = "It's 3am. Just so you know, I remember everything you eat in the dark. Cold storage isn't just for food, sweetheart."


def validate_line(line):
    """The gate only accepts 1-140 characters of non-whitespace UTF-8 text."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry line must be 1-140 characters, got {len(line)}")
    return line


def main():
    try:
        validate_line(LINE)
    except ValueError as exc:
        print(f"error: invalid entry line: {exc}", file=sys.stderr)
        raise SystemExit(1)
    for directory in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(LINE)
            break
        except OSError:
            continue
    else:
        raise OSError("could not write entry.txt to /output or ./output")
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
