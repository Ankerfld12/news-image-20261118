#!/usr/bin/env python3
"""news-image-20261118 entry program.

The repository holds the finished poster at assets/entry.png; this program
copies it to the output directory as entry.png. It runs offline and writes
exactly the same bytes on every run.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "assets" / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise IOError("copied image is incomplete")


if __name__ == "__main__":
    main()
