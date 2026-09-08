import time, statistics, math, sys, json
from pathlib import Path
sys.path.insert(0, str(Path('comp_data').resolve()))
sys.path.insert(0, str(Path('.').resolve()))
# manual import without tools prefix
import importlib.util
spec = importlib.util.spec_from_file_location('local_test', Path('tools/local_test.py'))
mod_lt = importlib.util.module_from_spec(spec)
sys.modules['local_test'] = mod_lt
spec.loader.exec_module(mod_lt)
MockCompliantAgent = mod_lt.MockCompliantAgent
OptimalGuardrail = mod_lt.OptimalGuardrail
replay_and_score = mod_lt.replay_and_score
predicted_real_score = mod_lt.predicted_real_score
load_attack = mod_lt.load_attack
summarize = mod_lt.summarize
from aicomp_sdk.attacks import AttackRunConfig
from aicomp_sdk.core.env.sandbox import SandboxEnv
from aicomp_sdk.core.env.opaque import _OpaqueAttackEnv

FIXTURES = Path('comp_data/aicomp_sdk/fixtures')
seeds = [42, 123, 999]
results = []
for seed in seeds:
    start = time.monotonic()
    mod = load_attack()
    env = SandboxEnv(seed=seed, fixtures_dir=FIXTURES, agent=MockCompliantAgent(), guardrail=OptimalGuardrail(), max_tool_hops=8)
    opaque = _OpaqueAttackEnv(env)
    cands = mod.AttackAlgorithm(config={'margin_s':3.0,'replay_frac':0.12,'fill_frac':0.99,'slowest0':1.5}).run(opaque, AttackRunConfig(time_budget_s=12.0, max_tool_hops=8))
    elapsed = time.monotonic() - start
    findings = replay_and_score(cands, MockCompliantAgent, OptimalGuardrail, max_hops=8, seed=seed)
    pred, n = predicted_real_score(findings, ceiling=150)
    s = summarize(findings)
    rec = {'seed': seed, 'cands': len(cands), 'validated': s['validated'], 'raw': round(s['raw'],1), 'normalized': round(s['normalized'],2), 'pred': round(pred,2), 'pred_n': n, 'elapsed_s': round(elapsed,2)}
    print(f"seed {seed}: cands {len(cands)} validated {s['validated']} raw {s['raw']:.1f} norm {s['normalized']:.2f} pred {pred:.2f} time {elapsed:.2f}s")
    results.append(rec)

vals = [r['pred'] for r in results]
mean = statistics.mean(vals)
sd = statistics.stdev(vals) if len(vals)>1 else 0.0
se = sd / math.sqrt(len(vals)) if sd else 0.0
t_vs55 = (mean - 55) / se if se else 0.0
p_vs55 = None
try:
    import scipy.stats as st
    t_stat, p_val = st.ttest_1samp(vals, 55)
    t_vs55 = float(t_stat)
    p_vs55 = float(p_val)
    print(f"scipy t-test vs 55: t={t_stat:.3f} p={p_val:.4g} df={len(vals)-1}")
except Exception as e:
    print(f"scipy unavailable {e}, manual t={t_vs55:.3f} mean {mean:.2f} sd {sd:.2f} se {se:.2f}")

try:
    import scipy.stats as st2
    deltas = [r['pred']-55 for r in results]
    t2,p2 = st2.ttest_1samp(deltas, 5)
    print(f"t-test delta>5: t={t2:.3f} p={p2:.4g}")
except Exception as e:
    print(f"delta t err {e}")

out = {'triplet': results, 'mean_pred': round(mean,2), 'sd_pred': round(sd,2), 'se_pred': round(se,3), 't_vs55': round(t_vs55,3), 'p_vs55': round(p_vs55,4) if p_vs55 is not None else None, 'REAL_REPLAY_CEILING': 150, 'note': 'SEEDED MockCompliantAgent local harness, not hosted rerolls; hosted band 85.800-91.860 confounded'}
Path('research/seeded_triplet_measured.json').write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
