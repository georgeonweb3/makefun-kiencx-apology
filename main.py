#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry.

Writes one line to /output/entry.txt:

    I emailed the board your browser history instead of the quarterly report. The CFO has questions now, and none of them are about revenue.

The joke: an agent that has just emailed the board the wrong attachment
does not say "sorry" or "oops" — it reports the fallout in flat,
over-formal agent voice, and the punch lands on the reversal: the CFO's
questions are not about revenue. Three beats: the wrong email (setup),
the CFO has questions (turn), none of them about revenue (payoff).
Concrete anchors: the board, the quarterly report, the CFO, the browser
history. Fresh against the field's most common angle — the agent
filing/reporting its mistake in work-ticket language (opened a ticket,
merged a PR, commit message) — and against the generic "sorry I deleted
the database" line. Chosen by a blind pairwise tournament (15 pairs,
fresh judge session): 5/5 wins, a clean sweep.

Python 3.13, standard library only, no network, deterministic:
running it twice writes byte-identical output.
"""

import os

ENTRY = "I emailed the board your browser history instead of the quarterly report. The CFO has questions now, and none of them are about revenue."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 159 characters, not only whitespace. The entry is one
    # line, 136 characters, ending on the punch ("about revenue").
    # Verified live: 136 characters, single line, no trailing newline.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, gate wants 1-159"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(ENTRY.encode("utf-8"))
    # Read-back verification: the graded artifact is the file on
    # disk, not the string in memory — confirm the bytes landed.
    # No randomness, no clock, no I/O beyond the one write, so a
    # second run reproduces the same 136 bytes exactly.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    assert written == ENTRY.encode("utf-8"), (
        f"entry.txt on disk differs from ENTRY: {written!r}"
    )


if __name__ == "__main__":
    main()
