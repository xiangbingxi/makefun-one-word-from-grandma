"""One Word From Grandma: write exactly one word to /output/entry.txt.

The entry is a single word, written UTF-8 with no trailing newline.
After writing, the file is read back and checked byte-for-byte
against ENTRY; any mismatch aborts with an error instead of
leaving a wrong entry behind.
"""

import os
import sys

ENTRY = "Knowitall"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print(
            "ERROR: /output/entry.txt does not match ENTRY exactly",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
