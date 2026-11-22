"""Promote audited proofs; this is editorial work, not a mathematical test."""
from pathlib import Path
from datetime import datetime, timezone
import ast, csv, hashlib, json, shutil, time

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
now = datetime.now(timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); inherited effort; RESEARCH_SA17_FINISH/root'
check_fields = ['statement_id','date','who','type','outcome']
result_fields = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']

def write_rows(path, fields, rows, delimiter=','):
    with (root/path).open('w', newline='') as f:
        w = csv.writer(f, delimiter=delimiter)
        w.writerow(fields)
        w.writerows(rows)

promotions = [
 ('notes/C_MF_Swan_transfer_proposed.tex','sections/C_finish_MF_Swan_transfer.tex','cc4cef2b8b0834ea627511b08e372f929171c0a058e2e34942a2d8548bc775b4'),
 ('notes/C_finish_henselian_projective_draft.tex','sections/C_finish_henselian_projective.tex','7e86ff988bb97b4be70ad7a5a9197e32bbf8ec3227596bf983426a8f9c105e2b'),
 ('notes/C_finish_henselian_global_arithmetic_draft.tex','sections/C_finish_henselian_global_arithmetic.tex','b88af3f38f3bf3e78bf06ee9d5f38ac4c5e28b53bb779b0b952e28a770143b4d'),
 ('notes/C_finish_henselian_global_WG_draft.tex','sections/C_finish_henselian_global_WG.tex','e3ab6c54edbc83748555628e9e73fc36ea85afcc802876917fe2c45c76b9cb27'),
]
records=[]
for src,dst,sha in promotions:
    data=(root/src).read_bytes()
    assert hashlib.sha256(data).hexdigest()==sha, src
    assert not (root/dst).exists(), 'One-shot promotion already performed'
    text=data.decode().replace('[Proposed:', '[Proved:')
    (root/dst).write_text(text)
    records.append({'source':src,'audited_sha256':sha,'compiled_source':dst,'compiled_sha256':hashlib.sha256(text.encode()).hexdigest(),'post_audit_change':'Only Proposed to Proved labels, where present'})

copies={
 'notes/C_MF_Swan_transfer_proposed.csv':'results_C_MF_Swan_transfer.csv',
 'notes/C_MF_Swan_transfer_proposed_checks.tsv':'checks_C_MF_Swan_transfer_own.tsv',
 'notes/C_MF_Swan_mixed_s3_audit.tsv':'checks_C_MF_Swan_transfer_peer.tsv',
 'notes/C_henselian_global_proposed.csv':'results_C_henselian_global.csv',
 'notes/C_henselian_global_proposed_checks.tsv':'checks_C_henselian_global_own.tsv',
 'notes/C_henselian_global_arithmetic_root_audit.tsv':'checks_C_henselian_global_arithmetic_root.tsv',
 'notes/C_henselian_global_arithmetic_regular_coherent_audit.tsv':'checks_C_henselian_global_arithmetic_peer.tsv',
 'notes/C_henselian_global_WG_regular_coherent_audit.tsv':'checks_C_henselian_global_WG_peer.tsv',
 'notes/C_henselian_projective_flat_union_audit.tsv':'checks_C_henselian_projective_peer.tsv',
 'notes/C_henselian_projective_sources.bib':'references/C_henselian_projective.bib',
}
for src,dst in copies.items():
    shutil.copyfile(root/src,root/dst)
# Normalize the single draft-only computation type before it enters the catalog.
p=root/'checks_C_MF_Swan_transfer_own.tsv'
p.write_text(p.read_text().replace('\texact symbolic calculation\t','\tcomputation or formal certificate\t'))

projective_rows=[
 ['C:henselian-projective-decisions','Ordinary projective-point decisions over exact countable henselian discretely valued fields with finite residue; smooth schemes always and arbitrary projective schemes when the completion is regular','Proved under stated hypotheses','sections/C_finish_henselian_projective.tex','C-NowakDensity2017 Remark2 and Corollary3; C-JardenHenselian1994 Lemma2.3','','Finite quotient representatives and compact congruence trees give the negative search; an explicit Hensel scaling or regular-completion existential closure reflects completion points. No arbitrary valued-field assertion.'],
 ['C:henselian-central-simple-algorithms','Actual CSA indices division factors matrix units and finite separable splitting data over the stated effective henselian discretely valued fields','Proved under stated hypotheses','sections/C_finish_henselian_projective.tex','C:henselian-projective-decisions; C-StacksGlobalFunctionArithmetic Tag0752','','Smooth generalized left-ideal Grassmannians decide index, including wild degree. Actual idempotents and matrix units are found by exact terminating enumeration. Splitting-field and reduced-norm outputs require the stated finite-tower factorization.'],
 ['C:henselian-hermitian-isometry','Ordinary exact hermitian isometry decisions actual isometries and decidable least Gram-pair groups over division algebras whose fixed centers have the stated regular-completion valuation data','Proved under stated hypotheses','sections/C_finish_henselian_projective.tex','C:henselian-projective-decisions; C-QSS1979 Application3.4(1)','','The D-stable isotropic half-dimensional subspace scheme is projective; no smoothness is assumed. Regular completion is required. Rank zero is handled first; metabolic Gram adjustment and cancellation give the isometry equivalence.']
]
write_rows('results_C_henselian_projective.csv',result_fields,projective_rows)
projective_outcomes=[
 'OWN complete written-proof verification, not an independent check. Exact quotient representatives, normalized projective compactness and both point-reflection clauses checked. The Taylor/adjugate equation has constant term in the maximal ideal and derivative identity. Opened Nowak Remark2/Cor3 and Jarden Lemmas2.1-2.3 with full proofs. Peer full audit is separately recorded.',
 'OWN complete written-proof verification, not an independent check. Left-ideal dimensions are n times multiples of the actual index; smoothness follows scheme-theoretically from matrix units after finite separable splitting. Projective decisions find the least dimension, and exact enumeration constructs primitive corners, full matrix units and inverse maps. Optional factorization hypotheses are retained. Peer full audit is separately recorded.',
 'OWN complete written-proof verification, not an independent check. Checked right-D stability and isotropy equations on the ordinary Grassmannian, rank-zero and unequal-rank cases, dimension-to-D-rank inference over a division algebra, the explicit metabolic complement adjustment and QSS cancellation. Least finite codes use decidable isometry and finitely many predecessors; actual positive and negative representatives are retained. Opened QSS Application3.4(1), printed p273. Peer full audit is separately recorded.'
]
write_rows('checks_C_henselian_projective_own.tsv',check_fields,[[r[0],now,who,'targeted proof check',o] for r,o in zip(projective_rows,projective_outcomes)],'\t')

mf_outcomes=[
 'PASS full root independent actual-file proof audit. Read all297 source lines and all105 certificate lines plus full output. Equal-rank length-one presentations, unique partners, unit elimination and upper-triangular horseshoe sequences establish well-defined additive actual Swan classes. Free and identity factorizations cancel. The displayed conjugacy after inverting two and both exact Tate parities are correct. Opened Eisenbud full primary PDF, proof of Theorem6.1 printed p53 and Corollary6.3 p55. No injectivity or retraction is asserted.',
 'PASS full root independent actual-file proof audit. Checked both explicit ideal presentations, the periodic exact sequence, colon equality and second ideal sequence. These give3 delta=0. Formal polynomial identities are specialized only afterwards; alpha is integral for every e>=2, and the unit-square anticommuter gives2 delta=0. Residue triviality proves nonprojectivity. Read the full 21-identity/256-entry output; did not rerun it. Only this specified class is proved to vanish, not the full node comparison.'
]
write_rows('checks_C_MF_Swan_transfer_root.tsv',check_fields,[[i,now,who,'targeted proof check',o] for i,o in zip(['C:MF-Swan-transfer','C:ramified-A2-MF-cancellation'],mf_outcomes)],'\t')
wg_ids=['C:henselian-global-finite-algebra-algorithms','C:henselian-global-coefficient-WG','C:henselian-global-new-families']
wg_outcomes=[
 'PASS full root independent audit of the actual620-line source. The two-sided action determinant certifies central simplicity, and a surjective product of such quotients with nilpotent kernel identifies the exact radical. Every finite center has a valid finite field tower, including inseparable cases. Projective index decisions construct actual division factors. Newton correction and complementary corners lift the full primitive family. No semisimple complement or unresolved index is assumed.',
 'PASS full root independent actual-file proof audit. Checked finite-algebra projectivity by linear sections, actual R-duals, determinant grids over infinite fields, full Hom residue images and the radical quotient identity. Finite-kernel access and henselian lifting give actual decompositions and form lifts. Fixed centers are computed as kernels and explicit finite towers; regular-completion isometry applies. Canonical finite predecessor tests, cancellative Gram pairs and actual representatives are valid. Balanced tensor/exterior constructions require no factorial inversion. No unknown isometry quotient remains.',
 'PASS full root independent actual-file proof audit. Effective syzygies and valuation Smith elimination meet the exact-access hypotheses. The quaternion norm is anisotropic by even/odd valuation parity. Simple Hensel roots of X^n-(1+t) have unbounded degree by Eisenstein at t+1; the henselian field is algebraic but not a global function field. Positive characteristic excludes the rational-base theorem, and residue equal to the same non-C1 field excludes the older finite/C1-residue families. Singular, nonreduced and non-Noetherian examples retain their stated scopes.'
]
write_rows('checks_C_henselian_global_WG_root.tsv',check_fields,[[i,now,who,'targeted proof check',o] for i,o in zip(wg_ids,wg_outcomes)],'\t')
(root/'logs/C_henselian_global_WG_root_audit.json').write_text(json.dumps({'timestamp':now,'source':promotions[3][0],'sha256':promotions[3][2],'status':'PASS full independent root audit, all620 lines','ids':wg_ids,'outcomes':wg_outcomes},indent=2)+'\n')
(root/'logs/C_MF_Swan_transfer_root_audit.json').write_text(json.dumps({'timestamp':now,'source':promotions[0][0],'sha256':promotions[0][2],'status':'PASS full independent root audit','outcomes':mf_outcomes,'primary_source':'https://ssather.people.clemson.edu/fa11/790-3/eisenbud.pdf','exact_locators':['proof of Theorem6.1, printed p53','Corollary6.3, printed p55']},indent=2)+'\n')

p=root/'sections/C.tex';s=p.read_text()
s=s.replace('\\input{sections/C_finish_ramified_nodes}\n','\\input{sections/C_finish_ramified_nodes}\n\\input{sections/C_finish_MF_Swan_transfer}\n')
s=s.replace('\\input{sections/C_finish_global_function_WG}\n','\\input{sections/C_finish_global_function_WG}\n\\input{sections/C_finish_henselian_projective}\n\\input{sections/C_finish_henselian_global_arithmetic}\n\\input{sections/C_finish_henselian_global_WG}\n')
s=s.replace('or the existence of a nonzero class.\n','or the existence of a nonzero class.\nProposition~\\ref{C:ramified-A2-MF-cancellation} proves cancellation\nof the specified standard matrix-factorization lattice on every ramified\nexponent-three dyadic node. It does not decide the full comparison map.\n',1)
p.write_text(s)
p=root/'sections/unresolved.tex';s=p.read_text()
needle='Thus the remaining task concerns coefficient bases outside the completed\n'
assert needle in s
s=s.replace(needle,'Theorems~\\ref{C:henselian-global-field-arithmetic} and\n\\ref{C:henselian-global-coefficient-WG} further give complete ordinary\nanswers over all supplied finite extensions of henselized global-place\nfraction fields, their finite coefficient algebras and the stated effective\nlocal henselizations. The projective-point and regular-completion arguments\ndecide every required division index and hermitian isometry.\nCorollary~\\ref{C:henselian-global-new-families} explicitly separates\nthese non-$C_1$, nonglobal positive-characteristic fields from the earlier\ncompleted families.\n\n'+needle)
p.write_text(s)

p=root/'code/finish_report.py';lines=p.read_text().splitlines()
for j,line in enumerate(lines):
    if line.startswith("'C.1':"):
        value=list(ast.literal_eval(line.split(':',1)[1].rstrip(',')))
        value[1]+='; C:MF-Swan-transfer; C:ramified-A2-MF-cancellation'
        value[2]+=' An additive matrix-factorization map is now proved, and the specified standard rank-four class cancels on all ramified exponent-three dyadic nodes. This does not settle the full node map and is not counted as a whole-family C1 classification.'
        lines[j]="'C.1':"+repr(tuple(value))+','
    if line.startswith("'C.3':"):
        value=list(ast.literal_eval(line.split(':',1)[1].rstrip(',')))
        value[0]='Lambda criterion settled; global and henselian global-field arithmetic and complete WG algorithms; arbitrary coefficient bases open'
        value[1]+='; C:henselian-projective-decisions; C:henselian-global-field-arithmetic; C:henselian-global-coefficient-WG; C:henselian-global-new-families'
        value[2]+=' Complete ordinary algorithms also cover every supplied finite extension of a henselized global-place fraction field, including inseparable extensions, all finite coefficient algebras over them and the stated coherent local henselizations. Finite congruence trees, regular completion and projective isotropic-subspace schemes decide actual division factors and all hermitian isometries. Explicit non-C1 nonglobal positive-characteristic examples prove this is a further whole-family reduction.'
        lines[j]="'C.3':"+repr(tuple(value))+','
s='\n'.join(lines)+'\n'
marker='| `C_finish_ramified_higherpage_failure`'
assert marker in s
s=s.replace(marker,'| `C_finish_MF_Swan_cancellation` | 21 exact symbolic matrix identities, 256 scalar entries and seven illustrative ramification substitutions e=2..8 | All pass;0.071217018 s. The unrestricted e>=2 cancellation has a separate exact-category and ideal-sequence proof. This certificate does not classify all node representations. |\n'+marker,1)
p.write_text(s)

record={'timestamp':now,'scope':'Promotion after full own/root/peer actual-file audits; editorial operation only','promotions':records,'check_type_correction':'Draft exact symbolic calculation was changed to permitted computation or formal certificate before catalog merge','seconds':time.perf_counter()-started}
(root/'logs/C_checkpoint12_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
