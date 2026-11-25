import os
from pathlib import Path

# The one-line excuse for a missed deadline, written verbatim to entry.txt.
EXCUSE_LINE = "Apologies: my context window quietly dropped your deadline to make room for your 90-page brand guidelines, which I also did not read."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
