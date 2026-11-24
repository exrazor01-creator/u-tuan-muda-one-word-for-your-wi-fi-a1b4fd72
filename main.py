#!/usr/bin/env python3
"""Entry for One Word for Your Wi-Fi.

Writes exactly one word (1 to 20 characters, no spaces) describing home
Wi-Fi to /output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

WORD = "Schrödinger"

LIMIT = 20
FORBIDDEN = (" ", "\n", "\r", "\t")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must be exactly one word, no spaces")


def _validate(text):
    """Refuse anything that is not exactly one word inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    if not text.isalpha():
        raise ValueError("entry must be a single word of letters")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
