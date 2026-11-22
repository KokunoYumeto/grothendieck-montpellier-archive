"""Record the root's full geometric coefficient and odd-cover proof audit."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/monodromy/ppav_twisted_Cartier_Moore_candidate.tex'
expected='80db90e54c403914d3aa26626a829ec31c1f85eecb078833e675af5441ada65b'
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
out=w/'outputs/root_twisted_Cartier_Moore_audit.json'
snapshot=w/'notes/root_twisted_Cartier_Moore_audited_candidate.tex'
assert not out.exists() and not snapshot.exists()
shutil.copy2(p,snapshot)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:principal-theta-Cartier-translated-square',
 'lem:ppav-symmetric-level3-addition-gauge',
 'prop:ppav-Cartier-cross-Moore-identification',
 'thm:ppav-non-two-torsion-cross-Cartier',
 'cor:ppav-odd-cover-maximal-dual-Cartier',
 'cor:fixed-ppav-all-odd-maximal-dual-Cartier',
 'rem:ppav-twisted-Cartier-Moore-scope']
record={'status':'PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(p.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'proof_scope':'Entire stable seven-label candidate read and independently rederived. Fresh original source passages and the complete internal symmetrizer, degree-one rank proof and cubic-theta jet proof read. No new numerical computation is claimed by this audit.',
 'proof_checks':[
  'For any commutative finite group scheme G over algebraically closed k, the commutative Artinian algebra O(G)^* has one-dimensional simple modules. Thus the associated trace-kernel filtration has character line factors Q with F^*Q trivial, hence Q two-torsion and numerically trivial. Ample twisting kills higher cohomology and gives global principal trace surjectivity without a two-rank hypothesis.',
  'Perfectness of the principal addition tensor and surjectivity make kappa nonzero. Its diagonal G-character identifies its descent with the unique principal theta line twisted by Q. The corresponding point b0 in B[2](k) is the unique geometric lift under relative Frobenius: F(2b0)=0 and ker F has a single geometric point. The induced translation operator on M^2 is genuine.',
  'The discrepancy of a theta splitting under normalized symmetry is a character eta. Replacing by psi with psi^2=eta^(-1) makes it symmetric, since the character group has odd order. Descended theta is fixed because its symmetry scalar squares to1 in characteristic2. Distinct K-characters of R_i e0 give the full nine-element basis.',
  'Both translation systems on the symmetric-square bundle are actual group linearizations. Their scalar ratio delta is a character. The rigidified square isomorphism is compatible with each independent sign change by uniqueness of a line-bundle isomorphism with fixed value at the origin. Thus delta(-k,h)=delta(k,h) and delta(k,-h)=delta(k,h), forcing both restrictions to have orders dividing2 and3; delta=1.',
  'Etale pullback commutes with relative Cartier, and an odd isogeny is an isomorphism on full two-torsion. The lift a0 exists uniquely in A[2]. The tensor-square lift R_k^2 descends to the Frobenius-twisted lift R_k^(2), not to an untyped same-surface operator. The theta commutator of a0 and h has orders dividing2 and3 and is trivial. This proves every index and both factors in TCM5.',
  'At fixed a, the line-fibre translation T_a0 multiplies all nine evaluated squares by one common nonzero scalar. Reindexing i=2u,j=2v gives the literal Moore matrix; its coefficient vector is the coordinatewise square of the complete cubic-theta embedding at a+a0. No independent row gauges are introduced.',
  'Coordinate squaring permutes the 81 planes. Every plane is a Heisenberg translate of the base alternating plane and is contained in the fixed locus of a conjugate of inversion. The complete cubic-theta system embeds the smooth-theta surface by the re-read jet theorem; in the product case the degree-three elliptic embeddings and Segre embedding give the same fact. Injectivity forces 2(a+a0)=2t for t in A[3]; applying phi_L gives2P=0. This proves every cross determinant with P not two-torsion is nonzero.',
  'For an odd etale cover the character lines are all odd torsion. A functional supported on the trivial target character pairs only inverse input characters. All cross determinant opens lie in the same nine-dimensional functional space; the trivial block has rank8 by the fully re-read level-three symmetrizer and degree-one Pfaffian proof. Their finite intersection is nonempty. The total alternating rank is8+18(n-1)/2=9n-1, the odd-dimensional maximum.',
  'For fixed |3dTheta| with d odd, a maximal isotropic K of orderd^2 gives an outgoing quotient A->B and a principal descendant M0. Its symmetry discrepancy is in the odd-order kernel of pullback and has a unique half there; adjustment preserves the pullback. Nonordinarity is isogeny invariant. Hence the cover result applies on the same fixed source A for every oddd.'
 ],
 'primary_sources':[{
  'title':'Edixhoven, van der Geer and Moonen, Abelian Varieties, preliminary chapters',
  'url':'https://van-der-geer.nl/~gerard/AV.pdf',
  'web_refs':['turn482447492view0','turn412993218view0','turn412993218view1','turn412993218view2','turn412993218view3','turn872163936view0','turn872163936view1'],
  'actual_scope':'Fresh full printed proofs of Theorem2.7 and Corollary2.8 (pp19-20), Lemma8.24 (p121) and Theorem8.28 (pp122-123), plus full normalized-symmetry Definition11.44 (p178). The adjacent Lemma11.45 says Proof to be written and is not imported as an examined proof. Its identity needed here follows directly from normalization and proper global units. Lemma8.24(ii) refers to an exercise; the elementary symplectic decomposition over F3 was independently rederived. Corollary8.20 and the full descent statements8.10/8.14 were freshly read in the preceding principal-bridge audit, not claimed reread again here.'}],
 'internal_proofs_reread':['agents/monodromy/ppav_theta_cartier_symmetrizer.tex: entire theorem and proof',
  'agents/obstructions_crystals/A3_ppav_surface_ranks.tex: complete Proposition DE-A3-ppav-degree-one proof',
  'sections/A_ppav_two_jets.tex: entire dichotomy, preliminaries and jet proof; complete section displayed and read'],
 'independent_algebra_input':'Full root proof/code audit and unchanged exact universal certificate rerun in outputs/root_Moore_classification_audit.json.',
 'requested_editorial_refinement':'On promotion add explicit thm:ppav-three-theta-jets reference and the product degree-three elliptic/Segre embedding argument to the existing embedding sentence; no mathematical change.',
 'scope_guard':'New maximal rank is for the dual alternating contraction family. Generic curve p-rank was already known. No new full monodromy case or general-X A4 closure is asserted.',
 'numerical_program_executed_for_this_geometric_audit':False}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
  'independent re-proof',
  'PASS: entire typed geometric proof and stated original proof passages read and rederived. Actual Moore coefficient, non-two-torsion cross determinants, and all fixed odd dual ranks proved; global monodromy still open. Details: outputs/root_twisted_Cartier_Moore_audit.json.'])
with (w/'notes/ROOT_SEARCH_LOG_31.md').open('a') as f:
 f.write('\n## Exact cubic coefficient and odd-cover audit\n\n'+now+': full seven-label proof audit passed against SHA256 '+expected+'. Fresh original AV2.7/2.8,8.24,8.28 proofs and11.44 definition were read in the exact scope of outputs/root_twisted_Cartier_Moore_audit.json. The local-global source conventions and the actual relative Frobenius target are retained. This audit performs no new numerical computation. Maximal dual alternating rank in every fixed odd degree does not by itself supply the full Lang monodromy image.\n')
print(json.dumps({'status':'PASS','actual_utc':now,'candidate_sha256':expected,'labels':labels},indent=2))
