"""Record complete P19/R31 readings and synchronize the live scope."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json
R=Path(__file__).resolve().parent; W=R.parent; O=W.parent/'deliverables'
guard=R/'integration_22_check_events.tsv'; assert not guard.exists()
now=datetime.now(timezone.utc).isoformat()
who='GPT-6 Astra Pro; /root; effort not exposed; CUE_GCT_20261121_R1'
expected={
 'purity/P19_all_cubic_balanced.tex':'4bb5f2f9588840bf41986b657ba3493ebd92cda0f01bea09f52ba896b1535cee',
 'rectangular/r31_fragment.tex':'b707e90d76de328d39f6a6f87ab6b4c9f6e989cdf3b6a041837f690b99335976'}
for rel,h in expected.items(): assert hashlib.sha256((W/rel).read_bytes()).hexdigest()==h
assert 'P-19.' in (W/'purity/findings.tex').read_text()
assert 'R-31:' in (W/'rectangular/findings.tex').read_text()
audits={
 'P19': 'Complete proof read, including the complete P18 dependency. Independently reconstructed both rank-at-least-two derivative submatrices across the cut after j. Homogeneous left degrees make their ranks add. At most one exclusive middle variable and two endpoint intersections give at most three middle coordinates. The Vandermonde kernel has no vector on those coordinates; exterior projection is injective, yet every support triple is killed. Grid, all-characteristic scope, reversal and the degree interval [4,n-4] follow with the stated lowest-component inheritance. No higher-degree or growing-width conclusion is inferred.',
 'R31': 'Complete proof read. The compensated transposition fixes F and the auxiliary covector and has determinant -1. Normalization by zeta with zeta^r=-1 gives an SL element acting on the enhanced vector by (-1)^b because ms=rb. Dense independent-factor and auxiliary parameters imply odd invariant vanishing on the entire enhanced common subcone. Cartan extraction gives the multiplicity statement. Closed-orbit separation puts w and -w in the same orbit, excluding no-scaling closed points. The result concerns only the two-product subcone, and quotient restriction gives no vanishing assertion for either full orbit closure.'}
for name,body in audits.items():
 rel=next(k for k in expected if name[:1].lower() in k.split('/')[0] and name[1:] in k.split('/')[-1])
 (R/f'independent_review_{name}_root.md').write_text(f'# Complete root proof reading: {name}\n\nActual record: {now}\n\nWho: {who}.\n\nSHA256: {expected[rel]}\n\nOutcome: PASS. {body}\n')

p=R/'grothendieck.tex'; s=p.read_text(); marker='\\subsection{What the manuscript record does and does not establish}'
addition=r'''
\paragraph{P-19. A three-coordinate transversal and an injective exterior projection.}
Over the distinct-node base, the rank-three Vandermonde map
defines a kernel bundle $K$. Every coordinate subbundle on at
most three nodes meets $K$ trivially; projection away from such
nodes is consequently injective on $K$ and on its third exterior
power. The P-18 ordered-support reduction and two disjoint
rank-two coefficient blocks show that a smallest width-three
cubic counterexample would have all its monomial supports
meeting one set of at most three coordinates. Its decoded
section of $\bigwedge^3 K$ would be killed by that injective
projection. This contradiction works on every field fiber of
the distinct-node base. The proof uses determinantal coefficient
charts from D-FGA, split-torus degree blocks from D-S3, and the
exterior operations of D-S6. It closes both boundary cases of
P-18, with $20(n+1)^2$ evaluation points, and leaves degrees
four through $n-4$ as the remaining balanced width-three gate.

\paragraph{R-31. A residual scalar character on a common parameter scheme.}
On the open parameter scheme where the $2m+1$ product and
padding factors are independent, a compensated transposition
fixes the polynomial and its auxiliary covector. Its determinant
character is $-1$. After lifting to the special linear group,
the enhanced tensor has character $(-1)^b$. Density forces
every odd graded invariant to vanish when $b$ is odd. The
coordinate ring and its Cartan extraction are the D-FGA and
D-S6 constructions of G-22; the stabilizer character belongs
to D-S3. Over $\mathbb C$, closed-orbit separation then rules
out a nonzero closed point with trivial scalar period on this
common enhanced subcone. It does not impose the same character
on the larger permanent or determinant schemes. The obstruction
therefore narrows the next stable-point construction rather
than supplying an equation or multiplicity comparison for the
full cones.

'''
assert marker in s; p.write_text(s.replace(marker,addition+marker))

p=R/'intro.tex'; s=p.read_text()
old='P-18 proves an arbitrary-length trilinear three-block class with $20(n+1)^2$ balanced samples and reduces the unrestricted cubic problem to at most two shared boundary variables.'
new='P-18 proves the trilinear class and a smallest-counterexample support reduction. P-19 closes both remaining boundary cases: every multilinear width-three cubic is hit by balanced two-pair evaluation, in every characteristic and with no restriction on the number of variables, using $20(n+1)^2$ samples. Any remaining balanced width-three annihilator has its homogeneous degrees in the interval $[4,n-4]$.'
assert old in s; s=s.replace(old,new)
s=s.replace('boundary faces beyond $m$ rows and individual finite degrees retain their separate scope.','boundary faces beyond $m$ rows and individual finite degrees retain their separate scope. R-31 proves a scalar-period obstruction for the unchanged two-product family at $2m+1$ rows in specified strict directions. Its odd-degree vanishing is a subcone statement, not a statement about either full orbit closure.',1)
p.write_text(s)
p=R/'open_gates.tex'; s=p.read_text()
s=s.replace('P-18 additionally\ncovers an arbitrary-length trilinear class and reduces a smallest\nunrestricted cubic counterexample to at most two shared boundary\nvariables.','P-19 closes the unrestricted cubic case in every characteristic\nand every variable count, using the P-18 support reduction.\nEvery remaining annihilator has homogeneous degrees in\n$[4,n-4]$.')
s=s.replace('changing\ndirections and efficient finite-degree extraction remain open.','changing\ndirections and efficient finite-degree extraction remain open.\nR-31 excludes the unchanged two-product no-scaling construction\nin specified $2m+1$-row directions by an unavoidable scalar\nperiod; other common pencils and the full cones remain open.',1)
p.write_text(s)
p=W/'assemble.py'; s=p.read_text()
s=s.replace('through ten variables. Purity gives additional','through ten variables. A smallest-counterexample support argument additionally proves the full cubic statement in every variable count. Purity gives additional',1)
p.write_text(s)

with guard.open('w',newline='') as f:
 wr=csv.writer(f,delimiter='\t',lineterminator='\n'); wr.writerow(['statement_id','date','who','type','outcome'])
 for name,body in audits.items(): wr.writerow([name[0]+'-'+name[1:],now,who,'targeted proof check','PASS whole-proof reading. '+body])
(R/'integration_22_review_hashes.json').write_text(json.dumps({'checked_utc':now,'who':who,'status':'PASS complete proof readings','hashes':expected},indent=2)+'\n')
with (O/'LEDGER.md').open('a') as f:
 f.write(f'\n\n## {now} — unrestricted cubic theorem and next-row family obstruction\n\nP19 closes the complete balanced two-pair cubic statement for width three, all variable counts, every characteristic, with 20(n+1)² samples. Both shared-boundary cases of P18 are resolved by the rank-four cut contradiction and the injective exterior projection away from at most three nodes. Root and isolation read the complete proof and its P18 dependency. R31 proves odd-degree vanishing on the specified two-product enhanced cone at2m+1 rows, excluding its no-scaling strategy; it does not assert vanishing on the full determinant or permanent cone. Both root and purity read its complete proof. The main growing-width sampling gate is still open.\n')
with (O/'IMPLICATIONS.md').open('a') as f:
 f.write('\n\n### All cubic balanced width-three instances are resolved\n\nP19 removes the variable-count restriction from the cubic theorem. Its proof forces a smallest counterexample to have a three-coordinate support transversal, which is impossible for the third exterior power of the Vandermonde kernel. The uniform sampler has20(n+1)² points in every characteristic over the stated working field. Reversal and lowest-component inheritance restrict any remaining width-three annihilator to homogeneous degrees4 throughn−4. This is a genuine degree reduction, without a polynomial-in-growing-width PIT conclusion.\n\nR31 identifies a residual scalar character that prevents the current two-product common family from furnishing a no-scaling closed point in certain strict2m+1-row directions. The obstruction is internal to that family. New common families or separate stable constructions on the two full cones are still available approaches.\n')
print(now)
