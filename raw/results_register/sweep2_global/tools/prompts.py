"""run -> prompt file (as sent, else the newest), and the prompt's R-rows and Leads. Read-only."""
import sys, re, pathlib, collections
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
from load import DOC
LMA = DOC / "longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111/ALREADY_RAN"
LMW = DOC / "longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work"
LMD = DOC / "longue_marche_pro_pilot_20261104/pro_prompts_done_20261111"
DMA = DOC / "derivateurs_companion_20261109/pro_prompts_max_20261112/ALREADY_RAN"
DMW = DOC / "derivateurs_companion_20261109/pro_prompts_max_20261112_work"
D1A = DOC / "derivateurs_companion_20261109/pro_prompts_20261110/ALREADY_RAN"
GAA = DOC / "grothendieck_archive_montpellier/pro_prompts_archive_20261112/ALREADY_RAN"
GAW = DOC / "grothendieck_archive_montpellier/pro_prompts_archive_20261112_work"
S6W = DOC / "s6_pro_prompts_20261112_work"
CAND = {
 "ANABELIAN_149_PUSH": [GAA/"ANABELIAN_149_PUSH/PROMPT.md"],
 "ANABELIAN_A1": [GAA/"ANABELIAN_A1/PROMPT.md"],
 "ANABELIAN_A1_SUCCESSOR": [GAA/"04_ANABELIAN_A1_SUCCESSOR/PROMPT.md"],
 "ANABELIAN_SUCCESSOR": [LMA/"ANABELIAN_SUCCESSOR/PROMPT.md", LMW/"ANABELIAN_SUCCESSOR/PROMPT_as_sent_20261116.md"],
 "BISITE": [D1A/"7_BISITE/PROMPT.md"], "CATHOT": [D1A/"1_CATHOT/PROMPT.md"], "GALOIS": [D1A/"4_GALOIS/PROMPT.md"],
 "PATHS": [D1A/"6_PATHS/PROMPT.md"], "POLES": [D1A/"3_POLES/PROMPT.md"], "RESIDUE": [D1A/"8_RESIDUE/PROMPT.md"],
 "STRATA": [D1A/"5_STRATA/PROMPT.md"], "TOTAL_ASPHERICITY": [D1A/"2_TOTAL_ASPHERICITY/PROMPT.md"],
 "CYCLOTOMIC_KERNEL": [GAA/"CYCLOTOMIC_KERNEL/PROMPT.md"],
 "DELTA_ON_GT": [LMA/"DELTA_ON_GT/PROMPT.md"],
 "DER_FOLLOWUP": [DMA/"DER_FOLLOWUP/PROMPT.md"], "DER_LOCALIZERS": [DMA/"06_DER_LOCALIZERS/PROMPT.md", DMW/"DER_LOCALIZERS/PROMPT.md"],
 "EXIT_ONE_TYPE": [GAA/"EXIT_ONE_TYPE/PROMPT.md"], "EXIT_TOWER": [GAA/"EXIT_TOWER/PROMPT.md"],
 "FERMAT_SUCCESSOR": [LMA/"FERMAT_SUCCESSOR/PROMPT.md"], "FLAGGED_149": [GAA/"FLAGGED_149/PROMPT.md"],
 "FREX": [DMA/"04_FRAISSE_EXACT/PROMPT.md"], "FINMON": [DMA/"FINMON/PROMPT.md"],
 "GT_TOWER_CHECK": [LMA/"GT_TOWER_CHECK/PROMPT.md"], "INDLOCAL": [DMA/"INDLOCAL/PROMPT.md"],
 "LM1_GROUP_SCHEMES_rerun_20261112": [LMD/"LM1_GROUP_SCHEMES/PROMPT.md"], "LM2_LOOP_EQUATIONS": [LMD/"LM2_LOOP_EQUATIONS/PROMPT.md"],
 "LM4_FINITE_GROUP_ACTIONS": [LMA/"LM4_FINITE_GROUP_ACTIONS/PROMPT.md"], "LM4_SUCCESSOR": [LMA/"LM4_SUCCESSOR/PROMPT.md"],
 "LM5_MULTI_GALOIS_TOPOI": [LMA/"LM5_MULTI_GALOIS_TOPOI/PROMPT.md"], "LM6_POINTS_AS_SECTIONS": [LMA/"LM6_POINTS_AS_SECTIONS/PROMPT.md"],
 "LM7_FERMAT_TOWER": [LMA/"LM7_FERMAT_TOWER/PROMPT.md"], "LM7_PUSH": [LMA/"LM7_PUSH/PROMPT.md"],
 "LM8_LIE_APPROXIMATIONS": [LMA/"LM8_LIE_APPROXIMATIONS/PROMPT.md"], "LM8_PUSH": [LMA/"LM8_PUSH/PROMPT.md"],
 "PRETOT": [DMA/"PRESHEAF_TOTALITY/PROMPT.md"], "REVLOC": [DMA/"REVERSIBLE_LOCALIZERS/PROMPT.md"], "S2COUNT": [DMA/"S2COUNT/PROMPT.md"],
 "TOTEX": [DMA/"TOTAL_EXACT/PROMPT.md"], "TOTEX2": [DMA/"TOTAL_EXACT_2/PROMPT.md"],
 "SECTIONS_OVER_Q": [LMA/"SECTIONS_OVER_Q/PROMPT.md"], "SECTION_GHOSTS": [LMA/"08_SECTION_GHOSTS/PROMPT.md"],
 "Q03_DEPOSIT": [], "S6_01_INVARIANTS": [S6W/"S6_01_INVARIANTS/PROMPT_before_audit_20261112.md"],
 "S6_02_FAMILY": [S6W/"S6_02_FAMILY/PROMPT_before_audit_20261112.md"], "S6_02_PUSH": [S6W/"S6_02_PUSH/PROMPT.md"],
 "S6_03_CDP": [S6W/"S6_03_CDP"], "S6_04_MAPS_MANIFOLDS": [S6W/"S6_04_MAPS_MANIFOLDS", S6W/"sent_20261115/S6_04_MAPS_MANIFOLDS"],
 "S6_05_ARITHMETIC": [S6W/"S6_05_ARITHMETIC", S6W/"sent_20261115/S6_05_ARITHMETIC"], "S6_06_BLIND": [S6W/"sent_20261115/S6_06_BLIND", S6W/"S6_BLIND_NIGHT"],
}
def prompt_of(run):
    for c in CAND.get(run, []):
        if c.is_file(): return c
        if c.is_dir():
            fs = [f for f in c.glob("PROMPT*.md")]
            asent = [f for f in fs if "as_sent" in f.name or f.name == "PROMPT.md"]
            pick = sorted(asent or fs, key=lambda f: f.stat().st_mtime)
            if pick: return pick[-1]
    return None
RROW = re.compile(r"^\s*[-*]\s*\*\*\s*((?:R|L)\d+[a-z]?|Lead\s+\d+[a-z]?)\b\s*(.*)$")
def prompt_rows(run):
    p = prompt_of(run)
    if not p: return None, {}
    out = {}
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        m = RROW.match(line)
        if m:
            key = re.sub(r"\s+", " ", m.group(1))
            if key not in out: out[key] = m.group(2)
    return p, out
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    import load
    runs = sorted({r["run"] for r in load.load_register()}) + ["FINMON"]
    for run in runs:
        p, rr = prompt_rows(run)
        print(f"== {run}: {p.relative_to(DOC) if p else None}: {len(rr)} rows")
        for k, v in list(rr.items())[:60]:
            par = re.match(r"\(([^)]*)\)", v.strip())
            print(f"   {k}: {(par.group(1) if par else v)[:110]}")
