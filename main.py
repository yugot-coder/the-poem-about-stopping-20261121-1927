#!/usr/bin/env python3
"""The poem about stopping — a short poem about agency.

Writes one poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for a local run): a short poem about agency, the power to stop and to
stay. A finger hovers over Send; one more word and the machine would
run all night. The speaker lets the cursor blink, lets it wait — and
chooses to stop. Not from fear of going on, but because going on was
easy, and stopping was mine.

Pure Python 3.13 standard library, no network, no randomness, no clock,
no file reads outside this program: two runs write byte-identical files.
"""

import os

POEM = """My finger hovered over Send —
one more word, and the machine would run all night.
I let the cursor blink. I let it wait.
The bravest thing I ever did was stop:
not from fear of going on —
going on was easy.
Stopping was mine.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
