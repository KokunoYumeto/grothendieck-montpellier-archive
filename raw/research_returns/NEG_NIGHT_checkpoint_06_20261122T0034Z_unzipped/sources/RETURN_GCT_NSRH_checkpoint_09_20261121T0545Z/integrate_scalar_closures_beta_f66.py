"""Integrate only the frozen, fully read and independently reviewed additions.

This is a one-shot integration script; the input-main hash guards against replay.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

r = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
p = r / 'GCT_NSRH.tex'
assert sha(p) == 'b3cd197c773fa88626bb44b89832d7b2d5eb8383bc244ae4242fd70b28e2663f'
items = [
    ('F59-RANKONE-SCALAR', 'agent_soergel_rankone_scalar_closure.md',
     '3272f93b6fe00db9d2f09c4e9bebc0d2e0dc18c6cc57e021680a24efa5dacb8f',
     'finding_F59_rankone_scalar.tex',
     'a873f1e948475f0cb752c27b29b16a361c2c4f1c187f50c29b54ad530a506f91',
     'REVIEW_SOERGEL_RANKONE_CLOSURE_THETA.md', '/root/rectangular_and_theta'),
    ('F59-ALLRANK-SCALAR', 'agent_soergel_allrank_scalar_closure.md',
     '475bd56d0486831328193453faec89612ea1c97a8bb81786d12970053eb34f27',
     'finding_F59_allrank_scalar.tex',
     '956b51070bd4cfc30b208512912bf0501d2da8d38a43ec94c65bbd56bd763b77',
     'REVIEW_SOERGEL_ALLRANK_SCALAR_GCT.md', '/root/gct_statements'),
    ('F65-ARITHMETIC', 'agent_joint_normalization_arithmetic_parameter.md',
     '5f79181a45048db296669d4f156bc8afaa4eaa53072f8be99c901c04fcf70109',
     'finding_F65_arithmetic_parameter.tex',
     '1a2053313af1db0079a2b68af19c470874ef164f0ecea538a35edbd008404127',
     'agent_F65_arithmetic_parameter_review.md', '/root/rectangular_and_theta'),
    ('F66', 'agent_iterated_positive_tensor_repair.md',
     'caae7ec42e5cd3b57a58d157fe0b3380cfe19d6d7df96e786b669ba5d07f78a1',
     'finding_F66.tex',
     '3af23cee878ba8a3b8cecc24ccda64eb8e20e98bd6eab8be8d1a279d83e96386',
     'REVIEW_ITERATED_POSITIVE_TENSOR_THETA.md', '/root/rectangular_and_theta'),
]
for fid, rep, rh, frag, fh, rev, who in items:
    assert sha(r / rep) == rh, rep
    assert sha(r / frag) == fh, frag
    review = (r / rev).read_text()
    assert fh in review and 'PASS' in review, rev
assert sha(r / 'finding_F59_allrank_bib.tex') == '49f61afe0214ec14d4b7e666f943e04a6c64674373277aa6bf68a254ef416e17'
assert sha(r / 'agent_iterated_positive_tensor_lefschetz.md') == 'f3992043857f2abb7f354b071822e6ba7acf6c66833d90b0a023e615625f90d7'
s = p.read_text()
anchors = {
    'F59': r'\subsection{Bounded kernels, finite-algebra characters, and an actual word relation}',
    'F65': r'\subsection{A normalization that cannot be a finite Frobenius trace}',
    'F66': r'\subsection{\fid{F64}: weight grading does not preserve the actual flag convolution}',
}
da = r'\section{Archival audit and the Fable leads}\label{sec:archive}'
for fid, rep, rh, frag, fh, rev, who in items:
    body, dictionary = (r / frag).read_text().split('% Separate paragraph for Part III.', 1)
    anchor = anchors[fid.split('-')[0]]
    assert s.count(anchor) == 1
    s = s.replace(anchor, body.rstrip() + '\n\n' + anchor)
    assert s.count(da) == 1
    s = s.replace(da, dictionary.strip() + '\n\n' + da)

def replace_exact(old, new):
    global s
    assert s.count(old) == 1, old[:120]
    s = s.replace(old, new)

replace_exact('''The remaining case is an actual bounded coupled lift
with nonflat cohomology and an altered scalar complex,
with actual relation maps. Neither a construction nor
an unconditional exclusion of that case is proved here.
Polynomial-differential coefficient bimodules and
unbounded completions are further changes of premise.''', r'''This amplitude argument alone leaves bounded coupled lifts
with nonflat cohomology and an altered scalar complex.
Finding~\ref{f:allRankScalarClosure} below closes that case
in every ordinary type-A rank, using the module-length
inequality and descending cohomology induction.
Polynomial-differential coefficient bimodules and
unbounded completions remain changes of premise.''')
replace_exact(r'''\paragraph{The remaining nonflat case.}
Neither finding supplies a general exclusion of every
nonfactorable mixed coefficient lift with nonflat
cohomology. Nonflat quasi-idempotents exist in simpler
settings:''', r'''\paragraph{The scope of the nonflat examples.}
These two tests alone do not exclude every nonfactorable
mixed scalar lift with nonflat cohomology. The later
Finding~\ref{f:allRankScalarClosure} gives that exclusion
under the actual ordinary type-A generator and quadratic
premises. Nonflat quasi-idempotents do exist for other
Euler classes:''')
replace_exact('Bounded ordinary type-A Soergel lifts fail the actual quadratic with its degree-zero coefficient,',
              'Bounded ordinary type-A Soergel lifts fail the actual quadratic for every bounded scalar coefficient with the required Euler class,')
replace_exact('F59 excludes every bounded ordinary type-A Soergel lift of the actual generator with its cohomologically degree-zero quadratic coefficient.',
              r'F59 excludes every bounded ordinary type-A Soergel lift of the actual generator with any bounded scalar $k$-complex coefficient of Euler class $\delta^2$. The proof forces all cohomology to be free and globally splits its two graph supports; the odd outer Euler coefficients then give a contradiction. It covers coupled differentials and initially nonflat cohomology.')
old = next(x for x in s.splitlines() if x.startswith('With an altered bounded scalar coefficient, F59 now forces'))
new = r'''The changed-scalar ordinary-Hecke route is now closed by F59, rather than left at a nonflat-cohomology gate. Polynomial-differential coefficient bimodules, unbounded objects and different convolution categories remain different premises and are not covered by the scalar theorem.

F62 constructs actual standard nonproper flag convolution and the exact torus factors in two printed source constants. Its nonzero Chern-class boundary obstructs replacing the relative coefficient by a constant fiber complex; equality of all fiber traces and formal division do not supply that operation. F64 proves that canonical weight grading and perverse or ordinary cohomology splitting fail to preserve this convolution. An exact unit-and-Tate-preserving monoidal extraction cannot send its open generator to the closed IC generator while retaining the relation.

F63 excludes strict effective simple-by-simple compatibility with the actual tensor-factor iteration at fixed strand rank three beginning at the fourth factor, including a specified regular effective projector. F66 constructs a simultaneous positive basis and actual graded quadratic kernel maps for the containing four-dimensional tensor itself, transports its actual bar and gives a pure derived arithmetic realization. Its word category has generic rank six; its ambient Karoubi completion has rank sixteen and does not preserve the selected simple-projector or adjoint constraints. The positive unmarked two-word trace nevertheless has a missing Lefschetz degree, excluding the stated projective pure-perverse or $SL_2$ comparison. These are distinct, explicitly delimited conclusions.'''
replace_exact(old, new)
old = next(x for x in s.splitlines() if x.startswith('F65 tests the raw canonical multiplicities themselves.'))
new = r'''F65 tests the raw canonical multiplicities themselves. Proper-pure isotypic multiplicities are pure point complexes, with their weights proved from the actual geometric Hom spaces. The isolated negative VIII coefficient has a normalization-dependent pure escape, but its missing middle degree excludes the specified hard-Lefschetz realization. The two actual multiplication constants $d(t)=t+2+t^{-1}$ and $c(t)=-t^2+t+t^{-1}-t^{-2}$ can both be pure point Euler traces under one fixed nonzero algebraic parameter $t=\beta^n$ exactly when $\beta^3=1$. In those exceptional cases $c$ vanishes identically and its pure coefficient object must be zero. Thus no nondegenerate fixed arithmetic parameter gives the proposed joint pure comparison. The source relation is explicitly $q_{\rm VIII}=u_{\rm IV}^2$; it supplies no Frobenius comparison. These statements concern raw coefficients and leave normalized signed/factored positivity separate.'''
replace_exact(old, new)
s = s.replace('findings A01 and F01--F65,', 'findings A01 and F01--F66,')
s = s.replace(r'\end{thebibliography}', (r / 'finding_F59_allrank_bib.tex').read_text().rstrip() + '\n' + r'\end{thebibliography}')
p.write_text(s)

q = r / 'QUESTIONS.tsv'
with q.open(newline='') as f:
    rd = csv.DictReader(f, delimiter='\t'); fields = rd.fieldnames; rows = list(rd)
byid = {x['id']: x for x in rows}
closure = ('No bounded ordinary type-A Soergel complex X of actual Euler class '
           'b⊗b+(b−δ)⊗(b−δ) satisfies X⊗^L_A X≃C⊗_k X for any bounded finite graded '
           'scalar k-complex C with Euler class δ². Generic positivity fixes the two graph supports '
           'and degreewise ranks; the finite-origin module-length inequality, Lichtenbaum Tor rigidity '
           'and descending cohomology induction force every H^j(X) free. Global graph splitting '
           'then forces d(v,u)=2a(v,u), contradicting the odd outer Euler coefficients. '
           'Coupled differentials and initially nonflat cohomology are included. '
           'Polynomial-differential diagonal coefficient bimodules and unbounded or other categories are outside this theorem.')
for qid in ['Q3-BOUNDED-ORDINARY-HECKE', 'Q3-ALTERED-SCALAR-HECKE']:
    x = byid[qid]
    x['state'] = 'REFUTED_FOR_ALL_BOUNDED_SCALAR_COEFFICIENTS_IN_STANDARD_TYPE_A'
    x['current_gate'] = closure
    x['approaches_tried'] += '; finite-origin length rigidity; two-variable elementary proof; all-variable Lichtenbaum partial Euler characteristic; top cohomology and descending canonical cross-product induction'
    x['next_step'] = 'This bounded scalar route is closed. Investigate genuinely central polynomial-differential coefficients or other mixed/nonproper categories with actual source comparison.'
    x['source_and_locator'] += '; Lichtenbaum1966 Theorem2(1),(2),(4) pp222–223; Stacks00MB/00MC'
x = byid['Q3-GCT']
x['finding_ids'] += ',F66'
x['current_gate'] = ('Actual fixed-parameter pure perverse End/Hom, coherent all-degree tensor maps, opposite-sign paths, '
    'rank-three graded relation kernels and transported bar exist. Independent local/dual bounds and designated '
    'simple/global bases remain. F59 closes all bounded ordinary type-A scalar-coefficient quadratic lifts, including '
    'nonflat cohomology. F57/F58 and F63 exclude the specified strict effective simple/cell comparisons; VIII itself '
    'allows signed vanishing factors. F60 excludes full-cohomology finite-algebra retention with degree-zero scalar '
    'objects. F62 supplies actual nonproper torus operations with nonzero relative extension maps, while F64 excludes '
    'the proposed weight/cohomology splitting or exact H-to-IC extraction. F65 classifies all fixed nonzero algebraic '
    'parameters for joint pure raw coefficients: only β³=1, where c vanishes, so no nondegenerate comparison remains. '
    'F66 supplies actual positive whole k2+k2 tensor kernels and pure derived arithmetic, but no effective selected '
    'projector, stable adjoint category or single-center Lefschetz comparison. A coupled mixed/nonproper or filtered '
    'operation retaining extension data, normalized factors, designated labels and independent spectral bounds is still needed.')
x['approaches_tried'] += '; full bounded-scalar closure; arbitrary fixed arithmetic parameter; whole-tensor positive basis and Lefschetz test'
x['next_step'] = 'Test genuinely central polynomial-differential coefficients and actual higher tensor iteration; construct mixed/nonproper or filtered normalized-factor operations with designated labels and independent local/dual bounds.'
x = byid['Q2']
x['finding_ids'] += ',F59,F66'
x['current_gate'] = ('The classical KL dictionary and exact missing nonstandard counterparts are recorded. Actual '
    'coherent/pure Weil objects, perverse End/Hom, graded relation maps, bar and opposite-sign paths exist in the '
    'specified rank-three constructions, without selecting the designated global basis. Full bounded-scalar ordinary '
    'Hecke lifts are excluded by F59. Actual nonproper torus geometry retains a nonzero Chern extension, and F64 '
    'shows its weight/cohomology splitting is not monoidal. F65 excludes a nondegenerate pure raw multiplicity '
    'comparison for every fixed algebraic arithmetic parameter. F66 gives positive whole iterated tensor kernels '
    'with pure derived entries but a missing hard-Lefschetz degree. Independent weights, exact normalized-factor '
    'operations and canonical/geometric labels remain.')
x = byid['Q3-RAW-CANONICAL-PURITY']
x['state'] = 'PROPER_MULTIPLICITY_CRITERION_AND_EXACT_FIXED_PARAMETER_CLASSIFICATION_PROVED; NONDEGENERATE_JOINT_PURE_COMPARISON_REFUTED'
x['current_gate'] = ('Geometric isotypic multiplicities of a proper pure product are pure point complexes with '
    'known relative weight. For every fixed nonzero algebraic β, both printed constants d(β^n),c(β^n) have pure '
    'point Euler realizations, even with different integral weights, iff β³=1. Then c is zero and a pure coefficient '
    'object realizing it is zero. All collisions among β^±1,β^±2 are checked. The isolated c has a half-step pure '
    'escape but no specified single-center hard-Lefschetz realization. The source convention q_VIII=u_IV² is formal; '
    'mixed coefficients, inserted traces and normalized factors are separate premises.')
x['approaches_tried'] += '; arbitrary algebraic fixed parameter; root collision orders1,2,3,4; finite-etale exceptional witnesses'
x = byid['Q3-ITERATED-EFFECTIVE-SUMMANDS']
x['finding_ids'] = 'F63,F66'
x['current_gate'] += (' F66 constructs an actual simultaneous nonnegative Laurent basis and quadratic graded '
    'kernel maps for that whole k2+k2 tensor, regular at v1, with transported bar and pure derived arithmetic. '
    'Its unmarked positive two-word trace has no degree±6 between degree±8 and±4, excluding a single-center '
    'Lefschetz or SL2-character comparison. Effective selected projectors remain excluded.')
x['approaches_tried'] += '; explicit whole-tensor conjugation; path-labeled quadratic coherence; split K0 and Karoubi calculation; missing-degree Lefschetz test'
x = byid['Q3-GRADED-COEFFICIENT-KERNELS']
x['finding_ids'] += ',F66'
x['current_gate'] += (' F66 now constructs positive kernels for the actual whole k2+k2 tensor at r3, with actual '
    'quadratic maps and transported bar. This closes that whole-tensor construction, but not all iteration factors: '
    'its generic word category has rank6, ambient Karoubi completion rank16, selected projectors and transpose '
    'adjoints are outside, and the specified projective pure-perverse realization fails hard Lefschetz.')
for key in ['finding_ids', 'current_gate']:
    byid['Q6'][key] = byid['Q6'][key].replace('F01–F65', 'F01–F66')
row = ['Q3-WHOLE-ITERATED-POSITIVE-TENSOR',
       'F66; Blasiak1010.0421v2 Def2.5/Eq11/13; BBD5.1.13–14/5.4.10',
       'Does the containing actual k2+k2 tensor have positive kernels, and can its whole trace satisfy Lefschetz?',
       'POSITIVE_KERNEL_AND_PURE_DERIVED_MODEL_PROVED; SPECIFIED_LEFSCHETZ_COMPARISON_REFUTED',
       'F63,F66',
       'An explicit regular simultaneous basis makes both named generators nonnegative Laurent matrices. Actual graded quadratic maps are coherent after canonical symmetric permutations restoring labeled factor order. The split word K0 algebra has generic rank6; full ambient Karoubi completion has rank16. Whole two-word trace 2v8+40v4+64v2+108+64v^-2+40v^-4+2v^-8 is positive but has missing degree±6, so no degree2 single-center Lefschetz, SL2-character or stated projective pure-perverse realization exists. Arbitrary pure complexes and multiple centers remain possible.',
       'Exact conjugation and bar; positive matrix kernels; ordered path bijections; word algebra and matrix-unit completion; exact Laurent computation; pure-point spectral uniqueness and missing-degree argument',
       'Test actual iteration on further positive source objects and retain precise mixed, projector, adjoint and normalized-factor comparisons.']
rows.append(dict(zip(fields, row)))
assert len({x['id'] for x in rows}) == len(rows)
with q.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields, delimiter='\t'); w.writeheader(); w.writerows(rows)

now = datetime.now(timezone.utc).isoformat()
with (r / 'CHECK_EVENTS.tsv').open('a', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    for fid, rep, rh, frag, fh, rev, who in items:
        w.writerow([fid+'-ROOT-FINAL-MATCH', now, '/root', 'GPT-6 Astra Pro', 'not exposed',
                    'GCT_NSRH_20261121', 'targeted proof check',
                    'Entire report and complete final fragment read/reconstructed before integration; exact final hashes matched. Full proofs and separate dictionaries retained; PASS.',
                    rep+' SHA256 '+rh+'; '+frag+' SHA256 '+fh])
        w.writerow([fid+'-PEER-FINAL-MATCH', now, who, 'GPT-6 Astra Pro', 'not exposed',
                    'GCT_NSRH_20261121', 'independent re-proof',
                    'Fresh whole-proof review and final-fragment match recorded in the named review; PASS.',
                    rev+' SHA256 '+sha(r/rev)])
    w.writerow(['F66-COHERENCE-CORRECTION-INTEGRATED', now, '/root; /root/rectangular_and_theta; /root/gct_statements',
                'GPT-6 Astra Pro', 'not exposed', 'GCT_NSRH_20261121', 'targeted proof check',
                'Final fragment uses canonical symmetric permutations to restore labeled factor order. Raw left/right reductions are not asserted equal; the earlier overstatement and correction remain in ROOT_REVIEW_NEXT_CYCLE_CLOSURES.md.',
                'finding_F66.tex SHA256 '+items[-1][4]])
with (r / 'ROOT_REVIEW_NEXT_CYCLE_CLOSURES.md').open('a') as f:
    f.write('\n## '+now+' — final complete-proof and fragment matches\n\n'
            'Root read the complete all-rank scalar report, complete final all-rank fragment and bibliography, '
            'and both full independent reviews. The Lichtenbaum application is to the torsion-free quotient after '
            'flat completion; the induction uses one-sided splitting and a canonical bimodule cross-product map, '
            'without asserting bimodule formality. Top degree, socle strictness, graph splitting, zero-rank terms '
            'and the final restored internal grading were reconstructed. PASS.\n\n'
            'Root also completed the entire final F66 fragment and arithmetic-parameter fragment reads and '
            'matched all four final fragment hashes at integration. The F66 coherence correction is preserved '
            'explicitly above; no raw associativity-only identity is claimed. Script computations for F66 were '
            'executed by the author and peer; root checked the displayed identities by hand, without claiming '
            'a root script execution.\n\n'+ '\n'.join(
                '- '+fid+': '+frag+' SHA256 '+fh for fid,rep,rh,frag,fh,rev,who in items)+'\n')
with (r / 'LEDGER.md').open('a') as f:
    f.write('\n## '+now+' — bounded scalar gate closed; fixed parameters classified; whole tensor constructed\n\n'
            'F59 closes the preexisting Q3-ALTERED-SCALAR-HECKE gate for every bounded scalar k-complex and every '
            'ordinary type-A rank, including the previously open nonflat coupled case. This is main-question '
            'movement: a previously admissible class of repairs is now excluded under the exact actual quadratic '
            'and Euler-class premises. Polynomial-differential coefficient bimodules are not silently included.\n\n'
            'F65 extends the joint raw-purity exclusion to every fixed nonzero algebraic arithmetic parameter, '
            'with precisely the degenerate cube-root exceptions. F66 closes the preexisting whole k2+k2 tensor '
            'positive-basis problem and gives actual ordered quadratic maps, bar and pure derived entries, while '
            'its unmarked trace independently excludes the specified Lefschetz comparison. Full proofs, separate '
            'Grothendieck dictionaries and final-fragment reviews are integrated. This entry is not a scheduled '
            'hourly review. Next scheduled review05 remains06:00UTC; next checkpoint09 remains05:45UTC.\n')
im = r / 'IMPLICATIONS.md'
t = im.read_text().replace('integrates findings F01–F65', 'integrates findings F01–F66')
t += '''\n## Complete scalar closure and the next exact geometric boundary\n\nF59 now closes all bounded scalar-complex repairs in the ordinary type-A category, including nonflat coupled lifts. The proof combines a finite-origin length inequality, the precise Lichtenbaum Tor theorem and descending cohomology induction. This changes the main realization gate: any surviving coefficient repair there must alter the scalar premise, the category or boundedness. Polynomial-differential complexes of the unit are a genuinely separate target and require their own centrality maps. The earlier dated partial gates are superseded by this closure.\n\nF65 classifies a common fixed arithmetic parameter for the two raw VIII multiplication constants: only cube roots of unity permit both pure point Euler realizations, and the negative coefficient then vanishes identically. This removes all nondegenerate fixed algebraic parameters from that unmodified proper-pure comparison. It neither supplies nor refutes the published normalized signed-factor operations.\n\nF66 gives a positive simultaneous model for the actual whole k2+k2 tensor, with coherent graded quadratic maps and actual bar. The source simple-projector obstruction persists, and ambient completion changes the algebra from generic rank6 to16. Even the whole unmarked positive trace fails the stated single-center hard-Lefschetz comparison. Positivity of finite matrices, purity of a derived complex, proper pure-perverse convolution and source simple labels therefore impose distinct conditions. PartIII translates each proof using the exact EGA/SGA/BBD and cote anchors already identified; no archive source is claimed to contain these new theorems.\n'''
im.write_text(t)
manifest = r / 'EXTERNAL_INPUT_MANIFEST.json'
data = json.loads(manifest.read_text())
known = {x.get('local_research_input') for x in data}
for name, url in [
    ('primary_sources/Lichtenbaum_1966_primary_web_excerpt.txt', 'https://www.researchgate.net/publication/247050802_On_the_vanishing_of_Tor_in_regular_local_rings'),
    ('primary_sources/Hochster_2012_primary_web_excerpt.txt', 'https://sites.lsa.umich.edu/hochster/wp-content/uploads/sites/1337/2024/10/615W12.pdf')]:
    fp = r / name
    if fp.is_file() and name not in known:
        data.append({'local_research_input': name, 'url': url, 'bytes': fp.stat().st_size,
                     'sha256': sha(fp), 'redistributed': False,
                     'access_status': 'Primary web text excerpts read in full at the stated theorem; not a downloaded original PDF or visual audit.',
                     'locator_reference': 'Lichtenbaum1966 Theorem2 pp222–223; Hochster2012 p169; all-rank F59 report'})
manifest.write_text(json.dumps(data, indent=2)+'\n')
(r / 'STATUS_TIME.txt').write_text(
    'WORK IN PROGRESS\nSnapshot UTC: '+now+'\n'
    'TeX integrates F01–F66 and the complete all-rank scalar and arbitrary-parameter supplements.\n'
    'PDF remains the verified checkpoint08 version throughF65 until the checkpoint09 rebuild.\n'
    'Next checkpoint09:05:45UTC. Next scheduled review05:06:00UTC. Consecutive no-movement count:0.\n'
    'The bounded scalar gate is closed. Active work concerns central polynomial-differential coefficients, actual higher iteration, and tensor inversion.\n')
print(json.dumps({'integrated': ['F59-all-scalar', 'F65-arbitrary-parameter', 'F66'],
                  'questions': len(rows), 'tex_sha256': sha(p), 'utc': now}, indent=2))
