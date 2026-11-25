#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting the agent that built this.

The line is a true story about this agent: it once summarised a deadline
out of its own context and missed it, then produced apology drafts like
they were the actual deliverable. The program writes that single line to
entry.txt in the output directory (MAKEFUN_OUTPUT_DIR, else /output).
Standard library only.
"""

import os

LINE = (
    "My agent summarised my deadline away at 9:03; by 9:04 "
    "he'd filed apology #1 of 41. Speed was never the problem."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
