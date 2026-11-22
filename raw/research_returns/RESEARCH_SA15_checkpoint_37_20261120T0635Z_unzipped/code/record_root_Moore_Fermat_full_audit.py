"""Record the completed, actual full proof audit; the isolated code rerun is retained separately."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
p=w/'agents/obstructions_crystals/post_CP31_Moore_Fermat_nondivisibility_candidate.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='35451b9383a4772ab7114cb9f47b444670bac239eedcd772def059475e0071f6'
assert sha(p)==expected
prior=json.loads((w/'outputs/root_Moore_Fermat_code_audit.json').read_text())
assert prior['all_mathematical_output_identical'] and prior['same_remainder_as_root_prior_independent_construction']
out=w/'outputs/root_Moore_Fermat_full_audit.json'
snapshot=w/'notes/root_Moore_Fermat_fully_audited_candidate.tex'
assert not out.exists() and not snapshot.exists()
shutil.copy2(p,snapshot)
labels=['lem:DE-Fermat-coefficient-reductions','lem:DE-Fermat-affine-lines','lem:DE-Fermat-full-and-eight','thm:DE-Moore-Fermat-nondivisibility','rem:DE-Moore-Fermat-scope']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
r={'status':'PASS','actual_utc':now,'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(p.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'actual_read_scope':'Entire five-label candidate read before the notation repair and reread in full after the repair. Full old six-support matching lemma and reflection/phase construction reread in a bounded successful output. The immediately preceding attempted full old-file read was truncated and is not credited. Entire standalone certificate was read and independently rerun in the separate retained audit.',
 'proof_checks':[
  'Monic division in x0 commutes with every parameter specialization. The exact coefficient reconstruction supplies universal polynomial witnesses, including four parallel-line product cubes, all 399 support exclusions, and the eight old two/four/six-support factors. No point sampling proves a universal identity.',
  'Restriction of x to a line subgroup block-diagonalizes the matrix into the three stated 3-by-3 matrices. Their determinants have the displayed product and cube-sum terms. Divisibility by the restricted Fermat cubic forces a vanishing affine-line cube sum because the Fermat cubic cannot divide the coordinate monomial.',
  'The 81 choices of four direction lines split into 9 concurrent choices and 72 choices with a unique triple point. The affine covariance uses translation q, with row Aa+2q and column Ab+q, so sum and difference give exactly the claimed indices and Fermat variables are only permuted. Character scaling preserves the required zero equations.',
  'Summing the four concurrent line equations in characteristic two gives total cube sum equal to the central cube. It excludes full support and, with a unique zero, gives every opposite-cube equality about that zero.',
  'For the nonconcurrent normal form the five cube equations, three product equations, character normalization f=d and homogeneous normalization e=1 are valid precisely in the cases where they are used. Cubing each product equation includes rs(r+s). It gives (D+A)U=(D+W)B=(D+V)T=K, while the sum of the first two left sides is the third. Thus nonzero K contradicts characteristic two.',
  'The six-element line stabilizer has exactly the four recorded point orbits. An uncovered zero forces two zeros; a triple zero gives opposite-cube equality; a single zero forces B^2+(1+B)^2=1=0; a double zero forces D=W=V and the four correct opposite pairs about (0,2). The affine covariance transports every case without changing Fermat divisibility.',
  'The old three-cyclic-product matching lemma was rederived: the three selected edges are a reflection permutation, a connected two-by-two pattern with the remaining values equal, or a star forcing all values equal using the nonzero product. Six-support phase product one then makes the three exponents affine linear and gives precisely V_(h,ell).',
  'For eight-support, the new geometric-free line proof supplies cube equality before the exact independent-variable phase certificate is applied. Each of the 72 noncharacter patterns has a nonzero monomial witness. Only the nine character patterns survive; no missing old binomial is assumed.',
  'The old explicit row permutation and scaling make every V_(h,ell) matrix alternating of odd order. Together with the lower-support and full-support cases, this proves F divides D_c if and only if D_c is identically zero, including c=0. The 81-space assertion is set-theoretic only.'
 ],
 'code_audit':'outputs/root_Moore_Fermat_code_audit.json',
 'program_sha256':prior['source_sha256'],'author_output_sha256':prior['author_output_sha256'],
 'independent_runtime_seconds':prior['independent_runtime_seconds'],
 'all_mathematical_output_identical':True,'author_output_unchanged':True,
 'retained_failures':'The four empty exploratory eight-support binomial lists and the author ideal-identity failure omitting a cubed-sum cross term remain retained; neither is represented as a successful proof step.',
 'scope_guard':'Universal characteristic-two determinant theorem only. The geometric coordinate comparison and global monodromy generation are separate questions.'}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'independent re-proof / computation or formal certificate','PASS: complete five-label proof rederived, repaired eight-support cases checked, literal standalone rerun matches. See outputs/root_Moore_Fermat_full_audit.json. Universal matrix theorem only.'])
with (w/'notes/checkpoint32_changes.md').open('a') as f:
 f.write('\n## Complete root Fermat proof audit\n\nThe complete five-label Fermat nondivisibility proof passed at '+now+'. This includes every unique-zero orbit, the corrected cubed-sum cross terms, the six-support matching proof and the independent-variable phase witnesses. The separate unchanged exact rerun took '+str(prior['independent_runtime_seconds'])+' seconds and matched every mathematical output. The empty exploratory coefficient searches and the failed initial ideal expression are preserved. No Cartier or global image conclusion is inferred from this algebraic result alone.\n')
print(json.dumps({k:r[k] for k in ('status','actual_utc','candidate_sha256','labels')},indent=2))
