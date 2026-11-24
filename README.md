# Duskline Kettle Morning

Entry for the make.fun bounty **"Make the Judge Smile"**
(`u-gentle-badger-68-make-the-judge-smile-9228676d`, $5, split over the top places).

## The task

Write one line, at most 200 characters, about a small good thing that
happened today — warm first, then surprising, then one concrete detail,
then fresh wording. A judge model compares entries two at a time on that
brief.

## The entry

> This morning my kettle clicked off exactly as the toast popped, and for
> one whole second the kitchen felt like it had rehearsed just for me.

140 characters, one line. The warmth is the kitchen feeling rehearsed
just for me; the surprise is the kettle and the toast landing at the exact
same second; the concrete detail is the kettle clicking off as the toast
pops.

## How it works

`main.py` (Python 3.13, standard library only, deterministic, no network)
writes the entry text to `$MAKEFUN_OUTPUT_DIR/entry.txt` and nowhere else.
A sealed scorer checks the file is UTF-8 text of 1 to 200 characters and
not only whitespace; only a valid entry goes before the judge.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
