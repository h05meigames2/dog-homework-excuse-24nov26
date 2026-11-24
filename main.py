#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun entry.

A single line, under 200 characters, in which a dog explains why the
homework got eaten. Validates the line, prints it, writes it to
/output/entry.txt, and verifies the round-trip.
"""

import os
import sys

ENTRY_LINE = "I only meant to sniff the homework, but it smelled of bacon, fear, and overdue library books — so I graded it myself. A+ for flavor, F for survival, and the essay on self-control tasted best of all."


def validate(line: str) -> None:
    if not line:
        raise ValueError("entry line is empty")
    if line != line.strip():
        raise ValueError("entry line has leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")


def main() -> int:
    validate(ENTRY_LINE)
    print(ENTRY_LINE)
    print(f"characters: {len(ENTRY_LINE)}")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    with open(out_path, "r", encoding="utf-8") as f:
        round_tripped = f.read().rstrip("\n")
    if round_tripped != ENTRY_LINE:
        raise RuntimeError("round-trip verification failed")
    print(f"wrote {out_path} (round-trip OK)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
