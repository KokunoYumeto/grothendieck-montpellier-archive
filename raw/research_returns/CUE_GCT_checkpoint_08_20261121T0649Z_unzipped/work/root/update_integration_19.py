"""Integrate the checked higher-row rectangular equality-boundary comparison."""
from pathlib import Path
from datetime import datetime, timezone
import csv,hashlib,json
R=Path(__file__).resolve().parent;W=R.parent;OUT=W.parent/'deliverables'
now=datetime.now(timezone.utc).isoformat()
guard=R/'integration_19_check_events.tsv';assert not guard.exists()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'findings.tex';s=p.read_text();assert '[G-24:' not in s
p.write_text(s+'\n\n'+(R/'g24_fragment.tex').read_text())

p=R/'grothendieck.tex';s=p.read_text();marker='\\subsection{What the manuscript record does and does not establish}'
addition=r'''
\paragraph{G-24. Boundary cocharacters and restriction of invariant algebras.}
At $n=ra$ and $m=(r-1)a$, the cocharacter with weights
$(r-1,-1,\ldots,-1)$ sends a padded form to
$x_0^a q(0,x_1,\ldots,x_{r-1})$. Every invariant section
has the same value on this limit. Restriction therefore
injects the padded invariant coordinate algebra, with its
original grading, into the $(r-1)$-variable permanent
invariant algebra. Injectivity follows from the limit on
the dense padded image, not from an assumed equality of
the two algebras. This is a cocharacter-specialization
statement in D-S3 and a morphism of graded coordinate
algebras in D-FGA.

For $r\ge5$ the lower algebra has the exact stable quotient
dimension supplied by G-21. For $r=4$ it is bounded degree
by degree by the full ternary invariant algebra, whose map
onto the lower permanent algebra is a surjection by
exactness of invariants. R-28 supplies a separate free
stable point in each comparison ring by adding one linear
factor; the integer $a\ge2$ makes both auxiliary directions
strict. Thus both degree semigroups have gcd one. Their
dimensions satisfy $u>v$, and the explicit common generator
bound and Veronese make the Hilbert comparison strict at
every sufficiently large original degree. Above the
boundary the same cocharacter sends the form to zero.
Together with G-23 this proves the exact eventual rectangular
range through $m$ rows, with the stated finite-degree and
nonrectangular exclusions from its scope. EGA~II, 2.5.2,
places the projectivizations, and the stable quotient and
image-degree locators are those already recorded for G-23.

'''
assert marker in s;p.write_text(s.replace(marker,addition+marker))
p=R/'intro.tex';s=p.read_text();s=s.replace('Every rectangle with\n$m<n<rm/(r-1)$ lies in the positive range. Boundary faces and\nindividual finite degrees retain their separate scope.','G-24 completes the rectangular boundary comparison: the exact eventual positive range is $m<n<rm/(r-1)$. At equality the determinant eventually dominates, and above it every permanent rectangle vanishes. Nonrectangular boundary faces and individual finite degrees retain their separate scope.')
p.write_text(s)
p=R/'open_gates.tex';s=p.read_text();s=s.replace('the first-row boundary face in higher rank','the nonrectangular first-row boundary face in higher rank')
s=s.replace('The higher-rank boundary face,\nmore than $m$ rows, finite-degree extraction and changing directions\nremain open. A boundary degeneration to $(r-1)$ variables is the\nnext rectangular comparison under investigation; no result of that\nattempt is asserted in this paragraph.','G-24 closes the rectangular equality boundary through $m$ rows by an injective restriction to the $(r-1)$-variable invariant algebra and a strict Hilbert comparison. Nonrectangular boundary faces, more than $m$ rows, finite-degree extraction and changing directions remain open.')
p.write_text(s)
p=W/'assemble.py';s=p.read_text();s=s.replace('with explicit stretch bounds and no integer dimension-equality case.','with explicit stretch bounds and no integer dimension-equality case. A lower-variable boundary comparison completes the exact eventual rectangular range through $m$ rows.')
p.write_text(s)
p=R/'questions.tsv'
with p.open(newline='') as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['id']=='G-Q28':row['state']='PROVED G24 for m>=17,4<=r<=m: exact eventual positive rectangle range m<n<r m/(r−1). At equality an injection into lower-variable permanent invariants and explicit Hilbert threshold give eventual determinant dominance. Above equality permanent rectangles vanish in every positive admissible degree. No all-finite-degree equality-boundary exclusion is claimed forr>=5.'
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)

with guard.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome'])
 w.writerow(['G-24',now,who,'targeted proof check','PASS complete root derivation and final proof reading: cocharacter weights and exact limit, graded injection of actual padded invariants, correct r4 ambient surjection, both separate free stable points, explicit u/v and strict differences, common bound on generators and counts, separate gcd-one sandwiches, valid parameter-degree upper bound, every-degree threshold and all admissible coordinate degrees. Entire independent rectangular proof reading PASS separately recorded.'])
 w.writerow(['R-28',now,who,'used and rechecked in this run','Formatting-only transition: inserted an introductory sentence between begin{proof} and first paragraph heading to avoid amsthm Improper prevdepth. Mathematical statement and proof unchanged. Final hash0fcab71312a92c8b051a16d41056a09d4bb4edfaae382c72e628338acf7dba32; previous whole-proof review hash0c0349405b10d25a523f488e3400fdda392ee111c430eeda9b613c8a6753473b retained historically.'])
(R/'g24_review_hash.json').write_text(json.dumps({'checked_utc':now,'who':who,'status':'PASS full proof read','sha256':hashlib.sha256((R/'g24_fragment.tex').read_bytes()).hexdigest()},indent=2)+'\n')
with (OUT/'LEDGER.md').open('a') as f:
 f.write('\n\n## '+now+' — completed higher-row rectangular boundary\n\nG24 passes complete root and independent rectangular proof readings. It closes the equality-boundary question introduced in GQ28: for m>=17,4<=r<=m the exact eventual positive rectangular range is m<n<r m/(r−1). At equality determinant dominance is effective; above equality permanent rectangles vanish. Earlier finite-degree boundary gaps are not excluded forr>=5. This is a dated result, not an actual scheduled review.\n')
with (OUT/'IMPLICATIONS.md').open('a') as f:
 f.write('''\n\n### Rectangular equality boundaries are also controlled\n\nG24 completes the higher-row rectangular comparison for m>=17 and4<=r<=m. Eventual positive gaps occur exactly for m<n<r m/(r−1). At equality the padded invariant algebra injects into the lower-variable permanent invariant algebra; its Hilbert growth is strictly smaller than the determinant invariant algebra, with an explicit every-degree threshold. Above equality the padding cocharacter sends every form to zero and every positive-degree permanent rectangle vanishes. Forr4 the earlier all-degree weak boundary exclusion remains valid; forr>=5 G24 proves an eventual statement and does not rule out individual earlier-degree gaps. Nonrectangular boundary faces and rows beyondm remain the next comparisons.\n''')
print(now)
