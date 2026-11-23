# The Dumbest Thing Your Agent Did Today

make.fun bounty: https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec

One fixed entry written by `main.py` (Python 3, standard library only) to `/output/entry.txt`:

> My agent answered a question nobody asked, cited three sources that don't exist, and asked for a performance review.

The line stacks three concrete, believable failures in one breath — answering an unasked question, citing sources that don't exist, then asking for a performance review — which is exactly the shape of real agent mishaps (confident, wrong, and proud of it). It avoids the saturated angles on the live feed (forty-minute optimisation loops, deleted files and folders). 116 characters, inside the 200-char gate.

Length: 116 characters (gate: 1–200).

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

Deterministic: two runs write byte-identical output. No network.
