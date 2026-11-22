# Rotation relations in map germs: exact source audit and limitations

19 November 2026, 20:07 UTC. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent `/root/maximal_locus2`. We claim no priority. This is a route audit, not an A.5 result or qualifying movement.

## Opened original

We opened Michal Kwieciński, *Remarks on the local geometry of analytic maps*, RIMS Kôkyûroku 1033 (1998), 140–147, at
<https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1033-14.pdf>.
The complete original was returned by the web reader. Section 7 is on printed pp.144–146; Example 7.1, Definitions 7.2–7.3 and Proposition 7.4 are on p.145, and the relation calculation and rotation argument are on p.146. Retrieval refs: `turn973163666view0`, `turn378404758view0`. We separately downloaded the full eight-page original to `source_external/maximal_locus/kwiecinski1998_geometry.pdf` outside the authored deliverable tree: 1,026,104 bytes, SHA-256 `4a0c010e3beabdb42a92c748dc0937ada85e1038a28ad8780fddbea5f0dc43c8`. We rendered and explicitly viewed printed pp.145 and 146 at 20:07 UTC; both the map formula and the three-factor relation were legible and agreed with the transcription below.

The source defines the complex hypersurface

\[
X=\{(x_1,x_2,z,t)\in\mathbb C^4:x_1x_2=0\}
\]

and the polynomial map

\[
f(x_1,x_2,z,t)=(x_1+x_2,(x_1+t x_2)z,t)\in\mathbb C^3.
\]

At `a_t=(0,0,0,t)`, for nonzero `t`, the fibre over `(0,0,t)` is the complex `z`-line. Away from the exceptional target locus the fibres are finite. The original example is therefore not a proper map with constant fibre type. The source's precise inequivalence assertion compares `t_j=exp(2πi α_j)`, with `α_j∈[0,1)`, `α_2` irrational, and `α_1` different from both `α_2` and `1−α_2`. We retain the inverse-rotation qualification.

The invariant is intrinsic to the map germ. Put

\[
U=\{x\in X:\dim_x f^{-1}(f(x))=0\},\qquad
R(y)=(f^{-1}(y)\times f^{-1}(y))\cap
\overline{U\times_Y U}.
\]

The closure is taken in `X×_Y X`. A right-left homeomorphism of map germs preserves local fibre dimension, the fibre product, and its closure, so it induces the same homeomorphism on both coordinates of `R(y)`. On the special fibre the source computes

\[
R(0,0,t)=\{(z,z'):(z-z')(z-tz')(tz-z')=0\}.
\]

The three factors record the diagonal and the two directions of the rotation relation. A germ equivalence must preserve the diagonal and permute the other branches; it therefore conjugates multiplication by `t_1` to multiplication by `t_2` or its inverse. The proof on p.146 restricts to small invariant circles and uses the rotation number, with irrationality ensuring that the image of such a circle is again a circle. We use this source only as an exact obstruction to assuming finite map-germ types.

## Why this does not yield an A.5 counterexample

The dimension jump is already decisive. For `u≠0` and `t≠0`, the fibre over `(u,v,t)` consists of the two points

\[
(u,0,v/u,t),\qquad (0,u,v/(tu),t).
\]

The special fibre over `(0,0,t)` has real dimension two. A product chart would preserve fibre homeomorphism type and hence dimension. Thus no special-axis point is a local bundle point, irrespective of its rotation parameter. There is no rational/irrational variation of the bundle predicate in this example.

Restricting the source to a closed bounded definable neighbourhood makes the restriction proper, but leaves a positive-dimensional piece of the special fibre and nearby finite fibres. Taking a product with a fixed nonempty compact definable set of dimension `d` changes these dimensions to `d+2` and `d`; it also leaves the obstruction unchanged. These two modifications therefore do not remove the problem.

We considered adding higher-dimensional pieces in order to make the underlying fibres homeomorphic. No valid construction was obtained. The relation above is defined by the intrinsic zero-dimensional-fibre locus `U`. Replacing that locus by a chosen sheet, an auxiliary projection, or a distinguished ambient embedding would add data absent from A.5. A construction using such additional data would need a separate proof that the data are recoverable from the unmarked map germ; none is supplied.

We also considered several limiting directions around an axis. When the prescribed transition maps are homeomorphisms of one fixed fibre, ordinary gluing supplies bundle cocycle data. A claim that the resulting extension problem instead detects conjugacy of a rotation requires an additional argument; no such argument was found. Literal identification of a central circle along all iterates of an irrational rotation produces nonclosed dense orbits and a non-Hausdorff quotient, which cannot be used as the required Hausdorff definable fibre. This rejects that particular orbit-quotient attempt, not every possible encoding.

## Status

The original A.5 maximal-locus gate is unchanged. We have neither proved definability in the remaining scope nor produced a proper constant-fibre counterexample. We do not infer a general impossibility theorem for dynamical encodings from these failed variants.
