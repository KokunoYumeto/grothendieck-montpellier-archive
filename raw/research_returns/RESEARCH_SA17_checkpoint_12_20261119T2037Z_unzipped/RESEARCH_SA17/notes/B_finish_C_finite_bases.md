# Complete finite-base extension

Agent dieudonne; run RESEARCH_SA17_FINISH-20261119;
GPT-6 Astra (OpenAI, ChatGPT Pro mode).
Full proofs are in sections/C_finish_finite_bases.tex, with references
in references/C_finite_bases.bib. Root and descent_groups independently
audited all three numbered statements. The compiled inclusion is owned
by root and belongs immediately after C_finish_finite_fields.

## Equality is decidable without a free polynomial basis

For A=R[x]/I with R finite and I finitely specified, every nonzero a
survives in some finite quotient A/m^N. Choose m containing Ann(a);
then a remains nonzero in A_m. Krull intersection gives a finite N
detecting it. A/m is finite by Nullstellensatz, and the successive
graded quotients m^j/m^(j+1) are finite, so A/m^N is finite.

Two searches decide whether a polynomial h belongs to I. One enumerates
bounded-degree combinations of the finite defining generators. The
other enumerates finite commutative ring tables, unital maps from R,
and evaluations of the generators satisfying the relations but with
h nonzero. The searches are dovetailed. Exactly one must eventually
succeed. Finite rings, not merely finite fields, are essential in the
second search: a nonzero nilpotent is invisible in every field.

This gives canonical representatives for the finite set of classes
of polynomials of degree at most d. These coefficient sets need not
be free R-modules. Hopf coaction identities are checked directly in
R[X,Y]/(orthogonality relations on X and Y). No unjustified
field-style Groebner freeness is used.

## Finite local representation category and QSS

Finite R splits effectively into finite local factors. On each factor
finite projectives are free; every idempotent summand of a finite free
representation remains free. The coaction, centralizer and conjugacy
searches are finite once the degree and rank are fixed. Minimal degree
is basis-invariant. All module isomorphism classes have specified least
representatives.

Endomorphism rings are finite. Fitting decomposition proves localness
on indecomposables; finite radicals are nilpotent and complete. These
are exactly the QSS categorical conditions, which do not require a
field base. The residue division ring is finite, hence a field, so the
same Z, Z/2, alternating, unitary and hyperbolic multiplicity-form
classification as in the finite-field section applies. Every generator
has a finite matrix construction, and every product/exterior power is
recovered by finite actual isometry search after decomposition.

The zero ring is handled separately. Global indecomposable indices
over a finite product are the local indices extended by zero to the
other factors. Operations are componentwise, including the unit.

## Primary-source search and actual openings

Searches included:

- finitely generated commutative rings residually finite word problem algorithm
- site.stacks.math.columbia.edu Krull intersection theorem
- site.stacks.math.columbia.edu Hilbert Nullstellensatz Theorem10.34.1
- finitely generated commutative rings residually finite

Opened Jaikin-Zapirain, Research in the Mathematical Sciences10(2023),44,
DOI10.1007/s40687-023-00408-9, full primary text:
https://link.springer.com/article/10.1007/s40687-023-00408-9 .
Section2.1, before Lemma2.1, records residual finiteness of finitely
generated commutative rings using local completions. The written proof
specializes the elementary argument to finite bases and explicitly
constructs the halting decision procedure. No novelty is claimed.

Opened Stacks00IP, Lemma10.51.4, and Stacks00FV, Theorem10.34.1(1).
Reread original QSS1979 pp269--273, including Prop2.4 transfer,
Prop2.5 existence/signs, and Thms3.2--3.3 and their three categorical
hypotheses. Local source: ../external_sources/C_finish/QSS1979.txt.
Primary URL: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/quebbemann2.pdf .

## Nonfield example and exhaustive certificate

For R=Z/9, S=Sym2(R^3), the complete endomorphism algebra is
E=R[I,K], K(A)=tr(A)I and K^2=3K. The sign/permutation argument reduces
the calculation to one plane rotation over the faithfully flat free
algebra R[z]/(z^2+1), with u=4z,v=z. Here u^2+v^2=1 and uv=5 is a unit.
The radical(3,K) has cube zero and quotient F3, so S is indecomposable.

The trace form Q and2Q give distinct residue square classes and differ
by exact order2 in split WG. The full code
code/B_finish_finite_base_forms.py exhausts all81 End elements,
54units,54 nonsingular invariant symmetric forms and2916 action
comparisons. It finds exactly two size27orbits, checks the only
idempotents are0 and1, verifies the faithfully flat rotation and the
rank12 double-sum congruence. Output:
logs/B_finish_finite_base_forms.json, actual run16:48:17UTC,
0.0553696949937148 seconds.

The code certifies this bounded example. The general equality algorithm
and canonical finite-base procedure are proved mathematically and are
not claimed to have been fully implemented.

## Records and source control

results_C_finite_bases.csv has three rows.
checks_C_finite_bases.tsv contains three own used/rechecked events,
and one actual executable certificate event. Root targeted audits are
recorded only in checks_finish_root.tsv.
checks_C_finite_bases_audit.tsv is the separate descent_groups audit;
its events are not copied into our file.
The independent Artinian-algebraically-closed audit is separately recorded
in checks_C_artinian_algclosed_audit.tsv, including the appended
non-Gorenstein example.

The earlier optional isolated TeX attempts failed before document loading
because the system formats were unavailable. Exact commands, exit statuses
and decisive errors are preserved in
logs/B_finish_C_templates_environment_failure.txt. Root uses the established
custom format and texmf for the actual full build; no further isolated
build attempts were made.
