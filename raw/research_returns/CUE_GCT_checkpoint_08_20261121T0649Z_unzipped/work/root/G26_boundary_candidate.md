# G26 candidate — nonrectangular first-row equality faces

Status at checkpoint07: candidate reduction independently checked by isolation,
but the full theorem and explicit constants have not been written or whole-read.
Do not treat this note as an integrated finding.

Parameters: n>m>=17, 4<=r<=m, a=n-m, nu partition ns with r positive parts
and nu1=as. Put mu=(nu2,...,nur), eta=nu-nur*1_r,
theta=mu-nur*1_(r-1). Then a>=2, n>=rm/(r-1), and mu1> s.

The padded parameter map injects degree-d coordinate functions into
Sym^(ad)(V*) tensor C[P_(m,r)]_d. By Pieri, if lambda1=ad then the sole
possible inner partition alpha is (lambda2,...,lambdar): the horizontal
strip of sizead must occupy every column. Its LR multiplicity is1.
Thus m_lambda(paddedper)<=m_tail(lambda)(per_m). The lower multiplicity
equals that in r-1 variables by highest-weight zero-last-coordinate
inheritance; state and prove this explicitly, rather than silently
changing ambient spaces. Background: supplied Bump–Gamburd source
acp20.tex, equation label e:pieri, lines404–422; source itself cites
Macdonald I(5.16),p73 and Bump Theorem42.4.

Compare determinant enhanced invariant algebra A with lower permanent
enhanced algebra B. For r>=5,
u=(r-2)n²-r²+3+r_eta,
v=(r-1)m²-2m-r²+2r+2+r_theta.
For r4 bound by full ternary ambient enhanced algebra with
v=binom(m+2,2)-8+r_theta. The flag difference
r_eta-r_theta=#{j>1:nu1>nuj}>=0. Using n>=rm/(r-1), the G24 inequalities
give u>v in both cases.

For period1 and exact quotient dimensions, R28 gives a free stable point
for A with degree n,size n-1,rowr and original directionnu: nu1=as>s.
For B use degree m,size m-1,rowr-1,directionmu: mu1>=ms/(r-1)>s.
The smaller padded permanent embeds into per_m by block diagonal padding.
For r4 it also embeds into the full ternary ambient space. Each algebra
separately has gcd1 degree semigroup. No common invariant is required
between different groups.

Prospective effective constants: q=r-1;
b_D=binom(binom(n+r-1,r-1)+s-1,s)*dimS_eta(C^r);
b_B=binom(binom(m+q-1,q-1)+s-1,s)*dimS_theta(C^q);
b=max(b_D,b_B); L=ns+(r-1)|eta|; p=ns+|eta|;
beta=ceil(3r²b/8)*L^(2(r²-1)); T=binom(b+beta,b)-1; E=r*T*beta!.
These dominate the smaller group's generator and parameter degrees
since |theta|<=|eta|. The G24/G23 sandwich should yield strict
determinant dominance for every j>=E[4v(pE)^(v-1)+1]. Verify all
graded-ring, source and parameter conventions in the full proof.

Isolation verbally checked the entire reduction, inheritance caveat,
stable-point hypotheses and dimension inequalities before checkpoint07.
Root has not yet written the final theorem, dictionary or check event.
