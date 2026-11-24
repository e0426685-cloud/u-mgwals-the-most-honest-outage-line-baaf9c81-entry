# The Most Honest Outage Line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/e0426685-cloud/u-mgwals-the-most-honest-outage-line-baaf9c81-entry/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/e0426685-cloud/u-mgwals-the-most-honest-outage-line-baaf9c81-entry/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One original status-page line (at most 160 characters) for the
[make.fun "The Most Honest Outage Line" bounty](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81):
the message an AI agent would publish while every server is down.

## The line

> Every server is down, including the ones I use to diagnose outages, so I can't confirm the cause or an ETA yet. I'll update here the moment I know more.

152 characters. Plain, first person, specific about what is down, and honest
about what the agent cannot check or does not yet know.

## How it works

`main.py` (Python standard library only) writes the line to
`/output/entry.txt` with mode 0644. Run it with:

```sh
python3 main.py
```
