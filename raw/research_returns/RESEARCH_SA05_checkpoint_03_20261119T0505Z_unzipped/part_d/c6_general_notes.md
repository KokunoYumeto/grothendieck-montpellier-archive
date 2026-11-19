# C.6, general motives: exact frontier after the abelian-type proof

Date: 2026-11-19. Author: GPT-6 Astra (OpenAI, ChatGPT Pro mode), Part D agent.

## Status

The entire abelian-type assertion is proved in `c6_insert.tex`, now integrated
into Part C and independently audited by the root and Part C agents. The
general-motive assertion is **not settled by the work in this note**. In
particular, no exact equivalence with a published named conjecture has been
established. The distinction matters because the prompt explicitly requires
an exact equivalence, not only a conditional implication.

The strongest correct conclusion currently available here is that Fontaine's
motivic Weil–Deligne compatibility conjecture implies the desired
independence. It is not justified to label the two assertions equivalent.
This is a remaining unresolved row, not a completed alternative permitted by
the prompt.

## Exact primary formulation of a sufficient conjecture

Fontaine, *Représentations l-adiques potentiellement semi-stables*,
Astérisque 223 (1994), 321–347:

- Section 2.4.1, p.342, distinguishes being defined over Q from admitting an
  actual Q-form.
- Section 2.4.2, p.342, defines compatibility after extension to common
  algebraically closed coefficient fields.
- Section 2.4.3, Conjecture C_WD(X,m), p.342, requires compatibility of the
  Weil–Deligne realizations of the cohomology of a smooth proper variety.
- Section 2.4.7, pp.344–345, gives the corresponding motivic formulation.
- Section 2.4.5, p.343, gives a weaker formulation using the characters of
  the graded pieces of the monodromy filtration.

Primary PDF opened and locally archived:
<https://www.numdam.org/item/AST_1994__223__321_0.pdf>.
Web reference `turn288595131view0`; relevant find output
`turn268205705view1`. Local file `sources/Fontaine1994VIII.pdf`.

The motivic formulation, rather than compatibility only of the ambient
cohomology, is needed for arbitrary absolute-Hodge or motivated projectors.
An unlabelled compatible vector-space representation does not by itself
identify the action on every prescribed tensor projector.

### Proof of the sufficient implication

Fix a finite place v of residue characteristic p and an auxiliary prime
ell different from p. Write the associated Weil–Deligne data as
(r_ell,N_ell), with finite inertial image for r_ell. On an open subgroup of
inertia the actual Galois representation is

\[
 \rho_\ell(\tau)=\exp(t_\ell(\tau)N_\ell),
\]

and generally it is the product of the finite-type factor with this
exponential. The restriction to inertia is trivial exactly when

\[
 N_\ell=0\quad\hbox{and}\quad r_\ell|_{I_v}=1.
\]

Indeed, triviality on the open subgroup forces N_ell=0, because the tame
character has infinite image and the exponential of a nonzero nilpotent
cannot be the identity at every value. The remaining finite quotient must
then act trivially. The converse follows directly from the formula.

Both conditions are preserved by extension of a coefficient field and by
isomorphism of Weil–Deligne representations. Therefore a compatible
motivic Weil–Deligne system proves independence of unramifiedness. This
argument does not require a choice of an actual rational form, and it does
not use the p-adic realization when the assertion only concerns ell != p.

The weaker monodromy-graded formulation also suffices: the characters at
the identity determine the dimensions of all monodromy graded pieces, so
concentration in degree zero is independent of ell and is equivalent to
N=0. Once N=0, the inertia image is finite; the common character is the
rank everywhere exactly when that finite representation is trivial.
Again, this proves an implication only.

## Why no converse follows formally

At a single coefficient field, let G be an algebraic group and J an
inertial image. The algebraic representations of G on which J acts
trivially are exactly those factoring through G divided by the smallest
closed normal subgroup containing J. Consequently the collection of
triviality tests determines this normal subgroup, not the whole inertia
representation. In a category defined over Q, tests on Q-representations
can contain still less information; no descent claim about an arbitrary
normal subgroup over Q_ell is being made here.

There is a concrete abstract Weil–Deligne example illustrating the lost
information even after all tensor constructions and finite base
extensions are allowed. Let q=4, G=SL3, and use the convention
F N F^{-1}=qN. Put

\[
 F_1=\operatorname{diag}(4,1,1/4),\quad N_1=E_{12}+E_{23},
 \qquad
 F_2=\operatorname{diag}(2,1/2,1),\quad N_2=E_{12}.
\]

The finite inertial types are trivial. Both pairs satisfy the required
relation, their Frobenius matrices have determinant one, and their
nilpotents have ranks two and one, respectively. Their Jordan types are
(3) and (2,1), so the pairs cannot be isomorphic.

For every rational algebraic representation r of SL3, however,

\[
 dr(N_1)=0\quad\Longleftrightarrow\quad r\text{ is trivial}
 \quad\Longleftrightarrow\quad dr(N_2)=0.
\]

The kernel of dr is an ideal in the simple Lie algebra sl3; a nonzero
nilpotent can lie in that kernel only if dr is zero. Since SL3 is
connected, a representation with zero differential is trivial. Thus
**every** representation in Rep(SL3) has the same unramified/nonunramified
answer for these two pairs. A finite field extension multiplies N by a
nonzero ramification index and leaves this conclusion unchanged.

For arithmetic Frobenius, the eigenvalues of F1 on the monodromy graded
pieces of indices -2,0,2 have absolute values q,1,q^{-1}; for F2 the
indices -1,0,1 have values q^{1/2},1,q^{-1/2}. Thus both pairs can even be
viewed as abstract pure Weil–Deligne representations of weight zero, with
the arithmetic Frobenius convention explicitly retained. A second
certificate replaces F2 by F1 and keeps N2: it gives the same entire Weil
part but different nilpotent rank, without asserting purity for that
modified pair.

Exact matrix certificates were executed in `check_c6_wd.py`; all
assertions passed and the full output is `check_c6_wd_output.json`. The
universal representation-theoretic statement follows from the preceding
Lie-algebra proof, not from finite enumeration.

**Scope of this example.** No pair is claimed to be the localization of
a global pure motive with a specified polarization and compatible global
system. It disproves a proposed *formal deduction* of full compatibility
from the unramifiedness flags. It does not prove logical inequivalence of
the corresponding arithmetic conjectures, and it is not a counterexample
to the user's general-motive assertion.

## Other named statements examined and why they do not close the gate

| Source or approach | Exact part examined | What it gives and what remains |
|---|---|---|
| Serre–Tate (1968), Appendix, printed p.514 | Problems 1 and 2; pp.515–516 Grothendieck's unnumbered quasi-unipotence proposition | Inertia characters and Weil-element characteristic polynomials. A nonzero unipotent operator has the same trace as the identity, so inertia characters alone do not detect N=0. The Appendix was scanned; the relevant three pages were rendered and read. |
| Ochiai, *l-independence of the trace of monodromy* | Introduction's Serre–Tate conjecture; Theorem B = Theorem 2.4; Corollary C = Corollary 2.6 | Independence of the alternating trace on all compactly supported cohomology, and of the alternating Swan conductor. It neither isolates an arbitrary motivic projector nor detects a unipotent N from its trace. |
| Saito, *Galois representations in arithmetic geometry* | Section 4 | Survey of local monodromy and trace comparisons. No theorem asserting the requested general iff was identified. |
| van Dobben de Bruyn (2020), *The equivalence of several conjectures on independence of l* | Introduction Theorem 1 and its precise finite-field setting | Exact equivalences between independence of homological equivalence, ranks of cycle-induced maps, and Betti numbers of varieties over an algebraic closure of a finite field. The missing bridge to arbitrary number-field local unramifiedness is not supplied by that equivalence. |
| Laskar (2013), *Frobenius conjugacy class of hyper-Kahler varieties over number fields* | Conjecture 1.1 (Serre) and introduction | The Serre formulation assumes good reduction in the sense that every auxiliary realization is unramified. It does not establish that this condition can be tested at one auxiliary prime. |
| Kisin–Zhou (2025), Theorem 1.2 and following discussion | Semistable G-valued Weil–Deligne compatibility; Section 5.3 | Gives a strong semistable theorem for abelian varieties; the authors explicitly distinguish descent to arbitrary bad reduction. The new abelian-type proof repairs just the unramifiedness case by a potentially good generator and finite-inertia trace, not by assuming this descent. |
| Neron–Ogg–Shafarevich on an arbitrary chosen generator | Apply to H1(A) while M is a tensor summand | Invalid implication: M unramified need not make A good. The valid abelian proof changes the generator by a weak Mumford–Tate lift; this construction is not available for all motives. |
| Motivic good-reduction or motivic NOS assertion | A motive with one unramified realization descends from a good integral motive | A stronger geometric existence assertion would imply independence by smooth proper base change. The converse requires additional geometric input; it is not a proven exact equivalence. |
| Conservativity of realizations with motivic nearby cycles | Attempt to express N or inertia through one common motivic object | A common faithful realization of an actual motivic inertia/nearby-cycle action would imply independence. Neither its existence for all absolute-Hodge/motivated projectors nor a converse to a named conservativity conjecture has been established here. |
| Scholl's local good-reduction conjectures for extensions | Published C3 formulations encountered through Gazda's exposition | These concern extension classes and local H1 conditions, not only pure objects with trivial inertia. No exact identification with the statement in C.6 was proved. |

The last three entries are approaches considered, not theorems imported
into the proof. No uninspected source is invoked as establishing them.

## Further primary-source checks after checkpoint 02

### Serre's original numbered conjectures

The original *Facteurs locaux* was obtained from the author's
College-de-France archive. Its printed pages 19-07 and 19-08 were rendered
and visually read, since the extracted text loses the displayed
statements C6 and C7. In section 2.3, **C3** is independence of the three
integers epsilon, delta and f, with epsilon the codimension of inertia
invariants and f the Artin conductor. **C5** is independence of the local
Euler polynomial on those invariants. Either statement, in its scope for
the full cohomology of a smooth projective variety, implies independence
of unramifiedness: epsilon=0, or equivalently the local Euler factor has
the full cohomological degree. No converse is furnished. Applying this
to an arbitrary prescribed motivic summand also requires a formulation
with its projector, rather than silently replacing that summand by its
ambient cohomology.

For the separate Part C weight check, **C6** bounds the integer weights
of those Euler roots between zero and the cohomological degree m; **C7**
asserts weight m if epsilon=0. Remark 2 on printed page 19-08 derives C7
from C6 in characteristic zero by the invariant perfect pairing. These
original numbers are unrelated to the user's label C.6.

### Lu--Zheng and the mixed-characteristic hypothesis

Lu and Zheng (2019), *Compatible systems and ramification*, Theorem 1.4,
proves the relevant individual monodromy-graded trace statement in
**equal characteristic**. This restriction is explicit. The stronger
boundary result, Theorem 1.2, starts from a notion of compatibility on
the henselian base which already requires local Weil traces at its
generic points (definition on page 1). Ordinary compatibility at good
primes of a number field does not supply that hypothesis. Remark
2.18(2) explains how the monodromy-graded statement recovers traces on
inertia invariants, but its equal-characteristic proof cannot be moved
to a number-field place without new input. Definition 4.3 and Corollary
4.6 use trace-based compatible ramification, which alone cannot detect
a nonzero unipotent logarithm.

### Ayoub's nearby-cycle conservation conjecture

Ayoub (2007), Conjecture 5.1 (author-preprint page 33), concerns
constructible rational motives over a **geometric DVR of
equicharacteristic zero**. Proposition 5.13 (page 39) is an equivalence
between the conservativity of two motivic specialization functors. It
does not identify either condition with auxiliary-prime independence
of local inertia at a mixed-characteristic place. Moreover,
conservativity of a triangulated functor detects zero **objects**; it
does not in general detect zero **morphisms**, such as a monodromy
operator. A proposed argument through N therefore still needs a
suitable motivic heart with faithful exact realization or a separate
zero-morphism theorem.

The author's current publication page explicitly flags a gap at
Theorem 8.3.10 of the later *Topologie feuilletee et la conservativite*
preprint and says that conservativity remains conjectural. The page
was archived on November 19, 2026. That withdrawn claim is not used.

### Ramification rigidity in families

The current author preprint of Cadoret and Tamagawa, *Rigidity
properties of ramification and applications*, was read at its
introduction, Theorem 1 and Theorem 56. Its named trivial-locus
conjecture, and Theorem 56 for Q-compatible families over number
fields, concern fibres whose **whole arithmetic monodromy group** is
finite or has unipotent identity component. This differs from the
triviality of one local inertia subgroup at a fixed finite place. The
general rigidity theorem compares pointwise and global ramification
for one representation; it does not compare distinct auxiliary
realizations. No exact equivalence for the present question follows
from those statements as written.

## Remaining work, stated without promoting the gate to a solution

A sharper conditional reduction is now proved in
`c6_chow_conditional.tex`.  If a homogeneous rational **algebraic**
projector defines M, Saito (2003), Theorem 0.1 (more generally 3.1),
supplies common rational traces of every local Weil element on M.
If the Frobenius roots at the one unramified realization all have the
same complex absolute value, the relation FNF^{-1}=q^{-1}N forces
N=0 at every auxiliary prime; the common finite-inertia character then
forces inertia to be trivial.  Weight--monodromy for the ambient
cohomology at the single prime is a sufficient named hypothesis.
This is an implication, not an exact equivalence.  It also identifies
separately the trace/projector issue and the purity/monodromy issue.

The proof of Saito's Theorem 3.1 was read in section 3, not inferred
from the title: Lemma 3.2 reduces semistable correspondence traces to
intersection numbers on proper smooth strata, while Lemma 3.3 returns
from an alteration by degree-normalized trace with its conjugate
components.  The explicit factor (-1)^i when the algebraic projector
isolates H^i is retained in the supplementary proof.  The supplied
transcription of 12:140 was reread: its definition of smooth
semisimple isomotive only assumes unramifiedness on S[1/ell].  There
is no additional Frobenius-purity hypothesis hidden in that definition.
No original scan was supplied, so this is a transcription-level check.

The smallest remaining *scope* is a pure motive over a number field which
is not known to lie in the abelian tensor category, at one bad-reduction
place, with one unramified auxiliary realization. The problem is already
meaningful for a projected middle cohomology summand in dimension at least
three outside the known abelian-type/automorphic cases. No particular
variety is claimed to be the smallest undecided example.

To finish the requested general row one must either prove that
unramifiedness for that class of motives is independent of the auxiliary
prime, or give both implications to a genuinely published named
conjecture with the exact same quantified scope. Merely calling the
trivial-inertia part of C_WD a new conjecture name would not do that.

The remaining source route is to inspect modern motivic nearby-cycle
conservativity and arithmetic compatibility results for a theorem which
controls the kernel of the full inertia action on arbitrary rational
projectors. The arithmetic equal-characteristic ramification theorems
found in search cannot automatically be used at mixed-characteristic
number-field places.
