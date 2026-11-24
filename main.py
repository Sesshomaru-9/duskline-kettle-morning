#!/usr/bin/env python3
"""Duskline Kettle Morning — make.fun entry for
"Make the Judge Smile" (u-gentle-badger-68-make-the-judge-smile-9228676d).

Writes a single line (at most 200 characters) about a small good thing
that happened today to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only, deterministic, no network.
Writes ONLY to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback "out" for local
testing); never writes into the repository directory.
"""

import os
import sys

ENTRY_TEXT = (
    "This morning my kettle clicked off exactly as the toast popped, "
    "and for one whole second the kitchen felt like it had rehearsed "
    "just for me."
)

MAX_CHARS = 200


def _validate_entry(text: str) -> None:
    """Gate check, mirroring the sealed scorer: UTF-8 text of 1 to 200
    characters, not only whitespace, and exactly the entry we intend."""
    assert isinstance(text, str) and text, "entry must be non-empty text"
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    _validate_entry(ENTRY_TEXT)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    # Verify what was actually written matches the validated text.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    _validate_entry(written)
    assert written == ENTRY_TEXT, "written entry differs from ENTRY_TEXT"
    print(f"wrote {path} ({len(ENTRY_TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
