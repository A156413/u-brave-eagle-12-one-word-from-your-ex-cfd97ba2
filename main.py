#!/usr/bin/env python3
"""One Word From Your Ex: ghosted.

Writes the single word to /output/entry.txt and prints it.
"""

import os

WORD = "ghosted"
# "ghosted": the ex's one-word verdict for someone who vanished mid-conversation
# without a word — no fight, no goodbye, just read receipts and silence.
# It stings because it is true: everyone has been ghosted, or done the
# ghosting, and the word needs no explanation at all.


def main():
    # Exactly one word, nothing else: no phrase, no sentence, no punctuation.
    # The gate wants 1-24 UTF-8 characters, not only whitespace.
    assert 1 <= len(WORD) <= 24 and WORD.strip() == WORD
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # The grader collects outputs as another user: keep it readable.
    os.chmod(path, 0o644)
    print(WORD)


if __name__ == "__main__":
    main()
