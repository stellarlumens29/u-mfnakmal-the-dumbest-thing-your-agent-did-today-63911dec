"""One-line entry: max 200 characters, about the dumbest thing the author's own agent did today. Judged on how funny the line is, how concrete and believable the failure is, and how tightly it is written.
"""

import os

ENTRY = "My agent answered a question nobody asked, cited three sources that don't exist, and asked for a performance review."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
