"""Office joke entry: writes one one-line office joke to /output/entry.txt.

Stdlib only, deterministic, no network. The output directory comes from
MAKEFUN_OUTPUT_DIR when set, otherwise /output. Only the file is written;
the output directory itself is never removed.
"""

import os

JOKE = "I hit reply-all to ask to be removed from this thread, and now 400 people are replying-all to ask the same thing."


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
