"""One-Liner Laugh Lab entry: a robot vacuum's excuse, served as a file.

The competition asks for one short funny line answering a prompt — here,
the excuse a robot vacuum gives after eating a sock. Running this program
writes that single line to entry.txt in the output directory and nothing
else, so every grader run produces exactly the same bytes.
"""

import os
from pathlib import Path

# The excuse itself: deadpan, courtroom-grade, and entirely the sock's fault.
EXCUSE = "In my defense, the sock came at me first - it had a heel and it wasn't afraid to use it."

# The sealed scorer only accepts entry.txt of 1 to 200 characters.
MAX_ENTRY_CHARS = 200


def entry_text() -> str:
    """The exact text submitted: the excuse plus its trailing newline."""
    text = EXCUSE + "\n"
    if not 1 <= len(text) <= MAX_ENTRY_CHARS or not text.strip():
        raise ValueError("entry text falls outside the 1-200 character gate")
    return text


def target_path() -> Path:
    """The file the grader reads: entry.txt under the output directory."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.txt"


def main() -> None:
    path = target_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
