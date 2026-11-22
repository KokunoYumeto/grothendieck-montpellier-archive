"""Record the completed root proof audit of the ordinary hereditary synthesis."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
root=Path(__file__).resolve().parents[1]
path='parts/C/post25_research/D_arbitrary_cover_ordinary_unit_growth.tex'
data=(root/path).read_bytes()
sha=hashlib.sha256(data).hexdigest()
assert sha=='c1a26abffac4af77da9af3e8a647540a78382652638b0d6dc56e0bd634d5a975'
delta=json.loads((root/'parts/C/post25_research/arbitrary_cover_ordinary_growth_factor_delta.json').read_text())
initial=(root/'parts/C/post25_research/arbitrary_cover_ordinary_growth_pre_factor.source.txt').read_text()
assert data.decode().replace(delta['new'],delta['old'],1)==initial
assert hashlib.sha256(initial.encode()).hexdigest()==delta['initial_candidate_sha256']
out=root/'parts/D/post25_research/audit_C_arbitrary_cover_ordinary_unit_growth_root.json'
assert not out.exists()
record=dict(
 actor='root', model='GPT-6 Astra Pro', effort='setting not independently exposed', run='SA12 run1',
 recorded_utc=datetime.now(timezone.utc).isoformat(), type='targeted proof check', verdict='PASS',
 path=path, sha256=sha, labels=['D:arbitrary-cover-ordinary-hereditary-growth'],
 actual_file_scope='Complete actual candidate00d36372 read in full, including every proof line; the only revised component-prefactor block actually read on finalc1a26abf, with exact reversal checked here.',
 certificate_scope='Mathematical proof audit; no numerical certificate.',
 checks=[
 'Finite normalization is complete and semilocal, and its connected puncture selects one normal local factor. The fixed henselian base and specified relative-minimal model preserve the simultaneous O(t) resolution, genus and cycle budgets.',
 'The strong reduction cycle satisfies C<=Z<=alpha C and the required all-subcycle generation/vanishing inequalities. The scalar O(t) cohomology on each fixed LC follows independently from K=f*K0+R, 0<=R<=lambda C, fibre-dimension H2 vanishing, and adjunction.',
 'Each geometric ordinary representation supplies a length-f ordinary p-unit cycle of canonical full bundles, with regular forward arrows and inverse pole pC. No relative-canonical-family assertion is used to cover these geometric objects.',
 'The initial scalar character count is q^(O(t)), not one independent character at every phase. Nonnegative determinant multidegrees have sum O(tr), and the negative definite intersection form gives uniqueness of each exceptional extension for fixed punctured determinant. The stated binomial enumeration gives exp(O(ft log(r+1))) tuples of actual fixed global lines.',
 'Choosing b=p, N>=max(3,alpha), L=N+p ensures pN-p>N and retains the entire generating cycle Z in NC. Fixed line quotient presentations on LC cover all generated canonical bundles using r+1 sections and O(ftr^2) object coordinates.',
 'Both finite inverse equations are imposed as genuine Cartier-inclusion equations on LC. No localization of its nilpotent Cartier equation, or unsupported independent relation lifting, occurs.',
 'The locally split quotient presentation remains exact under absolute Frobenius over every coefficient ring. The forward and inverse residual line twists are respectively (1-p)Z and (p-1)Z+pC.',
 'All relevant fixed line terms have the form P/Q for generated lines P,Q of total degree O(tr). Regular sections on the full nonreduced Cohen--Macaulay curve give the displayed O(tr) H0+H1 bound. The (r+1)^2 repeated fixed-twist term has the sharper O(t) scalar bound, so total Hom dimension is O(tr^2), not O(tr^3).',
 'The complete all-coefficient finite-Hom proof was reread: fixed two-column Cech splittings, h delta h=0, exact polynomial transfer, cycle representatives and degree-minus-one boundary witnesses provide actual maps and exact product equalities after every coefficient change. Frobenius introduces only p-th powers. A bounded number of complexes per phase therefore gives O(ftr^2) variables/equations and degree bounded independently of t,r,f.',
 'The generating-tuple condition is one open subset of the affine zero scheme. Its closed complement does not require a degree estimate, since an open cannot increase the irreducible-component count. There is no unbounded chart union.',
 'Finite object effectivity constructs simultaneous objects and compatible arrows, preserving NC. Unique integral unit comparisons with the same N-jet glue the local constructions. No arbitrary finite bundle is independently algebraized without its unit data.',
 'Because Z is retained, the actual generating quotient and fixed determinant on Z lift by the weak-cycle result. The generated fixed-determinant Isom theorem applies even to noncanonical constructed families. Its object/rank-dependent comparison bound is only qualitative and contributes no atlas coordinates.',
 'Every original representation is recovered as its punctured unit class: its true formal object is a valid local-lift choice, and choice independence identifies it with the constructed family. Coverage is not merely of truncations.',
 'Disjoint clopen class images are bounded by irreducible components. The weighted affine lemma with unit weights retains the harmless (M+1) prefactor in the final revised display; it is absorbed into p^(O(ftr^2)). Multiplying the determinant tuple count yields q^(A_R t r^2).',
 'The theorem has no tameness hypothesis on the original finite cover. Its conclusion concerns ordinary GL representations only; twisted projective determinants, arbitrary PGL objects and full finite generation are explicitly excluded from its inference.'
 ],
 dependencies_rechecked=[
 'Complete actual source parts/C/post18_research/D_fixed_determinant_finite_Hom.tex, including all transfer identities, composition and all-ring boundary witness semantics.',
 'The actual scalar-character and exceptional determinant enumeration plus quotient/finite-Hom budget in parts/B/post24_research/D_ordinary_unit_determinants_cycle_Hom_B.tex.',
 'Complete actual parts/D/post19_research/D_weighted_component_bound.tex, including the arbitrary-dimensional component argument and the (M+1) factor.',
 'Current object-effectivity, comparable-cycle and generated fixed-determinant openness proof audits completed separately by root in this same interval.'
 ],
 fresh_primary_reads=[],
 primary_scope='No new external primary-source opening is claimed for this synthesis. Exact previously opened and audited inputs are reused; the new theorem has only internal references.',
 movement_scope='A complete new ordinary arbitrary-cover count is established. Its supporting units are not separate movement events. The strongest remaining gate comparison and any crown consequence are reserved for the scheduled formal review.'
)
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'path':str(out.relative_to(root)), 'sha256':sha, 'verdict':'PASS'},indent=2))
