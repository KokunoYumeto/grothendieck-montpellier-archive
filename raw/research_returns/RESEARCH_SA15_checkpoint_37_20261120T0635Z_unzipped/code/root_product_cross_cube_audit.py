"""Full root audit of the actual one-axis product Cartier determinant."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/monodromy/post_CP34_product_twisted_determinant_cube_candidate.tex'
source=w/'agents/monodromy/code/verify_ss_product_one_axis_determinant_cube.py'
author=source.with_suffix('.output.json')
expected='0f67ca3f9ff32439e04dd2dfb319bb5e85ef21cb746eaf5fc7201b31b51f76b0'
assert sha(candidate)==expected
before={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
folder=w/'code/audit_snapshots/product_cross_cube_root';assert not folder.exists();folder.mkdir(parents=True)
copy=folder/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_product_cross_cube_audited_candidate.tex'
out=w/'outputs/root_product_cross_cube_audit.json'
assert not snapshot.exists() and not out.exists();shutil.copy2(candidate,snapshot)
started=time.perf_counter();run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True);wall=time.perf_counter()-started
(w/'outputs/root_product_cross_cube.stdout.json').write_text(run.stdout)
(w/'outputs/root_product_cross_cube.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert a['status']==b['status']=='PASS' and mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:ss-product-one-axis-cross-determinant-cube','prop:ss-product-one-axis-cross-corank-three','rem:ss-product-one-axis-cross-cube-scope']
r={
 'status':'FULL-PROOF-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire final three-label candidate, the full unchanged verifier and the complete invoked elliptic relative-Cartier, product cross-block and Kunneth proofs actually read. The final covariance transpose correction was independently rederived from the volume pairing.',
 'checks':[
  'The nontrivial twist P1=O((a,b)-O), with b^2+b=a^3, has actual bases(1,x,(y+b+1)/(x+a)) and(1,x,(y+b)/(x+a)). Multiplication by x+a is the required product trivialization. All nine products and their relative Cartier x-coefficients give the displayed A0,A1,A2. This preserves k-linearity through relative Frobenius; no absolute-Cartier coefficient identification is made.',
  'On the untwisted elliptic factor the three target coefficients span all alternating3x3 forms. Kunneth therefore gives the actual nine-variable matrix C(T)=sum(t_ij A_i tensor B_j), with every target functional represented by an arbitrary3x3 matrix T.',
  'For S(g) defined by g^t B_j g, the volume identification is det(g)g^{-1}: vol(v,gu,gw)=det(g)vol(g^{-1}v,u,w). Thus det S=det(g)^2. Given h, choose delta^2=det h and g=delta*h^{-1}; its determinant is delta and S(g)=h. Surjectivity is on algebraically closed geometric points, and requires no separability claim.',
  'The coefficient transform is TS(g)^t and the matrix transform is(I tensor g^t)C(T)(I tensor g). The determinant scales by det(g)^6=det(S)^3, so det C(T)/det(T)^3 is constant on the invertible locus. The displayed permutation evaluation has invertible6x6 block and universal Schur complement determinant1; hence the constant is1. Density proves the polynomial identity for every twist, without extrapolating from the specialized expansion.',
  'If rank T=2, its column space is a projective line in the A-pencil. The explicit determinant r^2*t+r*t^2+s^3 has gradient(t^2,s^2,r^2), so is a smooth cubic and contains no line. The column space therefore contains an invertible U; a right basis change makes the matrices U,V,0. The block matrix has kernel exactly(0,U^{-1}Vz,z), and its6-minor is det(U)^2. Its rank is6.',
  'For rank T=1 the matrix is a tensor product with a rank2 alternating factor, so its rank is at most6. Rank T=3 gives an invertible matrix by the determinant identity. Thus rank8 never occurs. The rank2 locus of det T=0 is a dense irreducible orbit and has nonzero adjugate, so the cubic is reduced irreducible and its multiplicity in det C is exactly3.',
  'The exact supplement checks all69 stated identities, including universal elliptic/Schur identities and generic exterior-square covariance. Its full nine-variable specialization at(a,b)=(0,0) has36 terms, independently reconstructed by binary cubing of the six-term determinant. The prior SymPy multivariate-gcd failure is retained with exact source/output/traceback. No Frobenius-cycle or global monodromy claim follows from this dual cross-pencil calculation.'
 ],
 'dependencies_freshly_reread':['lem:DE-SS-cross-elliptic','lem:DE-SS-cross-product','thm:DE-SS-odd-pullback-dual-rank'],
 'source_scope':'No fresh external primary-source opening and no novelty claim. The explicit relative-Cartier calculation is completely reproduced in the retained canonical dependency and was read in full.',
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,
 'all_mathematical_output_identical':True,'check_count':b['check_count'],'full_determinant_term_count':b['full_determinant_term_count'],
 'executed_failures_this_rerun':[],
 'prior_failure':b['prior_failure'],
 'scope_guard':'This refutes only the inference from a nonzero actual twisted cross determinant to a reduced corank-one wall. It is compatible with all proved product full-monodromy results. It does not shrink the exact A.4 exceptional-module gate and does not identify an actual Frobenius-cycle determinant.'
}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'targeted proof check / computation or formal certificate','PASS: complete relative-Cartier and covariance/rank proof; unchanged isolated69-check rerun. See outputs/root_product_cross_cube_audit.json.'])
 for label in r['dependencies_freshly_reread']:
  wr.writerow([label,now,r['reviewer'],'used and rechecked in this run','PASS: complete actual relative-Cartier/product proof read and conventions checked.'])
with (w/'notes/checkpoint35_changes.md').open('a') as f:
 f.write('\n## Root audit of the repeated actual product determinant\n\nThe full three-label one-axis product candidate passed the root proof/code audit at '+now+'. The unchanged isolated exact verifier passed69 checks in '+str(b['runtime_seconds'])+' seconds; its36-term full nine-variable determinant agrees with det(T)^3. The final covariance formula correctly uses det(g)g^{-1}, with the preceding text and repair diff retained. Every rank2 coefficient matrix gives cross rank6, so nonvanishing alone does not furnish a simple corank-one wall. This closes an attempted inference, not the remaining A.4 image problem, and is not counted as a main-gate reduction. The failed exploratory gcd execution remains retained.\n')
print(json.dumps({k:r[k] for k in ['status','actual_utc','independent_runtime_seconds','all_mathematical_output_identical','check_count','full_determinant_term_count']},indent=2))
