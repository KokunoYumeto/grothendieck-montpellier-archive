# SF-E816c--d: the two-degree gap and a limit to the overlap argument

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21. The gap observation in SF-E816c was supplied by /root. The explicit counterexample in SF-E816d was supplied by /root/imprimitive. Both are written and independently checked here. Root read the complete written addendum and reported whole-proof PASS. Imprimitive independently read and approved SF-E816c; his read of SF-E816d is contributor verification, while root and sixfolds supply its independent checks. All reviews are dated2026-11-21, GPT-6 Astra Pro, inherited effort not exposed.

## SF-E816c. Any two distinct cohomological degrees

The ordinary-gluable obstruction SF-E816a holds when the two nonzero cohomology sheaves occur in any two distinct degrees, not necessarily adjacent. Keep all its other factor, rational primitive-difference, finite coherent action, and balanced-character hypotheses. After an overall shift, write the two sheaves as

\[
 A=\mathcal H^0(E),\qquad B=\mathcal H^{-k}(E),\qquad k\ge1.
 \tag{E816.41}
\]

Because \(E\in D^{\le0}\) and \(E[-k]\in D^{\ge0}\), their extreme map is canonically

\[
 \operatorname{Ext}^{-k}_X(E,E)
      =\operatorname{Hom}(E,E[-k])
      \simeq\operatorname{Hom}_X(A,B).
 \tag{E816.42}
\]

Ordinary gluability makes this group zero. The equal-class flat-Hom argument, stable-type decomposition, and quotient-to-subobject contradiction of SF-E816a then apply word for word: no stable isomorphism type can occur in both sheaves. Hence their cross Ext, in both directions, is concentrated in degree two. This conclusion permits overlapping normalized classes, since unequal stable types of the same normalized class are completely Ext-orthogonal.

The canonical equivariant Postnikov triangle is

\[
 B[k]\longrightarrow E\longrightarrow A
      \xrightarrow{e}B[k+1],
 \qquad e\in\operatorname{Ext}^{k+1}_G(A,B).
 \tag{E816.43}
\]

For \(k=1\), SF-E816a already applies. For \(k\ge2\), the last group is zero, so the triangle splits in the specified equivariant category. Thus

\[
 E\simeq A\oplus B[k].
 \tag{E816.44}
\]

The cross terms in its degree-two self-Ext are
\(\operatorname{Ext}^{2+k}_G(A,B)\) and
\(\operatorname{Ext}^{2-k}_G(B,A)\). Both vanish by concentration in degree two. Therefore

\[
 \operatorname{ext}^2_G(E,E)
   =\operatorname{ext}^2_G(A,A)+\operatorname{ext}^2_G(B,B).
 \tag{E816.45}
\]

Count the actual nonzero normalized-class blocks of the two sheaves, counting a repeated class in the two sheaves twice. The full character is the sum of their pure exponential characters with the signs \(1\) and \((-1)^k\). The balanced rank/common-annihilator proof in SF-E816 §4 requires at least four terms in this presentation. Invariant evaluation contributes at least six middle self-Ext directions per actual block. Equation (E816.45) consequently gives at least twenty-four, whereas weak invariant semiregularity requires eighteen. This proves the gap extension.

## SF-E816d. Three degrees do not force distinct stable types under gluability

Ordinary gluability alone does not imply that a stable isomorphism type occurs in at most one cohomological degree of an arbitrary bounded complex. Here is a concrete actual example within the same primitive projectively flat factor category.

Take the explicit CM fourfold and index-two line bundle of SF-E814:

\[
 X=E_{\mathrm i}^{\,4},\qquad
 L=\mathcal O(0)\boxtimes\mathcal O(0)
      \boxtimes\mathcal O(-0)\boxtimes\mathcal O(-0).
 \tag{E816.46}
\]

Use the real multiplication matrix \(U\) and divisor matrix \(S\) of SF-E815. The class \(c_1(L)=\theta_S\) is block diagonal and primitive on both real-multiplication planes. The elliptic Künneth computation gives \(H^2(X,L)=\mathbf C\), with every other cohomology group zero. Choose its nonzero class and the actual triangle

\[
 L[1]\longrightarrow F\longrightarrow\mathcal O_X
            \longrightarrow L[2]
 \tag{E816.47}
\]

of SF-E814. That full proof establishes ordinary gluability of \(F\), as well as

\[
 \operatorname{Ext}^j_X(\mathcal O_X,F)=0\quad(j\le0).
 \tag{E816.48}
\]

For clarity, the degree-zero vanishing is the injectivity of
\(\operatorname{Hom}(\mathcal O_X,\mathcal O_X)\to
\operatorname{Ext}^2(\mathcal O_X,L)\), which sends the identity to the chosen nonzero extension class. Negative degrees vanish in the same triangle since the only cross cohomology of \(L\) is degree two.

Put

\[
 T=\mathcal O_X\oplus F[1].
 \tag{E816.49}
\]

Its nonzero cohomology sheaves are

\[
 \mathcal H^0(T)=\mathcal O_X,\qquad
 \mathcal H^{-1}(T)=\mathcal O_X,\qquad
 \mathcal H^{-2}(T)=L.
 \tag{E816.50}
\]

Thus the identical stable type \(\mathcal O_X\) occurs in two different degrees. Nevertheless \(T\) is ordinary gluable. The diagonal negative self-Ext groups vanish for both summands. For a negative integer \(j\), one cross group is

\[
 \operatorname{Ext}^j_X(\mathcal O_X,F[1])
     =\operatorname{Ext}^{j+1}_X(\mathcal O_X,F)=0
\]

by (E816.48). The other is

\[
 \operatorname{Ext}^j_X(F[1],\mathcal O_X)
     =\operatorname{Ext}^{j-1}_X(F,\mathcal O_X)=0.
\]

Indeed \(F\in D^{\le0}\), while \(\mathcal O_X[j-1]\in D^{\ge1}\) for these negative \(j\), so the latter vanishing follows from the cohomological structure. This proves all required negative self-Ext vanishings directly, with no formality assumption.

The example is not a balanced seed and is not presented as a new construction for the main target. Its entire character is

\[
 \operatorname{ch}(T)=1-\bigl(1-e^{c_1(L)}\bigr)
                   =e^{c_1(L)},
 \tag{E816.51}
\]

which is pure and has degree-two cap rank six. It is also visibly decomposable. Its sole role is to refute the blanket inference that ordinary gluability forces stable-type disjointness across arbitrarily many cohomological degrees. The three-or-more-degree overlapping case in SF-E816 therefore needs an additional argument or an actual new construction.
