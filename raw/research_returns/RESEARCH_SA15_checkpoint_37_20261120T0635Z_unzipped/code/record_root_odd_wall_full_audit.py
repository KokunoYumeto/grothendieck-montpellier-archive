"""Record actual complete root audit of the common-coordinate Cartier wall theorem."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/monodromy/ppav_all_odd_full_root_inertia_candidate.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='0bb79d06ae2ec1a09d9ad1ac3b9cbad85d34621d91357129a4a9c5c11a4de8cf'
assert sha(p)==expected
algebra=json.loads((w/'outputs/root_Moore_Fermat_full_audit.json').read_text())
assert algebra['status']=='PASS'
out=w/'outputs/root_odd_wall_full_audit.json';snapshot=w/'notes/root_odd_wall_fully_audited_candidate.tex'
assert not out.exists() and not snapshot.exists()
shutil.copy2(p,snapshot)
labels=['lem:odd-cover-common-Fermat-coordinates','prop:odd-cover-common-rank-wall-nonempty','thm:odd-cover-full-hyperplane-inertia','cor:fixed-ppav-odd-full-hyperplane-inertia','rem:odd-full-hyperplane-inertia-scope']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
r={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(p.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'actual_read_scope':'Entire 300-line five-assertion candidate read in two successful bounded outputs. Entire conditional common-wall proposition and squared-frame lemma reread, central q-versus-Fermat coefficient proof reread, and complete strict-henselian moving-kernel Artin--Schreier proof reread. Exact TCM and fixed-basis symmetrizer dependencies were read in full in the preceding retained root audits and rederived here at the actual indices.',
 'proof_checks':[
  'The fixed symmetric theta basis and its actual Frobenius-twisted basis have central symmetrizer J=I. Full tensor symmetry and alternation make the central matrix alternating with both kernel coordinates s. Thus its wall is exactly sum(s_i^3), in the coordinates used by the universal algebra theorem.',
  'The inverse-character cross block is c*c_(u-v)(a)*x_(u+v) after i=2u,j=2v, so substitution lambda(e_i prime)=s_i gives precisely D_c(s). A nontrivial odd P is not two-torsion, so the already proved actual-parameter theorem makes this determinant nonzero.',
  'For multiplication with P=Q^2 choose phi_M(u)=Q. The bases e_i(z), e_j(z+2u), e_k prime(z prime+F_B(u)) have exactly the stated bundles. In the balanced coordinate w=z+u, a=-u, the first input remains literally e_i(z). Output row k and input column j give c_(k-j)(-u)*s_(2k-j)=c_(k-j)(-u)*s_(-(k+j)). Only index inversion acts on s, preserving Fermat. The fixed two-torsion Cartier shift changes c only.',
  'The central nonzero Pfaffian cubic is not proportional to Fermat by its explicit four direction coefficients. Fermat in P8 is smooth and integral. Each of the finitely many nontrivial multiplication and dual-cross determinants restricts nontrivially to it. Their nonvanishing opens intersect the central rank-eight open in an actual nonempty open.',
  'For the odd character decomposition, multiplication permutes target characters by the unique half and all nontrivial blocks are invertible on that same intersection. Its total rank is N-1 and its left kernel has only the central s coordinates. The same kernel gives dual rank8+18(n-1)/2=N-1. Hence a point lies on the maximal common-rank wall, without incorrectly using the smaller Frobenius-bijective common open.',
  'The universal hypersurface exact sequence works for every nonzero ample section, including singular divisors. H1(L^-1)=0 and Serre duality give E=ker(W* tensor O(-1) to O)=Omega1 on the entire coefficient projective space. Relative Frobenius is regular and locally equals the typed transpose M_s^t from (s^[2])perp to s perp. No smooth-wall member hypothesis is introduced.',
  'On the maximal common-rank open the derivative of the left-kernel map is the nondegenerate alternating form B_lambda transported through M_s. It is an isomorphism. Evaluation on s^[2] therefore makes the wall smooth with simple determinant order, and the kernel map restricted to it has differential rank N-2.',
  'If the linearized kernel lay in the squared first image, its projective differential would have rank at most N-3 because all squared frame coordinates have zero differential. The actual rank N-2 excludes that containment and proves stable loss exactly one.',
  'In the strict henselian DVR proof the r-1 regular unit sections give F=[[I,b],[0,a]], a a uniformizer times a unit. Maximal kernel variation makes db0_i independent, so each nonzero F2 combination of b_i/a^2 has nonsquare leading coefficient and is not an Artin--Schreier coboundary. The resulting full elementary inertia has order2^(N-2), even with imperfect separably closed residue field.',
  'The invertibility open is nonempty and contains a dense smooth-member open. Every connected finite etale cover of the normal integral base remains integral and connected after restriction to that open. The generic finite image is therefore unchanged, so inertia from the whole-space Euler model lies in the smooth-family image without a rank-drop specialization isomorphism.',
  'The already audited maximal-isotropic odd quotient has degree d^2 and descends 3dTheta to a cube of a principal polarization, with nonordinarity preserved by odd isogeny. Substitution N=9d^2 gives the stated fixed-surface subgroup for every odd d including1. No global generation or full-group conclusion follows merely from its existence.'
 ],
 'algebra_dependency':'outputs/root_Moore_Fermat_full_audit.json',
 'new_numerical_run':False,
 'scope_guard':'The local wall nonemptiness gate is closed in every stated odd principal-cube system. Global generation, irreducibility, new exact full-image degrees and the general A.4 row remain open.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'independent re-proof','PASS: full fixed-coordinate, nonempty-wall, Euler-model and actual-inertia proof rederived. See outputs/root_odd_wall_full_audit.json. Global generation remains open.'])
with (w/'notes/checkpoint32_changes.md').open('a') as f:
 f.write('\n## Complete root odd-wall proof audit\n\nThe five-assertion proof passed at '+now+'. Both twisted block families use the same central Fermat coordinates: the multiplication block introduces only index inversion. The maximal common-rank wall is consequently nonempty, and the actual whole-space Euler model gives full hyperplane inertia of order 2^(9d^2-2) for every fixed odd principal-cube degree. The independent generic-image argument transfers this subgroup to the dense smooth-family open. No new numerical run was needed, and global generation, new exact full-group degrees and general A.4 remain open.\n')
print(json.dumps({k:r[k] for k in ('status','actual_utc','candidate_sha256','labels')},indent=2))
