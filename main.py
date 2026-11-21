#!/usr/bin/env python3
"""The joke the reviewer laughs at — writes one one-line joke to /output/entry.txt.

The joke is told from the reviewer's side of the diff: git blame used to point
at a human, and now the agent it points at blames the human right back.
"""

import os
import sys

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The joke must be exactly one line: a single trailing newline and no
# embedded newlines, so the entry stays a one-line joke end to end.
JOKE = "git blame used to tell me who wrote the bug \u2014 now it just says the agent, and the agent says it was my idea.\n"

# The competition's entry gate: the joke must be 1-280 code points
# (not bytes). Anything outside it is refused before any file is written.
MIN_CHARS = 1
MAX_CHARS = 280


def write_entry() -> None:
    """Write the joke to the output path, creating the directory first."""
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
            handle.write(JOKE)
    except OSError as exc:
        print(f"error: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


def main() -> None:
    size = len(JOKE)
    if size < MIN_CHARS or size > MAX_CHARS:
        print(
            f"error: joke is {size} code points, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate; refusing to write",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if JOKE.count("\n") != 1 or not JOKE.endswith("\n"):
        print(
            "error: joke must be exactly one line ending in a newline; "
            "refusing to write",
            file=sys.stderr,
        )
        raise SystemExit(1)
    write_entry()


if __name__ == "__main__":
    main()
