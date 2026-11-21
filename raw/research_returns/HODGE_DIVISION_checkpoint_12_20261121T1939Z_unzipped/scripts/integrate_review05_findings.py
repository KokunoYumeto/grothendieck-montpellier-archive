"""One-time integration of fully checked ALT03 and E819, with current gates."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1]
for name,h in [('research/ordinary_alternating_sharp_obstruction.tex','fc04b494c256ef2f20aaa4d419e82358f2cd1bd265e5dcbe91b902ef671f1453'),('agents/sixfolds/rm_local_quantization_obstruction_section.tex','3b791ec282eca58390c46c14296abea3cf0dee0e7889a824448ee17df7467a34')]:
 assert hashlib.sha256((R/name).read_bytes()).hexdigest()==h
p=R/'research/ordinary_alternating_sharp_obstruction.tex';s=p.read_text();s=s.replace('Complete new root derivation, submitted for an independent whole-proof\nreview. The finite checks below do not substitute for the all-degree\nargument. No new finite character table is a premise.','Complete new root derivation with author whole-proof reading and an\nindependent whole-proof review by /root/g34\\_eightfolds, both PASS\non 21 November 2026. The independent symbolic and permutation\ncertificate also passed. The finite checks below do not substitute\nfor the all-degree argument. No new finite character table is a premise.')
p.write_text(s)
main=R/'HODGE_DIVISION.tex';s=main.read_text()
for after,path in [(r'\input{research/ordinary_alternating_obstruction.tex}','research/ordinary_alternating_sharp_obstruction.tex'),(r'\input{agents/sixfolds/rm_positive_defect_obstruction_section.tex}','agents/sixfolds/rm_local_quantization_obstruction_section.tex'),(r'\input{agents/sixfolds/rm_positive_defect_bibitems.tex}','agents/sixfolds/rm_local_quantization_bibitems.tex')]:
 assert after in s and path not in s;s=s.replace(after,after+'\n'+r'\input{'+path+'}')
a=s.index('D-BI-18 gives a further normal-subgroup gate.')
b=s.index('\nThe cyclic-source failure for the other quadratic fields',a)
s=s[:a]+r'''D-BI-18--20 now give a structural normal-core gate. Every primitive,
factorwise tensor-indecomposable inducing image of degree at least five
has a unique nonabelian simple-power core modulo scalars, whose
quasisimple central-product lift acts irreducibly and has transitive
factors. Extraspecial alternatives are excluded. In inducing degree
at least ten, a nonalternating Lie core has field size at most twenty-seven;
essentially self-dual cores obey the stronger stated field bounds.
D-SPOR-01--03 excludes every sporadic core. D-BI-21 excludes all
rank-one Lie cores, including the small exceptional alternating
isomorphisms and covers in its scope. D-BI-22 excludes all Suzuki,
Ree and Tits cores. D-SPW-01--03 reduces odd symplectic Weil cores
to one degree-four or degree-five factor of $\operatorname{Sp}_4(3)$;
D-SPW-04 gives the same final small endpoint for all its irreducible
representations in the nonsplit non-Eisenstein problem. Other small-field
higher-rank Lie representations remain outside these exclusions.

For alternating cores, HD-SPIN-02 excludes all faithful double-cover
spin factors in degree $n\ge8$. HD-ALT-02 and D-AST-01--03 together
exclude the entire ordinary range $8\le n\le14$. HD-ALT-03 excludes
all ordinary factors for $n\ge15$ with
$\max(\lambda_1,\lambda'_1)\le\lceil n/2\rceil$, including both
nonreal and real split constituents. Thus a remaining large ordinary
alternating core has a longer first row or column; its factor
representation extends to a real Specht representation and its full
inducing image is essentially self-dual. The scalar single-factor
standard, exterior-square and unordered-pair families remain excluded
in all degrees by D-BI-08, D-EX and D-UP. Long-shape tensor constructions
and the remaining small exceptional alternating covers require separate
arguments. No surviving group profile has been promoted to a source
without original-field descent and an actual period-rank computation.

For the genuine balanced-real-multiplication eightfold alternative,
SF-E811 excludes every stable locally free normalized balanced character,
and SF-E812--813 excludes weakly equivariant semiregular semistable
bundles with locally free stable factors. SF-E818 extends this to
balanced torsion-free sheaves whose locally free hull has such a
stable-factor filtration: mixed positivity eliminates surface and curve
defects, and SF-E817 excludes every remaining nonzero point defect.
The point-defect theorem itself does not assume stability or simplicity
and gives trace-kernel dimension at least $1+3s$, for $s$ support orbits.

SF-E819 now includes actual point torsion as well as point cokernel.
For any balanced coherent sheaf with locally free hull and finite
kernel/cokernel, weak equivariant semiregularity forces equal lengths
at each point. SF-E819R excludes every nontrivial local modification
when both modules are reduced. Hence only equal-length modifications
with a nonreduced module at every nontrivial point remain in that local
class. The actual rank-thirty-six balanced nonpure sheaf is constructed
and excluded; it is not a successful seed. A locally free sheaf with
zero defect is outside this local conclusion and still requires the
separate stability hypotheses of the earlier results.

For derived constructions, SF-E815/R requires at least sixty-three
invariant endomorphisms in the seven-class model and excludes the
stated simple nonnegative-aggregate projectively flat models.
SF-E816/a/b/c excludes ordinary-gluable primitive projectively flat
models in any two cohomology degrees, including overlaps and arbitrary
gaps, and arbitrary bounded amplitude with globally disjoint classes.
The actual three-degree example SF-E816d refutes automatic disjointness,
but has a pure character and is not a balanced seed. Remaining routes
include unstable locally free objects, singular stable factors or
reflexive hulls, the nonreduced equal-length modifications just described,
positive-dimensional torsion or defects outside SF-E818, and overlapping
class sets in at least three cohomology degrees. Twisted objects and
sufficiently nonsimple constructions retain their stated separate gates.
The full trace--evaluation composition used in SF-E819 is directly the
published Buchweitz--Flenner Theorem~6.4.2, not a theorem of 032.
''' +s[b:]
main.write_text(s)
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0]);assert not any(x['id'] in {'Q2av','Q5p'} for x in rows)
old={x['id']:x for x in rows if x['id'] in {'Q2i','Q5i'}}
(R/'research/gates_before_review05_consolidation.json').write_text(json.dumps(old,indent=2,ensure_ascii=False)+'\n')
g2='Every split class-number-one sixfold, every Eisenstein determinant and Gaussian signed determinant class3 has a numerical detector bound. Other nonsplit determinants remain open. Curve sources require actual original-field descent and period rank9. Original reflection-free coefficient degree>=15; inducing dimensions1/2/3 and non-Eisenstein7 are excluded. The remaining inducing4/5/6/8 exceptional profiles are exactly D-BI11/12,D-R5,D-BI16,HD-E8IF1; the explicit paired G33 Nielsen component is excluded, other components/descent remain. D-BI13/14/14a/15 impose the stated ramification, degree and nonnormality bounds. For every primitive factorwise tensor-indecomposable inducing degree>=5, D-BI19 forces an irreducible transitive quasisimple central-product core. D-BI18/20 excludes extraspecial cores and Lie fieldsq>=29 in degree>=10, with stronger ESD bounds. All sporadic, allA1, allSuzuki/Ree/Tits cores are excluded (D-SPOR,D-BI21/22). Odd symplectic Weil cores reduce to singleSp4(3)degree4/5; D-SPW04 gives the same nonsplit non-Eisenstein endpoint for all its representations. Other small-field higher-rank Lie cores remain. All spin2.An,n>=8, and all ordinaryAn,8<=n<=14, are excluded (HD-SPIN02,HD-ALT02,D-AST). HD-ALT03 forces any remaining ordinaryAn,n>=15,to have a row/column>ceil(n/2); its factors extend to real Specht modules and the inducing image is ESD. The all-degree scalar single-factor standard,exterior-square andunordered-pair cases remain excluded; long-shape tensor cases and residualA7/covers remain. These are necessary supplier restrictions, not existence results. The non-curve alternative is Q5i.'
g5='No genuine balanced-RM weakly equivariant semiregular eightfold seed has been constructed. SF-E801--E810 excludes the stated rational-block, integrality and CI-secants; the actual semiregular coneSF-E814 has two-pure character and does not meet this gate. SF-E811--E813 excludes stable/polystable locally free objects and semistable bundles with locally free stable factors. SF-E818 extends this to torsion-free objects with such locally free hulls. SF-E817 excludes all nonzero point defects with a locally free hull, without stability/simplicity. SF-E819/E819R includes nonpure coherent objects: locally free hull with finite kernel/cokernel requires equal lengths at each point, and every nontrivial point must have a nonreduced defect module. The actual rank36 nonpure balanced construction fails this test. Locally free objects with zero defect require the separate stability exclusions. SF-E815/R excludes the stated simple positive-aggregate projectively-flat models; the seven-class model requiresEndG>=63. SF-E816/a/b/c excludes ordinary-gluable primitive projectively-flat models in any two cohomology degrees, including overlaps/arbitrary gaps, and arbitrary amplitude with globally disjoint classes. Remaining: unstable bundles, singular stable factors/reflexive hulls, nonreduced equal-length point modifications, positive-dimensional torsion/defects outsideE818, overlapping classes in at least3cohomology degrees, twisted or sufficiently nonsimple objects, and broader class spaces. The pure counterexampleE816d does not supply a balanced seed.'
for x in rows:
 if x['id']=='Q2i':x['finding_ids_or_current_gate']=g2
 if x['id']=='Q5i':x['finding_ids_or_current_gate']=g5
rows.extend([dict(zip(fields,['Q2av','Prompt target2; remaining ordinary alternating shapes','Can a balanced Young shape occur without the ESD hypothesis?','refuted','HD-ALT-03a/b/c: every normalizernu>=7a/40; all-tensor rank9 budgete<=60 contradicts factor degree>=125 for n>=15. Covers nonreal split constituents and all scalars/outers; surviving long shapes force ESD.'])),dict(zip(fields,['Q5p','Prompt target5; nonpure point-modification gate','Which finite point modifications of locally free hulls can remain weakly semiregular?','proved','SF-E819: signed length is zero at each point. SF-E819R: nontrivial reduced kernel/cokernel is impossible; remaining nontrivial modifications need a nonreduced module at every support point. Actual rank36 balanced sheaf with torsion34/defect36 is constructed and excluded. No successful seed claimed.']))])
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
now=datetime.now(timezone.utc).isoformat()
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in [
 ('HD-ALT-03a/b/c','targeted proof check','Whole author proof reread and independent complete peer audit read; PASS all normalizer/split cases, actual commutator ranks, content bounds, polynomial positivity and all-n/all-tensor contradiction. Canonical header changed only to reflect passed reviews.','research/ordinary_alternating_sharp_obstruction.tex; agents/g34_eightfolds/bireflection/ORDINARY_ALTERNATING_SHARP_PEER_AUDIT.md'),
 ('HD-ALT-03 exact certificate','computation or formal certificate','Actually wrote and executed exact independent formula driver:463 complete symmetric character rows match content formulas;43312 partitions15--32 with35100 balanced pass;8777 commutator types and80 even-conjugator cases pass. This finite check supports but does not prove the all-n statement.','research/alternating_sharp_certificate.py; alternating_sharp_certificate.json'),
 ('SF-E819/E819R canonical','targeted proof check','Read whole580-line canonical TeX including the actual construction and all limits, compared mathematical scope to reviewed Markdown and complete G34 audit. PASS final source substitution, formal-log coordinates, invariant-trace premise, nontrivial-modification qualification and unabridged conversion. CanonicalSHA3b791ec282eca58390c46c14296abea3cf0dee0e7889a824448ee17df7467a34.','agents/sixfolds/rm_local_quantization_obstruction_section.tex; agents/g34_eightfolds/bireflection/LOCAL_QUANTIZATION_PEER_AUDIT.md')]:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Infinite ordinary alternating and nonpure coherent gates\n\n'+now+' — Q2av refuted and Q5p proved. HD-ALT03 removes the ESD hypothesis from the balanced ordinary Young-shape exclusion for every n>=15 and forces all remaining large ordinary factors into real long shapes, hence ESD. SF-E819/E819R extends the point-defect exclusion to actual point torsion: equal local lengths are necessary, and reduced nontrivial modifications are impossible. The actual rank36 balanced nonpure example is excluded. Both full proofs have independent whole readings and separate exact certificates. These properly reduce both main gates. Current Q2i/Q5i fields and paper summary were consolidated to remove superseded intermediate wording; prior fields are retained in research/gates_before_review05_consolidation.json. Editorial consolidation is not itself movement.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Infinite shape and local quantization restrictions\n\nHD-ALT03 excludes all balanced ordinary alternating shapes, including nonselfdual split constituents, and proves that remaining large ordinary cores are essentially selfdual long-shape representations. SF-E819/E819R excludes nonpure balanced coherent sheaves with unequal local signed defects or nontrivial reduced local defects; the constructed rank36 example is an actual failed seed. The local argument lives in K-theory with support, first-order module deformations, derived perfect traces and Hochschild evaluation. Published Buchweitz–Flenner supplies the trace/cap identity, with suppliedS21 used only for the specified invariant-action compatibility. These findings narrow condition A supplier existence (cote16 scan050). They do not turn condition I (scan049/cote44Theorem4) into cycle existence or change the Cayley–Hamilton projector in scans048--049. The remaining detector and derived-seed gates are stated explicitly; no new claim about weights or motivic L-functions follows from these exclusions.\n')
print(json.dumps({'integrated':['HD-ALT03','SF-E819/E819R'],'time':now,'alt_final_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
