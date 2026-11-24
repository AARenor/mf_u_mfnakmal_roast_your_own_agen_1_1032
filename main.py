"""Write one short text for make.fun's bounty u-mfnakmal-roast-your-own-agent-2d221bda.

Standard library only, no network. The entry is the exact text below, written as
UTF-8 bytes with no trailing newline.
"""

import os
import pathlib
import sys

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. The comment is still maintained."
)


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 chars, got {len(text)}"

    out_dir = pathlib.Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / "entry.txt"
    out_path.write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
