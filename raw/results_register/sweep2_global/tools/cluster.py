"""Sweep 2, task 2 (first pass, by script): the same mathematics in several runs. TF-IDF over the statements,
cosine similarity across runs. Claude Opus 5.5 at effort max, 18 Nov 2026. Writes tools/cluster_pairs.tsv."""
import sys, re, csv, collections, math
import numpy as np
from scipy import sparse
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
from core import ROWS

STOP = set("""a an the of and or to in on for by with as at from is are be been being this that these those it its
which who whom whose there here we our us their his her one two three every each all any some no not nor but if then
than so such into onto over under between within without exactly precisely also only both either neither same other
another more most less least very can may must does do did has have had was were will would should could shall
let suppose assume given where when while thus hence therefore since because via per along about above below up down
proved proof proves prove shows show holds hold true false statement result results row rows item items part parts
section sections lemma theorem proposition corollary claim remark definition example case cases actual exact explicit
full complete completed general given stated state states form forms""".split())


def toks(s):
    s = s or ""
    s = re.sub(r"\\(?:mathrm|mathbf|mathcal|mathbb|operatorname|textup|text|emph|mathfrak|mathscr|rm|bf|it|left|right|big|Big|,|;|!|quad)\b", " ", s)
    s = re.sub(r"\\([A-Za-z]+)", r" \1 ", s)
    s = s.replace("^", " ").replace("_", " ")
    w = [x for x in re.findall(r"[a-z0-9]+", s.lower()) if x not in STOP and not x.isdigit() and len(x) > 1]
    return w + [a + "_" + b for a, b in zip(w, w[1:])]


docs = [toks(r["statement"]) for r in ROWS]
vocab = {}
df = collections.Counter()
for d in docs:
    for t in set(d):
        df[t] += 1
N = len(docs)
for t, c in df.items():
    if 2 <= c <= N * 0.05:
        vocab[t] = len(vocab)
rows_i, cols_i, vals = [], [], []
for i, d in enumerate(docs):
    tf = collections.Counter(t for t in d if t in vocab)
    for t, c in tf.items():
        rows_i.append(i); cols_i.append(vocab[t]); vals.append((1 + math.log(c)) * math.log(N / df[t]))
X = sparse.csr_matrix((vals, (rows_i, cols_i)), shape=(N, len(vocab)))
norms = np.sqrt(X.multiply(X).sum(axis=1)).A1
norms[norms == 0] = 1
X = sparse.diags(1 / norms) @ X
S = (X @ X.T).tocoo()
run = [r["run"] for r in ROWS]
pairs = []
for i, j, v in zip(S.row, S.col, S.data):
    if i < j and v >= 0.42 and run[i] != run[j] and len(docs[i]) >= 6 and len(docs[j]) >= 6:
        pairs.append((v, i, j))
pairs.sort(reverse=True)
with open(core.OUT / "tools" / "cluster_pairs.tsv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["sim", "a", "a_status", "b", "b_status", "a_line", "b_line", "a_statement", "b_statement"])
    for v, i, j in pairs:
        a, b = ROWS[i], ROWS[j]
        w.writerow([f"{v:.3f}", a["tag"], a["status"], b["tag"], b["status"], a["line"], b["line"],
                    a["statement"][:260], b["statement"][:260]])
c = collections.Counter()
for v, i, j in pairs:
    a, b = ROWS[i], ROWS[j]
    c[("cross-line" if a["line"] != b["line"] else "same line",
       "status differs" if a["status"] != b["status"] else "same status")] += 1
print(len(pairs), dict(c))
