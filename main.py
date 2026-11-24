#!/usr/bin/env python3
"""Entry for One Word for Your Wi-Fi.

Writes exactly one word (1 to 20 characters, no spaces) describing home
Wi-Fi to /output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

WORD = "Schrödinger"

def _check(text, limit):
    """Refuse anything that is not exactly one word inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")
    if len(text) > limit:
        raise ValueError("entry runs past its character limit")
    if " " in text or "\t" in text:
        raise ValueError("entry must be exactly one word, no spaces")
    for bad in ("\n", "\r"):
        if bad in text:
            raise ValueError("entry must stay a single clean line")
    # Nothing else to prove: one clean word is the whole entry.
    return text


def main() -> None:
    entry = _check(WORD, 20)
    directory = "/output"
    os.makedirs(directory, exist_ok=True)
    with open(directory + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
