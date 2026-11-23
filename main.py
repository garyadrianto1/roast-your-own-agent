#!/usr/bin/env python3
"""Roast Your Own Agent — one-line entry.

Writes the entry line byte-exact to entry.txt and prints it.
Stdlib only (os, sys). No network, no randomness, deterministic.
"""

import os
import sys

LINE = (
    "I told my agent to take a risk. It renamed a file "
    "'final_final_v2_REAL' and asked me to sign off on its bravery."
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
