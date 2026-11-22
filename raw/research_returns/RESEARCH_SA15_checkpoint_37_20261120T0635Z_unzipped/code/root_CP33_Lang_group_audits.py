"""Retain actual full written proof audits; no finite experiment is claimed."""
from pathlib import Path
import csv, datetime, hashlib, json, re, shutil
w = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root'
items = [
 ('root_full_radical_image_structure_audit', 'notes/A_full_radical_image_structure_candidate.tex',
  '9d2e7f21840ef9025ee5c9a22d2f7ef5614876ccf55866d028697f6786b1d7f3',
  'targeted proof check', [
   'Entire final four-label author candidate reread. This is an author targeted proof check, not an independent re-proof of my own candidate. The prior geometric connected-component wording repair is included.',
   'A basis of normals chosen from S supplies every shear Hom(X,K) and every elementary row addition on X. These generate the complete pointwise stabilizer of K. The m=1 case uses GL1(F2)=1; the K=0 case has r>=2, so the fixed space is exactly zero.',
   'Conjugating full radicals follows the contragredient action on normals. The normal closure is the full pointwise stabilizer of its actual fixed subspace. Taking the inverse image of the restriction image proves equality as a natural block subgroup, including all shears and the full quotient GL.',
   'Every submodule containing a vector outside K contains all shear differences K and surjects onto the irreducible quotient; it is V. This proves unique maximality, the large orbit, and independence from the initial full radical. Covector absence is equivalent to quotient dimension at least two and does not force K=0.',
   'The final application concerns geometric monodromy and geometric connected components after algebraic closure. It invokes the already fully audited actual odd-system full-radical theorem and no-covector theorem. No new full-image degree or main-gate closure is inferred.'
  ]),
 ('root_Lang_polar_irreducibility_audit', 'agents/obstructions_crystals/post_CP32_Lang_polar_irreducibility_candidate.tex',
  '4226990b44304d3d26f45f20faad1f14046806fbb502318106f105860ac20058',
  'independent re-proof', [
   'Entire four-label candidate actually read, including every proof and scope paragraph. Independently rederived the coefficient-square-root construction A(y)^[2]=B(y^[2]) and the actual Lang equation with its Euler-bundle scaling quotient.',
   'The parity classes prove q is nonzero. Its gradient is sigma^[2], with primitive coordinates, so q is squarefree. Square polynomial coefficients make the derivations commute and square to zero, also after adjoining the independent section parameters.',
   'An irreducible homogeneous factor f gives delta_i(f)=f L_i with linear L_i. Applying delta_s twice gives the polynomial identity delta_s L_s=L_s^2. Restriction to the actual Lang scheme makes L_s F2-valued and additive; section scaling makes it descend to the actual projective local system.',
   'When that covector is zero, unit Lang vectors span the actual Euler fibre. Thus the constant matrix D transpose preserves generic lines and is scalar. The pre-restriction polynomial identity and alternation then force the scalar to vanish, rather than merely vanishing after the Lang equations.',
   'The radical equation puts grad(f)=h sigma^[2]. Primitivity forces h polynomial, and homogeneity for a proper factor forces negative degree or h=0. Over the perfect field df=0 would make f a square. This proves irreducibility, including degree-one q, with no height-three or birationality hypothesis.',
   'The actual common wall supplies y=sqrt(lambda) with original B(y^[2]) of maximal rank and q(y)=0. Thus cancelling the Pfaffian gcd has not falsely enlarged the relevant maximal-rank locus. The affine-line solution torsor over the nonempty irreducible polar open is irreducible; the Jacobian in y is minus identity, so this incidence is etale, has dimension N, and dominates the section cone and then projective space.',
   'The geometric application uses previously audited common Cartier rank, outgoing odd-isogeny maximal dual rank, actual full-rank Euler open, invariant-covector vanishing and the common-wall theorem. Exceptional lower-dual-rank components remain open. No exact full-image degree is added.'
  ]),
 ('root_Lang_main_orbit_audit', 'agents/obstructions_crystals/post_CP32_Lang_main_orbit_candidate.tex',
  'd3637b2c6536b126b86c70ec2ee13eb59547ba15e8d7e0005a9386ca38268d80',
  'independent re-proof', [
   'Entire two-label candidate actually read and independently rederived from the actual local wall model, the polar theorem and the exact group structure. No finite computation is needed.',
   'At the strict-henselian generic common wall the stable rank is r-1. The special Lang points lift uniquely through their etale neighbourhoods, so integral Lang vectors form exactly the regular hyperplane H. Valuation extensions do not supply additional integral solutions: reduction and etale uniqueness identify any such solution with one of those lifts.',
   'For a pole vector y, choose a the inverse of a coordinate of minimum valuation. Then z=ay is integral with nonzero reduction, and M_s^t z^[2]=a z. Reduction puts zbar^[2] in the actual one-dimensional left kernel k lambda0. The original maximal rank of B(lambda0) makes a maximal minor of B(z^[2]) a unit, so B(y^[2]) has maximal rank generically.',
   'The normal-closure fixed subspace K lies in the wall regular hyperplane H. Thus every vector outside H belongs to V minus K, and also to the unique maximal-dual-rank component. That component is consequently exactly the large monodromy orbit, of degree 2^r-2^dimK.',
   'All other possible nonzero components lie in K and over lower dual rank. The proof establishes neither odd degree of the large component nor absence of the other components. Boundary contributions in a projective degree calculation have not been discarded.'
  ])
]
records=[]
for name, rel, expected, event_type, checks in items:
 p=w/rel
 assert sha(p)==expected, rel
 out=w/'outputs'/f'{name}.json'
 snapshot=w/'notes'/f'{name}.audited_candidate.tex'
 assert not out.exists() and not snapshot.exists()
 shutil.copy2(p,snapshot)
 labels=re.findall(r'\\label\{([^}]+)\}',p.read_text())
 labels=[x for x in labels if not x.startswith('subsec:')]
 rec={'status':'PASS','actual_utc':now,'reviewer':who,'candidate':rel,
      'candidate_sha256':expected,'labels':labels,'event_type':event_type,
      'read_scope':'Entire exact candidate, every numbered proof and scope paragraph.',
      'proof_checks':checks,'finite_computation':'None needed or executed.',
      'external_source_scope':'Direct symbolic proofs; no fresh external theorem is imported or newly attributed.',
      'executed_failures':[]}
 out.write_text(json.dumps(rec,indent=2)+'\n')
 records.append(rec)
 with (w/'notes/root_check_events.tsv').open('a',newline='') as stream:
  wr=csv.writer(stream,delimiter='\t')
  for label in labels:
   wr.writerow([label,now,who,event_type,'PASS: full written proof and exact scope checked; see outputs/'+name+'.json.'])
with (w/'notes/checkpoint33_changes.md').open('a') as stream:
 stream.write('\n## Root written audits of the polar, large orbit and radical group\n\nActual full audits passed at '+now+'. The polar argument removes the polar-irreducibility gate without a base-height assumption. The local pole calculation identifies its component as the unique large orbit; lower-dual-rank components remain unresolved. The root-authored group proof received a targeted author check in addition to its two independent companion audits. These statements do not add a new full-monodromy degree.\n')
print(json.dumps([{'record':r['candidate'],'actual_utc':r['actual_utc'],'status':r['status'],'labels':len(r['labels'])} for r in records],indent=2))
