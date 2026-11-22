"""Complete independent proof audit of the conditional local wall criterion."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals'
source=root/'agents/monodromy/post_CP30_Cartier_kernel_wall_inertia_candidate.tex'
expected='b6eb395dbbeafb4587486b34c22af5070af538b45cd8784cf48e3acdcf2be163'
assert hashlib.sha256(source.read_bytes()).hexdigest()==expected
labels=re.findall(r'\\label\{((?:lem|prop|rem):[^}]+)\}',source.read_text())
assert len(labels)==3
now=datetime.now(timezone.utc).isoformat()
record={
 'status':'FULL INDEPENDENT PROOF PASS','actual_utc':now,
 'candidate':str(source.relative_to(root)),'candidate_sha256':expected,'labels':labels,
 'proof_read_scope':'Entire stable three-assertion local wall candidate read. Entire canonical moving-kernel full-root-inertia lemma and its strict-henselian Artin-Schreier proof freshly reread. The full root differential/birational criterion and actual common-incidence proof were independently checked immediately beforehand. No new numerical run or external-source opening is claimed.',
 'checks':[
  'After restricting to the smooth generic locus of the integral divisor, the first image I is a rank-r-minus-one subbundle. The map F on F_D^*I lands in I. Its kernel is exactly K intersect F_D^*I, so failure of bijectivity is equivalent to containment of the kernel line in F_D^*I.',
  'In the constant ambient bundle, a rational frame of F_D^*I has coordinatewise-square entries and hence zero Kahler differentials over the perfect ground field. Under the hypothetical containment, differentiating a kernel generator can therefore move its projective line only inside F_D^*I/K, of dimension r-2. This contradicts the assumed derivative rank r-1. The restriction to I is thus bijective, proving stable rank r-1 with no assumption that I itself is constant.',
  'On U, the differentiated left-kernel identity and M_s:W/ks->ker(lambda_s) identify d kappa with B_lambda_s. Its maximal rank makes kappa etale on that open. This uses the alternating bilinear tensor and not an unproved alternation of the full multiplication matrix.',
  'Along q=lambda_s(s^[2])=0, differentiation gives dq=(d lambda_s)(s^[2]); evaluation on the nonzero squared section is a nonzero functional on the quotient by lambda_s. Thus every nonempty wall point is smooth. Rescaling lambda multiplies dq by a unit along the wall, so the equation is intrinsically reduced.',
  'The full transpose induces an isomorphism modulo its kernel line. Restriction to the squared-section annihilator has determinant equal, up to a unit, to the evaluation of that line on s^[2]. Hence the relative determinant has order exactly one and first corank exactly one on the wall.',
  'The projective kernel map on each wall component is the restriction of the etale kappa and has derivative rank N-2. The Euler bundle embeds locally in constant W*, with its Frobenius pullback in constant(W^(2))*. The preceding lemma applies with r=N-1 and gives stable loss one. All ambient and Frobenius-domain types agree.',
  'The complete earlier inertia lemma now applies: simple determinant, one kernel line, stable rank r-1 and maximal kernel motion. Its regular Lang frame yields independent differentials of the residue kernel coefficients; each nonzero F2 combination of the Artin-Schreier right sides has a nonsquare leading coefficient at pole order2, so all r-1 classes are independent. This gives the full hyperplane radical even for an imperfect strictly henselian residue field.',
  'Nonemptiness of the wall in U is genuinely retained as a condition. Nonzero determinant polynomials on the trivial nine-space need not remain nonzero on its smooth cubic. No new divisorial component, full inertia on an unverified wall, or global normal-generation/full-monodromy conclusion is inferred.'
 ],
 'dependencies_freshly_read':[
  'agents/monodromy/mixed_degree_one_uniform_full_groups.tex: entire lem:moving-kernel-full-root-inertia-candidate and proof',
  'sections/A_route_limitations_29.tex: full dual-kernel differential/birational criteria',
  'agents/obstructions_crystals/A4_common_Cartier_incidence.tex: full common-pair proof'
 ],
 'source_scope':'No new primary-source reading claimed. The exact Stacks finite-part inputs are reused only through the fully audited canonical moving-kernel lemma, whose entire argument was freshly read here.',
 'numerical_scope':'No numerical experiment or rerun needed or claimed.',
 'scope':'Conditional smooth-wall, stable-loss-one and full local hyperplane-radical theorem. Wall nonemptiness and global generation remain unproved in a new higher-degree application.'
}
audit=own/'Cartier_kernel_wall_independent_audit.json'
with audit.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:
  f.write('\t'.join([now,label,'independent_full_proof_audit',str(source.relative_to(root)),
                      'Complete squared-frame stable-image, Euler wall and strict-henselian inertia proof',
                      'PASS; conditional nonempty-wall scope',str(audit.relative_to(root))])+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'record':str(audit.relative_to(root)),'labels':labels}))
