"""Record complete post-CP22 proof audits and preserve an isolated exact rerun.

The detailed mathematical checks were actually read and rederived by root.
This script records those checks; string hashes are not a proof audit.
"""
from pathlib import Path
import contextlib,csv,datetime,hashlib,io,json

w=Path(__file__).resolve().parents[1]
files={
 'direct':'notes/nonordinary_genus_two_trigonal_direct_candidate.tex',
 'galois':'agents/monodromy/nonordinary_genus_two_triple_ramification_candidate.tex',
 'graph':'agents/monodromy/nonordinary_three_theta_graph_reduction_candidate.tex',
 'root':'agents/obstructions_crystals/post_CP22_mixed_common_power_candidate.tex',
 'petri':'agents/obstructions_crystals/post_CP21_positive_index_Petri_notes.tex'}
hashes={k:hashlib.sha256((w/v).read_bytes()).hexdigest() for k,v in files.items()}
assert hashes['galois']=='698001da7d90674305e8399bea66352a92fbeef6dd7f1ef394e28893ad2a0533'
assert hashes['graph']=='662e13a5034afb25d7e423a0428b4751cf7ab2ce099741442a42cd8095536fb2'
author=w/'agents/monodromy/outputs/genus_two_three_total_ramification_checks.json'
author_hash=hashlib.sha256(author.read_bytes()).hexdigest()
source=w/'agents/monodromy/code/genus_two_three_total_ramification_checks.py'
program=source.read_text()
needle="out=Path(__file__).resolve().parents[1]/'outputs/genus_two_three_total_ramification_checks.json'"
assert program.count(needle)==1
target=w/'outputs/root_genus_two_three_total_ramification_checks.json'
snapshot=w/'code/audit_snapshots/genus_two_three_total_ramification_checks_at_root_audit.py'
out=w/'outputs/root_post_cp22_audits.json'
assert not target.exists() and not snapshot.exists() and not out.exists()
executed=program.replace(needle,'out=Path('+repr(str(target))+')')
snapshot.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
(w/'outputs/root_genus_two_three_total_ramification_checks_stdout.txt').write_text(stream.getvalue())
run=json.loads(target.read_text())
assert run['status']=='PASS'
assert hashlib.sha256(author.read_bytes()).hexdigest()==author_hash
direct_run=json.loads((w/'outputs/nonordinary_trigonal_direct_certificate.json').read_text())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
 'lem:root-nonordinary-trigonal-three-excluded-candidate':
 'The complete root-authored direct proof was rechecked: the non-Weierstrass pole uses the genus-two gap sequence; the characteristic-two nonordinary normal forms admit the displayed invertible changes with u nonzero and h(0)=1. The Q-prime expansion cancels the three possible denominator poles; infinity is a simple zero. Riemann--Roch makes the chosen function the actual trigonal pencil. A nonzero fully ramified fibre necessarily has a triple root of the cubic elimination polynomial. Two further values force the separable quadratic remainder to divide P, then R1=R0=R2=0, and the exact identity forces the affine singularity at h=0. The t=0 case has at most one extra root. The certificate checks universal identities and is not used for the global ramification inference.',
 'cor:root-nonordinary-theta-no-three-triples-candidate':
 'Three theta points in one subgroup coset killed by three give three disjoint effective divisors 3P,3Q,3R in the same two-dimensional complete section space. Their common basepoint-free pencil is trigonal and total at each point. No isotropy assumption is used.',
 'rem:root-trigonal-direct-scope-candidate':
 'Scope checked: only exponent-three kernels on nonordinary genus-two theta curves; no conclusion for arbitrary odd kernels and no node-permutation or gluing conclusion. The independent Galois/Cartier proof has no dependence on this direct normal-form calculation.',
 'lem:char2-genus-two-three-total-ramifications-candidate':
 'Full independent rederivation: different degree8 permits exactly four tame cubic points or three tame cubic points plus one wild quadratic point of different2. The cyclic case has two positive and two negative Kummer exponents and the displayed bijective off-diagonal Cartier matrix. In the S3 case the sign quotient is rational with involution z+1; its cyclic cover has six distinct branches and genus4. All four regular differential orders and the involution matrix were checked. The invariant space has dimension2 and equals the injective pullback from the genus2 quotient; no general wild invariant-differential descent is assumed. All four Cartier columns and the restricted matrix give determinant square ab+c, nonzero by cubic separability. Stacks0C1B full Riemann--Hurwitz/different discussion and Lemmas53.12.2/53.12.4, and 09DX full Kummer proof, were actually reopened and read at root in this audit.',
 'cor:nonordinary-genus-two-no-three-torsion-triple-candidate':
 'The Riemann--Roch pencil has dimension2 and is basepoint-free because the stated total fibres have disjoint supports. Thus three torsion-equivalent points contradict the proved trigonal lemma, for every subgroup killed by3.',
 'cor:nonordinary-theta-three-torsion-nodal-norm-candidate':
 'Invariant differentials identify the theta Gauss map with the canonical map, so a nontrivial tangent identification has g=2(P-W). Since 3g=0, the class 3(P-W) is geometric two-torsion. In two-rank0 it is0, and in rank1 it is0 or W-prime-W. The linear systems |3W|=W+|K| and |K+W-prime|=W-prime+|K| force the point to be Weierstrass, contradicting g nonzero. Hence all nonzero translates meet transversely in2 points. Principal theta has trivial translation stabilizer; exponent3 no-triples plus the etale quotient makes the norm integral nodal with2 nodes per unordered type and |K|-1 total nodes.',
 'rem:three-total-ramification-Cartier-certificate-candidate':
 'Entire exact program read and rerun in an isolated saved snapshot, preserving the author output byte-for-byte. Matrix/involution, coefficient Cartier, resultant, critical-value and ramification-budget checks PASS. No finite-sample ordinarity inference is made.',
 'rem:nonordinary-three-torsion-triple-scope-candidate':
 'Only nodality for kernels killed by3 is proved. Independence of node permutations and all gluing hearts remain separate inputs; no higher-odd-kernel extrapolation is made.',
 'lem:normal-base-clopen-Lang-closure-candidate':
 'The derivative of Fv-v is minus the identity, so the finite-type Lang scheme is separated quasi-finite etale and normal over the normal integral Noetherian base. Its finite disjoint irreducible components all dominate. The invariant finite etale subgroup on the open is clopen there and its closure is a union of these components, closed under the operations by density on the etale fibre product. A finite etale subgroup on a connected integral source is an open and closed immersion into the base-changed Lang scheme. Intersections have constant finite rank; either generic containment persists by openness of an etale complement. No rank constancy of the whole Lang fibre is claimed.',
 'lem:three-theta-odd-labelled-graph-candidate':
 'Edge counts 9k-3, two independent coboundaries and selected connected doubled triangle give dimensions9k-5 and9k-9. Unselected coordinates are independent modulo coboundaries. Hearts have annihilator constant on all18 coordinates/type; fixed loops anchor that constant while each pair difference ranges over allK under sum r=0, forcing a single all-ones cycle. Thus their span has codimension1, not zero. Any nonconstant coordinate of an invariant S yields all pair vectors of a type; a selected single cross edge and unselected loop violate containment in a suitable T_r. Remaining type-constant vectors vanish by r=(-u,0,u) and invertibility of2 inK.',
 'thm:three-theta-conditional-full-image-candidate':
 'The theorem is conditional exactly on the two displayed geometric inputs. All translated source unions have sum r=0 and lie in one complete system. The projection to U is uniform only on the connected dense maximal-rank source open. Ambient H1 restricts injectively to each theta normalization, so graph cohomology embeds in the relative Lang fibre. Clopen closure handles the rank-dropping common boundary. Projection zero gives a full-rank subspace in every T_r and hence0. Surjective projection plus shears gives all hearts; G0 has codimension1 and finite etale intersection rank persists, so any proper S is a hyperplane, excluded by the previously proved odd invariant-covector theorem. For transvection-normal subgroup J, the socle is full by global irreducibility. The actual GL8 natural constituent occurs once and belongs to one J-simple summand; rank-one gluing puts all17t heart dimensions there, exceeding R/2, so conjugation forces J irreducible. The already source-audited transvection classification and absence of a GL8-invariant form on its natural block force GL_R. No false inequality 8>number-of-types is used.',
 'rem:three-theta-conditional-geometric-gates-candidate':
 'Both additional inputs are retained explicitly. Arbitrary odd theta norms may be tangent or have triple identifications. An actual GL8 block does not itself give independent S18 factors or shears. The newly proved exponent3 theta nodality closes only the individual-norm part at this audit time.',
 'lem:DE-A3-mixed-common-power-root':
 'The full integral ordinary/local-local polarization blocks and exact group-scheme dictionary were rechecked. Divisibility of both blocks by n kills all of A[n], hence the actual fppf quotient [n] factors lambda_M as n phi. Hom torsionfreeness makes phi symmetric. Root actually read the complete original AV Proposition11.2/Corollary11.3 pp159-160: the Poincare construction uses X[4] and the isotropic X[2] descent to a line bundle in every characteristic, including2. Pic0 divisibility then corrects H0 to an actual root H^n=M. Ampleness, both index subtractions, chi/n squared and maximality follow from the integral polarization equality. Algebraic closure is explicit and no field-of-definition descent of the root is asserted.',
 'thm:DE-A3-mixed-index-ordered-ranks':
 'The entire prior index-zero theorem was freshly rechecked. For0<a<=b the maximal root has ordinary index0 and the identical complete system has exponent d-prime=2^a d, always even. Substitution in the proved index-zero even formula gives9Dd squared minus2; no genericity is transferred through a restricted pullback family. Genus, relative coherent dimension and ambient stable rank1 yield the stated full p-rank. The ambient-hypersurface conclusion retains the exact regularity/surjectivity hypothesis.',
 'cor:DE-A3-mixed-primitive-rank-gate':
 'The actual same-surface root identifies the full families, with exponent multiplied by2^min(a,b). The previously closed a=0 sector and new0<a<=b sector leave only primitive a>0,b=0. This strictly shrinks the A3 mixed-polarization gate; it does not prove the remaining cup-product radical vanishing.',
 'lem:DE-A3-positive-restricted-Petri-note':
 'The sheaf determinant-direction sequence is the K sequence twisted by P with its two summands interchanged. The fixed P squared trivialization and no common zero give surjectivity; higher cohomology of E0,E1 vanishes, yielding the exact sequence and equal h0(KP),h1(KP) codimension. Cup and wedge signs multiply to plus, so the actual quotient Sym squared U is appropriate in char2; its dual is used without identifying divided powers. The Serre-duality contraction formula exactly dualizes Psi, hence equal ranks. No smoothness or reducedness of the determinant curve is assumed.',
 'cor:DE-A3-positive-Petri-radical-note':
 'Common radical equals common kernel of the actual Psi family. An invertible member makes it zero; conversely the proved trace-zero matrix-space theorem says an all-singular space is zero or a single nilpotent line, each having nonzero common kernel. A change to Serre-duality bases preserves this condition. Dualizing the exact section sequence identifies the annihilator with H1(KP) dual, with the twist essential.',
 'rem:DE-A3-positive-Petri-radical-scope-note':
 'This is an equivalent restricted nonvanishing test, not a new lower bound or gate movement by itself. The determinant directions cannot be enlarged to all sections, and no identification with a curve-pencil multiplication map is imported.'}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():
        wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
    wr.writerow(['lem:root-nonordinary-trigonal-three-excluded-candidate',now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','computation or formal certificate','PASS. Root universal nine-identity certificate actually executed at the UTC and runtime recorded in outputs/nonordinary_trigonal_direct_certificate.json. No rerun claimed by this record.'])
    wr.writerow(['rem:three-total-ramification-Cartier-certificate-candidate',now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','computation or formal certificate','PASS. Author-preserving isolated root rerun; original output hash unchanged. Runtime '+str(run['elapsed_seconds'])+' seconds.'])
record={'status':'FULL PROOF AND SOURCE AUDITS PASS; GRAPH THEOREM CONDITIONAL AS STATED',
 'actual_utc':now,'events':len(checks)+2,'candidate_files':files,'candidate_sha256':hashes,
 'galois_root_rerun_seconds':run['elapsed_seconds'],'galois_author_output_sha256_unchanged':author_hash,
 'root_direct_author_certificate':direct_run,'source_reads':[
  'AV11.2/11.3 full original pp159-160 recovered and actually read after a prior context-truncated output',
  'Stacks0C1B full section including Lemmas53.12.2/53.12.4, retrieved turn848924346view0',
  'Stacks09DX full Lemma9.24.1 proof, retrieved turn848924346view1'],
 'checks':checks}
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k not in ('checks','root_direct_author_certificate')},indent=2))
