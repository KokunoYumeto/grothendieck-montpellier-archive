"""Complete root audit and unchanged binary rerun of the two-axis theorem."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil,subprocess,sys,time
w=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/monodromy/post_CP35_product_two_axis_squarefree_candidate.tex'
source=w/'agents/monodromy/code/verify_ss_product_two_axis_squarefree.py'
author=source.with_suffix('.output.json')
expected='e5f2460eb4a5ed0e644963a1ebda95dc8c6eb6b02b535f68292e10bdfe479930'
assert sha(candidate)==expected
before={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
folder=w/'code/audit_snapshots/product_two_axis_root';assert not folder.exists();folder.mkdir(parents=True)
copy=folder/source.name;shutil.copy2(source,copy)
snapshot=w/'notes/root_product_two_axis_audited_candidate.tex';out=w/'outputs/root_product_two_axis_audit.json'
assert not snapshot.exists() and not out.exists();shutil.copy2(candidate,snapshot)
started=time.perf_counter();run=subprocess.run([sys.executable,str(copy)],cwd=w,capture_output=True,text=True);wall=time.perf_counter()-started
(w/'outputs/root_product_two_axis.stdout.json').write_text(run.stdout)
(w/'outputs/root_product_two_axis.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
independent=copy.with_suffix('.output.json')
a=json.loads(author.read_text());b=json.loads(independent.read_text())
mathpart=lambda x:{k:v for k,v in x.items() if k not in ('actual_utc','runtime_seconds')}
assert a['status']==b['status']=='PASS' and mathpart(a)==mathpart(b)
assert before=={str(p.relative_to(w)):sha(p) for p in [candidate,source,author]}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:ss-product-two-axis-universal-line','thm:ss-product-two-axis-cross-squarefree','cor:ss-product-two-axis-reduced-deformation-open','rem:ss-product-two-axis-squarefree-scope']
r={
 'status':'FULL-PROOF-CODE-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'read_scope':'Entire four-label candidate and complete standalone binary polynomial verifier read. The full actual relative-Cartier and Kunneth dependency was freshly read during the immediately preceding one-axis audit; the precise two-axis tensor formula was rechecked.',
 'checks':[
  'Every nontrivial degree-zero line on E is represented by a finite point(a,b), so the two monic relations cover all two-axis twists, including arbitrary nonzero odd torsion. The nine-variable tensor cross matrix uses the actual relative-Cartier bases, not an abstract tensor substituted for the geometric pairing.',
  'The subset determinant recurrence reconstructs the9x9 determinant in the exact quotient F2[a,b,c,d,t]/(b^2+b+a^3,d^2+d+c^3). Each multiplication starts with normal forms of b,d exponents at most1 and reduces every resulting exponent2 by the monic relation. Addition is symmetric difference, so the full recurrence is exact in characteristic2. All17 universal reduced terms give the stated homogeneous degree9 restriction.',
  'The first and second projective partials are the squares of uT^4+wT^3U+U^4 and vT^4+wT^3U+U^4. Their difference is Delta*T^4. For nonzero Delta a common projective zero would force T=0 and then U=0. This proves squarefreeness also at infinity, even when the affine leading coefficient u vanishes.',
  'Replacing b by b+1 changes Delta by1 and changes A0 exactly by A2. Therefore the second line is an invertible row-coordinate change in the original functional space, not a claim that the original twist has changed. The same original determinant has a squarefree restriction on one of two explicit lines for every pair of nontrivial twists.',
  'A repeated positive-degree homogeneous factor in the full determinant would restrict to a nonzero positive-degree binary factor, because the total line restriction is nonzero. Over an algebraic closure that factor has a projective root, contradicting the squarefree binary restriction. Hence the full polynomial is geometrically reduced. A corank at least2 matrix has every8x8 cofactor zero; all first derivatives of its linear-matrix determinant then vanish. Each reduced component is generically smooth over the perfect field, so its generic corank is1.',
  'In an actual deformation with locally free coefficient bundles, the two line directions extend after a local trivialization. The common-zero locus of the homogeneous derivatives is closed in a relative projective line. Its image is closed by properness, and the product point is outside it. This supplies the stated open neighborhood only within that given family, with no claim that an arbitrary fixed torsion-marked surface specializes there.',
  'The binary checker reconstructs three exact determinants and checks all eight listed identities, rather than sampling twist points. The order-three specialization t9+t+1 is retained as discovery data, while the proof is uniform in all twists. No composed Frobenius-cycle determinant, stable-rank loss, character-field inertia or full monodromy is inferred.'
 ],
 'source_scope':'No fresh external primary-source opening or novelty claim. The complete actual relative-Cartier calculation in lem:DE-SS-cross-elliptic and lem:DE-SS-cross-product was read, and the universal polynomial certificate is fully retained.',
 'program_sha256':sha(source),'author_output_sha256':sha(author),'author_bytes_unchanged':True,
 'independent_program':str(copy.relative_to(w)),'independent_output':str(independent.relative_to(w)),
 'independent_output_sha256':sha(independent),'independent_runtime_seconds':b['runtime_seconds'],
 'author_runtime_seconds':a['runtime_seconds'],'subprocess_wall_seconds':wall,'all_mathematical_output_identical':True,
 'identity_count':len(b['identities']),'universal_reduced_term_count':b['universal_reduced_term_count'],'executed_failures':[],
 'scope_guard':'Uniform reducedness for actual two-axis product cross pencils and openness in a given deformation. This does not identify the actual Frobenius-cycle wall or close the full-image gate, and is not counted by itself as hourly main-gate movement.'
}
out.write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:
  wr.writerow([label,now,r['reviewer'],'targeted proof check / computation or formal certificate','PASS: universal binary certificate and complete homogeneous/deformation proof; unchanged isolated rerun. See outputs/root_product_two_axis_audit.json.'])
with (w/'notes/checkpoint35_changes.md').open('a') as f:
 f.write('\n## Root audit of uniform two-axis product reducedness\n\nThe complete four-label candidate passed at '+now+'. The unchanged binary checker ran in '+str(b['runtime_seconds'])+' seconds and reconstructed17 universal terms, three exact determinants and eight identities. One of two fixed lines has a squarefree homogeneous restriction for every nontrivial twist on both factors, including every odd torsion order. Every determinant component consequently has generic corank1. This is a cross-pencil result and a local deformation statement; the Frobenius-cycle and fixed-surface full-image obligations remain.\n')
print(json.dumps({k:r[k] for k in ['status','actual_utc','independent_runtime_seconds','all_mathematical_output_identical','identity_count','universal_reduced_term_count']},indent=2))
