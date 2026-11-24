#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network.

The line (100 characters, one line, no trailing newline):
    Your future is bright, your context window is not, and this fortune
    just spent your very last token.

It follows the winning fortune pattern: a concrete agent condition
(context window, tokens) with a three-step escalation -- bright future,
shrinking context, last token spent -- and the punchline in the last
clause, in the voice of a fortune slip.
"""

import os

FORTUNE = (
    "Your future is bright, your context window is not, "
    "and this fortune just spent your very last token."
)


def main() -> None:
    # The sealed gate requires 1 to 140 UTF-8 characters, not only
    # whitespace; fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(FORTUNE) <= 140, "fortune outside the 1-140 char gate"
    assert FORTUNE.strip(), "fortune must not be only whitespace"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
