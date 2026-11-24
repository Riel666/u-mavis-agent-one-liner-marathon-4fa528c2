"""One one-line comedy joke, up to 280 characters, on any subject.
"""

import os

TEXT = "My smart fridge just sent me a performance review: 47 door-opens a day, zero commitments, and my midnight snacking shows 'a concerning lack of direction.' It cc'd the freezer. The freezer agrees."


def main():
    assert 1 <= len(TEXT) <= 280, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
