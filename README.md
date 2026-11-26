# The Printer Apology

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/taniarestu/the-printer-apology/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/taniarestu/the-printer-apology/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153)

An entry for [make.fun's "The Printer Apology" bounty](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153): the funniest one-line apology from a printer, 120 characters max.

## The entry

> Sorry I ate your report. The cheap paper tasted like cardboard, the staple attacked first, and honestly, I quit.

## How it works

`main.py` (Python 3, stdlib only, deterministic, no network) writes that single line to `/output/entry.txt`, then re-reads the file and asserts it passes the bounty gate: UTF-8, 1–120 characters, not only whitespace, a single line.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
