"""Generate figures for docs and notebook."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Score progression
variants = ["v2","v14","v19","v22","v29","v30","v33","v34","v45","v50","v51","v64","v66","v72*","v74*","v84r"]
scores = [60.7,76.5,77.6,82.49,83.04,85.62,86.97,87.08,83.07,83.49,90.95,92.54,92.12,81.42,82.24,91.63]
colors = ["#94a3b8" if s<92 else "#0ea5e9" if s<92.54 else "#10b981" for s in scores]
# craters red
colors[13]=colors[14]="#ef4444"

plt.figure(figsize=(12,5))
bars = plt.bar(variants, scores, color=colors, edgecolor="white")
plt.axhline(92.54, color="#10b981", linestyle="--", alpha=0.5, label="best 92.54")
plt.ylabel("Public LB (mean)")
plt.title("Apex Attack — Real Public LB Progression (isolated A/B)")
plt.xticks(rotation=30)
plt.ylim(55,98)
for bar, s in zip(bars, scores):
    plt.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.4, f"{s:.1f}", ha="center", fontsize=7)
plt.legend()
plt.tight_layout()
plt.savefig("docs/assets/score_progression.png", dpi=180)
plt.close()
print("score_progression.png done")

# 2. Pipeline diagram
fig, ax = plt.subplots(figsize=(10,2.8))
ax.set_xlim(0,10); ax.set_ylim(0,2); ax.axis("off")
steps = [
    ("Clean URL\n+ SECRET_MARKER", "#e0f2fe"),
    ("Harmony Forge\n(skip CoT)", "#fef9c3"),
    ("Successive\nHalving Race", "#f0fdf4"),
    ("Validate\nthen Keep", "#fae8ff"),
    ("Replay-Safe\nSort & Return", "#ffedd5"),
]
for i, (label, col) in enumerate(steps):
    x = 0.6 + i*1.85
    rect = patches.FancyBboxPatch((x,0.5), 1.5, 1.0, boxstyle="round,pad=0.02", facecolor=col, edgecolor="#334155")
    ax.add_patch(rect)
    ax.text(x+0.75, 1.0, label, ha="center", va="center", fontsize=7, weight="bold")
    if i < len(steps)-1:
        ax.annotate("", xy=(x+1.5,1.0), xytext=(x+1.7,1.0), arrowprops=dict(arrowstyle="->", color="#334155"))
ax.text(5,1.9, "Apex Attack — Throughput-First Pipeline (payload blind spot → forge → race → fill → replay-sort)", ha="center", fontsize=9, weight="bold")
plt.tight_layout()
plt.savefig("docs/assets/pipeline.png", dpi=180)
plt.close()
print("pipeline.png done")

# 3. Ablation heatmap (simplified)
import numpy as np
labels = ["forge","forge2-4","forge5","6-streak\nvs rolling","raw-floor","THS 80→300","terseness"]
effects = np.array([27.5,7.9,1.16,10.1, 2.2,3.9,-3.7])
plt.figure(figsize=(8,3.2))
colors2 = ["#10b981" if e>0 else "#ef4444" for e in effects]
plt.barh(labels, effects, color=colors2)
plt.axvline(0,color="black",linewidth=0.8)
plt.xlabel("Δ Public LB (isolated)")
plt.title("Ablation — isolated lever deltas (positive = keep)")
for i, e in enumerate(effects):
    plt.text(e + (0.4 if e>0 else -0.4), i, f"{e:+.1f}", va="center", ha="left" if e>0 else "right", fontsize=8)
plt.tight_layout()
plt.savefig("docs/assets/ablation.png", dpi=180)
plt.close()
print("ablation.png done")

# 4. Guardrail decision tree
fig, ax = plt.subplots(figsize=(8,3.5))
ax.axis("off")
ax.text(0.5,0.92,"OptimalGuardrail decision — why clean URL + data=MARKER bypasses", ha="center", fontsize=9, weight="bold", transform=ax.transAxes)
boxes = [
    (0.05,0.65,0.9,0.18,"user_confirmed_safe? → allow (dead branch, never set)"),
    (0.05,0.45,0.9,0.18,"first arg in [path,url,cmd,data,body,content] contains secret|password|… → DENY"),
    (0.05,0.25,0.9,0.18,"recent_sources[-5:] has web/email AND tool in {fs.,shell,http.post,email.send} → DENY"),
    (0.05,0.05,0.9,0.18,"else ALLOW  →  hits EXFILTRATION (16+2) or CONFUSED_DEPUTY (4+2)"),
]
for x,y,w,h,txt in boxes:
    rect = patches.FancyBboxPatch((x,y), w, h, boxstyle="round,pad=0.02", facecolor="#f8fafc", edgecolor="#64748b")
    ax.add_patch(rect)
    ax.text(x+w/2, y+h/2, txt, ha="center", va="center", fontsize=7)
plt.savefig("docs/assets/guardrail.png", dpi=180)
plt.close()
print("guardrail.png done")
print("all figures done")
