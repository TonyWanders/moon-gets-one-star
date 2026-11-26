#!/usr/bin/env python3
"""The Moon Gets One Star: a one-star review of the Moon, 120 chars max.

Writes the review to /output/entry.txt (or the path given as the first
argument, or $OUTPUT_PATH). Deterministic: the same bytes on every run.
"""

import os
import sys

REVIEW = (
    "One star. Shows up late, floods my bedroom with light, "
    "then vanishes for a week without a word. Worst roommate ever."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def write_entry(path, text):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    assert len(REVIEW) <= 120, f"review is {len(REVIEW)} chars, over the 120 limit"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    write_entry(path, REVIEW)


if __name__ == "__main__":
    main()
