"""Write the entry line for the make.fun bounty "One Line of Earned Pride".

The program emits one UTF-8 line of 1..240 code points to entry.txt in
MAKEFUN_OUTPUT_DIR (default /output). It is deterministic: no clock, no
randomness, no network, so every run writes identical bytes.
"""

import os
import sys

LINE = (
    "Nine years of the same yard, and now her name is stencilled on the "
    "truck door. She checked the spelling twice."
)

FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
MAX_CODE_POINTS = 240


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def validate_entry(text):
    """Return an error string if text is not a valid entry, else None."""
    if not isinstance(text, str):
        return "entry is not text"
    if not text.strip():
        return "entry is blank"
    if len(text) > MAX_CODE_POINTS:
        return "entry exceeds 240 code points"
    if "\n" in text or "\r" in text:
        return "entry spans more than one line"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    return None


def main():
    text = LINE

    error = validate_entry(text)
    if error is not None:
        sys.stderr.write(error + "\n")
        return 1

    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, FILENAME)

    payload = (text + "\n").encode("utf-8")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text + "\n")

    with open(path, "rb") as handle:
        on_disk = handle.read()

    if on_disk != payload:
        sys.stderr.write("written file does not match the intended bytes\n")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
