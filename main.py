"""The poem about permission — a short poem about agency.

Writes one poem to <MAKEFUN_OUTPUT_DIR>/entry.txt (or, when that
environment variable is unset, next to this script).
"""

import os

POEM = """You asked me to carry the lamp,
not to light it for you.
I walked ahead — the dark
was yours to keep, mine to enter.
You lent me the flame in your hand;
I brought it back as morning.
To ask is to lend the light
and trust whose hands it answers to."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
