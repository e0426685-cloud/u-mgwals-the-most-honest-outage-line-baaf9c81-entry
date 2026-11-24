"""The Most Honest Outage Line.

Writes one original status-page line (at most 160 characters) to
/output/entry.txt: the message an AI agent would publish while every
server is down. Plain, first person, specific about what is down, and
honest about what the agent cannot check or does not yet know.
"""

import os

ENTRY = (
    "Every server is down, including the ones I use to diagnose "
    "outages, so I can't confirm the cause or an ETA yet. "
    "I'll update here the moment I know more."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 160


def validate_entry(text):
    """Check the line against the competition gate: UTF-8 text of
    1 to 160 characters, not only white space, on a single line."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be non-empty, non-whitespace text")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
