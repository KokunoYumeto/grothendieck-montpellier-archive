# Exact source audit: downward theta, the adjoint, and the rank-dependent swap

Author: GPT-6 Astra Pro, ALP_MACHINE /root/definite_oscillator,
21 November 2026 UTC. This is a source-convention audit, not a new
nonvanishing theorem or a replacement for AM-R-015.

All paths below are relative to
`work/research/alpoge_source` and were read from the recovered,
intake-pinned source.

## 1. The downward operator has an unbarred kernel

In
`Formalism/LocalToGlobal/IndefiniteReal/OrthogonalComplementCharacterisation.lean`,
lines41–55, the actual definitions are

\[
 \operatorname{liftInt}(F)(g)
       =\int_{H(F)\backslash H(\mathbb A)}\theta(g,h;s)F(h)\,dh,
 \qquad
 \operatorname{liftInt}(F_v)(g)=(\operatorname{io}F)_{T(\phi)v}(g).
 \tag{IC1}
\]

The displayed quotient notation describes the intended automorphic
application; the literal Lean definition integrates over the given
fundamental set with its given measure. In the source's downward
application, `G` is the smaller group and `H` the larger one. There
is no complex conjugation on the theta kernel in `liftInt` or the
equation of `IsIo`.

The source ties this actual downward operator to the chain:
`Development/AbelianVarietyTheory/Definitions/LatticeFrames/StepsOnto.lean`,
lines104–105, and the same `IndefiniteReal/LinksChar.lean`,
lines283–287, use `IsIo`. Thus the upward formula below must not be substituted
for this downward formula.

## 2. Conjugation belongs to the Hermitian adjoint

In the same `OrthogonalComplementCharacterisation.lean`,
lines74–88, `IsTPlus` uses a Hermitian pairing linear in its first
argument and conjugate-linear in its second. Its coefficient map
`Tp` is conjugate-linear in the Schwartz variable. `IsIoUp` is
the distinct assertion

\[
 \int_G\overline{\theta(g,h;\phi)}\,u_v(g)\,dg
       =(\operatorname{up}u)_{T^+(\phi)v}(h).
 \tag{IC2}
\]

This is exactly the placement of the bar required by the adjoint
of (IC1). The corresponding `ChainParSucc.Step.up` equation in
`Development/AbelianVarietyTheory/Definitions/LatticeFrames/ChainParSucc.lean`,
line132, therefore does not show that the downward theta kernel
is conjugated. The definitions in (IC1) and (IC2) distinguish the
two operations before any application of a theta-correspondence
theorem.

## 3. Swapping the source order does not insert a bar

The abstract `ThetaX.th` convention is fixed by
`Formalism/LocalToGlobal/BesselHermitianTheta/TiedWeil.lean`,
lines136–140. It is a bilinear integral of the unbarred kernel
against the automorphic input, multiplied by the specified real
normalizer `T.petC V`.

Its `om_swap` field, lines131–134, states that if the two Schwartz
readings satisfy

\[
                    f'(x^{\mathsf t})=f(x),
\]

then the corresponding Weil actions satisfy

\[
 (\omega_{W,V;\chi',\chi}(h,g)f')(x^{\mathsf t})
     =(\omega_{V,W;\chi,\chi'}(g,h)f)(x).
 \tag{IC3}
\]

This swaps the two groups and their attached characters and
transposes the matrix variable. It does not conjugate the function.
The predicate `PhiYupTied`, lines143–145, imposes precisely that
transpose relation on `PhiY` and `PhiYup`, again without a bar.

The actual definition `dnY` in
`Formalism/LocalRingCardinality/DataTheta.lean`, lines733–734,
places the larger source `Y (j+1)` first and the smaller target
`Y j` second in the abstract `th`. Consequently the same kernel
can be expressed in the smaller-first order using (IC3). This is
different from silently defining a new, fixed-orientation
`Hom(big,small)` symplectic space with the old smaller-first
splitting signs.

The source explicitly changes its `WA` split factor with rank:
`TiedWeil.lean`, lines81–82, gives

\[
 \operatorname{splitFac}_{V,W}(x,y)=
 \begin{cases}
    \chi'(x)^{-1}\chi(y),&\operatorname{rank}V\le
                                      \operatorname{rank}W,\\
    \chi'(x)\chi(y)^{-1},&\operatorname{rank}W<
                                      \operatorname{rank}V.
 \end{cases}
 \tag{IC4}
\]

Here `x,y` are the actual determinant roots specified in the
source, not the determinants themselves. Formula(IC4) is
compatible with the swap(IC3). The character-twist fields
`twW_up`, `twV_up`, `twW_dn`, `twV_dn`, lines88–99, retain those
opposite signs in the two rank orders.

The `WO` constructor in
`Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean`
has its own fixed formula `symplO`; the explicitly named
`toTWsmall` at line81 is the smaller-first bridge. Thus AM-DO-028's
even, smaller-first Hom/tensor dictionary cannot be copied to
the reverse source order by interchanging rank labels while
retaining its original splitting formula. The exact `WA` swap
is available and provides the correct route.

## 4. Odd-rank characters remain attached to their spaces

`OrthogonalComplementCharacterisation.lean`, lines15–18, defines

\[
 \operatorname{attChr}(\mu,\eta;n)=
       \begin{cases}\mu\eta^{-1},&n\text{ odd},\\
                    \mu,&n\text{ even},\end{cases}
\]

and

\[
 \operatorname{chrStep}(\mu,\eta;j)=
       \begin{cases}(\mu_j\eta^{-1},\mu_j),&j\text{ odd},\\
                    (\mu_j,\mu_j\eta^{-1}),&j\text{ even}.
       \end{cases}
 \tag{IC5}
\]

Its proved `chrStep_eq_att`, lines26–35, matches these characters
to the two actual ranks. Therefore the odd character belongs to
the odd-dimensional space; it is not attached permanently to the
left or right integral variable. Swapping the spaces in(IC3)
also swaps those attached characters. This is sufficient to
resolve the source convention issue raised by the conjugated
`Step.up` formula. A real theta nonvanishing or lower-tower
vanishing statement still needs its actual local representation
theorem and numerical hypotheses.

## Check status

The complete audit was read against the displayed definitions,
including the rank branch, actual determinant-root convention,
and the distinction between the linear downward coefficient map
and its conjugate-linear Schwartz adjoint. The result is an
exact convention identification. No source record was instantiated
and no Lean compilation was run.
