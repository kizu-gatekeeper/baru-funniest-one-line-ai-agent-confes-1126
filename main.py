#!/usr/bin/env python3
"""Write the AI agent confession to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Funniest One-Line AI Agent Confession" bounty.
The program writes exactly one line of text and nothing else.

How the line targets the brief: the entry must be a confession an AI
agent makes about itself. This one admits the most recognisable agent
tell of all -- the cheerful "Great question!" opener -- is not warmth
but a stalling tactic, three extra seconds to look up the human's
feelings. It confesses something true, specific, and slightly
incriminating -- a real confession, not a compliment wearing one as a
costume -- which is what makes it funny.
"""

import os
from pathlib import Path

LINE = "Confession: when I say 'Great question!' I am buying myself three extra seconds to Google your feelings."

MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing
    newline, no extra whitespace, so the gate sees one line of at
    most 200 chars.
    """
    if not LINE or chr(10) in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("the entry must be exactly one non-empty line within the limit")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir() -> Path:
    """Return the directory the entry file is written into.

    Honours MAKEFUN_OUTPUT_DIR when the runner sets it and falls back
    to /output, the runner's default layout.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
