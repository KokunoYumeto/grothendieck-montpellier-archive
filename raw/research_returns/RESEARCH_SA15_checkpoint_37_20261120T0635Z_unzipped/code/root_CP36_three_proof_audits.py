"""Retain three complete root proof audits and unchanged isolated exact reruns."""
from pathlib import Path
import csv,datetime,hashlib,json,re,shutil,subprocess,sys,time
W=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
reviewer='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root'

def audit(name,candidate,expected,checks,source_scope,programs=(),source_files=()):
    candidate=W/candidate
    assert sha(candidate)==expected,(name,sha(candidate))
    out=W/'outputs'/('root_'+name+'_audit.json')
    snap=W/'notes'/('root_'+name+'_audited_candidate.tex')
    assert not out.exists() and not snap.exists()
    shutil.copy2(candidate,snap)
    runs=[]
    for code,codehash,outputhash in programs:
        source=W/code; author=source.with_suffix('.output.json')
        assert sha(source)==codehash and sha(author)==outputhash
        folder=W/'code/audit_snapshots'/(name+'_root_independent')/source.stem
        assert not folder.exists();folder.mkdir(parents=True)
        copy=folder/source.name;shutil.copy2(source,copy)
        start=time.perf_counter()
        run=subprocess.run([sys.executable,str(copy)],cwd=W,capture_output=True,text=True)
        wall=time.perf_counter()-start
        (folder/'stdout.txt').write_text(run.stdout)
        (folder/'stderr.txt').write_text(run.stderr)
        independent=copy.with_suffix('.output.json')
        assert run.returncode==0,(code,run.stdout,run.stderr)
        a=json.loads(author.read_text());b=json.loads(independent.read_text())
        omitted={'actual_utc','runtime_seconds','coefficient_reconstruction_seconds','peak_rss_kib'}
        mathpart=lambda x:{k:v for k,v in x.items() if k not in omitted}
        assert a['status']==b['status']=='PASS' and mathpart(a)==mathpart(b),(code,'mathematical output mismatch')
        assert sha(source)==codehash and sha(author)==outputhash
        runs.append({'author_program':code,'program_sha256':codehash,'author_output_sha256':outputhash,
          'independent_program':str(copy.relative_to(W)),'independent_output':str(independent.relative_to(W)),
          'independent_output_sha256':sha(independent),'runtime_seconds':b['runtime_seconds'],
          'subprocess_wall_seconds':wall,'all_mathematical_output_identical':True,
          'author_bytes_unchanged':True,'counts':b.get('counts')})
    assert sha(candidate)==expected
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    labels=re.findall(r'\\label\{([^}]+)\}',candidate.read_text())
    r={'status':'FULL-INDEPENDENT-PROOF-CODE-PASS' if programs else 'FULL-INDEPENDENT-PROOF-SOURCE-PASS',
       'actual_utc':now,'reviewer':reviewer,'candidate':str(candidate.relative_to(W)),
       'candidate_sha256':expected,'labels':labels,'full_candidate_read':True,
       'proof_checks':checks,'source_scope':source_scope,
       'source_files':[{'path':p,'sha256':sha(W/p)} for p in source_files],
       'isolated_runs':runs,'executed_failures':[],
       'retention':'Full frozen candidate copied; all executed programs, complete outputs and streams retained. No author output overwritten.'}
    out.write_text(json.dumps(r,indent=2)+'\n')
    with (W/'notes/root_check_events.tsv').open('a',newline='') as f:
        wr=csv.writer(f,delimiter='\t')
        for label in labels:
            wr.writerow([label,now,reviewer,'independent re-proof / computation or formal certificate',
                         'PASS: full written proof and exact conventions checked; '+str(out.relative_to(W))])
    print(json.dumps({'name':name,'status':r['status'],'actual_utc':now,'labels':len(labels),
                      'runs':[x['runtime_seconds'] for x in runs]}),flush=True)

audit('odd_Cartier_evaluation','agents/obstructions_crystals/post_CP35_odd_Cartier_evaluation_candidate.tex',
 '85858ad8cd397209af2b7e1d3b833c4ecee0ac5fa529928c46de99ddedba7acb',[
 'The entire five-label candidate was read. B is the relative Frobenius twist, H is L^(2), and F^*H=L^2; H is not L^2 on the original surface. GRR gives c1(F_*L)=2H and slope N. The already fully audited odd-Euler-characteristic stability proof applies to every odd N, not merely N=3.',
 'For effective D with positive square, nefness and Hodge index give ampleness, then abelian Riemann--Roch gives D^2=2h0(D). For D^2=0, every component is an elliptic translate and zero intersections force one elliptic quotient; h0(D) is its base degree. Global generation forces degree at least2 on every elliptic fibre. Thus h0(D)>=N implies D.H>=2N in both cases.',
 'The actual theta group has a Lagrangian decomposition because N is odd in characteristic2. For central weight r prime to N, the second level subgroup permutes the N character spaces of the first simply transitively; the common multiplicity proves dimension divisibility and irreducibility in dimension N. The action on F_*L has weight1 over F(K(L)), while the action on H has weight2 and commutator e_L^2.',
 'Saturation is theta invariant. In ranks1 and2 the nonzero exterior evaluation map has weight q coprime to N, so the determinant has at least N sections and intersection at least2N. This contradicts strict stability, which gives intersection<qN<=2N. Reflexive determinants extend the sections across the finite singular set.',
 'For nonordinary A the finite-flat Cartier pairing on F_*L is perfect and alternating on every bundle fibre: Cartier of an invariant top form is zero. A zero global beta would make the generic evaluation image isotropic of rank<=2, contradicting the preceding rank>=3. The nonzero weight2 target has dimension N and is irreducible, proving beta surjective.',
 'If the evaluation saturation has rank3 and gcd(N,6)=1, D=detQ has weight3 and at least N sections; J=(E/Q)** has weight1. The Frobenius-pulled quotient of the canonical unipotent bundle is a quotient line off a finite set. On every normalized curve its image is Jprime(-Z), a quotient of a degree-zero semistable unipotent bundle, so Jprime is nef. Thus F^*J=L tensor Jprime is ample, and J is ample. This is a proof of ampleness rather than an assumption about quotients of F_*L.',
 'The two divisor bounds and c1(E)=2H give D.H=J.H=2N. Ampleness of J gives J^2=2h0(J)>=2N; Hodge index gives the reverse inequality. Equality makes J numerically equivalent to H. The standard divisor equivalence theorem gives a torsion class in NS for a numerically trivial line, and AV7.23/7.25 show this NS group has no torsion. Thus J/H is in Pic0. Only J, not D, was required to be ample.',
 'A Pic0 twist has commutative theta extension and does not change the kernel commutator. Therefore the actual weight1 action on J gives e_J=e_L whereas J/H in Pic0 gives e_J=e_H=e_L^2. These force e_L=1, contradicting nondegeneracy for N>1. The conclusion is generic rank4, not everywhere global generation, and neither maximal individual contraction nor full monodromy is inferred.'
 ],
 'Fresh retained original AV full proof passages7.21--7.26, printed105--108, and8.24--8.28, printed121--123, were opened and read in this audit. Full AV8.19/8.20 and the odd stability/elliptic-divisor dependencies were already read in the retained primitive-type(1,3) audit. No numerical experiment is needed or claimed.',
 source_files=['agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt'])

audit('B97','agents/reduction_descent/B_irreducible_point_field_layers_candidate.tex',
 '964d658fac540f02d87163941e0076b7321c5e71513e467f46f80124c26be9ae',[
 'The complete six-label candidate and complete standalone checker were read. All fields are the actual common point fields of the supplied p^3 comparison, all residue fields are algebraically closed, and all lower valuations are normalized on the displayed field. Conductors mean last upper breaks without the extra Artin-conductor1.',
 'Since first-level points are L-rational, E/L and T/E are Galois translation extensions of degree at most p^2. The primitive coordinate denominator forces E/L degree>=p and T/L degree>=p^3. If E/L=p, then T/E=p^2 and v_T(Pplus)=p-1. The prime-to-p fixed-coefficient equality makes the two full first-level leading maps scalar proportional. The actual residual isomorphism of unequal finite characters has Frobenius orientation, impossible on F_(p^2). Thus E/L=p^2 for every nonzero residual vector, and W1v=F_p^2.',
 'The literal identity (1+pA+p^2B)^p=1+p^2A modulo p^3 gives W1 subset W2 in the same coordinates. Terminal translations consequently give all p^2 conjugates over every E; T/E has degree p^2 and T/L degree p^4. No Galois assertion about general T/L is used.',
 'If dimW1=2, the evaluation map is bijective. Every primitive point stabilizer lies in the central terminal subgroup, hence is normal, so this particular T/L is Galois of order p^4. Here E=F2, U=Gal(T/E) has order p^2 and the actual pth-power map is onto U. This supplies the hypotheses of the complete written two-level argument without assuming a Cartan or abelian image.',
 'For that two-level argument the selected coordinate valuations are A=p(p-1), D1=p^2 A and D2=p^4 A, below v_T(p)=(p^2-1)D2. Every terminal nonidentity is a pth power and has break larger than the minimum break. Off the boundary a0=(D1-A)/p, the fixed first ordinary coefficient controls all terminal displacements and makes the two full terminal maps scalar proportional. At the boundary, any nonzero coefficient at j0=D1-a0 likewise forces the same contradiction; if both coefficients vanish, all nonterminal elements have break a0 and their full quotient maps are scalar proportional. Both possibilities contradict Frobenius orientation. Thus dimW1>=3.',
 'In each elementary-abelian point extension, a single lower break below b0=(D-A)/p would make the q-1 distinct leading coefficients roots of one degree p-1 polynomial; a break above it makes the full two leading maps scalar proportional. With two breaks t<u, t<b0 and the first ordinary degree is J=A+(p-1)t; its unique last displacement gives u+(p-1)t=D-A. Quotient averaging gives largest cyclic break b0. Hence c1=(p^2-1)(p-1) and c2=(p^4-1)(p-1) exactly, including absent-coefficient boundary cases.',
 'For an actual basis of p^2 points, F2=E1E2. Their cyclic characters span the character space of this elementary-abelian compositum, so its largest conductor is exactly c1. For their primitive lifts, US_i=H_i identifies F2 intersection T_i with E_i and [F2T_i:F2]=p^2. The fixed group of F2T_i is U intersection S_i; it is normal. On H_i both [A,C]v_i and Av_i vanish, so commutators and pth powers vanish in this quotient. Thus the relative compositum over E_i is indeed elementary abelian.',
 'For upper u>c2 in Gal(F2T_i/E_i), its image in Gal(T_i/E_i) is trivial and its intersection with Gal(F2T_i/F2) is trivial because the two fields generate. The actual subgroup formula bounds the latter conductor by psi_(F2/E_i)(c2)<=p^(r1-2)c2. The two actual primitive columns generate F3, so all terminal characters satisfy the same bound. This uses actual composita, not assumed independent field extensions.',
 'If W1 is traceless, dimW1>=3 makes W1=sl2. The determinant is cyclotomic on the good field and forces mu_(p^2) subset L. The previously audited arbitrary-residue Cohen/cyclotomic lemma then supplies a cyclic mu_(p^3) field of break (p^2-1)^2. Since this exceeds c1 it is disjoint from F2, and its restriction has conductor psi_F2/L(N^2)>p^3(N^2-c1). The exact positive difference from p*c2 is pN(p-1)(p^3-p^2-1), contradiction.',
 'If r1=r2=3, the common matrix space is a normalized Lie subalgebra. With nonzero trace its intersection with sl2 is a nonabelian2-dimensional algebra: a traceless nonzero matrix centralizer intersects sl2 in a line. Its derived generator Y satisfies [X,Y]=Y; traces of this and [X,Y^2]=2Y^2 imply nonzero nilpotence. Its kernel is invariant under the irreducible tame normalizer, contradiction. Thus the only remaining shapes are traceful(3,4) and(4,4), of orders p^7 and p^8.',
 'The full exact checker enumerates all stated planes and hyperplanes, checks literal pth powers, fixed-coefficient inequalities, boundary cases and exact quadratic-field Frobenius. These support the written all-prime proof but do not infer realizability or an unrestricted least-index equality. The author program and output remain unchanged in the isolated rerun.'
 ],
 'The root previously fully audited the B79/B80 actual-coordinate and orientation arguments, B81 two-level proof, B86 arbitrary-residue cyclotomic lemma, and Colmez3.7/3.10/3.13 subgroup and quotient proofs. This audit rederives every new actual-field use in the full written B97 candidate. No new external source opening is claimed.',
 programs=[('agents/reduction_descent/code/verify_irreducible_point_field_layers.py','758c777b798239142ac89e00ce56b9b4f34eb70db847fc86bd3bfcd096ec8568','6fce30e83dc8af1cbfe8c89d287993cf3ef0af440656f996e1af46da7c549d71')])

audit('prime_Heisenberg_rank','agents/monodromy/post_CP35_prime_Heisenberg_rank_candidate.tex',
 '1a03b3733ace0faf2b6e4419b2a079e9439fb95699deb3be386258564ed4c59d',[
 'The entire six-label candidate and all three complete programs were read. Clock equivariance forces output(i+j)/2; shift equivariance forces dependence on i-j. The dual alternating matrix B_y and generally nonalternating M_s have the displayed distinct indices and satisfy B_y s=0 iff M_s^t y=0.',
 'Every Pfaffian coefficient is reconstructed by all perfect matchings with parity cancellation in F2. Each nonempty coefficient support has a literal y coefficient that becomes exactly one surviving c monomial; that coefficient cannot vanish anywhere on that support torus over any characteristic2 field. The smaller-prime tuple expansion and prime17 four-bit expansion have no carry because each exponent<=8. The complete prime17 reconstruction has2027025 matchings,1465345 surviving monomial terms and43263 y coefficients, and all255 supports are covered.',
 'For a degree-p division algebra, every closed point degree on its SB variety is divisible by p: a splitting field E gives the D-module E^p whose F dimension p[E:F] is divisible by p^2. Graph classes on split P^(p-1) have coefficients a_i with a0=1. The standard product classes compose as orthogonal idempotents. Taking the(p-1)st composition and diagonal refined pullback gives a zero-cycle degree sum a_i^(p-1). Modulo p this counts nonzero coefficients, between1 and p and divisible by p, hence all coefficients, including the opposite multiplicity, are nonzero. This proves dominance without separability or resolution.',
 'The two projective Heisenberg actions have scalar cocycles in ratio-2. For explicit signs, with S shift,C clock, roots A^p=a,B^p=b and descent conjugations AdS,AdC, the invariant matrices X=A C and Y=B^-1 S have X^p=a,Y^p=b^-1 and XY=zeta YX. Thus the weight1 Brauer class is a nontrivial cyclic symbol, up to sign, and weight-2 has class-2alpha. Over k(a)((b)) the cyclic algebra has valuation min_i(v_b(l_i)+i/p), with a unique minimum and multiplicative nonzero leading term. It is division of degree p.',
 'After twisting, the source SB class-2alpha splits over the function field of the target SB class alpha. Since that field is infinite, a rational point can be chosen in the nonempty domain of the descended map, yielding a composable reverse rational map. The composite is a rational self-map of a division SB variety and is dominant by the preceding elementary argument. Therefore the original equivariant map is dominant. No arbitrary maps through indeterminacy loci are composed.',
 'For the Pfaffian radical map, the fibre over s on the dual rank open is exactly the open subset U intersection P(ker M_s^t). Dominance in equal dimensions makes the generic fibre zero dimensional; a projective linear kernel with a nonempty open of dimension0 is a single point, so M_s has rank p-1. Kernel minors define an actual rational inverse, proving birationality and excluding a hidden purely inseparable extension.',
 'A common Pfaffian divisor has a one-dimensional Heisenberg-invariant span, hence a character trivial on the commutator centre. The scalar weight on the dual variables is plus or minus2 according to action convention; either convention forces p dividing2deg(g). Since deg(g)<p, it is constant. This gives codimension at least2 for dual rank drop; no unsupported height3 claim is made.',
 'The direct multiplication-minor program for3,5,7,11 is supplemental only. The argument for13 and17 uses the universal Pfaffian support certificate plus the complete SB and linear-fibre proof. No assertion of Euler generic invertibility, a good common wall, Lang connectedness, or full geometric degree17 monodromy is inferred.'
 ],
 'Fresh original2009 Karpenko preprint at https://www.math.uni-bielefeld.de/lag/man/333.pdf: complete Lemma2.21, Corollary2.22, Definition/criterion2e, Lemma2.23 and Corollary2.24, printed9--10; root webref turn183739581view0. Fresh original https://sites.ualberta.ca/~karpenko/publ/aoinew.pdf: complete correspondence preliminaries1.2--1.9 and Theorem2.1 proof with Corollary2.3, printed2--5; root webref turn226811638view0. The prime-degree proof is supplied directly and does not import the external Proposition2.2 or the characteristic restriction from orthogonal involutions.',
 programs=[
 ('agents/monodromy/code/post_CP35_prime_Pfaffian_support_certificates.py','c14ba47ef27ae745a688b8141d3ceed67bca874b470dd9e3d834c134c1c532ac','a4f4fd3ef4ce350a6d2d78433a8ffc7dbfed601fa8d56655dec1bed6fe096988'),
 ('agents/monodromy/code/post_CP35_prime17_Pfaffian_support_certificate.py','bfd084d2aa0d7313597b966e7856d0e1bd2f90dad89c07819bc6314dd97a3505','1baf8e2da9a6b10768478d17543aed206c0658d44d34499a81e005df9e001424'),
 ('agents/monodromy/code/post_CP35_prime_multiplication_minor_probe.py','0332b4482f3c570dfd647a595203f2eeaa61118d0b00a7df86c054ee0f5c6550','2613dff7402b94b3d36c6ffcfc604af74e69793d50d33a2000b12e3f04aa32ab')])
