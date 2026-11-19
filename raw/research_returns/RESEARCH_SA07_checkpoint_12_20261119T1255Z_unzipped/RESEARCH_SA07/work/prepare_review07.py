"""Prepare the proof assessment; recording it remains guarded by the real clock."""
from pathlib import Path
import json

root = Path(__file__).resolve().parent.parent
out = root / 'output' / 'RESEARCH_SA07'
previous = json.loads((out/'PROGRESS_REVIEW_STATE.json').read_text())
assert previous['review_number'] == 6
gates = dict(previous['main_gates'])
gates['A.4c / H1'] = (
    'Exclude nonzero algebraic normalized h for an actual non-CM elliptic curve, '
    'already E*:y^2=4x^3-4x-1. The exact analytic quotient has differential '
    '(-h/c,1/c), with (h,c) not both algebraic. A.4.36-A.4.40 give the actual '
    'symmetric-tensor and conjugate-extension maps, ordinary integral tangent and '
    'isogeny law, graph rank bound, period-product second jet, and exact finite-place '
    'sizes of each algebraic-slope leaf. None identifies the ordinary integral line '
    'with the complex Hodge line, constructs a third independent algebraic graph '
    'point, or proves the first logarithmic derivative transcendental. The normalized '
    'period-product Taylor field is Qbar(h,c^2), including the actual rational '
    'modular coordinate u=37/64; its higher-jet obstruction leaves algebraic h '
    'possible. The enhanced quasi-isogeny orbit calculation supplies no arithmetic '
    'height bound for the required actual Galois orbit. This is the same gate.'
)
gates['E.2 separation'] = (
    'Determine the full pure integral transporter image, with the proposed equality '
    'image(Aut_tensor omega_Q,Z -> Gal(Qbar/Q))={1,c}, already for the two real '
    'embeddings of alpha^4-alpha-1=0. The exact CM/Artin image is Gamma_Fcm union '
    'c Gamma_Fcm with two lifts. The restricted quartic-swapping comparison includes '
    'all CM factors and non-CM simple factors of dimension at most three; the first '
    'unhandled fixed-Mumford-Tate instance is an arbitrary simple fourfold with '
    'End=Z. For all abelian varieties E.2.22 retains the condition of proper integral '
    'H1 on every finite Belyi cover. E.2.30 expresses this condition by the actual '
    'embedded completion Hc and one common inner adjustment; this is an equivalent '
    'description. E.2.31 constructs a specified conjugator outside Hc with its '
    'conjugated cusp generator in Hc, but supplies no full peripheral automorphism '
    'in the actual Galois image satisfying the all-cover premise. The one-cover '
    'boundary-extension and CM Kummer work does not establish that premise. The '
    'all-cover Galois intersection and extension to the full pure category remain.'
)
gates['F.3'] = (
    'The full profinite LM6 normalizer and general affine-curve cuspidality gates '
    'were closed by F.3.31-F.3.34 and credited at review06. F.3.35 gives the opened '
    'arbitrary-characteristic abelian fourfold theorem in the exact correspondence '
    'scope used here. F.3.36 fills the previously omitted known characteristic-zero '
    'scope: numerical=homological equivalence for smooth projective dimension<=4 '
    'and every abelian variety, with the whole abelian tensor-category comparison. '
    'The remaining general smooth-projective kernel-annihilation obligation and '
    'historical identification of M_alpha are unchanged. The field-extension, '
    'projector and tensor maps are proved; this known-family scope correction '
    'does not close or strictly reduce the remaining general main gate. Each '
    'documentary obligation and original ambiguous LM6 reading remains recorded.'
)
assessment = {
    'previous_review_number': 6,
    'expected_status_changes': [],
    'movement': False,
    'main_gates': gates,
    'reasoning': (
        'Root compared all 307 canonical assertions, including each of the 67 OPEN, '
        'READING and DOCUMENTARY-GAP obligations, and all eleven main gates against '
        'the actual review06 state. There is no canonical status change and no '
        'strict reduction of a remaining main gate. The nine newly integrated '
        'statements A.4.36-A.4.40, E.2.30-E.2.31 and F.3.35-F.3.36 supply exact '
        'maps, established family cases, equivalent descriptions and exclusions '
        'of specified proof routes. The actual non-CM algebraic-h case, conjugate '
        'period relation, all-cover Galois transporter, general geometric essential '
        'images and manuscript-definition obligations remain as stated. The '
        'period-map jets, rational modular coordinate, enhanced isogeny orbit '
        'and one-cover CM Kummer work likewise do not satisfy the missing main '
        'premises. New computations, independent checks, source retrieval, '
        'typesetting and packaging are not counted as movement. The normalizer '
        'closure was already credited at review06 and is not credited again. '
        'This is the first consecutive actual hourly review without movement; '
        'continue the unresolved work until the next due review at 13:55 UTC.'
    ),
}
assert set(gates) == set(previous['main_gates'])
path = root/'work'/'timed_review07_assessment.json'
path.write_text(json.dumps(assessment, indent=2)+'\n')
print(path)
