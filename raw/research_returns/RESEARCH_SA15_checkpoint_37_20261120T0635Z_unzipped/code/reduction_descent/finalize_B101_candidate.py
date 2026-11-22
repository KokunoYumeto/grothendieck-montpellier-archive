from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re
own = Path(__file__).resolve().parents[1]
p = own/"B_uniform_wild_trace_arcs_candidate.tex"
code = own/"code/verify_uniform_wild_trace_arcs.py"
out = code.with_suffix(".output.json")
data = json.loads(out.read_text())
assert data["status"] == "PASS"
old = p.read_text()
new = old.replace(r""" b+(p-1)J_v
   =p^v\{b+(p-1)U\}=eN=d .
 \qquad
 P(0)=p,\quad P(X)\equiv X^d+O(X^{d+1})\pmod p .
""", r"""\begin{gathered}
 b+(p-1)J_v=p^v\{b+(p-1)U\}=eN=d,\\
 P(0)=p,\qquad P(X)\equiv X^d+O(X^{d+1})\pmod p .
\end{gathered}
""")
new = new.replace(r""" q_j=2p^j-1\quad(0\le j\le v+2),\qquad
 q_{v+2}-\frac a{p-1}=2p^v-1>0 .
""", r"""\begin{gathered}
 q_j=2p^j-1\quad(0\le j\le v+2),\\
 q_{v+2}-\frac a{p-1}=2p^v-1>0 .
\end{gathered}
""")
before = """A standalone exact supplement will check all branch
identities and the upper recurrence, without inferring
effectivity from a finite range.
"""
after = r"""The standalone exact supplement
\path{code/reduction_descent/verify_uniform_wild_trace_arcs.py}
passed at 06:16:28.907787 UTC on 20 November 2026 in
0.35733604000415653 seconds. It checks eight symbolic
identities and 11,556 arcs at the 12 primes from five
through43, with $0\le v\le8$, $1\le h\le6$ and
$n=h+v+1$. There are 40,446 degree-$q$ and 46,224
degree-$p$ iteration checks, 285,714 intermediate
and tail-weight comparisons, and 98,226 integral
$p$-coefficient cutoffs. The certificate explicitly
checks 648 excluded equality ties, 2,592 choices
avoiding $N\mid A$, and the upper recurrences for
108 exact-family members. Its 30,984 logarithm
monomials check the descent weights through level15.
The full finite ranges, executed code, complete output
and stdout are retained; no mathematical checker
failure occurred. No effectivity assertion is inferred
from this finite range.
"""
assert new.count(before) == 1
new = new.replace(before, after)
hist = own/"notes/B101_certificate_finalization"
hist.mkdir(exist_ok=False)
(hist/"candidate.before.tex").write_text(old)
(hist/"candidate.diff").write_text("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile="candidate.before.tex", tofile=p.name)))
p.write_text(new)
sha = lambda f: hashlib.sha256(f.read_bytes()).hexdigest()
record = {
    "status":"CANDIDATE", "actual_utc":datetime.now(timezone.utc).isoformat(),
    "candidate":str(p), "candidate_sha256":sha(p),
    "labels":re.findall(r"\\label\{([^}]+)\}", new),
    "program":str(code), "program_sha256":sha(code),
    "output":str(out), "output_sha256":sha(out),
    "author_actual_utc":data["actual_utc"], "author_runtime_seconds":data["runtime_seconds"],
    "counts":data["counts"],
    "source_scope":"Exact original HG recurrence/coefficient/specialization passages freshly opened and completely read for B100 are reused; precise URLs/refs/scopes in outputs/B100_candidate_record.json. No additional new source opening or image claimed.",
    "proof_dependencies":"Canonical B62 integral arc and generic quotient/compatible-Kummer lift; B64 actual-target coefficient/logarithm estimate; B76 strict wild cyclic/mixed bound and dimension detection. No unpromoted B100 assertion used.",
    "claim_scope":"Exact existential mixed p^n threshold e>p^(2n−3−vp(e)) only for n>=vp(e)+2, p>=5, p−1|e. Exact full height-two family ν_min(p,2p^v(p−1),2)=v+2 for v>=0, perfect residue and µp. No universal formula for other e or assertion that both comparison groups are whole potentially good.",
    "retention":"Initial candidate, two display-only line splits/certificate diff, exact executed code/output/stdout retained. No mathematical checker failure or canonical/shared change."
}
(own/"outputs/B101_candidate_record.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
