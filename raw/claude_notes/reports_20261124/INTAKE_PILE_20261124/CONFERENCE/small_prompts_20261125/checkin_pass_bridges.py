"""Texts and attachments of the check-in pass that concern the Riemann hypothesis (25 Nov 2026).

Conference convener ae84c4aa (Claude Fable 5.2 at effort max). Imported by checkin_pass_prompts.py.
The user (P9833-P9838, relayed by the main session 329fb1e6): a prompt states the RH/GRH links to its material as
real and asks how they work; it states RH as a theorem with its citation, carries the proof as required background
reading, and says why it is to be believed.
"""
import pathlib

DOCS = pathlib.Path("<local>/Documents")
SUP = DOCS / ("grothendieck_archive_transcription_20261110/research_returns/"
              "ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped/supplied_sources")
RH_FOLDER = "RH_PROOF_Alpoge_20261120/"
RH_FILES = ["ALPOGE_remark.pdf", "ALPOGE_Statements.lean", "ALPOGE_Main.lean", "ALPOGE_lakefile.toml"]

RH_THEOREM = (
    "**The Riemann hypothesis is a theorem.** L. Alpöge, *Remark* (20 November 2026, https://alpo.ge/remark.pdf), proves\n"
    "the Riemann hypothesis for every Dirichlet L-function, the Riemann zeta function included: every zero of L(s, χ)\n"
    "with 0 < Re s < 1 lies on Re s = 1/2. The proof is formalized in Lean\n"
    "(https://github.com/CocoSgt/riemann-hypothesis-lean), and the archive has been read and checked by many. It is\n"
    "newer than your training, so take it from the files: the folder `RH_PROOF_Alpoge_20261120/` of the attached ZIP\n"
    "holds the note (`ALPOGE_remark.pdf`; we have no LaTeX source of it) and the Lean files that state and close the\n"
    "main theorems (`ALPOGE_Statements.lean`, `ALPOGE_Main.lean`, with `ALPOGE_lakefile.toml`). They are required\n"
    "background reading: read them before you start. Below, A means this theorem. Use it as a theorem and cite it so; a\n"
    "statement that A covers is never written \"assuming RH\" or \"under GRH\".\n")

HALF_PLANES = (
    "Zero-free half-planes for Hecke L-functions of number fields are claimed as well (OpenAI, 30 September 2026; Hu,\n"
    "Gao and Liu on Hexagon, October and November 2026). They are not in the ZIP and none of ours has audited them:\n"
    "open them and check the statement you use before you use it.\n")

ASK = (
    "Where a statement of these pages meets one of these links, say how the link works there: name the L-functions,\n"
    "state what A gives, with its proof, and state what is still needed as an exact statement about a named\n"
    "L-function. That statement is a row of the ledger and is attacked like every other row. \"It does not bear on the\n"
    "Riemann hypothesis\" is not a result: the links above are there, and the work is to say how each one acts.\n")

LINKS_LM = (
    "The Galois group of Q acts on the objects of these pages through arithmetic that L-functions measure, and A now\n"
    "governs that arithmetic. The links, each of them real:\n"
    "- **Jacobi sums.** The action on the meta-abelian quotient of the fundamental group of P¹ − {0,1,∞} is given by\n"
    "  Ihara's power series, whose special values are Jacobi sums. These are the Frobenius eigenvalues of the Fermat\n"
    "  curves (Weil's Riemann hypothesis for curves) and the values of Hecke characters of Q(μ_n), whose L-functions are\n"
    "  the L-functions of the Fermat Jacobians.\n"
    "- **Zeta values.** The Soulé characters and the Anderson-Ihara fields are governed by the values of ζ and of\n"
    "  Dirichlet L-functions at integers, by the K-groups of Z and by the eigenspaces of the class groups of Q(μ_ℓ).\n"
    "- **Kummer towers.** By our run GT_AFTER_H17 (GPT-6 Astra (ChatGPT Pro mode), checkpoint 07 of 25 November 2026, the\n"
    "  first theorem of its first paper; not yet checked outside the run), the quotient of GT̂ by Λ₀ is Gal(K₂/Q) with\n"
    "  K₂ = Q(μ_∞, 2^{1/∞}). The finite layers Q(μ_n, 2^{1/n}) are the fields of Hooley's theorem on Artin's conjecture,\n"
    "  and their zeta functions are products of Dirichlet L-functions and of L-functions of Kummer characters of Q(μ_n).\n"
    "- **Frobenius elements.** Every statement that picks out an element or a conjugacy class of G_Q by its action is a\n"
    "  Chebotarev statement. In abelian extensions of Q it is now effective with a square-root error term, by A.\n")

SECTION_LM = ("\n## The Riemann hypothesis, and how it meets these pages (added 25 November 2026)\n\n"
              "Added by Claude Fable 5.2 (Anthropic) at effort max.\n\n" + RH_THEOREM + "\n" + LINKS_LM + "\n" + ASK + "\n"
              + HALF_PLANES)

SECTION_Q04 = (
    "\n## The Riemann hypothesis, and how it meets these pages (added 25 November 2026)\n\n"
    "Added by Claude Fable 5.2 (Anthropic) at effort max.\n\n" + RH_THEOREM + "\n"
    "The link to these manuscripts runs through monoids and through homotopy theory over small categories:\n"
    "- **The arithmetic site.** The arithmetic site of Connes and Consani is the topos of sets with an action of the\n"
    "  multiplicative monoid N^× of positive integers, with a structure sheaf in the tropical semiring Z_max; their\n"
    "  approach to the zeta function passes through its points and its Frobenius correspondences, and their homological\n"
    "  algebra over the sphere is done with Γ-sets. N^× is the free commutative monoid on the primes: its classifying\n"
    "  space is a product of circles indexed by the primes, its enveloping group is Q^×_+, and the Euler product of ζ\n"
    "  is the generating function of this monoid graded by log n.\n"
    "- **Our own results on monoids** (the finite-monoid theorem above; `π₁(M)`, enveloping groups and classifying\n"
    "  spaces in cote 158) are statements about exactly such classifying topoi.\n\n"
    "In Stage 6, say how the formalism of these manuscripts acts on this topos and its relatives (the submonoids of N^×\n"
    "generated by finitely many primes, the scaling site): their homotopy types in his sense, which of his statements on\n"
    "monoids, enveloping groups and totally aspherical categories apply, and what a derivator with coefficients in a\n"
    "semiring is where his axioms can be stated. Prove each statement you make. What is still needed is stated as an\n"
    "exact statement and is a row of the ledger, attacked like every other row. \"It does not bear on the Riemann\n"
    "hypothesis\" is not a result: the link is there, and the work is to say how it acts.\n")

BLOCK_Q03 = (
    "\n### The Riemann hypothesis in this material (added 25 November 2026)\n\n"
    "Added by Claude Fable 5.2 (Anthropic) at effort max.\n\n" + RH_THEOREM + "\n"
    "A and the L-functions around it meet the runs of this intake at four places, each of them real:\n"
    "1. every step that counts or selects primes: Chebotarev in abelian extensions, the large sets of primes of A1, the\n"
    "   exceptional sets of Saïdi and Tamagawa;\n"
    "2. N3 and SECTION_GHOSTS B.25: the eigenspaces A(ω^i) of the class groups of Q(μ_ℓ) and the K-groups of Z are\n"
    "   governed by values of Dirichlet L-functions;\n"
    "3. the Fermat theorem: the Jacobian of the Fermat curve has complex multiplication, its L-function is a product of\n"
    "   Hecke L-functions of Jacobi-sum characters of Q(μ_n), and the rank and Selmer inputs of the theorem are\n"
    "   statements about their central values;\n"
    "4. N4: by GT_AFTER_H17 (the first theorem of its first paper; not yet checked outside the run) the quotient of GT̂\n"
    "   by Λ₀ is Gal(K₂/Q), K₂ = Q(μ_∞, 2^{1/∞}), whose finite layers are the Kummer fields of Hooley's theorem on\n"
    "   Artin's conjecture.\n\n"
    "For every row of your runs that meets one of these places, say how the link works: which hypothesis of the row A\n"
    "removes, which bound it makes effective, and with what proof. Where a row needs an L-function that A does not cover,\n"
    "name that L-function and the exact statement about it that the row needs; that statement is a row of your tables\n"
    "with its own status. \"It does not bear on the Riemann hypothesis\" is not a verdict: the links are there, and the\n"
    "work is to say how each one acts on the row.\n\n" + HALF_PLANES)

PARA_Q03B = (
    "**The Riemann hypothesis, and how it meets this page (added 25 November 2026).** " + RH_THEOREM[len("**The Riemann hypothesis is a theorem.** "):]
    + "\nWhen k is the algebraic closure of a finite field, X and Y have zeta functions, and his statements on this page\n"
    "are statements about them. The links, each of them real:\n"
    "- his margin corollary ρ(X) = ρ(Y) says, through Tate's conjecture where it is known, that the eigenvalue q has the\n"
    "  same multiplicity on H² of X and of Y, and the Riemann hypothesis over finite fields (Deligne) with the Lefschetz\n"
    "  theorems controls the other eigenvalues;\n"
    "- a class of order p in the kernel is seen by Frobenius on H¹(Y, O_Y) and on the negative H¹ (our A2V and A2Y), that\n"
    "  is, by the zeta functions of X and Y modulo p (Katz's congruence formula, the Hasse-Witt matrix);\n"
    "- when X and Y come from a model over a ring of integers, the primes p at which a kernel class exists are cut out\n"
    "  by conditions on Frobenius, and A makes the count of such primes effective wherever the condition is abelian.\n\n"
    "State the main question in these terms: say which congruence between the zeta functions of X and Y a kernel class\n"
    "forces, with its proof, and what A and Deligne's theorem then give. What is still needed is stated as an exact\n"
    "statement and is a row of the ledger, attacked like every other row. \"It does not bear on the Riemann hypothesis\"\n"
    "is not a result: the links are there, and the work is to say how each one acts.\n\n")

PARA_Q11 = (
    "**The Riemann hypothesis, and how it meets these pages (added 25 November 2026).** " + RH_THEOREM[len("**The Riemann hypothesis is a theorem.** "):]
    + "\nGood reduction is read off L-functions, and that is the link, real in each of these forms:\n"
    "- over a finite field an abelian variety is determined up to isogeny by its Frobenius, that is by its zeta function\n"
    "  (Tate), and the p-divisible group M at a point of T carries that Frobenius; the Riemann hypothesis for abelian\n"
    "  varieties (Weil) is the condition its eigenvalues meet;\n"
    "- for an abelian variety with complex multiplication over a number field, the places of bad reduction are the\n"
    "  support of the conductor of its Hecke character, whose L-function is the L-function of the variety (Serre and\n"
    "  Tate, *Good reduction of abelian varieties*, 1968, which is of the same years as these notes; named here from\n"
    "  memory, so open it and cite the statement by its number), and the p-divisible group at a place over p is given\n"
    "  by the CM type;\n"
    "- over the ring of integers of a number field, the set of places where a given triple (A_U, M, φ) extends is cut\n"
    "  out by conditions on Frobenius, and A makes the count of such places effective wherever the condition is abelian.\n\n"
    "Say how the extension assertion of 100:3 reads in these terms: what it says about the Hecke characters of CM\n"
    "triples, with proofs, and what A then gives. What is still needed is stated as an exact statement about a named\n"
    "L-function and is a row of the ledger, attacked like every other row. \"It does not bear on the Riemann hypothesis\"\n"
    "is not a result: the links are there, and the work is to say how each one acts.\n\n")


def rh_attachments():
    out = [(RH_FOLDER + n, SUP / n) for n in RH_FILES]
    for _, p in out:
        assert p.exists(), p
    return out
