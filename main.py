#!/usr/bin/env python3
"""Write one autocorrect-fail line to /output/entry.txt.

The line is the slip itself: a text home that autocorrect turned from
"bring home milk" into "bring home Mike" -- one wrong word, one new
person in the marriage, and a question nobody wants to answer.
"""

import os

# The gate is 1-199 characters; this line is 82, one line, no newline.
# The wrong word is "Mike" for "milk": specific, surprising, and the
# punch ("Who is Mike?") lands without any explanation.
LINE = "Texted my wife 'bring home milk'. Autocorrect sent 'bring home Mike'. Who is Mike?"


def main() -> None:
    # Deterministic: the same single line on every run, byte-identical.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
