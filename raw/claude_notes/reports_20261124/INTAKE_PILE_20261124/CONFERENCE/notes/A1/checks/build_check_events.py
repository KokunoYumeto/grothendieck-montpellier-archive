# Builds ../CHECK_EVENTS.tsv for the note gt_monoid_note.tex (columns as in the other notes of the project).
import io
import os

WHO = "Claude Fable 5.2 at effort max (conference convener, writer of the note)"
D = "2026-11-25"
H = ("statement_id", "date", "who", "type", "outcome")
R = [
    ("Theorem E(a) (= LM4_SUCCESSOR C.29): unit exponents give an automorphism; exponents equal for m >= 2", D, WHO,
     "independent re-proof",
     "holds: proved before the run's proof was opened (boundary classes of a finite cover satisfy one relation; m "
     "degree-one components with unit coefficients must be all the components; degrees over one boundary add up to "
     "the index), then the run's proof read line by line (C_further.tex l.474-506): the same argument. The note's "
     "proof is written through Lemmas 2.1 and 2.2."),
    ("Theorem E(a) (= LM4_SUCCESSOR C.29)", "2026-11-24",
     "Claude Opus 5.5 at effort high (LONGUE_MARCHE_A cluster reader of the intake pile)", "targeted proof check",
     "holds: every step followed (INTAKE_LM4_SUCCESSOR_20261124_CHECK_EVENTS.tsv, row C.29). Copied here from that "
     "file."),
    ("Lemma 3.1 (= LM4_SUCCESSOR C.30, equations C.30.2 to C.30.4): phi(xy) = h (xy)^lambda h^-1, h = x^m f(z,x)", D,
     WHO, "targeted proof check",
     "holds: recomputed twice, once in the run's cyclic form of (II) and once in the form of the note (relation (II) "
     "as in Boavida de Brito-Horel-Robertson, Definition 7.2); the substitution (x,y) -> (x,z), w = xyx^-1 = z^-1yz, "
     "the three values of f, and the product of the two rearranged equations. The computation uses neither "
     "invertibility nor that lambda is a unit."),
    ("Lemma 3.1 (= LM4_SUCCESSOR C.30)", "2026-11-24",
     "Claude Opus 5.5 at effort high (LONGUE_MARCHE_A cluster reader of the intake pile)", "targeted proof check",
     "holds: (C.30.2)-(C.30.4) re-derived by hand (INTAKE_LM4_SUCCESSOR_20261124_CHECK_EVENTS.tsv, row C.30). Copied "
     "here from that file."),
    ("Theorem E(b): on a sphere with m >= 3 holes the common exponent is 0 or a unit", D, WHO,
     "used and rechecked in this run",
     "the writer's own statement and proof, re-derived three times; NO SECOND READER. Steps: phi(F) lies in the kernel "
     "U of F -> H_1(S;Z/p) when p divides mu; every boundary component of S_U has degree p, there are m p^(m-2) > m "
     "of them; the classes of the phi(c_j) are nu times m distinct boundary classes; their sum is not zero in "
     "H_1(S_U;Z); Z-hat is torsion-free; so nu = 0."),
    ("Theorem E(b), homological input for the pair of pants", D, WHO, "computation or formal certificate",
     "checks/check_fermat_cover.py: in the cover of the wedge of two circles with group (Z/p)^2, p = 2, 3, 5, 7, the "
     "3p closed walks x^p, y^p, z^p span a lattice of rank 3p - 1, their sum is zero, and b1 + b2 + b3 is nonzero for "
     "every choice of one walk of each kind. Output: ALL AS CLAIMED."),
    ("Theorem A: (I) and (II) with lambda in 1+2Z-hat give lambda a unit and phi an automorphism", D, WHO,
     "used and rechecked in this run",
     "deduction from Lemma 3.1 and Theorem E(a), (b) for the sphere with three holes; the unit clause rests on "
     "Theorem E(b) and has NO SECOND READER. For unit lambda the statement is LM4_SUCCESSOR C.30, checked as above."),
    ("Proposition C: lambda = 1, f = [x,y]^k (k = 1, 2) satisfies (I) and phi is not surjective", D, WHO,
     "computation or formal certificate",
     "checks/check_examples.py, both conventions for the product of permutations: k = 1 in A_4 with x -> (123), "
     "y -> (124): f -> (12)(34), f^-1 y f -> (132), image of order 3; k = 2 in S_3 with x -> (12), y -> (13): "
     "f^-1 y f -> (12), image of order 2; the run's example k = 2 in A_5: image of order 12. Relation (I) holds "
     "identically. The cases k = 1 (A_4) and k = 2 (S_3) were also computed by hand. checks/search_examples.py "
     "lists all such pairs in S_3, S_4, S_5."),
    ("Lemma 5.1: a closed submonoid of a profinite group is a subgroup", D, WHO, "used and rechecked in this run",
     "holds: gamma^(n!-1) tends to gamma^-1. The run's C.30 has the same argument."),
    ("Corollary D(a): the Grothendieck-Teichmueller monoid equals its group of units", D, WHO,
     "used and rechecked in this run",
     "deduction from Theorem A, Lemma 5.1, continuity of (lambda,f) -> phi and compactness; the monoid structure is "
     "taken from Horel, Definition 7.1 (arXiv:1504.01605v2, text read) and Boavida de Brito-Horel-Robertson, "
     "Definition 7.2 (arXiv:1703.05143v1, text read). NO SECOND READER for the deduction."),
    ("Corollary D(b), (c): inputs Boavida de Brito-Horel-Robertson Proposition 7.3, Theorems 8.4, 11.1; Horel "
     "Theorems 7.2, 8.4", D, WHO, "carried as background without fault found",
     "statements read in the arXiv texts (1703.05143v1; 1504.01605v2); the proof of Proposition 7.3 read (it rests on "
     "Lemma 7.1, on Drinfeld 1990 section 4 and on Fresse's book, none of which was opened); the proofs of the "
     "theorems not checked."),
    ("Remark 5.3 (= LM4_SUCCESSOR C.31): the route through braid groups", D, WHO, "targeted proof check",
     "the torsion argument holds given phi_n(z_n) = z_n^lambda and torsion-freeness of the completed braid group. The "
     "run's derivation of phi_n(z_n) = z_n^lambda from the ribbon operad (Definition 6.4, Propositions 7.7, 8.1 of "
     "Boavida de Brito-Horel-Robertson) was NOT checked. The inductive derivation given in the remark is the writer's "
     "and has no second reader. Serre (I.2.6, I.3.3) and Chow 1948 are cited from memory, not opened."),
    ("Remark 5.3 (= LM4_SUCCESSOR C.31), torsion argument", "2026-11-24",
     "Claude Opus 5.5 at effort high (LONGUE_MARCHE_A cluster reader of the intake pile)", "targeted proof check",
     "holds given its cited inputs, which were not opened (INTAKE_LM4_SUCCESSOR_20261124_CHECK_EVENTS.tsv, row C.31). "
     "Copied here from that file."),
    ("Remark 5.3: delta_n^n = delta_(n-1)^(n-1) y_n in B_n, the two factors commute", D, WHO,
     "computation or formal certificate",
     "checks/check_full_twist.py: verified for n = 2..6 in Artin's faithful action on the free group. Output: ALL AS "
     "CLAIMED. An induction (delta_n^k = delta_(n-1)^k s_(n-1)...s_(n-k) for k <= n-1) gives it for all n."),
    ("Lochak-Schneps 2006: the definition of GT-hat with the invertibility requirement, and Question 1.1", D, WHO,
     "used and rechecked in this run",
     "read at the source (author's PDF, text of pp. 3-4): the requirement, the sentence quoted in section 1.1 of the "
     "note, both halves of Question 1.1, and the remark that it concerns the full profinite setting only."),
    ("Fresse's survey, arXiv:1811.12536, section 2.6: no simple characterization of the invertible pairs in the "
     "profinite setting", D, WHO, "carried as background without fault found",
     "read through an automatic summary of the arXiv HTML that quoted the sentence used; the text itself was not "
     "opened. To be opened by the next reader."),
]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "CHECK_EVENTS.tsv")
with io.open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write("\t".join(H) + "\n")
    for r in R:
        assert len(r) == 5 and all("\t" not in x and "\n" not in x for x in r)
        f.write("\t".join(r) + "\n")
print(len(R), "events written")
