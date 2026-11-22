"""Record the actual component audit and the already-accounted review14 scope."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
source = root / 'parts/D/post21_research/D_SNC_tree_component_presentations.tex'
digest = hashlib.sha256(source.read_bytes()).hexdigest()
assert digest == 'c70590403a7ddc5fc60eb05720db7357f4cde874de4e01fe943331cf555b3b32'
record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'actor': 'root', 'model': 'GPT-6 Astra Pro (OpenAI)',
    'effort': 'inherited; no separate control exposed', 'run': 'SA12 run1',
    'check_type': 'full actual-file mathematical proof audit and stated fresh primary-source proof read',
    'path': str(source.relative_to(root)), 'sha256': digest, 'outcome': 'PASS',
    'checks': [
        'Read the entire corrected candidate. Split lifted flags give kernel weight zero; full-preimage flags would not. The explicit T/Q kernel has the stated homogeneous basis and invariant coarse source over arbitrary coefficient algebras.',
        'The first rank condition is imposed on P1 to P(g), as required; its composite into T^h need not have residual rank one at marked points. Unit-minor cancellation supplies actual vector bundles and both locally free end modules over every coefficient ring.',
        'The fixed rank-two syzygies use only the two positive ordinary Hom lines. The T/Q Cartier resolutions are exact on normal thickenings. Distinct point supports have zero derived Hom, and individual root-character invariants bound the remaining supported blocks without squaring the number of marks.',
        'Fixed-width column increases and positive normal order make the HPL series finite. The explicit Cartier null-homotopy in the last column preserves the total-complex identity. Separate lengths seven and three preserve the stated Hom error ranges; the identity test uses the actual surjective P(g) source.',
        'The thick-node fibre-product identity holds by monomial comparison over all coefficient rings. Finite-projective module pasting, homogeneous rectangular frames and derived restriction of Q give actual component gluing, with a bounded number of invariant slots per entry.',
        'The normal weights, residual frame weights, bounded Frobenius carries and fixed diagram width give the claimed polynomial presentation budget. The statement fixes all formal background data and makes no unsupported claim about their coefficient complexity, coefficient-gerbe counts, or a completed tree representation count.'
    ],
    'fresh_primary_reads': [{
        'source': 'Stacks Project, Section15.6, Tags0D2G and0D2J',
        'urls': ['https://stacks.math.columbia.edu/tag/0D2G','https://stacks.math.columbia.edu/tag/0D2J'],
        'retrieval_refs': ['turn435210213view1','turn435210213view0'],
        'scope': 'Situation15.6.1 and entire written statements/proofs of Lemmas15.6.4 through15.6.8, section lines20–26 and52–131; full Lemma15.6.9 proof separately at Tag0D2J lines22–31. Both actual outputs read; the section output alone stopped before the end of15.6.9, supplied in full by the separate page.'
    }],
    'reused_inputs': 'Previously read full Borne Proposition3/Theorem4 and Borne–Vistoli Theorem6.1 proofs; previously audited fixed partial resolutions, Cech/HPL, normal-window and unit-Isom inputs. No fresh complete reread of those unchanged sources is claimed.',
    'movement': 'Two auxiliary units only. A tree projective count and main-gate reduction still require a separate synthesis.'
}
audit = root / 'parts/D/post21_research/audit_D_SNC_component_presentations_root.json'
assert not audit.exists()
audit.write_text(json.dumps(record, indent=2)+'\n')

assembler = root / 'code/assemble.py'
s = assembler.read_text()
marker = "'','## Files and continuation','',"
addition = """'Ten completed units are assembled after checkpoint21. Two exceptional-tree geometry results identify residues, coefficient-gerbe extensions and marked spectral categories; two further results give minimal marked slope windows and uniform Hom depth. These four are auxiliary and do not yet give a tree count. A finite cyclic tame-coefficient H2 bound is proved without inflating H2 through a normal wild subgroup. Fixed partial resolutions then yield ordinary projective counts q^(C_R t r²) on every degree-t radially tame cover of the one-curve resolution, uniformly in scalar order and geometric period. Exact nonsplit wreath lifting and the projective count close faithful projective automorphism crowns with bounded graph quotient and bounded stabilizer field-image order. The conditional unbounded-field theorem is explicitly conditional. These results belong to the single crown reduction recorded at review14, including its timestamped scope addendum; their assembly creates no new movement.',
'Unbounded-field projective semilinear descent remains an exact open gate: the actual coefficient gerbe on the field cover must have a coherent extension compatible with the deck and band actions and retain the index-linear weighted budget. An arbitrary extension at the geometric period does not establish that coherence. Root-extension and character-sector compression are under investigation. No new semilinear projective count is claimed from the H2 bound alone.',
"""
assert marker in s and 'Ten completed units are assembled after checkpoint21.' not in s
s = s.replace(marker, addition+marker, 1)
scope = """crown_scope='; ordinary projective counts are hereditary on radially tame covers of the one-curve resolution, and faithful projective automorphism crowns with bounded graph quotient and bounded stabilizer field-image order have uniform multiplicity and generator bounds'
crown_labels='D:tame-hereditary-projective-count; D:nonsplit-automorphism-wreath-lifts; D:bounded-field-automorphism-crowns'
outcomes=[(item,state+crown_scope,locator+'; '+crown_labels) if item in ('D.1','D.2(ii)','L8') else (item,state,locator) for item,state,locator in outcomes]
"""
assert "report=['INCOMPLETE'" in s
s = s.replace("report=['INCOMPLETE'", scope+"report=['INCOMPLETE'",1)
assembler.write_text(s)

unresolved = root / 'parts/D/unresolved_D.tex'
u = unresolved.read_text()
u += r'''

\paragraph{Ordinary projective heredity and bounded-field automorphism crowns.}
Theorem~\ref{D:tame-hereditary-projective-count} supplies
$q^{C_Rtr^2}$ ordinary projective counts on all degree-$t$ radially
tame covers of the one-curve resolution, using actual fixed partial
resolutions. Lemma~\ref{D:radial-tame-cyclic-H2} bounds the full
twisted coefficient obstruction on the tame quotient without an
invalid degree-two inflation through the normal wild subgroup.
Proposition~\ref{D:nonsplit-automorphism-wreath-lifts} gives the exact
nonabelian lifting bijection without assuming that the outer
extension splits. Theorem~\ref{D:bounded-field-automorphism-crowns}
then controls the stated projective automorphism crowns when the
graph quotient and the stabilizer field-image order are bounded.
The field size, projective rank and diagonal part remain unrestricted.
These statements belong to the one review14 crown reduction.

The unbounded-field projective count in
\ref{D:bounded-graph-projective-crown-reduction} remains an explicit
hypothesis. The unresolved geometric step is to extend the actual
coefficient gerbe coherently with the deck and band actions on the
field cover and to retain the index-linear weighted complexity.
Choosing an arbitrary root-gerbe extension at the geometric period
does not prove this compatibility. No such descent is inferred from
the ordinary projective count or the obstruction-class bound.

\paragraph{Exceptional trees: geometry and map depth.}
Lemmas~\ref{D:SNC-tree-Brauer-geometry} and
\ref{D:SNC-tree-residual-category} give exact residues, actual
coefficient-gerbe extensions, component spectral categories and
reduced node gluing for a simple-normal-crossings exceptional tree.
Lemmas~\ref{D:SNC-tree-minimal-marked-windows} and
\ref{D:SNC-tree-uniform-Hom-depth} give uniform marked slope windows,
original-cycle pole bounds and normal Hom depth. They are auxiliary:
they do not by themselves yield an effective object atlas, its unit
class comparison, or an unbounded-period representation count for
this larger exceptional configuration.
'''
unresolved.write_text(u)
print(json.dumps({'utc':record['utc'], 'audit':str(audit.relative_to(root)), 'sha256':digest,
                  'updated':['code/assemble.py','parts/D/unresolved_D.tex'],
                  'additional_movement_events':0},indent=2))
