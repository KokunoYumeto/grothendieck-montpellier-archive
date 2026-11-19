# Independent checks for cote 93, scans 73–91

These are new checks made in this audit, not inherited check events. A calculation can establish that a displayed transcription is mathematically inconsistent; it cannot decide whether the manuscript, Pro, or Codex contains the error. All local analytic assertions below concern smooth complex curves unless another base is stated. The earlier run’s nilpotent-model ideas remain labelled as its ideas.

## 1. Quotients, locality, and the connection convention

On a coordinate disc, every holomorphic one-form has a primitive. Consequently `d: O -> omega` is locally surjective and its kernel is the locally constant functions. The difference `dg-df` is an additive cocycle. Equality of two such differences means `g-h` is constant; a common initial value makes it zero. This proves C-SA04-205. It does not prove surjectivity on global sections of an arbitrary curve.

If `E` denotes local coordinates, `df` must be a frame. With f fixed, the form `-df` cannot equal `dg-df` for g in E, since it would imply `dg=0`. This refutes the Pro reading of scan 75, lines 1033–1034. The Codex reading has O in that position and is true. The correction on scan 76 replaces the additive range by the frame torsor and uses `dg/df`; a prescribed unit u is attained locally by integrating `u df`, whose derivative is nonzero. The two source witnesses must therefore remain distinct in the historical conclusion.

A frame f of a line bundle defines a unique connection `D_f` making f horizontal. If `g=u f`, the Leibniz rule gives

\[
(D_g-D_f)(f)=-u^{-1}du\,f.
\]

Thus the difference is **minus** dlog u. Conversely a connection in a frame is solved locally by a nonzero horizontal frame using an exponential of a primitive. This proves the local quotient `L*/C* = Conn(L)`, with the sheaf of locally constant scalars understood. The positive dlog cocycle is itself valid; only its naming as `D_g-D_f` is inconsistent with the horizontal convention. No silent change to the manuscript’s convention is made.

For the quotient by translations and scalings, a local coordinate f gives the horizontal-frame connection `D_df` on omega. Two such coordinates give the same connection exactly when `dg/df` is locally constant, hence `g=af+b`. This proves the local affine quotient. Ordinary connections on a complex curve are flat because two-forms vanish; existence of a global horizontal frame is still a separate issue.

The vector `g/dg` is invariant under multiplication of g by a constant. If it equals `h/dh` near a point where g and h are nonzero, then `dlog g=dlog h`, so g/h is constant. Equal nonzero initial values give equality. At a common zero, t and 2t violate that conclusion. The vector zero is never the image of a local coordinate, so the author’s surjectivity objection is valid. Restriction to nonzero coordinates gives `dlog g` in the frame torsor, and `g'/g=1/phi` is solved by `g=c exp(integral dt/phi)` when phi never vanishes. These are local statements.

## 2. Exact differential identities and counterexamples

The saved program `programs/b_computations.py` uses exact symbolic arithmetic. Its output `outputs/b_computations.json` records zero residuals, named counterexamples and exact matrices. It does not make note verdicts or select source readings.

Use the manuscript normalization

\[
G(t,f)=-2\frac{f'''}{f'}+3\left(\frac{f''}{f'}\right)^2=-2S_t(f).
\]

For a frame `f(dt)^n`, with n a nonzero integer, a horizontal n-th root induces a connection with coefficient `lambda=-f'/(nf)`. Substitution in `2lambda'+lambda^2` gives

\[
c_n(f)=-\frac{2}{n}\frac{f''}{f}+\frac{2n+1}{n^2}\left(\frac{f'}{f}\right)^2.
\]

Changing the root multiplies it by a locally constant n-th root of unity; changing its primitive adds a constant. These are affine changes and do not change the induced projective structure. The construction therefore exists sheaf-locally over C. In a real category, even roots require a sign choice or a positive frame; in characteristic dividing n, this argument is unavailable.

The mixed expression is the difference of two projective coefficients. This proves its cocycle by cancellation, and direct substitution proves `c_(nr)(f^r)=c_n(f)` for nonzero r. The coefficient with no n remaining is the specialization n=1. Substitution of `f'` for the frame coefficient gives `c_1(f')=G(t,f)`.

Under variation of the line connection by `eta=h dt`,

\[
2(\lambda+h)'+(\lambda+h)^2-(2\lambda'+\lambda^2)
=2(h'+\lambda h)+h^2.
\]

This is the stated quadratic change `2D eta+eta^2`. For a nonzero quadratic differential `f(dt)^2`,

\[
\delta(f(dt)^2)=c_t+
\left(f-\frac{f''}{f}+\frac54\left(\frac{f'}{f}\right)^2\right)(dt)^2.
\]

The added f is required by the definition `gamma beta_2 + the quadratic differential`; it is not optional. Taking f=u² gives `delta((u dt)^2)=gamma beta_1(u dt)+(u dt)^2`. The direct identity `G(t,exp u)-G(t,u)=(u')^2` provides the same check. The script verifies all these equalities.

Further decisive tests:

* `(dg/g)/(df/f)=(dg/df)(f/g)`. With f=t and g=t² on a punctured disc, the left side is 2, whereas the printed factor g/f gives 2t².
* In `c_n(g)-c_m(f)`, the second logarithmic derivative must be f'/f. For m=1,n=2,f=t,g=t² the correct answer is zero; the transcribed mixed derivative gives `-9/t²`.
* Proportional logarithmic derivatives do not force projective equivalence. For f=t²,g=t, the factor is 2, while `G(t,t²)=3/t²` is nonzero.
* If `(dlog f)^2=(dlog g)^2`, nonvanishing derivatives allow local division and give `dlog f=+dlog g` or `-dlog g` on a connected small disc. Thus f=cg or c/g. This is the actual valid special case.
* The equation f+1/f=h is quadratic. Nonzero h does not ensure an etale solution: h=2 forces f=1 over characteristic zero, and the derivative of f+1/f is `1-f^-2`, zero at f=±1.

The original factor-12 integral jet identity is audited under C-SA04-122 by notes_93_a. Here, a torsor under A pushed out along `A --phi--> A` is defined even if phi is not invertible. Its local cocycle is multiplied by phi. If phi is a unit, the resulting semilinear map is an isomorphism. Multiplication by 12 is not an isomorphism in characteristics 2 or 3, and a pushout by it does not prove universal optimality. The universal coherent-target assertion also fails without generation/surjectivity: append an unused direct summand O to the target and append zero to the invariant.

## 3. Earlier-run Hasse-jet ideas, independently re-proved

These statements belong to items SA04-231–235 and are not added to the map of Grothendieck’s claims merely because the earlier notes contained them. Let A be an F_p-algebra and D_j the Hasse derivatives in a variable t. The common kernel of D_1,D_2,D_3 is read coefficientwise from `D_j(t^d)=binom(d,j)t^(d-j)`. Lucas’s digit rule, or the elementary binomial congruences for j≤3, gives

\[
\bigcap_{j=1}^3\ker D_j=
\begin{cases}
A[t^p],&p>3,\\
A[t^4],&p=2,\\
A[t^9],&p=3.
\end{cases}
\]

For p=2 the first two binary digits must vanish; for p=3 the units and threes digits must vanish. Coefficients are arbitrary in A. Without a Frobenius-surjectivity hypothesis on A these subrings are not the sets of literal p-th, fourth or ninth powers of polynomials.

Set q=p for p>3, q=4 for p=2, q=9 for p=3, and let `B=A[t]/(t^q)`. D_1,D_2,D_3 descend to B because q is a power of p at least four and the relevant binomial coefficients vanish. Suppose s in B has invertible D_1s and

\[
Q(s)=-\frac{D_3s}{D_1s}+\left(\frac{D_2s}{D_1s}\right)^2=0.
\]

Write `s=s_0+s_1t+...`; invertibility of D_1s implies s_1 is a unit. Fractional linear transformations with A-coefficients first make the constant term zero, then the linear coefficient one, then the quadratic coefficient zero. For the last step, if y=t+a_2t²+..., use `y/(1+a_2 y)`; its denominator is invertible because y is nilpotent. The integral 3-jet composition identity shows that vanishing of Q is preserved by these transformations (equivalently expand their 3-jets and cancel the two terms in Q).

For the normalized series, suppose d≥3 is the lowest index with a_d nonzero. In

\[
(D_1s)(D_3s)-(D_2s)^2=0
\]

the coefficient of t^(d-3) is `binom(d,3)a_d`. The competing square starts in higher degree, and the lower coefficients have already vanished. For 3≤d<q, `binom(d,3)` is a nonzero element of F_p: for p>3 this follows from d(d-1)(d-2)/6; for p=2 only d=3 occurs; for p=3 the threes digit of d is 1 or 2. Hence a_d=0, contradiction. The normalized series is t, proving the fractional-linear description over **every** A with these stated hypotheses, including nonreduced A.

The same conclusion for `B=A[t]/(t^q-alpha)` follows with the additional hypothesis Pic(A)=0. Adjoin u with u^q=alpha. The algebra `A'=A[u]/(u^q-alpha)` is finite free and faithfully flat over A. Over A', write v=t-u; then v^q=0 and the preceding argument gives an invertible projective matrix representing s. On the double overlap any two representatives differ by a scalar unit: cross-multiplication and the independence of 1,t,t² in the monic degree-q algebra show this after composing one projectivity with the inverse of the other. The local representatives thus descend to a rank-one projective module of matrices. Finite-projective descent is Stacks Proposition 10.83.3 (tag 058Q). Pic(A)=0 makes this line free, giving an actual matrix over A. Its determinant and its denominator in B are units by faithful flatness. This proves exactly the stated restricted extension, without removing its Picard hypothesis.

An invertible determinant cannot be normalized to one without a square root. For s=2t over F_5, uniqueness of the projective representative makes every representing matrix a scalar multiple of diag(2,1); its determinant is 2d², which is 2 or 3, never 1. This checks every hypothesis of the counterexample. The saved enumeration over F_2[t]/t⁴, F_3[t]/t⁹ and F_5[t]/t⁵ gives respectively 4,18,100 solutions with unit derivative and Q=0, equal to p²(p-1); these finite diagnostics supplement, and do not replace, the proof over arbitrary A.

Finally, ordinary derivative constants are too coarse in small characteristic. For p=2, s=t+t² gives D_1s=1,D_2s=1,D_3s=0, hence Q=1. For p=3, s=t+t³ gives D_1s=1,D_2s=0,D_3s=1, hence Q=-1. Both have the same ordinary differential as t.

## 4. Rank-two algebras and the characteristic-two boundary

For a free rank-two module E, identify `E tensor E tensor det(E)^-1` with End(E) using the alternating pairing. The kernel of its trace is generated by the two diagonal symmetric tensors and their mixed symmetric tensor, namely `Gamma^2(E) tensor det(E)^-1`. The scalar submodule corresponds to the alternating tensor; its quotient is `Sym^2(E) tensor det(E)^-1`. These statements can be checked in a basis and are invariant under its changes, so descend to vector bundles. They remain distinct at 2. The usual rank-two identity `E* = E tensor det(E)^-1` and invariance of End(E) under line twist are valid without inverting 2.

With quotient projectivization, the universal sequence is `0 -> K -> f*E -> O(1) -> 0`; K equals `f*det(E) tensor O(-1)`. The relative tangent bundle is `Hom(K,O(1))=O(2) tensor f*det(E)^-1`. Its global relative vector fields are End(E)/O, as the matrix action shows. An arbitrary Brauer–Severi curve need not have a global E: the real conic x²+y²+z²=0 has no real point, whereas P(E) over R is P¹_R and has real points. It becomes P¹ over C, so meets the local hypotheses. The correct global obstruction is the Brauer class, not an error in the local projective formulas.

Use e=E12, h=diag(1,0) modulo scalars, f=E21. Matrix commutators give

\[
[e,h]=-e,\quad [f,h]=f,\quad [e,f]=2h.
\]

The saved Killing calculation gives matrix

\[
\begin{pmatrix}0&0&4\\0&2&0\\4&0&0\end{pmatrix},\qquad \det=-32.
\]

It is nondegenerate precisely when 2 is invertible. In the trace-zero basis e,H=diag(1,-1),f, the table is instead `[e,H]=-2e,[f,H]=2f,[e,f]=H`, and H maps to 2h. The map sl2 to pgl2 is an isomorphism after inverting 2. In characteristic 2, sl2 has a scalar center, while pgl2 has zero center and an abelian derived plane W=span(e,f), with `[h,w]=w`.

Over a field of characteristic 2 an automorphism of this latter Lie algebra must preserve its derived plane. It is exactly `w -> Aw, h -> h+v`, where A belongs to GL(W) and v to W: the coefficient of h must be one by the bracket. This group has dimension six, whereas PGL2 has dimension three. The same calculation proves that every line of W is stable under ad(h); it is not legitimate to recover only two root lines from this Lie action. The group torus, with its characters, still contains more information.

The map D defined by `D(e)=f,D(h)=D(f)=0` is a derivation in characteristic 2, as direct substitution in the three bracket identities shows. No inner derivation can send e to f, so it is outer. This refutes the unqualified inner-derivation assertion on scan 89, and matches its explicit correction on scan 90. On A¹ in characteristic 2 the connection `d+D dt` preserves the bracket yet sends the lowest filtration line to f dt, outside the two-step Borel filtration. Thus bracket compatibility alone does not supply the desired transversality.

Relative first jets of the tangent line on P¹ have an exact sequence `0 -> O -> P^1_rel(T) -> T -> 0`. After pushforward, relative jet prolongation supplies an O_base-linear, PGL2-equivariant splitting, so the result is O direct-sum g. A canonical comparison with M=End(E) would give an equivariant retraction M to its scalar submodule. For a field of characteristic 2, invariant linear forms on M are multiples of trace (test conjugation by elementary matrices), and trace(I)=0. Such a retraction does not exist. After inverting 2, trace/2 gives it. This is the obstruction to the questioned **canonical equivariant** identification, not to an arbitrary local isomorphism of rank-four modules.

## 5. Marked sections, extension filtrations, and duality

For a projective line bundle with section sigma and conormal line Omega, use `A=O(sigma) tensor f*Omega`. Its restriction to sigma is canonically O. Pushing forward the divisor sequence gives `0 -> Omega -> L=f*A -> O -> 0`. Local P¹ calculations show rank two and the asserted base changes. Restriction to the first infinitesimal neighbourhood is an isomorphism on this pushforward because `A(-2sigma)` is relatively O(-1), with H⁰ and H¹ zero. Restriction modulo I alone has rank one, so the first-neighbourhood quotient must be modulo I². This does not decide which exponent is on the scan.

The complement of sigma consists of quotients whose restriction to Omega is invertible; after that identification it is the sheaf of retractions L to Omega. Such retractions form an Omega-torsor. A second disjoint section is a retraction and splits the extension. The two associated left ideals of End(L) are the endomorphisms killing the respective kernel lines; a direct-sum decomposition of L makes these complementary left ideals as modules. They are not two subalgebra factors of a product algebra.

For the upper triangular change of frame `T=[[1,a],[0,1]]`, conjugation on g in the basis (e,h,f) is

\[
\begin{pmatrix}1&-a&-a^2\\0&1&2a\\0&0&1\end{pmatrix}.
\]

This gives the filtration with graded lines Omega,O,Omega inverse and verifies the middle extension. When 2 is invertible, the Killing pairing identifies the quotient g/Omega with the dual of the middle subbundle. In characteristic 2 this can fail globally. On a smooth elliptic curve over an algebraically closed field of characteristic 2, choose a nonzero class in H¹(O) and its nonsplit extension `0 -> O -> L -> O -> 0`. Its transitions are the matrices T above. The quotient g/Omega then has transition `[[1,2a],[0,1]]=I`, so splits; L-dual remains nonsplit because dualizing twice recovers L. Thus the proposed identification is false without the 2-invertible hypothesis, with every bundle in the counterexample satisfying the indicated ranks and markings.

The central quotient SL2/mu2=PGL2 is nevertheless valid as an fppf sheaf in all characteristics. To lift a local GL2 representative to determinant one one may adjoin a square root of its determinant by a finite flat cover. The kernel is mu2. This topology is essential at 2, where mu2 is nonreduced. Failure of a Lie-algebra identification cannot be used to refute this group-scheme quotient.

## 6. Connections, restricted data, and the remaining torsor

For an inner connection coefficient `a e+b h+c f`, the adjoint matrix, with columns the images of e,h,f, is

\[
\begin{pmatrix}b&-a&0\\-2c&0&2a\\0&c&-b\end{pmatrix}.
\]

This reproduces the completion on scan 90. Passing to a filtration quotient kills the term `df tensor section` in the Leibniz rule, so the induced successive maps are O-linear. Their coefficients satisfy `c12=-2c23`. Vanishing c23 means preservation of the Borel filtration, equivalently horizontality of the marked section for the projective connection. For connections actually induced from PGL2 these statements are valid as matrix statements; identifying **all** bracket-preserving connections with them requires the earlier restriction on 2.

The sheaf of connections on a fixed principal projective bundle is locally a torsor under g tensor omega: the difference of two connections is an adjoint-valued one-form. In Borel frames, derivatives of transition functions are Borel-valued. Therefore the normal-component quotient has a distinguished zero, and fixing a given normal component i leaves a torsor under L tensor omega. These sheaves may have no global section.

The restriction `C_Omega:Omega -> L tensor omega` is a first-order differential operator with symbol the inclusion of Omega in L. Its quotient is `-2i`. At 2 this restriction loses the coefficient c, although the quotient connection can retain it. Specifying one restriction is therefore not always equivalent to specifying the other. With fixed i and fixed C_Omega, the remaining difference is `a e`, a section of Omega tensor omega.

If `j=-2i:Omega -> omega` is an isomorphism, 2 must be invertible (its action on a nonzero rank-one fibre cannot be invertible in residue characteristic 2), and omega must be a line bundle. The universal property of first principal parts factors C_Omega uniquely through an O-linear map

\[
P^1(\Omega)\longrightarrow L\otimes\omega.
\]

It is the identity on the symbol subbundle and j on the quotient; hence it is an isomorphism by the two short exact sequences. Identifying Omega with omega via j gives `L=P^1(omega) tensor omega^-1` and the universal first-order operator. Conversely, if 2 is invertible and omega is a line bundle, this construction provides the restricted data. No smoothness conclusion follows merely from omega being invertible, and no global full connection was constructed. The remaining full compatible connections form an omega²-torsor, locally nonempty. Over a smooth complex curve this is the usual transverse PGL2-oper/projective-connection description.

## 7. Conditional calculations and unresolved source data

If the uncertain E on scan 81 is Omega inverse direct-sum O, its endomorphism and twisted trace-zero matrices follow by Hom of line bundles, giving Omega direct-sum O direct-sum Omega². If, additionally, the base is a compact connected smooth complex curve of genus g≥2, Riemann–Roch and duality give h⁰(omega)=g, h⁰(O)=1, and h⁰(omega²)=3g-3: the last equality uses h⁰(omega inverse)=0 since its degree is negative. The total is 4g-2. This is a conditional reconstruction. It neither identifies the draft E nor determines the scope of the cancellation strokes.

The undefined objects and questioned arrows of scan 81, the unfinished terminal product on scan 80, and the disputed “faux”/“plus bas” on scan 87 have no independent proof check: they receive textual-comparison events only. No proof, disproof, or historical outcome is manufactured for an assertion that cannot be identified.
