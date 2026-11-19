# Independent review of the root A.1 derived-tail and completion arguments

GPT-6 Astra (OpenAI, ChatGPT Pro mode), SA08 D-agent, 2026-11-19.
These are checks performed during the proof development and communicated
to the root agent. They are recorded here so the check events have a file.

1. Literal-versus-graded correction: accepted after independent verification.
For discrete X=N, literal H0 is product_N Gamma_k(T), while tensoring
H0(X;k) with Gamma_k(T) allows only a uniform finite weight bound. The
sequence T^[n] distinguishes them. The all-X literal formula with
H^i(X;I_i) follows by resolving the constant coefficient ideal with the
weight tail F^iA and dimension shifting; low weights have no cochain
terms in degree i and cannot affect H^i. This is independent of the
shadow theorem, which uses the weightwise direct sum.

2. Universal cycle resolution. Over B=Gamma_Z(T), each simplex admits
the basis T,X1,...,Xn. The divided-power Poincare contraction is
B-linear and preserves weight. Hence the exact de Rham cycle sequences
split in each simplicial degree, and their cycle modules are graded
B-projective. The normalized complex of Z^i starts in simplicial degree
i and has sole homology I_i in that degree. Thus NZ^i[-i] is a graded
projective resolution of I_i. The neighboring normalized A^{i-1}
has sole homology Z in degree i-1, with B acting through augmentation.
The connecting triangle has the shifts used in root theorem A006.

3. Actual cocycles versus homotopy classes. The map A^{i-1}->Z^i is
surjective in every simplicial degree for i>0, by the degreewise
Poincare exactness. A surjection of simplicial abelian groups is a Kan
fibration. A nullhomotopic map X->Z^i therefore lifts a homotopy from
zero through this fibration, yielding a preimage map X->A^{i-1}.
Consequently the actual quotient defining de Rham H^i equals the
cokernel of [X,A^{i-1}]->[X,Z^i]; no projectivity or finiteness of X is
being assumed. Dold--Kan identifies [X,V] with derived maps from the
normalized free chains of X, a bounded-below complex of free modules.
The long exact sequence of derived Hom in the triangle then gives
the image formula using E_i=S tensor_B^L I_i and E_{i-1}.

4. Multiplication. The shuffle comparison on normalized simplicial
modules turns the cycle product into I_i tensor_B^L I_j->I_{i+j}
after removing the indicated homological shifts. Its source is
homologically connective and its target is a degree-zero module;
therefore the map is determined by H0. The universal multiplicative
comparison computes that H0 map as ordinary binomial ideal
multiplication. Base change gives the E_i pairing. Products of a
boundary with a cocycle are boundaries in the original DGA, so the
lift-and-image product is independent of the chosen representatives.

5. Completion. The relevant completion is total weight, including
coefficient filtration and all polynomial/exterior generator weights.
In bar degree h, the minimum generator weight is i+h. The completed
bar differential's first term is convergent because gamma_a(t) tends
to zero in filtration at least a; all other coefficients involve only
finite sums in each fixed weight. Comparison maps and chain homotopies
between the graded projective cycle resolution and the graded bar
resolution can be chosen homogeneous of weight zero by the usual
projective lifting induction. Their base changes preserve the total
filtration and extend continuously to the completions. Thus this
comparison transfers quasi-isomorphism by actual homotopy equivalence,
not by assuming that completion is exact.

6. Under gr S=Gamma_k(T), the associated graded augmented completed
bar complex is the tail resolution over Gamma_k(T). It is exact in
positive homological degree. The Z-free integral resolution may be
base changed to arbitrary k without losing that exactness because its
homology tail modules and contraction construction are Z-flat. Solve
a cycle successively by increasing total filtration; the correction
primitives form a convergent sum because S is complete and separated
and minweight=i+h. The augmentation has image exactly F^iS by the
stated closed-tail definition. This proves Ehat_i equivalent F^iS and
the completed image formula in A008. Without the associated-graded
hypothesis only the completed derived-tail model is justified.

No additional gap was found after the total filtration and the
closed-tail hypothesis were stated explicitly. This review does not
claim that arbitrary completion of arbitrary resolutions is exact.
