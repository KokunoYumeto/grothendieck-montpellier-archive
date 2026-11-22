"""Author provenance for B88 and complete bounded reciprocal incidence audit."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
own=Path(__file__).resolve().parents[1];work=own.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
candidate=own/'B_p5_full_image_ramification_candidate.tex'
program=own/'code/verify_p5_full_image_ramification.py';out=program.with_suffix('.output.json')
assert sha(candidate)=='59e1f80c1b6a5b1b269859c2b5bd7ab488771a008409d4c9760931cdf9293fab'
labels=re.findall(r'\\label\{([^}]+)\}',candidate.read_text())
rec={'status':'COMPLETE_CANDIDATE_AWAITING_INDEPENDENT_AUDITS','actual_utc':now,
     'source':str(candidate),'source_sha256':sha(candidate),'labels':labels,
     'program':str(program),'program_sha256':sha(program),'output':str(out),'output_sha256':sha(out),
     'author_run':json.loads(out.read_text()),
     'source_scope':'Full B87 actual coefficient and point-field proofs reused. Retained original Colmez2.12 full tame-uniformizer proof and3.7 through3.10 full norm/Herbrand proof reread at01:46-01:47UTC; prior original web access recorded in B86. No new download or image view claimed.',
     'scope':'Necessary actual tame-sector full-image profile only. Does not exclude or realize cyclotomic break3, a full-image pair, or any other residual sector.',
     'failures':[]}
(own/'outputs/B88_candidate_record.json').write_text(json.dumps(rec,indent=2)+'\n')

src=work/'agents/obstructions_crystals/post_CP30_common_Cartier_incidence_candidate.tex'
expected='a66b95b4de7a405fe4f0aa143a57ad5f6186254d530b846995de573206a5b8f7'
assert sha(src)==expected
alabels=re.findall(r'\\label\{([^}]+)\}',src.read_text());assert len(alabels)==4
deps=[work/'agents/monodromy/ppav_twisted_Cartier_Moore.tex',
      work/'agents/monodromy/ppav_theta_cartier_symmetrizer.tex',
      work/'agents/obstructions_crystals/A3_ppav_surface_ranks.tex',
      work/'sections/A_route_limitations_29.tex']
audit={'status':'FULL_INDEPENDENT_PROOF_PASS','actual_utc':now,'source':str(src),
 'source_sha256':expected,'labels':alabels,'complete_read':True,
 'proof_checks':[
  'The actual three-index tensor beta(e_i,f_j)=c_((i-j)/2)g_((i+j)/2) gives the other multiplication contraction with entries c_(k-j)v_(2k-j). Since2=-1 in F3, this is the same Moore matrix after the independent variable permutation x_h=v_-h. A nonzero dual determinant therefore genuinely yields the other determinant here, not by a generic-rank heuristic.',
  'For Q squared=P, a fixed translation with phi_M(u)=Q balances M and MP into MQ^-1 and MQ. The relative target M^(2)Q^(2) pulls back to M squared P and translates by-F(u) to M^(2). This is a fixed linear isomorphism on section spaces, so the determinant remains a nonzero polynomial.',
  'The finite-theta full symmetrizer supplies an actual fixed k-linear J:V0 -> W0dual; on the trivial rank8 block its left-kernel vector is J(s0), not a semilinear or untyped twist identification. Extending this vector by zero is the unique full left kernel once every nontrivial multiplication block is invertible.',
  'Every nontrivial character determinant and every inverse-pair dual determinant is nonzero on the same nine-space, the latter after composition with J. The finite intersection with the degree-one rank8/sharp/smooth open is nonempty over the algebraically closed infinite field. The full ranks are exactly8+9(n-1) and8+18(n-1)/2.',
  'The smooth etale pullback is connected by H1(L^-1)=0. Actual coherent character decomposition puts all ambient H1 in the trivial character; the nontrivial blocks form finite half-character cycles of invertible semilinear maps. The trivial relative block is the chosen degree-one sharp block. No assertion that arbitrary etale pullback preserves sharpness is used.',
  'The outgoing odd maximal-isotropic isogeny yields the actual complete system L=pi*(M0 cubed); symmetry is adjusted by the unique half of an odd kernel character. The common point then satisfies the proved differential identity rank(dkappa)=rank(B_lambda)=h-1. Dominance is separable, and the unique radical line supplies the rational inverse.',
  'Divisorial inertia, global radical generation and additional full-monodromy degrees remain explicitly unproved.'
 ],
 'dependencies':[{'path':str(p),'sha256':sha(p)} for p in deps],
 'dependency_read_scope':'Entire current TCM canonical and theta symmetrizer read; actual degree-one rank proposition proof and full root differential/birational section reread. Full Moore universal classification was separately audited and rerun earlier this turn.',
 'external_source_scope':'No new external-source read needed for the new index identity and finite-open intersection. Earlier complete AV and Moore dependency audits are reused with their precise scopes.',
 'computation_scope':'No new numerical program required or run for this four-label geometric proof.'}
(own/'outputs/independent_common_Cartier_incidence_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join((now,label,'COMPLETE_CANDIDATE_AUTHOR_CHECK','Actual full-image point-field and cyclotomic necessary profile; complete proof and exact finite certificate retained.','outputs/B88_candidate_record.json','Independent audits pending; no full-image exclusion'))+'\n')
 for label in alabels:
  f.write('\t'.join((now,label,'FULL_INDEPENDENT_AUDIT_PASS','Full common Cartier incidence/triality/linear symmetrizer/actual relative rank/birational proof independently rederived.','outputs/independent_common_Cartier_incidence_audit.json','No divisorial-inertia or global-monodromy claim'))+'\n')
print(json.dumps({'actual_utc':now,'B88_candidate':sha(candidate),'common_incidence_audit':'PASS','labels':alabels},indent=2))
