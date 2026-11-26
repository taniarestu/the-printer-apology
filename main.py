#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one single-line apology from an office printer to /output/entry.txt.
Deterministic, Python 3 stdlib only, no network.

Gate (from the kit): /output/entry.txt must be UTF-8 text of 1 to 120
characters, not only white space, on a single line.
"""

import os

ENTRY = (
    "Sorry I ate your report. The cheap paper tasted like cardboard, "
    "the staple attacked first, and honestly, I quit."
)

MAX_CHARS = 120


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= MAX_CHARS, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    text.encode("utf-8")  # must be valid UTF-8

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Gate guard: re-read what was written and verify it passes the gate.
    with open(out_path, "rb") as f:
        raw = f.read()
    written = raw.decode("utf-8")  # raises if not valid UTF-8
    assert written == text + "\n", "written bytes differ from entry"
    body = written.rstrip("\n")
    assert 1 <= len(body) <= MAX_CHARS, f"written length {len(body)} out of range"
    assert body.strip(), "written entry must not be only whitespace"
    assert "\n" not in body and "\r" not in body, "written entry must be one line"
    assert len(raw) == len(written.encode("utf-8")), "byte/char mismatch"


if __name__ == "__main__":
    main()
