#!/usr/bin/env python3
"""Promote the audited arbitrary-field upper-cone theorem and exact inputs."""
from pathlib import Path
import csv
import datetime
import json
import time

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
aux=(base.parent/'C'/'B2_alteration_abelian_realization.tex').read_text()
aux=aux.replace('Auxiliary B.2 lemma: abelian realization through a Galois alteration',
                'Statement B.2t (Proved): abelian realization through a Galois alteration')
aux=aux.replace('[Proposed; precise equivariant alteration data]', '[Equivariant alteration data]')
aux=aux.replace('[Proposed; realization of every invariant abelian subgroup]', '[Realization of invariant abelian subgroups]')
aux=aux.replace('[Proposed; relative Picard sheaves with finite constants]', '[Relative Picard sheaves with finite constants]')
aux=aux.replace('B.R.1','B.2.14')
aux=aux.replace('Application and current verification scope','Application to the fixed comparison group')
old='''The preceding realization lemma is designed to replace an
unjustified assertion that an alteration over $k^{\\mathrm{perf}}$
has no separable constant extension.  Its semilinear descent
and finite-evaluation-kernel arguments are written explicitly
for independent audit.  Until that audit is complete, this
fragment is separate from the checked main text.
'''
new='''The construction retains the possible separable constants of an
alteration over $k^{\\mathrm{perf}}$.  Its semilinear action,
translation quotient and purely inseparable field homomorphism
are part of the proof, rather than an assumption that those
constants disappear.  All three lemmas have undergone the
targeted proof checks recorded in the accompanying ledger.
'''
assert old in aux
aux=aux.replace(old,new)
(base/'B2_alteration_abelian_realization.tex').write_text(aux)

path=base/'B2_arbitrary_field_stabilization.tex'
general=path.read_text().replace('% Complete proposed extension, kept separate until actual-file audits finish.',
                                '% Complete proof after independent actual-file audits.')
general=general.replace('Statement B.2u:','Statement B.2u (Proved):')
path.write_text(general)
path=base/'paper_B.tex'
paper=path.read_text()
assert 'Statement B.2t ' not in paper and 'Statement B.2u ' not in paper
paper=paper.replace('normal source.  Nor does it settle the remaining imperfect-field\nimage problem in B.2, whose permitted models can have singular\ntargets.',
                    'normal source.  This vanishing alone does not control the\nPicard images at singular targets; Statements B.2t--u below\nsupply that additional argument over arbitrary fields.')
paper=paper.replace('\\begin{remark}[The remaining image problem]',
                    '\\begin{remark}[The separate image problem]')
paper=paper.replace('argument cannot be silently imported into the permitted category.\n\\end{remark}',
                    'argument cannot be silently imported into the permitted category.\nStatements B.2t--u solve this image problem by successive\nrestrictions at bad divisorial valuations.\n\\end{remark}')
paper=paper.replace('not erase the obstruction of Statement B.2i.  The unresolved\noriginal-field image problem is therefore genuinely a descent and\ngeometric-realization problem, rather than a failure to obtain a\nfinite field of definition for the stable perfect-field model.',
                    'not erase the obstruction of Statement B.2i.  The additional\noriginal-field realization is supplied by B.2t--u; its proof\nuses semilinear alteration constants and valuation restrictions,\nrather than only a finite field of definition for this model.')
paper=paper.replace('line bundles, and the norm argument of B.2j.  The missing uniform\nbound for the images $h_X$ is unchanged.',
                    'line bundles, and the norm argument of B.2j.  The separate\nuniform bound for the relevant image quotients is proved in\nB.2t--u by a valuation restriction argument.')
paper=paper.replace('proved in B.2h over perfect fields and in B.2s whenever a proper regular\nbirational model exists, in particular in dimension at most three.  The\nremaining arbitrary-field scope is stated separately in B.2-U.  We do not infer its failure from this example.',
                    'proved over every ground field in B.2u below.  Thus both\ncohomological boundedness and weak upper-cone stabilization\nhold, while constant cofinality fails in the present example.')
path.write_text(paper+'\n\n'+aux+'\n\n'+general)

path=base/'results_B.csv'
with path.open() as stream:
    reader=csv.DictReader(stream);fields=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['id']=='B.2-U':
        row.update(statement='Previously tracked weak upper-cone replacement over arbitrary fields, now closed by B.2u',status='Proved; former unresolved gate closed',where_proved='paper_B.tex Statement B.2u',depends_on='B.2r; B.2t; B.2m; fixed-Jacobian bound; successive bad-valuation restrictions',notes='The full weak assertion holds above every initial permitted model over every field. Historical unresolved entries are retained in the chronological check log. Constant domination-cofinal diagrams remain separately refuted by B.2q.')
    if row['id']=='B.2k':
        row['notes']=row['notes'].replace('the imperfect-field image gate remains separate.', 'the separate image problem is solved in B.2t--u.')
    if row['id']=='L6c':
        row['notes']=row['notes'].replace('or resolve the singular-target B2 image gate.', 'by itself; the singular-target B2 image argument is supplied separately in B.2t--u.')
rows.extend([
dict(id='B.2t',statement='Equivariant regular alteration data with semilinear finite constants realize every invariant abelian Picard subgroup up to an explicit isogeny; full relative Picard sheaves commute with finite constant restriction when a smooth open exists',status='Proved',where_proved='paper_B.tex Statement B.2t and Lemmas B:equivariant-constant-data / B:invariant-abelian-realization / B:Pic-finite-constants-sheaf',depends_on='deJong1997 Situation5.3/Theorem5.13/Corollary5.15; finite-presentation descent from kperf; ACMV2026 Albanese torsors; Galois descent; Frobenius/Verschiebung; generator-open trivialization',manuscript_pages='29/075',notes='Finite separable alteration constants are retained, with Γ-semilinear action. Translation killing and q-power field descent give image [n]V^e exactly the given abelian subgroup. Full-fppf Pic identification includes nonreduced parameter schemes; no equality of tau-Weil restrictions is assumed.'),
dict(id='B.2u',statement='Above every initial proper geometrically normal model over every characteristic-p field there exists a model whose entire upper cone has isomorphic Pic^tau group schemes',status='Proved',where_proved='paper_B.tex Statement B.2u',depends_on='B.1g; B.2d; B.2m; B.2r; B.2t; fixed extended divisorial valuation and generic-fibre restriction; bounded exponent dN',manuscript_pages='29/075',notes='Closes the formerly unresolved weak replacement in all dimensions and over arbitrary imperfect fields. It does not assert cofinality: B.2q gives incompatible stable branches. Root/C/D actual-file checks are recorded; no priority claim is made.')])
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(rows)

events=[
('B.2t','/root/part_c','proved','C wrote the complete semilinear finite-constant alteration, invariant abelian-torsor realization and full relative-Picard sheaf lemmas. The unjustified pure-constant shortcut was discarded before promotion.'),
('B.2t','/root/part_b, actual-file reading','targeted proof check','B read the full source: descent from kperf including finite separable constants; fixed-field purity; finite evaluation kernel; Γ0 translations; Galois torsor descent; exact q-power base change and [n]Verschiebung image; all-parameter Picard rigidification via Weil restriction of a smooth open. No gap found.'),
('B.2t','/root, actual-file reading','targeted proof check','Root read all three written lemmas, independently reopened de Jong Situation5.3/5.12.1/Theorem5.13/Corollary5.15, and checked semilinear action, invariant fields, finite evaluation kernel, torsor descent and full fppf Picard identification. No gap found.'),
('B.2u','/root/part_b','proved','Wrote the full arbitrary-field theorem with source abelian group A_* distinguished from its image A0, divisor w above bad K-valuation v, restriction on the full ambient group and uniform dN quotient exponent.'),
('B.2u','/root/part_c, actual-file reading','targeted proof check','C read the full theorem and verified fixed-L normal graphs, κ(w)/κ(v) finite, normal generic-fibre Picard injection on all parameters, nonconstant torsor-image cut, strict abelian-dimension descent, dN isogeny lift and Jacobian rank maximum. No correction needed.'),
('B.2u','/root, actual-file reading','targeted proof check','Root read the complete theorem plus full Pic-finite-constants lemma and checked every comparison and field-base change, including source-versus-image abelian groups, finite kernel, valuation persistence, coefficient subgroup and final arbitrary constants reduction. Primary de Jong/Tanaka/Kelly inputs reopened. No gap found.'),
('B.2u','/root/part_d, actual-file reading','targeted proof check','D read the entire theorem and all three C lemmas. Checked finite valuation-residue extension and divisor persistence, full ambient restriction on all parameters, positive-dimensional torsor detection, strict cuts, A_* versus A0 and dN bound, Jacobian maximum, semilinear torsor descent and full Picard rigidification. No gap found. This event does not claim D reopened de Jong or ACMV in this pass.'),
('B.2-U','/root/part_b','proved','Former weak upper-cone gate closed by B.2u. The cofinal-diagram counterexample remains valid and separate. The historical gate is not deleted from the audit chronology.')]
with (base/'CHECK_EVENTS_B.tsv').open('a') as stream:
    for statement,who,kind,detail in events:
        stream.write(statement+'\t2026-11-20\tGPT-6 Astra (OpenAI), '+who+'\t'+kind+'\t'+detail+'\n')

(base/'unresolved_B.tex').write_text('% The former Part B weak-upper-cone gate is proved in Statement B.2u.\n% No unresolved Part B assertion remains in this fragment.\n% Constant domination-cofinality is separately refuted in B.2q.\n')
path=base/'corrections_B.tsv'
lines=path.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('B-C06\t'):
        f=line.split('\t')
        f[-2]='Uniform h1 boundedness is proved. The category need not be filtered, and a constant domination-cofinal Picard diagram is refuted by a geometrically normal threefold over an imperfect field. The weaker assertion of a stable upper cone above each initial model is nevertheless proved over every field by B.2u. Thus the meaning of essential constancy must be specified; cofinal constancy and upper-cone constancy are different assertions.'
        f[-1]='B.2; B.2i; B.2q; B.2u'
        lines[i]='\t'.join(f)
path.write_text('\n'.join(lines)+'\n')

path=base/'notes.md'
notes=path.read_text()
notes=notes.replace('## Current state at 2026-11-20 00:48 UTC','## Historical checkpoint at 2026-11-20 00:48 UTC',1)
current='''## Current checked state after closure of the weak gate

All requested Part B assertions and the separately tracked weak replacement are decided. B.1 and all margin variants are proved, including the infinitesimal part. B.2 uniform h1 boundedness holds over every field. The stronger claim of one constant domination-cofinal Picard diagram is false over imperfect fields by the explicit threefold B.2q. The distinct weak assertion, a stable upper cone above every initial permitted model, is proved over every field in B.2u. B.3 has the requested proof without fundamental-group theory and the corrected ell-not-equal-p rank formula. L6c proves R1 normal-to-regular birational vanishing in every dimension. Complete proofs, exact primary locators, finite example certificates and independently scoped audit events are saved. No priority or original-discovery claim is made.

The chronological working entries below preserve earlier failures and gates; they are historical and are superseded by this current state.

'''
notes=notes.replace('## Historical checkpoint at 2026-11-20 00:48 UTC',current+'## Historical checkpoint at 2026-11-20 00:48 UTC',1)
notes+='''
## Final weak-gate closure: all-dimensional semilinear alteration proof

The fixed comparison group is R=Res_l/k Picτ(Y/l), with Γ acting semilinearly on the finite alteration constants. Every invariant abelian subgroup is realized up to [n]V^e by a rational abelian-torsor map over K: the construction keeps separable constants, kills translations for Γ0, descends through the finite Galois constant extension, and uses the q-power field homomorphism for the remaining purely inseparable extension. Its normal graph is either allowed and realizes the subgroup, or has a bad divisorial K-valuation. Maximizing that valuation's allowed centre and restricting on a fixed divisor above it in L imposes a closed subgroup condition that strictly cuts the excessive abelian part. The finite induction ends with ambient quotient of bounded exponent N. The comparison kernel is killed by d=[L:K], so the source Picard quotient by its maximal abelian variety is killed by dN; a fixed Jacobian bounds its order. A maximal-order model is stable under every later permitted domination. No filteredness or geometrically normal common refinement is used. The previously tracked gate B.2-U is closed; strong cofinality remains refuted, not silently weakened.
'''
path.write_text(notes)
with (base/'sources'/'search_log.md').open('a') as stream:
    stream.write('\n## Closure of arbitrary-field weak stabilization\n\nThe exact de Jong1997 Galois-alteration inputs were reread, including Situation5.3 and condition5.12.1, Theorem5.13 and Corollary5.15. The construction is first used overkperf, and all finite separable constants and semilinear actions are retained during descent. The all-parameter Picard finite-constants identification is proved directly using a smooth affine open and a generator-open trivialization; it is not quoted as an equality of tau-components. Stacks0200 (Chow lemma30.18.1) was opened directly and used only to make the fixed normal divisor model projective; it is not used to assert geometric normality of an arbitrary refinement. Root, C and D independently audited the complete written chain within their recorded scopes.\n')
record=dict(operation='integrate_arbitrary_stabilization_B',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),statements=['B.2t','B.2u'],former_gate='B.2-U closed',elapsed_seconds=time.perf_counter()-started)
(base/'code'/'output'/'integrate_arbitrary_stabilization_B.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
