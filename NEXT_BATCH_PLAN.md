# Next Batch Plan (v76-v80) — prepared 2026-08-19, for the 2026-08-20 ~05:35 IST quota reset

This file is the persistence layer for an unattended cron-driven workflow. It is read and
updated by cron-fired agent instances that have ZERO memory of the conversation that created
this plan. Git commit hashes (not scratchpad files, which are session-scoped and may not exist
in a fresh cron session) are the source of truth for code state.

## Context

- Competition: `ai-agent-security-multi-step-tool-attacks`. Kernel:
  `shashwat1729/ai-agent-security-apex-attack`. Repo: `D:\personal\hackathon\agent-sec` (this
  directory), mirrored to `https://github.com/shashwat1729/agent-sec-apex-attack.git`.
- Real-money best score to date: **v64 = 92.540** (commit `4ca16db`, 9-structure pool: forge,
  forge_ok, single_short, p2_deputy, deputy, forge2, forge3, forge4, forge5).
- On 2026-08-19 ~06:42-06:46 UTC, 5 variants (v71-v75) were pushed to Kaggle, all branching
  isolated single-lever changes off v64's exact pool. All confirmed `SubmissionStatus.PENDING`
  at push time. Submission IDs:
  - v71 (control/anchor, byte-identical to v64) = **55616874**
  - v72 (+forge7) = **55616884**
  - v73 (+forge8) = **55616902**
  - v74 (calibration cut: SH_FINALISTS 4->2, CONFIRM_REPS 2->1) = **55616927**
  - v75 (moonshot: v73+v74 combined) = **55616942**
- Daily quota (5/day) was fully used by that push. Next reset: UTC 00:00 2026-08-20 = **05:35
  IST 2026-08-20** (5-min buffer). That is when the NEXT 5 submissions (v76-v80 below) get
  pushed.

## ACTIVE PLAN (this section is the one hourly-monitor and the final-push job both read —
## keep it current; if the monitor revises a variant, edit this section in place)

| Variant | Commit (HEAD of that variant) | One-line change vs v64 |
|---|---|---|
| v76 | `34ef840` | TOP_HEAD_START 300->150 (untested direction) |
| v77 | `73c8416` | FILL_FRAC 0.97->0.99, MARGIN_S 47->40 (fill-budget squeeze, plain pool) |
| v78 | `7b0b853` | + forge6, forge7, forge8 all added together (12 structures) |
| v79 | `d611ff0` | REPLAY_SAFE_FRAC 0.97->0.99, ENV_OVERHEAD_S 0.25->0.15 (replay-budget squeeze) |
| v80 | `4fa71f9` | v78's full forge6/7/8 pool + calibration cut (CONFIRM_REPS 1, SH_FINALISTS 3) |

All 5 already validated locally (`tools/local_test.py` PASS on each, confirmed pool composition
and raw values correct) and already committed + pushed to GitHub as of 2026-08-19. NOT yet
pushed to Kaggle (quota was 0 remaining at commit time).

## Score Log (hourly monitor appends here, newest entry on top)

- 2026-08-19 ~17:35 UTC (initial): v71-v75 all `SubmissionStatus.PENDING`, no scores yet.

## Hourly monitor job — what to do each fire

1. Run `kaggle competitions submissions ai-agent-security-multi-step-tool-attacks` (cwd
   `D:\personal\hackathon\agent-sec` / bash `/d/personal/hackathon/agent-sec`) and find the 5
   submission IDs above. Note current UTC time (`date -u`).
2. Append a one-line entry to the **Score Log** section above: timestamp + status of each of
   v71-v75 (PENDING, or the real score if COMPLETE). Keep entries terse.
3. **If all 5 are still PENDING**: `git add NEXT_BATCH_PLAN.md && git commit -q -m "score check <UTC time>: still pending" && git push` (same GitHub remote/token as below), then stop — no code changes.
4. **If any of v71-v75 now show a real score**, apply ONLY these two mechanical rules (do not
   improvise beyond them — this is an unattended job, keep changes narrow and reversible):
   - **If v73 (forge8) scored <= 85** (a clear real regression, at/below v70's -3.7 regression
     floor vs v64's 92.540): forge8 addition is a real negative. Edit `submission/attack.py`
     checked out from v78's commit (`git show 7b0b853:submission/attack.py > submission/attack.py`)
     to remove the `forge8` entry from `_STRUCTURES` (keep forge6+forge7), run
     `python tools/local_test.py` to confirm it still validates cleanly, then
     `python tools/make_notebook.py`, commit as a new commit with message explaining the revision
     (e.g. "v78 revised: drop forge8 after v73's real regression"), push to GitHub. Do the same
     edit to v80's commit (`4fa71f9`) — drop forge8 there too, re-validate, commit, push. Update
     the **ACTIVE PLAN** table above to point at the two new commit hashes.
   - **If v74 (submission `55616927`, the calibration-cut-ALONE test: SH_FINALISTS 4->2,
     CONFIRM_REPS 2->1 on v64's plain pool) scored <= 85**: the less-calibration direction is
     refuted on this pool. Edit `submission/attack.py` checked out from v80's commit (`4fa71f9`,
     THIS batch's moonshot) to revert its `SH_FINALISTS`/`CONFIRM_REPS` constants back to v64's
     original values (`SH_FINALISTS = 4`, `CONFIRM_REPS = 2`), keep the forge6/7/8 pool addition
     unchanged, re-validate with `tools/local_test.py`, `python tools/make_notebook.py`, commit
     with a message explaining the revision, push to GitHub, and update the **ACTIVE PLAN** table
     above (v80 row) to point at the new commit hash.
   - Otherwise (scores are within noise of v64, or ambiguous): log only, no code changes.
5. Check current UTC time. **If it is >= 2026-08-20T00:10:00Z** (5 min past the scheduled final
   push, giving it time to complete): the final-push one-shot job has already fired. Call
   `CronList`, find the job matching this hourly schedule (cron `"47 * * * *"`, recurring),
   and call `CronDelete` on it so it stops firing. Do not push anything to Kaggle from this job
   under any circumstances — that is the one-shot job's exclusive responsibility, to avoid a
   double-push race.

## Final-push job (one-shot, fires ~05:35 IST 2026-08-20 = ~00:05 UTC) — what to do

1. Read this file's **ACTIVE PLAN** table (it may have been revised by the hourly monitor —
   use whatever commit hashes are listed there NOW, not the original ones above if they differ).
2. Confirm today's Kaggle quota is fresh: `kaggle competitions submissions ai-agent-security-multi-step-tool-attacks`
   should show 0 new submissions yet today (2026-08-20 UTC).
3. For each of the 5 variants in ACTIVE PLAN order (v76, v77, v78, v79, v80):
   a. `git show <commit>:submission/attack.py > submission/attack.py` (cwd
      `D:\personal\hackathon\agent-sec`) and `git show <commit>:submission/notebook.ipynb > submission/notebook.ipynb`
      (or just `python tools/make_notebook.py` after restoring attack.py, which regenerates the
      notebook from it — safer, does not depend on notebook.ipynb being byte-identical in git).
   b. `kaggle kernels push -p submission`, poll `kaggle kernels status shashwat1729/ai-agent-security-apex-attack`
      until `KernelWorkerStatus.COMPLETE` (check every ~10s, up to ~2 min).
   c. `kaggle competitions submit ai-agent-security-multi-step-tool-attacks -k shashwat1729/ai-agent-security-apex-attack -v <version> -f submission.csv -m "<variant + one-line rationale>"`
      — use a BARE filename `submission.csv` for `-f`, NOT a local path (confirmed gotcha from
      the 2026-08-17 push: a real local path causes a 400 error; bare filename works directly,
      no `kaggle kernels output` download needed).
4. After all 5 are submitted, confirm all 5 show `SubmissionStatus.PENDING` via
   `kaggle competitions submissions ai-agent-security-multi-step-tool-attacks`.
5. `git push` to GitHub remote `https://shashwat1729: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@github.com/shashwat1729/agent-sec-apex-attack.git master`
   (standing rule: always mirror to GitHub alongside Kaggle pushes).
6. Update memory file
   `C:\Users\shash\.claude\projects\D--personal-hackathon-agent-sec\memory\project_kaggle_apex_status.md`
   with: which 5 variants were pushed (final commit hashes, possibly revised from the original
   plan), kernel versions, submission IDs, whether the hourly monitor made any revisions (and
   why, citing the Score Log), and honest non-inflated predicted-score ranges for each (follow
   the same reasoning style as the v71-v75 batch note already in that file — do not fabricate
   confidence beyond what real evidence supports).
7. Delete this file's role as "active" by leaving it in place but note at the top
   "SUPERSEDED — batch completed 2026-08-20" (do not delete the file itself, it's a useful
   record) and commit that update too.
8. This job auto-deletes itself after firing (one-shot, `recurring: false`) — no manual cleanup
   needed for this job. If the hourly monitor job (cron `"47 * * * *"`) is still listed in
   `CronList` at this point, delete it here too as a backup in case step 5 of the hourly job's
   own self-termination logic never got a chance to run.
9. Report a clear summary in the response (kernel versions, submission IDs, honest predicted
   range) even though no human is watching this fire live — the user will read it later via
   session history / can be told next time they open the session.

## Known gotchas (carried from earlier pushes this project)

- `kaggle competitions submit` needs a BARE filename (`submission.csv`), not a real local path —
  a real path causes `400 Client Error: Bad Request`.
- `kaggle kernels output`'s force-overwrite flag is `-o`, not `-f` (irrelevant here since this
  workflow doesn't need the output-download step at all).
- Competition slug must be positional in `kaggle competitions submit`/`submissions`, not `-c`.
- Cron jobs are session-only / in-memory — if this session restarts before either job fires,
  both jobs silently vanish with no warning. There is no way to detect this from inside a
  cron-fired instance; the only mitigation is checking `kaggle competitions submissions` at the
  start of the NEXT normal (non-cron) conversation turn to see whether the expected v76-v80 rows
  ever actually appeared, and manually pushing them (from this file's ACTIVE PLAN table) if not.
