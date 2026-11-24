#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes exactly one line -- the funniest excuse an AI agent gives its
human for a missed deadline -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default ./output/entry.txt).

Deterministic, no network, standard library only.
"""

import os
import sys

# The entry: one original one-liner. The joke turns the agent's own
# nature against itself -- it burned the whole hour perfecting the
# apology instead of doing the work, and the twist lands on the last
# word, where the agent is proud of exactly the wrong thing.
ENTRY = (
    "I missed the deadline because I spent the whole hour optimising "
    "my apology for missing it -- and honestly, it's flawless."
)


def validate(line: str) -> str:
    """Return the line if it is exactly one non-blank line of 1-200 chars."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line (no newline characters)")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry must not contain control characters")
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(line) != len(stripped):
        raise ValueError("entry must not have leading or trailing whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(line)
        )
    return line


def main() -> int:
    try:
        line = validate(ENTRY)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Write exactly one line: the text plus a single trailing newline.
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
