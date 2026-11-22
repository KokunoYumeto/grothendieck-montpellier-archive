"""Record actual full root audit of the typed, rounded compatible-residual theorem."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/obstructions_crystals/post_CP34_compatible_residual_modules_candidate.tex'
expected='ccdb387fc0b28ecadecdfa7dc1c8b093d706c6f5151555239551b322ad098f74'
assert hashlib.sha256(p.read_bytes()).hexdigest()==expected
out=w/'outputs/root_compatible_residual_modules_audit.json';snapshot=w/'notes/root_compatible_residual_modules_audited_candidate.tex'
assert not out.exists() and not snapshot.exists();shutil.copy2(p,snapshot)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:DE-source-residual-projection','thm:DE-compatible-residual-module-sum','cor:DE-prime-compatible-wedge-bound','rem:DE-compatible-residual-module-scope']
reviewer='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root'
r={'status':'FULL-INDEPENDENT-PROOF-PASS','actual_utc':now,'reviewer':reviewer,
 'candidate':str(p.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire four-label original written candidate fully read. The entire saved final R_H-domain and cyclic-rounding diff was then read against that source; the resulting final source hash is the one recorded here. Full arbitrary-source, compatible-intermediate, deck-slice, full-radical and determinant-wedge proofs were independently audited immediately before this record, with the final wedge source facts checked in original retained text.',
 'proof_checks':[
  'The source and target are actual odd cubic-principal pullbacks, so both have generic sharpness and full hyperplane radicals, hence unique maximal proper canonical submodules. The common source-slice determinant open and common wall exist without a source full-GL assumption, by the complete arbitrary-source proof.',
  'On the source slice, the actual odd deck average e gives the splitting V0 plus Vnt. Dense-open restriction preserves the whole actual source image, not only a known subgroup. The same regular Lang lifting argument identifies an ambient full-radical fixed hyperplane H0 plus Vnt with this splitting at one valid base point.',
  'W=e(K) lies in the proper H0. It is invariant under the actual source image because e commutes with the slice image, K is ambient-invariant, and the slice projects onto that actual source image. The unique-maximal-proper-submodule theorem therefore gives W subset K0. No full source GL, independent block action or rank-dropping full-fibre specialization is assumed. The a=1 and n=1 endpoints remain valid.',
  'For each intermediate H, the source quotient e_H V/K_H exists on connected T_H where both systems are smooth sharp and outer cycles are units. The map from target K into this quotient vanishes on a nonempty open by the first lemma and therefore everywhere by local constancy. This puts all projected residual modules on the same S_D.',
  'The requested domain clarification is present: R_H in the central coefficient space requires the degree-one curve and its eta_H pullback to be smooth and sharp, plus all inner nontrivial blocks unit. It is integral, nonempty and contains S_D. Thus the pullback K_H and central projector really exist throughout the connected continuation domain. B-sharpness alone is not used.',
  'On the common fibre, e_D is the actual quotient-deck average after e_H. Narrow source and target slice bounds imply e_DK_H=e_DK=0. The projectors p_H=e_H+e_D are idempotent, pairwise orthogonal, and sum with e_D to1. Their images have dimensions9(ell-1), and K_H lies in its corresponding image. Thus K embeds into their actual direct sum, not an abstract sum of unrelated fibres.',
  'Taking dimensions gives q_target>=8+sum(q_H-8). The independently fully audited wedge theorem applies to each type(3,3ell) source and gives q_H>=3ell. This yields q_target>=3ell^2-5ell and k_target<=6ell^2+5ell-1. Main-component degree is stated only for the canonical fixed-principal target scope.',
  'For the sharper bound, a deck translation of the intermediate cover acts on the entire source coefficient family and fixes its central point. Naturality of the actual fibre representation makes its F2-linear action normalize the source geometric image. Uniqueness of K_H makes K_H an actual F2[C_ell]-submodule. Its invariant summand is zero, and all nontrivial simple factors have dimension f=ord_ell(2), so dimK_H is divisible by f.',
  'Combining that divisibility with the wedge bound gives k_H<=f floor((6ell-1)/f), and the already justified direct sum gives the final rounded target formula. For ell17, order2 modulo17 is8 (2^4=-1), each k_H<=96, total k<=1728 and quotient>=872 in rank2600. These are exact substitutions, not finite-pattern extrapolations. A nine-dimensional coherent character block is never treated as an F2 Lang block.'
 ],
 'requested_clarification':{'prior_sha256':'4c9a210e0434382b8ff5bcda70fbb1f45b8d1532f9783b0a0dedb4a44cc82b2c','scope':'Explicit R_H ensures source local systems exist at every continuation point; final delta also adds the complete deck-normalizer and cyclic-dimension rounding proof.','retained_delta':'agents/obstructions_crystals/notes/CP34_compatible_residual_typing_rounding/changes.diff'},
 'external_source_scope':'No new source theorem is imported by this direct proof. The only theta nondegeneracy needed for its wedge dependency was freshly read in the separate complete root wedge audit.',
 'computation':'No numerical program needed or executed.','executed_failures':[],
 'scope_guard':'An unconditional stronger bound on the exceptional module at a prime target degree. It does not prove K=0 in any new higher degree, classify H on K, or close general A.4.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,reviewer,'independent re-proof','PASS: full final proof including typed R_H, actual common-fibre projectors and rounded cyclic-module bound. See outputs/root_compatible_residual_modules_audit.json.'])
 wedge=json.loads((w/'outputs/root_Lang_wedge_pole_theta_bound_audit.json').read_text())
 for label in wedge['labels']:
  wr.writerow([label,wedge['actual_utc'],reviewer,'independent re-proof / used and rechecked in this run','PASS: complete wedge proof and full original theta-commutator proofs read. Event appended after CP34 freeze release; original audit time retained. See outputs/root_Lang_wedge_pole_theta_bound_audit.json.'])
with (w/'notes/checkpoint35_changes.md').open('a') as f:
 f.write('\n## Full root audits of the wedge and compatible residual bounds\n\nThe complete wedge/source audit occurred at '+wedge['actual_utc']+'; its per-label events were deferred during the preceding freeze and are appended with that original timestamp. The full final compatible-residual audit occurred at '+now+'. The final R_H continuation domain explicitly keeps every source local system defined. The same-fibre projectors and exact cyclic-module dimensions give quotient at least872 and exceptional dimension at most1728 at prime17, in rank2600, once these audited candidates are canonically promoted. This remains a dimension bound, with no new full-image degree. All exact candidates, requested typing/rounding deltas and independent audit records are retained.\n')
print(json.dumps({'status':r['status'],'actual_utc':now,'candidate_sha256':expected,'labels':labels},indent=2))
