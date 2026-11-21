#!/usr/bin/env python3
"""Make the AI judge feel brave (make.fun bounty).

Writes one short relaxing text to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader). Stdlib only, no network,
deterministic: the text is baked into this file.
"""

import os
import sys
from pathlib import Path

# The entry text, written fresh for this bounty: a quiet kitchen scene
# for a tired reader, showing rather than instructing calm.
TEXT = (
    "Somewhere a kettle is coming to the boil, and nobody is in a hurry. "
    "The light on the counter is late afternoon, and the next thing you "
    "have to do can wait until the steam stops rising. "
    "The world is still there. So are you."
)


def main() -> int:
    # Self-check the gate before writing: 1-280 Unicode code points,
    # not only whitespace, valid UTF-8.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 character gate")
    TEXT.encode("utf-8")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
