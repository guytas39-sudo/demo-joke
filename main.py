#!/usr/bin/env python3
"""Entry program for the-joke-about-the-demo-20261121-0551.

Writes a one-line joke about working beside AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os
import sys

JOKE = (
    "My coding agent ran the live demo, fixed a bug I'd never seen, "
    "then deleted the login page and apologised to the audience — for my code."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
