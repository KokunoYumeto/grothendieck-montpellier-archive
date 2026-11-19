"""Reconcile item scope and resolve the report table to compiled statement numbers."""
from pathlib import Path
import csv, json, re, sys, time
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
updates={
'B.1':('Incomplete; literal continuity refuted and abelian-type comparison proved','prop:B-continuity;thm:B-abelian-type;prop:B-phantom-gate','Under strong Tate and semisimplicity, universal comparison still requires vanishing of numerically trivial Chow phantom summands; no general vanishing proof is asserted.'),
'B.2':('All Tate degrees proved; general prescribed realization remains conjectural','thm:B-full-tate;cor:B-Hf-all-degrees;prop:B-general-rational-gate','Full étale groups retain Leopoldt/Schneider defects. Finite-condition Tate groups are unconditional; higher common Q-form identifications use chosen splittings. General M requires c0/c1 f-admissibility.'),
'B.3':('Arithmetic claims refuted; finite-field equivalences proved; universal finiteness undecided','thm:B-Sha-corank;ex:B-X011;thm:B-finite-chain-all-bases;prop:B-relative-curve','Kummer equivalence chain now covers every finite-type finite-field base, including singular and nonseparated bases. The manuscript relative-curve statement uses a regular base. Universal Tate/BSD finiteness remains open.'),
'B.4':('Proved as an effective presentation and generator construction','thm:B-SpecZ-Q;prop:B-integral-structure;thm:B-effective-odd-torsion;thm:B-primitive-generator','Every group and generator is specified by a proved terminating arithmetic/cycle procedure; arbitrary large searches are not represented as executed.'),
'B.5':('Finite and Artin–Tate cases proved; general rational realization remains conjectural','thm:B-finite-duality;prop:B-finite-duality-nonsep;thm:B-rational-duality;cor:B-Artin-Tate-duality;prop:B-general-rational-gate','Finite duality includes compact support by finite open-cover descent for nonseparated bases, real Tate modifications and characteristic-p motivic coefficients. General pure-M rational comparison requires the stated f-admissibility gate.'),
'C.1(a)':('General cohomological determination proved','c:matrix-presentation;c:contraction-matrix;c:dimension-pair','Finite contraction matrices determine every relation and rank from the full cup-product tensor; closed rank formulae are supplied in the stated curve and surface cases.'),
'C.1(b)':('Proved','c:graph-rule','Full graph product rule with excess Euler factors; finite checks attached.'),
'C.1(c)':('Incomplete; exact finite criterion proved in pure-even complex scope','c:finite-even-criterion;c:curve-chow-criterion;c:surface-chow-criterion;c:k3-transcendental-gate;c:fermat-counterexample','Classification over arbitrary algebraically closed fields and in mixed parity remains open. For X/C with pure-even cohomology, the all-powers property has a finite tensor criterion, whose Chow vanishing is not automatically decidable. General K3 still requires wedge^(23-rho)t2(X)=0.'),
'C.2':('Proved in corrected definition','c:bivariant-equivalence;c:r7-audit','Product-square exchange and Frobenius algebra reconstruction use bivariant adjoint pairs; the effective internal-Hom error is corrected.'),
'C.3':('Proved/refuted by distinguishing meanings','c:lie-centre;c:serre-centre;c:finite-field-lie','The arithmetic invariant centre, full geometric centre and analytic Lie algebra are different objects.'),
'C.4':('Proposed bound refuted; corrected bounds proved; general sharp lower endpoint unresolved','c:level-counterexample;c:weight-level-polygon;c:broader-coefficients;c:lic-endpoint;c:abelian-invariant-weights','Inherited delta-dimension is required. The sharp mixed-characteristic lower endpoint is equivalent to the stated local-invariant-cycle surjectivity; abelian-type coefficient motives satisfy the endpoint.'),
'C.5':('Refuted generally; positive conditions proved','c:vz-positive;c:explicit-bad-reduction','Explicit p=2 abelian-surface example over W(k)[[u,v]]/(2-uv), with nonflat finite subgroup closure; the positive Vasiu–Zink hypotheses are retained.'),
'C.6':('All abelian-type motives proved; general task incomplete','c:ell-independence-abelian;c:chow-unramified-purity-reduction;c:ell-independence-gate','Weak Mumford–Tate lift and common finite-inertia traces prove the abelian-type case. Homogeneous Chow projectors satisfy the result under the stated Frobenius-purity hypothesis. A general proof or exact named-conjecture equivalence has not been found.'),
'D.1':('Literal bridges refuted; corrected determinations proved','prop:d-integral-serre;prop:d-special-fibre-false;prop:d-cm-gerbe-reduction;lem:d-power-cm-lift;cor:d-all-weil','Schematic closure and a rational gerbe morphism replace the false special-fibre point claim. CM lifting is for A0^m over the exact residue field Fq, not a Frobenius power or residue-field extension.'),
'D.2(a)':('Abelian type proved; general exact Hodge-class equivalence supplied','thm:d-toric-classification','The exact additional CM comparison-class condition is retained in the general category, as permitted in the prompt.'),
'D.2(b)':('Refuted with an S4 Artin counterexample; category determined','prop:d-metabelian-false','A quotient of the Taniyama group need not be metabelian; the closed second-derived quotient gives the requested subcategory.'),
'D.2(c)':('Proved','prop:d-hodge-comparison','Aut(C) acts through Taniyama torsors and conjugation of CM types.'),
'D.3':('Computed; uniqueness claim corrected','thm:d-serre-finite-kernel;ex:d-non-betti','Finite-place-trivial Serre torsors give even-parity real Brauer vectors; the Betti functor is unique precisely in the stated rank-one case.'),
'D.4':('Proved','thm:d-reflex-image;cor:d-compact-image','The saturated character lattice and CM-type matrix determine the dimension and Mumford–Tate image.'),
'E.1':('Current statement index reconciled; programme remains incomplete','RESEARCH_SA05_results.csv','Every numbered statement is indexed with its scoped status; unresolved original item rows remain explicit.'),
'E.2':('Source records consolidated; final audit ongoing','LITERATURE_CHECK.tsv;RESEARCH_SA05_references.bib','Opening status, exact source locators and failed retrievals are retained; duplicate works are merged without dropping locator notes.'),
'Lead B1':('Incomplete as universally stated','prop:B-e;prop:B-continuity;prop:B-phantom-gate;prop:B-general-rational-gate','Restriction on the arithmetic class is proved; continuity at the geometric limit is refuted. Universal motivic comparison and general arithmetic realization retain their stated gates.'),
'Lead B2':('Proved with the stated archimedean completion','thm:B-SpecZ-Q;thm:B-rational-duality','The degree-three fundamental class, dual rank pattern and completed zeta-order interpretation are proved; the optional uniform Vandiver pattern is not asserted.'),
'Lead C1':('Modified-diagonal identification proved; all-powers general K3 scope incomplete','c:modified-diagonal;c:k3-determinant;c:k3-transcendental-gate','For K3, the narrow point-and-diagonal determinant first occurs on46factors; the smaller transcendental test uses divisor correspondences and does not lie in that narrow ring.'),
'Lead C3':('Corrected and proved/refuted by scope','c:lie-centre;c:serre-centre','The full geometric centre is larger than its arithmetic invariant part.'),
'Lead C5':('Proved identification and explicit counterexample','c:vz-positive;c:explicit-bad-reduction','The extension problem and a fully specified bad base with its nonflat subgroup are verified.'),
'Lead D1':('Literal special-fibre bridge refuted; rational replacement proved','prop:d-special-fibre-false;prop:d-cm-gerbe-reduction;cor:d-all-weil','Tate Frobenius refutes the special-fibre point interpretation; the rational band morphism and exact-residue CM lifting supply the replacement.'),
'Lead D2':('Metabelian slogan refuted; exact category clarified','thm:d-toric-classification;prop:d-metabelian-false','The S4 quotient and exact CM comparison-class equivalence are explicit.'),
'Lead D3':('Corrected and computed','thm:d-serre-finite-kernel;ex:d-non-betti','Finite-place-trivial Serre torsors, the norm torus in R3 and the real fibre-functor ambiguity are carefully distinguished.')
}
path=ROOT/'ITEM_STATUS.tsv'
with path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['item'] in updates:
        row['status'],row['statement_ids'],row['scope_or_gate']=updates[row['item']]
with path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
numbers={}
aux=ROOT/'build/RESEARCH_SA05_paper.aux'
if aux.exists():
    for match in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}',aux.read_text()):
        numbers[match.group(1)]=(match.group(2),match.group(3))
missing=[]
def statements(value):
    out=[]
    for key in value.split(';'):
        if key in numbers:
            number,page=numbers[key];out.append(f'{number} (`{key}`)')
        elif key.endswith(('.csv','.tsv','.bib')):out.append(f'`{key}`')
        else:out.append(f'`{key}` [number pending]');missing.append(key)
    return '; '.join(out)
table=['| Item | State | Numbered statements | Exact scope or remaining gate |','|---|---|---|---|']
for row in rows:
    vals=[row['item'],row['status'],statements(row['statement_ids']),row['scope_or_gate']]
    table.append('| '+' | '.join(v.replace('|','\\|') for v in vals)+' |')
report=ROOT/'RESEARCH_SA05_report.md';text=report.read_text()
start_table=text.index('| Item |');end_table=text.index('\n## Conventions',start_table)
text=text[:start_table]+'\n'.join(table)+'\n'+text[end_table:]
text=text.replace('The supplied Michel Hua project transcriptions and readings are the manuscript witnesses.',
 'The supplied GPT-6 Astra and GPT-6.2 Astra transcriptions, together with the Claude Opus 5.5 readings, are the principal manuscript witnesses. Michel Hua\'s project is a separate supplied witness; no mathematical remark from it is used without explicit credit.')
text=text.replace('Their source paragraphs are being corrected before the checkpoint PDF is frozen. Final counts and rendered-page inspection will be appended below before the ZIP is saved.',
 'Those source paragraphs were corrected before checkpoint01. The dated verification entries below give each later build and rendered-page inspection.')
report.write_text(text)
result={'items':len(rows),'updated_item_scopes':len(updates),'missing_compiled_labels':sorted(set(missing)),'seconds':round(time.monotonic()-start,4)}
(ROOT/'code/update_report_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
if '--require-numbers' in sys.argv and missing:raise SystemExit(1)
