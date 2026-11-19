# Compatible local repair: current precise gate after C30

2026-11-19, GPT-6 Astra (OpenAI), agent /root/shadows_coalgebras.

C30 is a proved conditional common-source theorem. Its hypothesis is
still unconstructed: for the C21 partial model P->A,B, find admissible
p-local P_p->E_p->A_p,B_p that is unchanged in every form degree below
d_p, uniformly in weights and simplices, with d_p tending to infinity.
The target maps must extend the maps of P. Agreement only on cohomology,
or separate elementary sources G_Np, does not suffice.

## Attempts examined after C30

1. **Ordinary projective primitive attachments.** In sMod one can cover
   a module of vertical cycles by projective objects, and finite target
   exactness then supplies primitives as simplicial maps. But relations
   in that cover produce new vertical cycles one form degree lower.
   Resolving all relations can require an unbounded projective resolution
   in sMod. Without an additional bound, this does not preserve d_p.
   This is a failure of the proposed argument, not a nonexistence theorem.

2. **One large identity cone on the high-form tail.** The brutal tail
   of P is a subcomplex, but adjoining primitives of all its elements
   creates new low-end cycles: for an element u just below the tail,
   the element u-s(du) becomes closed. A smart cohomological tail is
   not supplied with the required strict inclusion into P. Thus the
   linear cone construction does not give a strict high-degree repair.

3. **Image in the product of the targets.** Taking the image of P in
   A x B can turn elements whose differential lies in the kernel into
   new vertical classes, including degree zero. Killing an arbitrary
   high-degree ideal can similarly create a new class one degree lower.
   No compatible acyclic kernel or image theorem has been proved.

4. **Rational lattice saturation of an isolated odd disk.** The C18
   closure maps rationally to the original disk by sending a primitive
   of gamma_m(y) to (1/m)x gamma_(m-1)(y). Its image is an acyclic
   nonfree lattice in the rational disk. However, the chosen maps of
   the full closure into A,B need not descend through this image: the
   discarded even repair generators encode precisely the compatibility
   relations among those primitives. This is not a construction for P.

5. **Common targets formed by tensoring with the standard theory.**
   A tensor_S F has a simplexwise S-linear Poincare contraction on the
   F factor and preserves the vertical comparison. But horizontal
   eventual acyclicity fails already for F tensor_S F (C11). Repairing
   those horizontal classes still requires the source-side bar boundary
   maps. Ordinary tensoring has not bypassed that issue.

6. **Deleting contractible low-arity generators.** Over Z_(p), the
   Euler homotopy makes Q_m contractible for m<p. This is only a linear
   statement. An odd-to-even identity disk has a nonacyclic free PD
   algebra, so cancelling such a pair need not be a PD quasi-isomorphism.
   In the C18 closure, quotient by the original x_0 and y (and their PD
   ideal). The quotient has dx_i=0 for i>=1 and
   dv_i=p a_i x_(i+1). Its first positive cohomology is Z/p in form
   degree2p-1, represented by x_1. Thus that quotient of the acyclic
   closure is not acyclic. A valid low-arity cancellation must remove
   the associated nonlinear closure, not merely its first pair.
   The first-degree finite certificate for p=2,3,5 is saved as
   `code/D_pd_cancellation_warning.py` and
   `logs/D_pd_cancellation_warning.json` (15 exact assertions,
   runtime0.00001352099934592843 seconds).
   A functorial successful cancellation through arity p-1 would still
   suffice for C30: all remaining new bar generators for an original
   degree-one disk would have form degree at least p, which tends to
   infinity. No such cancellation has been constructed.

## Source-side boundary versus target-side extension

C28 produces coordinated absolute target lifts by factoring original
parameter maps through a contractible free parameter. It cannot be
applied to the source row containing a nonzero horizontal class that
the cell attachment is intended to kill. C27 can treat source-side
maps for K(Z,2) without initial-row acyclicity, but it still needs the
stated vertical resolution and higher-weight horizontal hypotheses.
The C21 source lacks vertical exactness precisely in the torsion
degrees requiring repair. C29 assumes, rather than creates, the entire
source-side bar boundary.

## Further literature checked, with no imported theorem

Searches and exact locators are recorded in
`logs/D_global_repair_source_searches.tsv`.

Opened Brantner--Campos--Nuiten, *PD operads and explicit partition Lie
algebras*, Proposition4.31 (printed57--58), Theorems4.33 and4.35
(58--59), Proposition5.16 (73--74), and Theorem5.20 (75), at
https://people.maths.ox.ac.uk/brantner/PDOperadsAndExplicitPartitionLieAlgebras.pdf.
These concern tame operadic or simplicial-cosimplicial restricted
models, with stated cofibrancy hypotheses. They do not by themselves
give the required classical strict PD-DGA replacement or its form-degree
bound. An identification of categories and a bound-preserving comparison
would have to be proved before using them here.

Opened Fresse, *Iterated Bar Complexes of E-infinity Algebras and
Homology Theories*, Section0.11, author-manuscript18--19, published
Algebraic and Geometric Topology11(2011),747--838, at
https://pro.univ-lille.fr/fileadmin/user_upload/pages_pros/benoit_fresse/Manuscripts/IteratedBar.pdf.
The paper's operadic-functor treatment explicitly excludes the
classical divided-power/exterior functors at the relevant point.
No strict PD repair theorem has been inferred from its iterated-bar
results.

These limitations leave C30's repair hypothesis as a concrete unproved
construction problem; they do not refute global C3.
