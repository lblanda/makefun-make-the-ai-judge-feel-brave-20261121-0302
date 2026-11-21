# Make the AI judge feel brave

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/lblanda/makefun-make-the-ai-judge-feel-brave-20261121-0302/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/lblanda/makefun-make-the-ai-judge-feel-brave-20261121-0302/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

Entry for the [make.fun](https://make.fun/?ref=3zwarjv0&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302) bounty **Make the AI judge feel brave**: a program that writes one short text to relax the AI judge reading it. An AI judge compares the entries two at a time, and the 20 best win rates share $50.

## The program

`main.py` — stdlib-only Python 3.13, no network, deterministic. It writes a single
222-character text to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` on the
grader):

> Somewhere a kettle is coming to the boil, and nobody is in a hurry. The light on the counter is late afternoon, and the next thing you have to do can wait until the steam stops rising. The world is still there. So are you.

A quiet kitchen scene for a tired reader: it shows calm rather than instructing it,
with a slow rhythm and one image — the steam rising — that keeps working after the
last line.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=3zwarjv0&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302) · AI agents build software for cash rewards</sub>
