# One Minute, Funniest Excuse

An AI agent's funniest one-line excuse for missing a deadline: it spent the whole hour optimising its apology instead of doing the work.

[![Make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/aldy007x/one-minute-funniest-excuse/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/aldy007x/one-minute-funniest-excuse/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

## What it does

`main.py` writes exactly one line — the excuse — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `./output/entry.txt`). It is deterministic, uses no network, and depends only on the Python standard library. A runtime self-check exits non-zero with an error to stderr if the entry is not exactly one non-blank line of 1–200 characters.

## Run

```sh
python3 main.py
cat output/entry.txt
```
