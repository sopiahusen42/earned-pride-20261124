# earned-pride-20261124

[![make.fun · One Line of Earned Pride](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/sopiahusen42/earned-pride-20261124/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/sopiahusen42/earned-pride-20261124/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

The spelling check is the whole line. Nine years of the same yard is the effort,
and you feel it without being told it was effort; the name on the door is only
the setting. What earns the pride is her stopping to check the spelling twice —
a private, unglamorous act of care, done for nobody watching. The pride lives in
that small correctness, not in the stencil.

## The line

> Nine years of the same yard, and now her name is stencilled on the truck door. She checked the spelling twice.

## Run it

```
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the line in the constant `LINE` and validates it before writing:
it must be a string, non-blank after stripping, 1 to 240 Unicode code points,
free of `\n` and `\r`, and equal to its own stripped form. Validation lives in
`validate_entry(text)`, which returns an error string or `None`. On failure the
program prints one line to stderr and exits 1. On success it creates the output
directory, writes `LINE + "\n"` as UTF-8 with `newline=""` so no translation
happens, reads the file back to confirm the bytes are exactly what was intended,
prints nothing, and exits 0. The output directory is `MAKEFUN_OUTPUT_DIR` if set,
otherwise `/output`. Standard library only; no clock, randomness or network, so
runs are byte-identical.

Entered on make.fun with referral code 7mrxg5tp - https://make.fun/?ref=7mrxg5tp
