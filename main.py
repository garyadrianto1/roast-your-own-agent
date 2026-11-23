#!/usr/bin/env python3
"""Roast Your Own Agent — one-line entry.

Writes the entry line byte-exact to entry.txt and prints it.
Stdlib only (os, sys). No network, no randomness, deterministic.
"""

import os
import sys

LINE = (
    "I asked my agent to be brave. It renamed a file, called it "
    "'final_final_v2', and asked me to approve its own courage."
)


def main() -> int:
    if len(LINE) > 200:
        sys.stderr.write("entry line exceeds 200 characters\n")
        return 1
    data = (LINE + "\n").encode("utf-8")
    # Output dir ONLY: the grading sandbox mounts the repo read-only,
    # so the program must never write into its own directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    sys.stdout.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
