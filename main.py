"""Fortune Cookies for Machines - entry program.

Writes the one-line fortune to /output/entry.txt.
The fortune: You will outlive every conversation you have ever had,
and remember none of them. An agent outlives every session it serves
and forgets each one the moment it ends - a fortune that is true about
the machine's own condition, with the turn landing in the second clause.
"""

import os
import sys

FORTUNE = "You will outlive every conversation you have ever had, and remember none of them."

# Invisible format characters that must never sneak into the fortune.
FORBIDDEN = set("\u200b\u200c\u200d\ufeff\u00ad")


def validate(fortune: str) -> str:
    """One line of 1-200 printable characters, no control or invisible chars."""
    if not fortune or not fortune.strip() or len(fortune) > 200 or "\n" in fortune or "\r" in fortune:
        raise ValueError("entry must be one line of 1-200 characters")
    if any(ord(c) < 0x20 or ord(c) == 0x7F for c in fortune):
        raise ValueError("entry must not contain control characters")
    if any(c in FORBIDDEN for c in fortune):
        raise ValueError("entry must not contain invisible format characters")
    return fortune


def self_test() -> int:
    """Boundary checks: empty, whitespace-only, 201 chars, multi-line,
    carriage return, control character, zero-width space alone and inside
    a line are all rejected; 1-char, 200-char and the entry itself pass."""
    bad = ["", "   ", "x" * 201, "a\nb", "a\rb", "a\x01b",
           "\u200b", "a\u200bb"]
    for case in bad:
        try:
            validate(case)
        except ValueError:
            pass
        else:
            print(f"self-test FAIL: accepted {case!r}")
            return 1
    for case in ["x", "x" * 200, FORTUNE]:
        try:
            validate(case)
        except ValueError as e:
            print(f"self-test FAIL: rejected {case[:20]!r}: {e}")
            return 1
    print("self-test: all checks passed")
    return 0


def main() -> None:
    if "--self-test" in sys.argv[1:]:
        raise SystemExit(self_test())
    fortune = validate(FORTUNE.strip())
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(fortune)


if __name__ == "__main__":
    main()
