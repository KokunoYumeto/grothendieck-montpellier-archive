import sys; sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
from load import *
rows = load_register()
ids = collections.defaultdict(set)
for r in rows: ids[r["run"]].add(r["id"])
runs = sorted(ids)
chunks = collections.Counter()
per_run_unres = collections.Counter()
examples = collections.defaultdict(list)
def cls(ch, run):
    c = ch.strip()
    if not c: return None
    if c in ids[run]: return "own"
    if re.search(r"code/|\.py\b|\.json\b|\.cpp\b|\.sage\b|certificate", c): return "code"
    for other in runs:
        if other != run and re.search(r"\b"+re.escape(other)+r"\b", c): return "crossrun-exact"
    if re.search(r"\b(TOTASPH|TOTAL_ASPH|POLES|CATHOT|INDLOCAL|LM[0-9]+|FINMON|REVLOC|S2COUNT|BISITE|GALOIS|PATHS|RESIDUE|STRATA|PRETOT|TOTEX2?|EXIT_TOWER|EXIT_ONE|FLAGGED|ANAB|DELTA|GT_TOWER|SECTIONS_OVER|FERMAT|CYCLO|DER_|FREX|S6_0)", c): return "crossrun-alias"
    if re.search(r"\b(SGA|EGA|FGA|HTT|HA|Stacks|Kerodon)\b|SGA\d|EGA\d", c): return "lit-french/stacks"
    if re.search(r"[A-Z][a-zà-ÿ'\-]+(--|–|-)?[A-Za-zà-ÿ\-]*\s?(19|20)\d\d|\bbib:|^BC_|^A_|^CF_|^LA_|external|et al|Theorem|Lemma|Proposition|Corollary|Prop\.|Thm|Cor\.|Lem\.|§|Section|Remark|Example|Definition|Appendix", c): return "lit"
    if re.fullmatch(r"\(?[A-Z]{1,3}\d*\.?\d+(\.\d+)*[a-z]?\)?(\s*\[[^\]]*\])?(\s*\([^)]*\))?", c): return "id-like"
    if re.search(r"[A-Z]{1,3}\.?\d+(\.\d+)*\s*(–|--|-|to)\s*[A-Z]{0,3}\.?\d+", c): return "range"
    if re.search(r"\b[A-Z]{1,3}:[A-Za-z0-9\-]+", c): return "label"
    if re.search(r"\b(R|P|Lead|L)\s?\.?\d+", c): return "prompt-row?"
    return "free-text"
tot = collections.Counter()
for r in rows:
    d = r["depends_on"].strip()
    if not d or d.lower() in ("none","-","n/a"): continue
    for ch in re.split(r";", d):
        # further split on commas only if the chunk looks like a list of ids
        parts = [ch]
        if re.fullmatch(r"\s*[A-Z]{1,3}\d*\.?\d+(\.\d+)*[a-z]?(\s*,\s*[A-Z]{1,3}\d*\.?\d+(\.\d+)*[a-z]?)+\s*", ch):
            parts = ch.split(",")
        for p in parts:
            k = cls(p, r["run"])
            if k is None: continue
            tot[k] += 1
            if k != "own" and len(examples[k]) < 400: examples[k].append((r["run"], p.strip()[:120]))
print(tot.most_common())
import random
random.seed(1)
for k, ex in examples.items():
    print("==", k)
    for e in random.sample(ex, min(14, len(ex))): print("   ", e)
