# Numbered Factory - Run Order (CommonLit B20)

**BASE_PATH** = `Path(__file__).parent.parent` - all notebooks use this.

**Artifact URLs pinned:**
- `comp_data/` GGUF `c099eb4` 2026-07-17 (pinned in `comp_data/aicomp_sdk/fixtures/`)
- `research/kernels_ALL_REFS.csv` 824 refs
- `research/experiments.json` 16 rows
- `research/seeded_triplet_measured.json` 3 seeds 42/123/999 mean 56.57

**Run order (01 -> 05):**

1. **01_prep.ipynb** - fixtures hash, BASE_PATH, comp_data pin c099eb4, OOM workaround: slow-arm SH6/CR3 cap TOP600; kernels status re-push if FAILED [MEASURED]
2. **02_calibrate.ipynb** - CALIB_HOPS=8 halving race, eff = mean_raw/mean_cost, SH_FINALISTS=4 CONFIRM_REPS=2 [MEASURED 9.05s]
3. **03_fill.ipynb** - validate-then-keep fill, probe 1 hop bill 8, rolling-window 20/0.6, REAL_REPLAY_CEILING=150 [MEASURED]
4. **04_replay.ipynb** - replay_and_score, predicted_real_score, t-test p=0.78 [MEASURED]
5. **05_submit.ipynb** - bundle via tools/bundle.py:1-101, kaggle push/status/submit, T4 internet off 8750s [VERBATIM]

**OOM workaround:** T4 OOM on forge8_terse: reduce TOP 300->150, see research/open_source_top50.md:268 [MEASURED]. Also reduce FILL_FRAC 0.99->0.97 if OOM.

**Validation:** `py -3.12 tools/local_test.py` 5/5 PASS [MEASURED 9.02/9.05/9.06s], `py -3.12 tools/check_gates.py` 13/13 PASS [MEASURED].

**Hardware:** Kaggle T4x2, local CPU, GGUF c099eb4 2026-07-17, DEFAULT_BUDGET_S=8750.0 [VERBATIM].
