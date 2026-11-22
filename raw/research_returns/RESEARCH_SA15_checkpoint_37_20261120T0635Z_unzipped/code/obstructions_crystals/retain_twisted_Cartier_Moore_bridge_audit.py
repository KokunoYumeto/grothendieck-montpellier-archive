"""Retain the complete independent geometric Cartier/Moore bridge audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root/'agents/obstructions_crystals'
source = root/'agents/monodromy/ppav_twisted_Cartier_Moore_candidate.tex'
expected = '80db90e54c403914d3aa26626a829ec31c1f85eecb078833e675af5441ada65b'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source) == expected
labels = re.findall(r'\\label\{((?:lem|prop|thm|cor|rem):[^}]+)\}', source.read_text())
assert len(labels) == 7
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL PROOF AND SOURCE PASS',
    'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected,
    'labels': labels,
    'proof_read_scope': 'Entire stable seven-label candidate read; all geometric identifications independently rederived. The entire principal theta bridge was independently audited immediately beforehand. The complete canonical level-three symmetrizer proof and the full degree-one alternating Pfaffian/rank proposition and its algebraic lemma were freshly reread. The universal Moore classification is the separately retained exact proof/certificate, not a new finite-to-geometric inference here.',
    'checks': [
        'For arbitrary two-rank, the dual algebra of ker(F) is commutative Artinian, so all simple representations over the algebraically closed field are characters. The trace-kernel filtration descends to line bundles killed by Frobenius pullback. These have order dividing two and are numerically trivial. After principal ample twisting, the entire filtration has vanishing higher cohomology, proving nonzero global trace without a two-rank-zero assumption.',
        'The diagonal linearization discrepancy is an actual character, and the nonzero Cartier contraction belongs to its descended principal eigenspace. The principal polarization identifies the character line with translation by a geometric two-torsion point on B^(2). Its unique Frobenius lift is two-torsion because ker(F) is connected. Thus the coefficient is a common nonzero translated theta square; this shift vanishes in two-rank zero.',
        'Theta splittings on each order-three Lagrangian can be made compatible with normalized symmetry by the unique square root in its odd-order character group. The K splitting descends symmetric principal M, and its theta section has symmetry scalar one in characteristic two. The nine K characters of the translated section are distinct, giving the stated theta basis.',
        'The two actual lifts of K-prime times K-prime translation on the square line differ by a scalar character. The rigidified square isomorphism is compatible separately with sign change in z and sign change in a: on its target these are swap plus both normalized symmetries, and swap, respectively. Agreement at the origin makes each compatibility exact. Therefore the discrepancy character is unchanged under inversion in each factor, has order dividing both two and three, and is trivial. This proves the exact lift identity, including its common scalar gauge.',
        'Etale pullback of the principal formula produces the e0 identity. The odd isogeny identifies full two-torsion group schemes, so its shift lifts to an actual a0. Tensor-square theta lifts descend under relative Frobenius to the coefficient-squared target lifts. The h lift commutes with translation by a0 because their theta commutator is killed by both three and two. Consequently the complete global identity has indices (i+j)/2 and (i-j)/2 and a single common parameter-fibre isomorphism. Reindexing i=2u,j=2v gives exactly c_(u-v)x_(u+v), with c the coordinatewise Frobenius theta evaluation vector.',
        'The 81 Moore planes are permuted by coordinatewise Frobenius. The base plane is contained in the projective fixed space of the index involution, and all others are its finite Heisenberg translates; multiplication by two on the character group produces every phase. In the symmetric theta representation these are fixed spaces of x->2t-x, t in A[3]. Since 3Theta is a closed immersion, a theta evaluation in such a plane forces 2(a+a0)=2t. Applying phi_(3Theta) gives 2P=0. Thus every non-two-torsion cross block has a genuinely nonzero determinant polynomial.',
        'For an odd etale cover, target functionals supported on the trivial character produce the trivial nine-dimensional block and inverse-character cross blocks. All cross determinants are nonzero polynomials on the same nine-dimensional functional space. The canonical symmetric theta tensor identifies the trivial dual contraction with the established rank-eight contraction. Finitely many nonempty opens intersect, yielding rank9n-1. Nonordinarity makes every form alternating and gives the matching odd-dimensional upper bound.',
        'For each fixed principally polarized source and odd d, a maximal isotropic subgroup of A[d] gives an outgoing etale quotient with dTheta as pullback of a principal line. Its symmetry discrepancy is corrected by the unique half in the odd character kernel without changing pullback. Cubing gives the actual system3dTheta, and the target remains nonordinary. This resolves the direction issue for this dual-rank statement. No new curve p-rank, Lang group or global monodromy statement is inferred.'
    ],
    'primary_sources': [
        {
            'title': 'Edixhoven, van der Geer and Moonen, Abelian varieties',
            'url': 'https://van-der-geer.nl/~gerard/AV.pdf',
            'web_ref': 'turn632268386view0',
            'retained_original_text': 'agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt',
            'retained_text_sha256': sha(own/'sources/edixhoven_geer_moonen_AV.txt'),
            'actual_read_scope': 'Fresh complete original proofs of Theorem2.7/Corollary2.8 pp19-20, Corollary8.20 p119, Lemma8.24 p121, Theorem8.28 pp122-123; full Definition11.44 and its normalized-symmetry discussion p178. The symmetry involution identity is derived by normalization, with no use of an unwritten proof in11.45. The full descent and representation passages8.10/8.14/8.30-8.32/9.14/9.17 were freshly read in the immediately preceding principal-bridge audit.'
        },
        {
            'title': 'Brion and Kumar, Frobenius splitting methods in geometry and representation theory',
            'url': 'https://www-fourier.univ-grenoble-alpes.fr/~mbrion/fbook.pdf',
            'web_refs': ['turn795799386view0', 'turn488996688view0', 'turn286513794view0'],
            'actual_read_scope': 'Complete Definition1.3.5, Lemma1.3.6/proof, Proposition1.3.7/full proof and Theorem1.3.8 pp26-28 read immediately before this audit. No new image-view claim.'
        }
    ],
    'dependencies_freshly_read': [
        'agents/monodromy/principal_theta_Cartier_bridge_candidate.tex',
        'agents/monodromy/ppav_theta_cartier_symmetrizer.tex',
        'agents/obstructions_crystals/A3_ppav_surface_ranks.tex: complete four-parameter lemma and degree-one proposition'
    ],
    'Moore_certificate': 'agents/obstructions_crystals/code/verify_Moore_singular_parameter_classification.output.json',
    'numerical_scope': 'No new numerical rerun is needed or claimed for these geometric identities. The complete Moore polynomial certificate remains separately retained and independently audited by root.',
    'scope': 'Every non-two-torsion cubic cross block is generically invertible; every fixed nonordinary ppav odd principal-cube system has maximal generic dual alternating rank. No new global Lang/full monodromy or curve p-rank consequence is claimed.'
}
audit = own/'twisted_Cartier_Moore_bridge_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_source_audit',
                           str(source.relative_to(root)),
                           'Complete exact theta lift, relative trace, Moore embedding and fixed-source quotient proof',
                           'PASS', str(audit.relative_to(root))])+'\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'record': str(audit.relative_to(root)), 'labels': labels}))
