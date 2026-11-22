"""Retain the actual full root proof/dependency audit of the deck-slice bound."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/obstructions_crystals/post_CP33_Lang_deck_slice_bound_candidate.tex'
expected='2b0420d99c26ab0947196c600fbc466f92a3f40c05db41e3d71e48be29b54355'
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
out=w/'outputs/root_Lang_deck_slice_bound_audit.json';snapshot=w/'notes/root_Lang_deck_slice_audited_candidate.tex'
assert not out.exists() and not snapshot.exists();shutil.copy2(p,snapshot)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:DE-Lang-block-slice-bound','prop:DE-Lang-deck-slice-quotient-eight','rem:DE-Lang-deck-slice-scope']
dependencies=['lem:DE-common-incidence-multiplication','prop:DE-common-Cartier-incidence','lem:odd-cover-common-Fermat-coordinates','prop:odd-cover-common-rank-wall-nonempty','thm:odd-cover-full-hyperplane-inertia','cor:fixed-ppav-odd-full-hyperplane-inertia']
r={'status':'FULL-INDEPENDENT-PROOF-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','candidate':str(p.relative_to(w)),
 'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire exact final three-label candidate read. Entire canonical common Cartier incidence and all-odd full-inertia files freshly read, including all proofs and scope paragraphs. Exact group, main-orbit, outgoing-quotient and fixed degree-one results reuse their previously complete audits, with their precise application hypotheses checked here.',
 'proof_checks':[
  'For the abstract group step, canonical K lies in every G0-conjugate of the full-radical hyperplane. Block preservation makes its normal a nonzero V0-dual vector extended by zero, and the full projected GL(V0) makes its orbit span V0 dual. Their intersection is exactly V1; no independence of the two block actions is required.',
  'The odd deck group is constant over the algebraically closed field. Its averaging idempotent sum(g) is genuinely F2-defined, since its odd order is1 inF2, and commutes with the actual coherent Frobenius. Image and kernel therefore split the Lang sheaf overF2 even when individual character lines do not.',
  'Odd etale pullback and trace identify ambient cohomology; the relative invariant block is precisely the degree-one rank8 sheaf. The complete Cartier-incidence proof supplies a common nonempty smooth sharp slice open with all nontrivial character cycles bijective, rather than an unjustified genericity transfer.',
  'Restriction to that additional dense open preserves the full GL8 image: connected finite etale covers of the normal integral degree-one sharp locus remain connected on a nonempty open. The slice image is only a subgroup of the ambient image; no surjectivity onto the entire ambient fundamental group is assumed.',
  'The exact fixed-coordinate Fermat nondivisibility and common-wall proof applies to every odd-degree cubic pullback, not just n=d^2. It supplies a slice point with central stable rank7, every other cycle unit, and a smooth reduced ambient wall with stable rank r-1. The smooth-curve condition may be imposed on a further dense punctured open; no claim that the chosen wall member itself is smooth is needed.',
  'The Lang equations have fibre Jacobian minus identity. Over the strictly henselian local neighbourhood, each regular special Lang point has its unique etale section; addition is preserved by uniqueness. Their r-1-dimensional constant space exhausts regular vectors at the generic point of the same wall, because the stable rank there is r-1.',
  'The ambient full radical fixes that regular hyperplane. The finite etale inclusion of canonical K into it persists on the connected punctured local neighbourhood and restricts to the punctured slice. The restriction compares the same unique regular lifts and gives H0 plus Vnt, without any full-fibre specialization across a rank drop.',
  'The group lemma now gives K contained in Vnt and quotient dimension at least8. Transport of base points carries the specified slice splitting; it does not identify distinct deck slices. The main-component degree consequence is explicitly restricted to fixed principal systems with n=d^2, exactly the scope of the canonical main-orbit lemma. The n=1 edge gives K=0, agreeing with the earlier exact degree-one image.'
 ],
 'dependencies_freshly_rechecked':dependencies,'finite_computation':'None needed or executed.',
 'external_source_scope':'No new external source or classification imported. All new reasoning is direct; earlier source audits retain their original scopes.',
 'scope_guard':'Strengthens the necessary exceptional-module bound to dim(V/K)>=8. It does not compare distinct deck slices, exclude all nonzero K, determine H, or add a new exact full-image degree.',
 'executed_failures':[]}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'independent re-proof','PASS: entire final written proof and exact actual-sheaf/specialization scope rederived; see outputs/root_Lang_deck_slice_bound_audit.json.'])
 for label in dependencies:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: complete canonical proof freshly reread; odd-degree cover scope, common determinant opens and regular-wall comparison verified.'])
with (w/'notes/checkpoint34_changes.md').open('a') as f:
 f.write('\n## Root audit of the deck-slice restriction\n\nThe complete three-label proof passed at '+now+'. The actual F2 averaging decomposition and the regular wall hyperplane give K contained in the nontrivial deck part and dim(V/K) at least8. The main-component degree bound is restricted to fixed principal systems. No new exact full-image degree is inferred. The exact final candidate, independent companion record and this root proof audit are retained.\n')
print(json.dumps({'status':r['status'],'actual_utc':now,'candidate_sha256':expected,'labels':labels},indent=2))
