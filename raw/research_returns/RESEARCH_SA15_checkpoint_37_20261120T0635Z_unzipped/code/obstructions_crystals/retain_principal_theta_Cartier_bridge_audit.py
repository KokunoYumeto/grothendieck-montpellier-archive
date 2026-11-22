"""Retain the full independent principal-theta Cartier proof/source audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
source = root / 'agents/monodromy/principal_theta_Cartier_bridge_candidate.tex'
expected = '2f37d09805d4b0fff3d5b95f682b926ccb98dd128e7a6318dce61a5fb1405a7e'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source) == expected
labels = re.findall(r'\\label\{((?:lem|prop|cor|rem):[^}]+)\}', source.read_text())
assert len(labels) == 5
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL PROOF AND SOURCE PASS',
    'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected,
    'labels': labels,
    'proof_read_scope': 'Entire stable five-assertion candidate read and every mathematical step independently rederived. The group-scheme representation, relative trace, diagonal linearization, and odd-character pairing arguments were checked with their actual twists and directions. No numerical theorem or program is needed for this proof.',
    'checks': [
        'The theorem of the square for a symmetric principal line bundle identifies the pullback under (z,a)->(z+a,z-a) with the external square line. The isogeny has scheme kernel diagonal B[2]. Its actual descent linearization supplies the level subgroup fixing the nonzero addition tensor.',
        'The central-product theta group gives a unique scheme-valued second lift tau(g); uniqueness descends its fppf construction. Multiplication makes tau a homomorphism, identity on B[2] and inversion on the center. Contraction of the addition tensor therefore intertwines two irreducible weight-minus-one representations and is an isomorphism. External tensor-product irreducibility can also be justified by the full matrix action algebra of each irreducible representation; no implication merely from scalar endomorphisms is needed.',
        'The printed geometric-character spanning sentence in AV8.31 is not used. The perfect universal Cartier-duality pairing identifies O(K)* with O(K), so all coefficient functions span. An invariant subspace is consequently an ideal and a translation subcomodule. The counit and antipode identities force such an ideal to be zero or the entire algebra. This verifies the group-scheme correction, including local-local kernels.',
        'The local relative Cartier coefficient formula gives a surjective sheaf trace. Frobenius is a torsor under G, and G dual is connected in two-rank zero; its coordinate algebra is local, so all simple G-representations are trivial. After pullback to the proper connected torsor, the trace map between trivial bundles has constant coefficients. Its kernel therefore comes from a subrepresentation, yielding a filtration with trivial line quotients. Ample-line higher cohomology vanishing makes the global principal trace surjective.',
        'Contraction of a perfect addition tensor by the nonzero principal trace is a nonzero section kappa of M squared. The difference between the two diagonal G-linearizations is a character because functions on G times the proper connected product are precisely O(G). Connectedness of G dual leaves only the identity geometric character, so the diagonal linearizations coincide scheme-theoretically.',
        'Finite duality trace is invariant under cover automorphisms after arbitrary base change. Tracing the diagonal action hence makes kappa invariant for the canonical Frobenius descent. Faithfully flat descent identifies that invariant space with the one-dimensional square-theta line. Thus kappa is a nonzero scalar times theta squared, with the stated target on the Frobenius twist.',
        'For an odd etale incoming isogeny, each principal character summand is one-dimensional. A functional supported on the trivial target character pairs only inverse characters, and their coefficients are the nonzero theta values squared under the explicit avoidance hypothesis. The trivial block and every diagonal vanish because the invariant top Cartier form vanishes in two-rank zero. The rank is therefore exactly n-1.',
        'The final scope retains the incoming auxiliary-cover direction. Theta avoidance on the target does not solve the corresponding outgoing quotient problem for a prescribed fixed source. The proposition and corollary imply no new curve p-rank or global Lang/monodromy theorem by themselves.'
    ],
    'primary_sources': [
        {
            'title': 'Edixhoven, van der Geer and Moonen, Abelian varieties',
            'url': 'https://van-der-geer.nl/~gerard/AV.pdf',
            'web_ref': 'turn632268386view0',
            'retained_original_text': 'agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt',
            'retained_text_sha256': sha(own/'sources/edixhoven_geer_moonen_AV.txt'),
            'actual_read_scope': 'Original author PDF freshly opened. Complete retained original text of Theorem8.10 and Corollary8.14 with their proofs, pp116-117; the full discussion8.30-8.32 including the printed8.31 issue, pp124-125; Theorem9.14 and Corollary9.17 with their complete proofs, pp133-134. No new image-view claim.'
        },
        {
            'title': 'Brion and Kumar, Frobenius splitting methods in geometry and representation theory',
            'url': 'https://www-fourier.univ-grenoble-alpes.fr/~mbrion/fbook.pdf',
            'web_refs': ['turn632268386view1', 'turn795799386view0', 'turn488996688view0', 'turn286513794view0'],
            'actual_read_scope': 'Original PDF freshly opened and complete original text of Definition1.3.5, Lemma1.3.6 and its proof, Proposition1.3.7 and its full proof, the projection-formula identification, and Theorem1.3.8 read on printedpp26-28. Relative Frobenius typing is obtained by the standard scalar twist over the perfect base. The screenshot request returned text placeholders only and is not counted as an actual image inspection.'
        }
    ],
    'numerical_scope': 'No numerical experiment, certificate rerun or elapsed numerical runtime is claimed.',
    'scope': 'Full five-label proof/source pass in the stated algebraically closed characteristic-two, two-rank-zero principal setting, with the conditional incoming-cover limitation preserved.'
}
audit = own/'principal_theta_Cartier_bridge_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_source_audit',
                           str(source.relative_to(root)),
                           'Complete scheme-theoretic proof and exact original AV/BK passages',
                           'PASS', str(audit.relative_to(root))])+'\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'record': str(audit.relative_to(root)), 'labels': labels}))
