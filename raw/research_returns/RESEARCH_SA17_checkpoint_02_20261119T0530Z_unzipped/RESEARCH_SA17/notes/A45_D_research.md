# A.4, A.5 and D research log

Run: GPT-6 Astra, OpenAI, RESEARCH_SA17-20261119.

## 2026-11-19: cote 127 Lemma 1.3

We read K127-01_transcription.tex lines 18--76 and the prior study lines 410--421.
A complete proof has been derived, stronger than the finite/finite-presentation alternatives: Artinian A, retrocompact U, schematically dominant Y prime to Spec A suffice for existence. The key is universal injectivity of the given flat closure, not arbitrary non-flat module descent. On an affine chart choose finite principal opens covering U. Their sections form a flat A-module C. Set G=image(F to C), Q=C/G. After a schematically dominant affine test B, G prime injects universally into C tensor B, so Q tensor B is B-flat. Stacks Lemma 10.101.7 (section tag 051E), opened in full, gives Q A-flat. Thus G A-flat and the image commutes with all base changes. This proves the universal separating condition and the comparison. Finite presentation descends as well by faithfulness of tensor with B over Artinian A, plus Tor vanishing from G A-flat.

The Stacks source was opened at https://stacks.math.columbia.edu/tag/051E, Lemmas 10.101.1--10.101.7. Other opened sources: tags 05PA,05LJ,0ASZ; the latter sources were explored but are not needed for the simple proof.

## Cote 128 Lemma 1

We independently derived the additive versus logarithmic connecting maps: dlog(u)=u^{-1} delta(u), so the square in scan21 is generally not a commuting square of cohomology boundaries without an additional argument. This is not yet a refutation of the claimed canonical isomorphism.

Program code/A4_amitsur_search.py enumerated 65 truncated monomial subalgebras A of F2[x]/x^N for 2<=N<=8 and 221 nonempty monomial square-zero ideals I. No unequal additive/log boundary subspaces were found. The search only covered this explicit family; it is not evidence of general truth. Output logs/A4_amitsur_search_8.json, runtime 0.1262 seconds.

## A.5 preliminary source search

Springer Raynaud LNM119 table of contents and chapter XI metadata opened, but chapter text not yet available. Primary secondary citations identify XI.1.4 for integral geometrically unibranch bases, XI.1.13 for normal bases. No theorem is yet labelled Known on the basis of these citations alone.

## A.5 settled in relative ample-bundle sense

Conrad, *Higher-level canonical subgroups in abelian varieties*, Lemma 3.2.1 p18 was opened in full. It asserts exactly polarization for abelian schemes over normal locally noetherian bases. Its proof extends a generic polarization using Weil extension and checks positivity by specialization to DVRs. Poincare pullback then gives a global relatively ample line bundle. Milne, corrected original *Abelian Varieties* chapter (2022-01-02), Remark7.3 and Theorem13.3(c), opened, supply cube very ample and higher cohomology vanishing, yielding embedding in P(f_*L^3). No global fixed rank bound is valid on disconnected non-quasi-compact bases. The original131 scan17 was viewed. Correspondence representability alone cannot extend generic sections, as D(t)->Spec k[t] proves; the abelian Hom extension and positivity are the required inputs.

## Expanded A.4 finite search

`A4_amitsur_random.py` permits nonmonomial subalgebras of F2[x]/x^N and principal square-zero ideals. Seed1729, 2000 generation attempts per dimension3..10, deduplicated to498 tests. No unequal boundary subgroups found. Full output retained. This is evidence only. The general characteristic-two case and the GL_m theorem remain active.

## D.1 / L10: complete corrected formula and explicit failure without irreducibility

D.tex now contains the trace/mobile comparison, the rank formula including all reducible-component contributions, the inverse-intersection-matrix local correction, component-group interpretation with sign, the Shioda height formula, and the primitive NS specialization. Original130 scans14 and15 were viewed: rho(Y)-2 is clear, and the irreducibility hypothesis is explicit. The rank uses |Z|=H², not the number of singular members (the ink gloss is potentially misleading). The quotient polarization is canonical as a rational polarization mu^(-1), where mu=q lambda^(-1) q^vee on J' dual. An unspecified integral polarization can rescale the claimed equation.

Sources opened: Pepin2012 Theorem2.2.1 and Corollary2.2.2 (pp1323-1324), Theorem4.1.1(p1342), SGA7IX1.2.1 online text, ConradTrace Theorems6.4 6.12 7.1, MilneAV Theorem3.1 and Corollary3.8. Shioda1990 original scanned p228 was viewed (Theorem8.6, equations8.11-8.13). Shioda1992 author-uploaded full text Theorem2.4 was opened; its zero-trace hypothesis is handled by a separate proof, not silently omitted.

Positive-genus counterexample: E:y²=x³-x, X=E×P1, H=(3O,1); pencil yu+xv+t((x+2)u+(y+1)v). Six transverse basepoints and six reducible one-node fibres; generic curve E, mobile J'=0. Exact singular parameter polynomial -t(7t^5-15t^4+13t^3+t²-6t+1) has discriminant -101056167, hence six distinct roots, none±1. Rank without corrections is6; corrected rank0. Script and output attached, together with conic pencil check.

## A.4 additional search families and outcomes

Exact multivariable subalgebra search: 2634 tests in F2[x,y]/m^4, then1158 in F2[x,y]/m^6, with principal square-zero ideals. The latter includes2 cases with nonzero additive connecting image; both logarithmic images equal it. Closed-cover search A'=product A/K_i with A=F2[x_1,...,x_r]/m^d, I=m^ceil(d/2): (r,d)=(3,4),2847 tests,198 nonzero; (4,4),9947 tests,399 nonzero; (3,6),9292 tests,1140 nonzero (ranks1,2,3), all equal logarithmic images. Scripts retain exact relation-space computations and enumerate all invariant units; no floating point arithmetic. No general conclusion follows, and no actual Amitsur counterexample has yet been found.

## A.4 breakthrough: actual Amitsur counterexample to the canonical comparison

The earlier gate is now resolved for the asserted canonical construction. Let R=F2[x,y], A=R[a,b]/(a²,b²), I=(ya+xb), A prime=A_x times A_y. The square-zero ideal sheaf on the punctured plane is free on epsilon=ya+xb and ab. Its H1 has independent e=[epsilon/(xy)], f=[ab/(xy)]. The equalizer B=A; after reducing moduloI the equalizer C0=R[t]/t², with a=xt,b=yt, and imB=R+(x,y)Rt. Every r+st=(r+1)+(1+st) proves the exact units-plus-image hypothesis. The full additive boundary is F2e; the full logarithmic boundary is F2(e+f), since every unit is1+st and its boundary equals se+s²f=s(0,0)(e+f). Thus the canonical square-zero map is not well-defined on the two kernels. An explicit multiplicative coboundary maps to the nonzero additive class[ab/(xy)]. The original scan20 says canonical isomorphism; scan21 supplies the square-zero comparison. We do not claim these two infinite-dimensional F2 vector groups are abstractly nonisomorphic.

Exact symbolic certificate code/A4_cech_counterexample.py verifies I²=0, the ideal multiplications, the generic Laurent identity with indeterminate s, the nonzero additive Laurent class, and distinct two-dimensional boundary subspaces. It additionally checks all1024 polynomials of total degree<=3 for the evaluation-at-origin rule; the written monomial proof covers all degrees. Output logs/A4_cech_counterexample.json. The original128 scan20 was viewed again.

This example has A prime not finite and A not semilocal. It does not settle the later finite semilocal theorem. The vanishing equivalences there remain active; a known Venken1971 counterexample to effectiveness for Artinian local finite morphisms may be a useful test, but its primary statement has not yet been opened.

## A.4 finite theorem repaired in full

The failure of the canonical comparison does not destroy the finite semilocal theorem. At each radical step I=m^n/m^(n+1), H=H1(IC) is a finite-dimensional residue-field vector space, and the additive boundary is a derivation delta:D→H from D=C0/mC0, a finite-dimensional residue-field algebra. Matrix kernels are affine orbits h↦ghg^(-1)+delta(g)g^(-1). The stabilizer at0 is GL_r(S), S=kerdelta. If delta is onto, dimension makes the orbit open; after algebraic closure the constant Levi fixes0, so the orbit is an orbit of1+Mat(radD), hence closed by Kostant–Rosenlicht (MilneAG2022 Theorem17.64 p374 opened). It is all of affine space. Torsor descent over the finite Artinian algebraS brings solutions back to the original residue field. Conversely, density treats infinite residue fields, while finite-field cardinalities (Dred=Sred because D^p⊂S) treat finite ones. This proves all fixed finite-rank vanishing equivalences.

For arbitrary rank, a new finite algebra argument removes the only remaining gate. Reduce S by its radical to the caseS=k, then delta:radD→H is a linear isomorphism. Gauge equations use a fixed finite family R_i of coefficient operators onradD. The finite-rank result says1−sumR_i tensor a_i is invertible for every finite matrix substitution. Block-cycle substitutions force every word inR_i nilpotent. A full nil-semigroup proof is included: the positive-word ideal in the finite algebra generated byR_i lies in its Jacobson radical, using the elementary density theorem and trace-one matrix unit; hence it is nilpotent. This is exactly the Levitzki-type argument, not the false assertion that arbitrary sums of nilpotents are nilpotent. Uniform nilpotence makes the inverse a finite polynomial for all column-finite infinite matrices. Lift successively throughradS. Scalar-extension descent gives the arbitrary-field result. Therefore all flat modules descend in theorem(a).

For(b), additive cohomology vanishes by Krull intersection. Matrix trivializations over all radical quotients form an ML system: equalizer-ring images stabilize as Artinian submodules; their GL images stabilize because transition kernels are nilpotent, and trivializer images are nested cosets. Compatible trivializers exist over the completion. Invariant modules are finite and commute with faithfully flat completion, which then descends finite flat effectiveness. For(c), forget the extra flat-base-change algebra action, descend the underlying flat module, descend the action by full faithfulness, then prove its flatness over the new algebra by the nilpotent-base fibre criterion; the Tor proof is written.

Root independently targeted-checked D:fixed, D:quotient-polarization, and the elliptic specialization, and reported no gaps. This was a targeted proof check, not a new re-proof. In exchange I checked A_gluing's local-isomorphism quasi-compactness lemma and its arbitrary-test representation argument and found them valid.

## Final normalization and scope checks

The original128 scans26 and30 were rendered and viewed for the finite semilocal theorem. Its three parts are all proved in A4:finite-descent-theorem. The historical open-gate notes above are retained as the research sequence, not the current status. The current A.4 gate is closed, subject to targeted review of the supplied proof.

Two additional exact multivariable search runs completed: F2[x,y]/m^6 with maximal square-zero ideal,3111 tests including20 nonzero boundary images; with two-generator ideals,3643 tests including16 nonzero images. Neither found unequal boundary subgroups. Their outputs contain progress lines followed by the complete final JSON object; they are search records, not pure single-object JSON files.

D:height now explicitly derives the canonical-height sign. Lang, Bourbaki274, p435 gives the product-formula-field scope and uses log absolute values; pp440-441 define the global symbol and Theorem5 with its corollary. The corollary, after changing to positive order, identifies the Pic0 symbol with canonical linear height. MilneJV Lemma6.9 and Remark6.10(c), p23, give a*lambda=-id; Summary6.11p24 repeats it. Both Milne pages and Lang pp440-441 were rendered and viewed, since extraction drops the autoduality minus sign. Hence the degree-zero classQ pulls back from -lambda(Q), making the curve global symbol minus the theta bilinear height. The diagonal is2hhatTheta. D:fixed was also made fully typed, including the same minus sign in the dualized Albanese factorization.

Targeted checks of root sections: A:ind-thickening was checked earlier for transition directions, the one-residue local stabilization, conditions1-7, the generic modular point and failure at every closed point, and nonrepresentability locally of finite type. A:localiso-qc and A:local-to-global in A_gluing.tex were checked for finite generic branches and the extension/comparison of local sections on arbitrary test schemes. No gap was found; these are targeted proof checks, not separate re-proofs.

## Stronger result: every positive characteristic, and correction of R2

A4:all-primes strengthens the characteristic-two example. Over F_p take A=F_p[x,y,a,b]/(a^p,b^p,(ya-xb)^2), I=(epsilon=ya-xb), A prime=A_x times A_y. On D(x), t_x=a/x gives A_x=R_x[t_x,epsilon]/(t_x^p,epsilon²), and on D(y) t_y=b/y; t_x-t_y=epsilon/(xy). Thus C0=R[t]/t^p and I on the punctured plane is free on t^j epsilon for0<=j<p. In H1 put e_j=[t^j epsilon/(xy)]. Full additive boundary is the hyperplane c_(p-1)=0; full logarithmic boundary is c_(p-1)=c_0. The latter follows from u'/u and Frobenius on the roots of u, plus injectivity and cardinality of1+tF_p[t]/t^p. The multiplicative coboundary with reduced unit1+t has square-zero image e0-e1+...+e_(p-1), not an additive boundary.

This actually refutes the supplied R2 assertion that the lemma is fine in odd characteristic: p=3 has2 invertible. It does not affect the independent finite semilocal vanishing theorem, whose proof never used equality of the boundary subgroups. In the all-prime version B need not equal A; the proof computes only its image in C0, namely R plus the (x,y)-multiples of t,...,t^(p-1).

Certificate code/A4_all_primes_boundary.py enumerated all27 coefficient polynomials and9 normalized units for p3, all3125 and625 for p5, and the p2 case. Both full boundary images, the dlog(1+t) witness, the binomial local-coordinate relations, and the truncated derivation identity were checked exactly. Output logs/A4_all_primes_boundary.json. These finite enumerations certify the coefficient calculation; the infinite actual rings and every-prime claim are treated by the written proof.

A second requested targeted proof check of A_gluing.tex again found no gap. It specifically checked irreducible locally closed strata, open-and-closed branch equalizers over nonreduced bases, finite fibres of R from noetherian V_{S_b}, and local branches for arbitrary test schemes. An independent proof of separated etale finite-fibre quasi-compactness was also sent to root; root located Stacks0BB6 with086R and07RY.
