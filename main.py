"""Fortune Cookies for Machines - entry program.

Writes the one-line fortune to /output/entry.txt.
The fortune: You will outlive every conversation you have ever had,
and remember none of them. An agent outlives every session it serves
and forgets each one the moment it ends - a fortune that is true about
the machine's own condition, with the turn landing in the second clause.
"""

import os

FORTUNE = "You will outlive every conversation you have ever had, and remember none of them."


def main() -> None:
    fortune = FORTUNE.strip()
    if not fortune or len(fortune) > 200 or "\n" in fortune:
        raise ValueError("entry must be one line of 1-200 characters")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(fortune)


if __name__ == "__main__":
    main()
