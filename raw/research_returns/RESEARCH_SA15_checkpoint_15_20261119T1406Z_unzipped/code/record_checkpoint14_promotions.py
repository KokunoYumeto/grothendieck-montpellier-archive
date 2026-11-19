"""Record audited post-review08 results without modifying the actual review."""
from pathlib import Path
import datetime, json, subprocess, sys
w = Path(__file__).resolve().parents[1]
marker = '## Further results after actual review08'
p = w / 'notes/checkpoint14_changes.md'
text = p.read_text()
assert marker not in text
text = text.replace('## Unpromoted work', '## Candidates at the time of review08')
text = text.replace('The proposed uniform supersingular norm-collision exclusions and a further nonproduct mixed-polarization extension are being written and checked. Until their full proofs pass independent audits, they do not change the current outcome table or count toward an actual progress review.',
                    'At the actual review08, the uniform supersingular norm-collision exclusions and the nonproduct mixed-polarization extension were candidates and were excluded from its movement count. Both were subsequently proved and independently audited, as recorded below. The immutable review remains an account of what was proved at its actual time.')
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
text += f'''
{marker}

Recorded at {now}. These are completed mathematical results after the actual review08; no extra hourly review is being fabricated.

### A.3: mixed surfaces beyond products

For a mixed abelian surface in characteristic two, write a(M) for the index of its polarization on the rank-one etale2-adic Tate module. Integral Dieudonne duality gives two paired elementary-divisor indices a(M),b(M), with v2(chi(M))=a(M)+b(M). The dual polarization chi(M)lambda_M^(-1) is integral, including inseparable polarizations. A prescribed etale principal norm source of degree chi(M) exists exactly when a(M)=0. In this class, for L=M³ and every d>=1, the generic relative stable rank is9chi(M)d²−1 in odd degree and9chi(M)d²−2 in even degree. The proof does not assume a product decomposition or odd chi(M). An even-degree Prym upper bound is also proved for every mixed polarization. The a(M)>0 class remains outside this theorem.

Root and monodromy complete independent proof/source/code audits passed. Oda's original integral skew Riemann form, including printed100–101 actually viewed, supplies the alternating lattice even in characteristic two; the inference uses W(k) being torsion-free. Exact finite-flat descent and duality sources were read. The author/root/monodromy certificate times are0.04614707099972293s,0.049978896997345146s and0.03037099799985299s. Universal block identities and289 index pairs,1024 odd norms and1024 even unions are retained; they supplement the geometric proof.

### A.4: uniform mixed contact with all other collisions excluded

For every finite odd subgroup of the fixed supersingular elliptic product whose two coordinate projections are injective, and every nonzero kernel difference, there is a globally smooth cubic source on its Hasse cubic whose norm image has exactly one simple self-tacnode and otherwise only ordinary nodes. The extra Cartier-kernel differential has unequal values at the identified tangents. The proof treats every moving pair and triple incidence, not merely a finite list of torsion points. Smooth coefficient-plane cubics give integral moving covers; explicit etale points handle nonflex cases, and the flex case has constant contact length3 and odd moving degree15. Triple limits exclude all remaining identifications. Irreducibility of the full contact family and the finite-flat length3 cluster argument combine these exclusions with source smoothness.

All three independent full proof audits passed. The final universal algebra certificate has author runtime0.19226371099648532s, root0.18832970500079682s and obstruction/crystal0.16412100700108567s. The first author program/output and the first root output are also retained. The final version replaces a tautological terminal expression check with actual source and translated branch substitutions; the leading coefficient is T+vF/h. The previously retained six-jet certificate places the global contact03 witness in the main incidence. Uniform tangent-triple bridges remain the current norm-family gate. No uniform higher-degree full-monodromy result is claimed.

### B.4: the smallest odd-prime height-two case is sharp

Theorem B-RD42 proves nu_min(3,2,2)=2 for the full permitted height-two class:27-torsion determines the requested character on prime-to-three inertia, whereas the explicit9-torsion ambiguity proves sharpness. Every remaining C4 pair normalizes to M_b:y²=x³−3x+3b and the pi-twist of M_b-prime. Their cyclic cubic good fields have Kummer classes determined by the residues of b up to sign. The reverse marked Fourier cocycle forces equal normalized unit residues; Fisher's reverse9 equation and an exact trace expansion then force b-prime²=b² in the residue field. Thus both curves have a common good extension of degree6, contradicting the previously necessary joint order18. This excludes the final branch.

Root and obstruction/crystal full proof/source/code audits passed. The actual reverse-marking involution in Fisher's original Section3 and the essential factor3 in Theorem4.3 were reread. Author/root/independent exact-certificate times are0.1415409550027107s,0.11300166400178568s and0.10002119700220646s. The initial structural-SymPy-equality failure and its complete program/trace are retained; no exact runtime was recorded for that failed attempt. The corrected polynomial-zero test is exact. The general B.4 least-index problem remains open; p=2,e=1,h=2 is a remaining small instance where4-torsion fails and8-torsion sufficiency is undecided.

### Current work and schedule

Promoted mathematical source files are frozen for checkpoint14 integration. Further tangent-triple and characteristic-two height-two work is being kept in separate candidate files. The next checkpoint is due13:20:40UTC, and the next actual hourly review is due13:50:40UTC. The no-movement streak remains0 from review08; packaging is not counted as movement.
'''
p.write_text(text)
subprocess.run([sys.executable, str(w / 'code/update_current14.py')], check=True, cwd=w)
print(json.dumps({'status': 'recorded', 'actual_utc': now}, indent=2))
