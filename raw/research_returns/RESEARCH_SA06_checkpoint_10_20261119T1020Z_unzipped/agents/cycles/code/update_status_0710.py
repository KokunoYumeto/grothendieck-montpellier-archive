"""Publish the current E.3 closure and retain dated earlier attempts."""
from pathlib import Path
from datetime import datetime, timezone
import json, time

start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
path=root/'STATUS.md'
text=path.read_text()
text=text.replace('Checkpoint state: 2026-11-19 06:16 UTC, updated through the exact endpoint image/standard-D reduction and the independently audited specified generic Walker counterexample.', 'Checkpoint state: 2026-11-19 07:10 UTC, updated through the fully specified morphic counterexample that refutes the universal complex E.3 converse, the exact one-motivic quotient, and integrated C.3v-w/C.4v-w.')
lines=text.splitlines()
for j,line in enumerate(lines):
 if line.startswith('| E.3 |'):
  lines[j]='| E.3 | DECIDED: characteristic-p forward implication proved; complex converse refuted; Lead E4 decided | E.3a–u: all earlier exact fixed-target equivalences and positive support cases; full morphic AJ kills N; the rational Lawson cylinder is a necessary condition; explicit degree14 section Y of Q6, gamma difference of plane sections, X=Y×E and normalized diagonal family give zero entire singular cylinder and injective Lawson cylinder; a specified generic elliptic point gives a nontorsion class modulo N under every complex embedding | No remaining gate for the requested universal decision. The additional comparison with the full morphic Jacobian is conjectural and is not used; low-codimension classification is not asserted. |'
 if line.startswith('| C.3 |'):
  lines[j]='| C.3 | INCOMPLETE; universal surjectivity classifications and all nonzero local-finiteness refutations settled | C.3a–w and C.1f: prior global obstruction sequences, exact Beauville tests and joint equivalence; strict-local cone injection; all nonzero ordinary local-finiteness ranges refuted; explicit Gysin/restriction failures; ordinary Picard injectivity; smooth-cone surjectivity all characteristics; exact ordinary divisor quotient with additive part already in dimension2; C.3w proves actual-family realization of proper local Picard abelian subgroups and integral positive-characteristic ordinary surjectivity in its algebraizable coefficient-field scope | General higher Griffiths/J injectivity (on all abelian varieties jointly equivalent to Beauville vanishing), higher local restriction kernels/cokernels, and extensions beyond the precisely stated geometric scope |'
 if line.startswith('| C.4 |'):
  lines[j]='| C.4 | INCOMPLETE | C.4a–w: all prior degree-one, integral-summand, ppav, scalar and numerical-cycle criteria; all supersingular surfaces; supersingular threefolds in characteristic≥5; full totally real multiplication cases in characteristic0, their good reductions, and ordinary full real multiplication cases in every positive characteristic including2 | Residual even-delta surfaces and residual primes2/3 for threefolds outside the affirmative families; exact integral numerical surface-class membership remains the test |'
 if line.startswith('| Lead E4 |'):
  lines[j]='| Lead E4 | RATIONAL EQUIVALENCE PROVED; literal INTEGRAL BICONDITIONAL REFUTED | E.3c, E.3j–k and E.3r settle the rational equivalence and provide the same fully specified fourfold where the family converse is true but the integral equivalence-relation equality is false. E.3u separately refutes the universal complex family converse, with a different sixfold and nontorsion family witness | None for the requested Lead decision; the integral and rational assertions remain distinct |'
text='\n'.join(lines)+'\n'
text=text.replace('This identifies the integral and rational family gates over C, but does not decide their truth universally.', 'This identifies the integral and rational family conditions over C. E.3u subsequently refutes their universal truth using full morphic Abel–Jacobi; the exact equivalences remain valid.')
text=text.replace('Current own-register totals: 56 statement rows and 110 check events.', 'At the dated 06:16 stage, own-register totals were 56 statement rows and110 check events. Current totals after the source audits and E.3s–u are59 statement rows and140 check events.')
text+='''
## Decisive morphic distinction and explicit E.3 refutation (07:10 UTC)

The original Walker2007 paper distinguishes its full morphic Jacobian from the finite coniveau Jacobian now commonly called the Walker Jacobian. The full map is exactly ordinary Albanese on zero-cycles and functorial for every correspondence of the nonnegative dimension shift needed here. Hence it kills every generator of N. Its Jacobian construction uses a countable integral Lawson group; strict Hodge filtration makes a nonzero rational H1 cylinder produce nontorsion morphic image. These are E.3t, with all exact primary statements opened.

E.3u specifies a degree14 geometric generic hypersurface Y in split Q6, using65891 independent coefficients, and gamma equal to the difference of its intersections with two displayed maximal planes. Gamma has zero integral H4 class, but its Lawson s-image is nonzero rationally. The latter is the effective Friedlander argument: the actual published input is Theorem3.4, not the4.5 locator printed in Walker6.1. Nagel vanishing through10 covers the proof's required restriction degrees8/6 and relative degree9. Smooth dominant spread handles extra transcendental coefficients. Taking the fixed elliptic curve v²=u³−u and X=Y×E produces a codimension4 family with zero singular cylinder and injective Lawson cylinder. Its specified geometric generic point e survives nontorsion modulo N by spreading a hypothetical finite N relation and contradicting the countable torsion preimage.

Thus N⁴(X) is strictly smaller than ker Walker=A*H, and P⁴(X) has a nontorsion kernel over the finite Walker Jacobian. The formerly open equality <H*²>₀=A*H is false universally. This does not refute the separately conjectured comparison of the large one-motivic quotient with the full morphic Jacobian; that comparison is not needed for any conclusion above. No codimension2 counterexample or Beauville-conjecture counterexample is inferred.

Root and Frobenius independently read the full typed E.3s–u proofs and exact primary sources. Their targeted checks, the nonproper-CH0 wording repair, locator corrections, and failed source URLs are recorded. New files: one_motivic_quotient.tex, morphic_counterexample.tex, morphic_results.csv (3 rows), morphic_CHECK_EVENTS.tsv (17 events), morphic_references.bib; generation_references.bib and generation_CHECK_EVENTS.tsv retain the preceding source/failed-route audits. code/check_morphic_counterexample.py and output/check_morphic_counterexample.json give the finite algebraic certificate and exact runtime0.056826961001206655 seconds. code/compile_morphic.py and output/compile_morphic.json retain the successful four-pass standalone7-page build, without undefined citations or overfull boxes at that version, in3.2785024129989324 seconds. Parent performs the integrated master build and visual review.
'''
path.write_text(text)
ledger=root/'PROGRESS_LEDGER.md'
with ledger.open('a') as f:
 f.write('''
### 2026-11-19 07:10 UTC — main E.3 gate closed by refutation

Integrated fully audited E.3s–u. Full morphic AJ, distinct from the finite Walker target, kills N and detects the specified zero-cylinder codimension4 elliptic family on a sixfold. Effective Friedlander/Nagel degree14, all-embedding spread, and a geometric generic point make the counterexample complete. The universal complex converse is false, while the characteristic-p forward theorem and rational Lead E4 equivalence remain proved; literal integral Lead E4 is already refuted on a separate specified fourfold. Root and Frobenius final proof/source checks passed. New3 results/17 events plus preceding13 source events produce59 owned result rows and140 owned events. This is a new main-gate decision, not a reformulation. C.3v-w/C.4v-w approved sibling/root fragments are integrated and current residual-scope paragraphs updated. Remaining work shifts to genuine primitive Griffiths/standard-conjecture and Beauville gates; full morphic nonvanishing is not asserted to refute Beauville.
''')
source=root/'notes/source_record.md'
with source.open('a') as f:
 f.write('''
## 2026-11-19 07:10 UTC primary morphic source audit

- Walker2007, full published Compositio143 pp909–944, DOI10.1112/S0010437X07002278. Example5.5 p928, Theorem5.7 p930, Corollary5.9 p932, Proposition3.3 pp916–917, Theorem6.2 proofpp933–934 opened, with original page images. Full morphic and finite coniveau Jacobians are different targets. Theorem6.1 citation4.5 is corrected against the original Friedlander publication; Corollary6.3 Y/X prose typo not propagated.
- Friedlander2000, Relative Chow correspondences and the Griffiths group, published AIF50(4)1073–1098, DOI10.5802/aif.1785. Published Definition3.1/Theorem3.2 p1081, Theorem3.4 p1082, Proposition5.1 pp1093–1095 and theorem proofpp1095–1097 read. Both published and author PDFs downloaded with hashes. Several web URLs failed, but official USC author PDF and direct Numdam published download succeeded.
- Ayoub2009, n-Motivic Sheaves, full3-page author report, Conjecture5 p2; published OberwolfachReport31/2009 DOI10.4171/OWR/2009/31 also opened. Comparison with full morphic AJ is explicitly conjectural; no comparison with the finite Walker Jacobian is attributed to it.
- Fresh search strings: "morphic Abel" "Albanese equivalence"; "Grothendieck" "morphic Abel" converse; "Beauville" "negative" "2026" Chow abelian conjecture. The first two returned the Walker and Ayoub literature and no exact previously stated manuscript formulation; no novelty claim follows. The third had substantial unrelated-name noise and requires stronger targeted primary searching.
''')
record={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'status':'Current status, ledger and source record updated; dated earlier attempts retained.'}
(root/'output/update_status_0710.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
