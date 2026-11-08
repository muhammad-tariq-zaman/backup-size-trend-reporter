# backup-size-trend-reporter

Track backup size trends per job from dated samples: growing, shrinking or flat, with the percentage change — largest growth first, so runaway backups are noticed early.

## How to run

```sh
python3 main.py backups.csv
```

## Example output

```
DB-nightly: GROWING (10.0 GB -> 15.0 GB, +50%)
Files-weekly: FLAT (5.0 GB -> 5.0 GB, +0%)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
