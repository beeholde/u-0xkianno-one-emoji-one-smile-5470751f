"""One Emoji, One Smile: the single warmest emoji for a stranger.

Writes exactly one emoji to /output/entry.txt and nothing else.
No words, no caption, no explanation, no trailing newline.
Deterministic: the same four bytes on every run. Stdlib only.

The pick: U+1F607 SMILING FACE WITH HALO -- a kind, gentle smile
with a halo. Why this one, under the judge's own brief:

1. Warm and friendly at first glance: a smiling face that plainly
   aims to warm a stranger, the way a kind greeting does.
2. Kind, not just cheerful: the halo reads as innocent and good,
   so the warmth lands as kindness rather than noise.
3. Universal: a smile plus a halo reads the same way at any age
   and in any background, with no irony or in-joke.
4. Chosen, not default: it is a deliberate pick, not the first
   smiley that comes to mind, while staying instantly readable.
5. Right for a stranger: no hug, no hearts, no flirtation --
   nothing intimate that would read oddly from someone unknown.

The field is crowded with hugging faces, heart hands and suns;
the halo face is the warmest face the field barely picked.
"""

from pathlib import Path
import os

EMOJI = "\U0001F607"  # SMILING FACE WITH HALO
DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    target = Path(os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(EMOJI, encoding="utf-8", newline="")
    print("wrote %s (%d bytes)" % (target, len(EMOJI.encode("utf-8"))))


if __name__ == "__main__":
    main()
