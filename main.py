#!/usr/bin/env python3
"""Write the one-word internet entry to /output/entry.txt.

One word for the whole internet: "feral". It is funny by itself, true
about the internet as a whole (wild, unmoderated, full of strange
creatures that cannot be domesticated), surprising rather than the
obvious first word, and five letters long so it lands in one beat.
"""
import os

TEXT = "feral"

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")
    # Gate self-check: UTF-8 text, 1-30 chars, not only whitespace.
    data = open("/output/entry.txt", encoding="utf-8").read()
    assert 1 <= len(data) <= 30 and data.strip(), "gate failed: entry must be 1-30 non-blank chars"

if __name__ == "__main__":
    main()
