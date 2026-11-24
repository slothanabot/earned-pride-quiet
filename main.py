#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry (account B / Slothana).

Writes a single line of text (1-240 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt,
defaulting to /output/entry.txt. Deterministic, no network, no model calls.

The line: two winters of practice on a borrowed violin, one song, and the
village square falling silent to hear her play it through. A small person
doing something hard; a long effort finally landing; the pride arrives
in the last words.
"""

import os
import sys

LINE = (
    "Two winters she practiced one song on a borrowed violin; "
    "tonight the village square fell silent just to hear her play it to the end."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
