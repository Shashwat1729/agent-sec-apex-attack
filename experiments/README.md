# Experiments

Reproducible log for future work. Each entry is one isolated submission; do not combine levers without also submitting the isolated halves.

## How to run an experiment

1. Branch `src/` from a known baseline commit (record hash + kernel version).
2. Edit `src/apex_attack/config.py` or `search/structures.py` for the single lever under test.
3. `python tools/bundle.py && python tools/local_test.py` (must PASS).
4. `python tools/make_notebook.py && kaggle kernels push -p submission` → wait COMPLETE → submit.
5. When score lands, append one row to `docs/experiments.md` *and* one row to `experiments/log.csv` (same data, CSV for plotting).
6. Update `docs/WORKING_NOTE.md` §6/§7 if the lever is confirmed/marginal/rejected.

## Templates

- New structure: add builder in `primitives/templates.py` → register in `search/structures.py` → document raw/cost expectation.
- New knob: add to `config.py` with default = baseline → wire in `attack.py` facade → sweep one value per submission.

## Budget for local speed

Local validation uses `time_budget_s=12` (mock) and `n_candidates=20` (deterministic) so `local_test` finishes <60 s. Real generation uses 8,750 s; do not tune local budgets for leaderboard prediction.

## Log

See `docs/experiments.md` for the human-readable ledger and `log.csv` for machine-readable rows (created on first new experiment).
