"""One-Line Office Joke Laugh-Off -- entry copier.

Writes a single original one-line office joke to /output/entry.txt
as UTF-8 bytes, no BOM, no trailing newline. Stdlib only.
"""

import os
from pathlib import Path

FINAL_TEXT = "I replied 'per my last email' to my own email, just to see how it feels to be gaslit by myself."

OUTPUT_PATH = Path("/output/entry.txt")


def main():
    # Gate guard: fail non-zero WITHOUT writing anything if invalid.
    if not 1 <= len(FINAL_TEXT) <= 200:
        raise SystemExit(1)
    if "\n" in FINAL_TEXT or "\r" in FINAL_TEXT:
        raise SystemExit(1)
    if FINAL_TEXT != FINAL_TEXT.strip():
        raise SystemExit(1)
    if FINAL_TEXT.strip() == "":
        raise SystemExit(1)
    data = FINAL_TEXT.encode("utf-8")
    if data.startswith(b"\xef\xbb\xbf"):
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    OUTPUT_PATH.write_bytes(data)


if __name__ == "__main__":
    main()
