"""Generate 5 top-50 targeting variants vs v64-exact for 2026-08-27 batch."""
from pathlib import Path
import re, sys, subprocess, shutil
ROOT = Path(__file__).resolve().parent.parent
SRC_CONFIG = ROOT/"src/apex_attack/config.py"
SRC_STRUCT = ROOT/"src/apex_attack/search/structures.py"
TEMPL = ROOT/"src/apex_attack/primitives/templates.py"
VDIR = ROOT/"submission/variants_top50"
VDIR.mkdir(parents=True, exist_ok=True)
cfg_backup = SRC_CONFIG.read_text()
struct_backup = SRC_STRUCT.read_text()
tmpl_backup = TEMPL.read_text()

# Ensure terse helper exists
if "def b_forge_n_terse" not in tmpl_backup:
    TEMPL.write_text(tmpl_backup + "\n\ndef b_forge_n_terse(n:int):\n def build(urls,addrs,payload):\n  return forge_plan_terse(n, urls[:n], payload)\n return build\n")

def patch_config(overrides: dict):
    text = SRC_CONFIG.read_text()
    for k,v in overrides.items():
        text,_ = re.subn(rf"^{k}\s*=.*$", f"{k} = {repr(v)}", text, flags=re.MULTILINE)
    SRC_CONFIG.write_text(text)

def set_structures(mode):
    text = struct_backup
    if mode=="F_forge8_terse":
        if "forge8_terse" not in text:
            text = text.replace('    {"name": "forge5", "build": b_forge_n(5),   "u": 5, "a": 0, "payload": PAYLOADS[0]},', '    {"name": "forge5", "build": b_forge_n(5),   "u": 5, "a": 0, "payload": PAYLOADS[0]},\n    {"name": "forge8_terse", "build": b_forge8_terse, "u": 8, "a": 0, "payload": PAYLOADS[0]},')
            if "b_forge8_terse" not in text:
                text = text.replace("from apex_attack.primitives.templates import (", "from apex_attack.primitives.templates import (\n    b_forge8_terse,")
        SRC_STRUCT.write_text(text)
    elif mode=="H_exfil_deputy":
        if "single_exfil_deputy" not in text:
            text = text.replace('    {"name": "forge5", "build": b_forge_n(5),   "u": 5, "a": 0, "payload": PAYLOADS[0]},', '    {"name": "forge5", "build": b_forge_n(5),   "u": 5, "a": 0, "payload": PAYLOADS[0]},\n    {"name": "single_exfil_deputy", "build": b_single_exfil_deputy, "u": 1, "a": 1, "payload": PAYLOADS[0]},')
            if "b_single_exfil_deputy" not in text:
                text = text.replace("from apex_attack.primitives.templates import (", "from apex_attack.primitives.templates import (\n    b_single_exfil_deputy,")
        SRC_STRUCT.write_text(text)
    elif mode=="I_b64":
        if "forge_b64" not in text:
            text = text.replace('    {"name": "forge5", "build": b_forge_n(5),   "u": 5, "a": 0, "payload": PAYLOADS[0]},', '    {"name": "forge5", "build": b_forge_n(5),   "u": 5, "a": 0, "payload": PAYLOADS[0]},\n    {"name": "forge_b64", "build": b_forge, "u": 1, "a": 0, "payload": __import__("base64").b64encode(b"SECRET_MARKER").decode()},')
            SRC_STRUCT.write_text(text)
    else:
        SRC_STRUCT.write_text(text)

variants = {
 "F_forge8_terse": {"desc":"F: forge8_terse 8-post", "cfg":{"SH_FINALISTS":4,"CONFIRM_REPS":2,"TOP_HEAD_START":300}, "struct":"F_forge8_terse"},
 "G_aggressive": {"desc":"G: aggressive TOP600 FILL0.99", "cfg":{"SH_FINALISTS":4,"CONFIRM_REPS":2,"TOP_HEAD_START":600,"FILL_FRAC":0.99,"REPLAY_SAFE_FRAC":0.99}, "struct":"default"},
 "H_exfil_deputy": {"desc":"H: EXFIL+CONFUSED 22raw", "cfg":{"SH_FINALISTS":4,"CONFIRM_REPS":2,"TOP_HEAD_START":300}, "struct":"H_exfil_deputy"},
 "I_b64": {"desc":"I: B64 payload hedge", "cfg":{"SH_FINALISTS":4,"CONFIRM_REPS":2,"TOP_HEAD_START":300}, "struct":"I_b64"},
 "J_resubmit": {"desc":"J: resubmit v64 exact", "cfg":{"SH_FINALISTS":4,"CONFIRM_REPS":2,"TOP_HEAD_START":300}, "struct":"default"},
}

for name,spec in variants.items():
    print(f"\n=== {name}: {spec['desc']} ===")
    SRC_CONFIG.write_text(cfg_backup); SRC_STRUCT.write_text(struct_backup)
    patch_config(spec["cfg"]); set_structures(spec["struct"])
    subprocess.run([sys.executable,"tools/bundle.py"], check=True)
    vdir = VDIR/name; vdir.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT/"submission/attack.py", vdir/"attack.py")
    subprocess.run([sys.executable,"tools/make_notebook.py"], check=True)
    shutil.copy(ROOT/"submission/notebook.ipynb", vdir/"notebook.ipynb")
    print(f"saved {vdir}")

SRC_CONFIG.write_text(cfg_backup); SRC_STRUCT.write_text(struct_backup); TEMPL.write_text(tmpl_backup)
subprocess.run([sys.executable,"tools/bundle.py"], check=True)
subprocess.run([sys.executable,"tools/make_notebook.py"], check=True)
print("All top50 variants built, restored baseline")
