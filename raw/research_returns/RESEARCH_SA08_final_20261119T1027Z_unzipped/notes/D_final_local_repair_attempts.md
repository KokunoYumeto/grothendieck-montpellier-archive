# Final local-completion attempts and exact stopping state

19 November 2026. GPT-6 Astra (OpenAI), inherited effort,
agent `/root/shadows_coalgebras`.

This note records uncompleted mathematical attempts after C30 and the
proved weakening C34. It proves no new coefficient case and does not
claim a necessary or equivalent reformulation of integral C3.

## The current sufficient construction

C34 needs, for the indicated pair and homotopy-equalizer targets, a
full admissible p-local theory E_p mapping to the target, together
with a strict isomorphism of form truncations

    P_p / P_p^{>=d_p}  =  E_p / E_p^{>=d_p},

compatible with the target maps, where d_p tends to infinity. A full
map P_p -> E_p is unnecessary. The fixed low truncation includes
every weight and simplex. It does not prescribe the outgoing
differential at degree d_p-1 or products landing in degree d_p.

I independently audited the complete C34 proof. The selected prime
component supplies every operation crossing its cutoff; refinements
invoke the given truncated isomorphism only when all involved degrees
remain below that cutoff. An independent rational elementary source
and two consecutive interval edges provide the actual target map.
The audit is in `logs/D_C34_CHECK_EVENTS.tsv`.

## Rational-image closures impose unwanted divisibility

An integral image inside a rational disk may be natural and acyclic
without admitting the required target maps. A proposed integration
formula on a bar word of length p sends a word on distinct degree-one
odd parameters to their product divided by p!. An extension to a
torsionfree target would therefore require divisibility of that odd
product by p. Standard de Rham exterior rows have primitive such
products. For example, in simplex dimension p take

    u_i = X_i^[w-1] dX_i = d(X_i^[w]),  w > 1.

Their product is one divided-power/exterior basis monomial, with
coefficient one. The initial row of weight w and form one is
horizontally acyclic, and so is the output row of weight pw and
form p. Thus those acyclicity hypotheses do not imply divisibility.
The fully written and independently audited p=2 version is C35.
No assertion about the unproved integration formula is needed for
that counterexample.

## Why a pointwise Tate closure has not supplied the missing object

For a chosen basis of a free parameter module, tensoring the unary
C18 closures supplies a pointwise acyclic PD algebra whose new
generators first occur in high form degree. The obstacle is a strict
simplicial structure and compatible maps to the prescribed targets.
Choosing primitives separately in each simplex does not give those
face and degeneracy maps, much less their identities.

A functorial construction using a free cover of all cycles introduces
linear relations. Resolving them inside simplicial modules can have
unbounded projective length, and moving that length into the cochain
direction loses the asserted lower bound on new form degrees. Merely
putting the choices in a second simplicial direction does not solve
this: tensoring several closures over the original defective disk
need not preserve its coefficient resolution. No valid diagonal or
realization argument with all three required properties was proved.

There is a useful but still uncompleted reformulation of the bar
calculation. For the positive bar closure of a disk with odd form
degree 2r-1, parameter arity m and bar length n satisfy

    form degree = 2 r m - n.

Regarding n as the homological degree turns this into the usual
nonnegative homological bar resolution over the divided-power
coefficient algebra. Pointwise Tate comparison theorems therefore
explain maps to chosen minimal closures. They do not produce a
functorial simplicial comparison or a form-degree-preserving
replacement. Passing to PD indecomposables cannot justify such a
comparison, by the already proved C26 counterexample.

For m<p, the relative low-arity linear complexes contract after
p-localization. One possible future approach would replace that
linear cancellation by a functorial strict PD cancellation that
retains the complete nonlinear closure of every removed odd-to-even
pair. The elementary cancellation warning in
`code/D_pd_cancellation_warning.py` rules out simply deleting the
pair. No such nonlinear cancellation, no bound on its coherence
generators, and no compatible target map have been constructed.

## Additional primary-source check

The Stacks Project, Section23.6, tag09PF, was opened in full online.
The warning after Definition23.6.5 explicitly distinguishes
differential compatibility from preservation of boundaries by
divided powers. Lemma23.6.9 constructs a nonnegative homological
Tate resolution of a ring map; Lemma23.6.11 gives its comparison
into a target with homology concentrated in degree zero. These are
not a simplicial positive-cochain completion theorem retaining the
specified low form rows and their maps. No such consequence was
imported. The exact URL and checked scope are saved in
`logs/D_late_source_inventory.tsv`.

A primary author-hosted DeBellevue dissertation URL returned502.
Its search snippet was not used as a theorem. Both the failed open
and the successful Stacks open are recorded in the same inventory.

## Formal movement assessment

As of the pre-10:21 review, this branch has no new coefficient case,
no resolved original open row, and no proved necessary or equivalent
strictly smaller gate for C3. C34 weakens a sufficient construction;
C35 refutes a particular proposed construction. Neither licenses a
reset of the user's no-movement count. The smallest unresolved base
for the original uniqueness/common-source question is still Z.
