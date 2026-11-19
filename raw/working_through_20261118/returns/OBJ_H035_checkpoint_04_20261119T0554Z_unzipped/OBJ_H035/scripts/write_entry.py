"""Write the complete entry from the checked inventory; results are a separate phase."""
from pathlib import Path
import csv,hashlib,sys
from datetime import datetime,timezone

root=Path(__file__).resolve().parents[1]
with (root/'STATEMENTS.tsv').open() as stream: rows=list(csv.DictReader(stream,delimiter='\t'))
with (root/'NOTES_VERDICTS.tsv').open() as stream: notes=list(csv.DictReader(stream,delimiter='\t'))
after_results='--results' in sys.argv
stamp=datetime.now(timezone.utc).isoformat()
text=r'''# H035 — Coherent modules from a functor and prorepresentability

**Working entry. The central Theorem 12 is proved in the reconstruction below;
H035.39–40 remain open. This is not a completed audit certificate.**

This entry separates the manuscript, later sources, and this run's mathematics.
The six supplied model notes are treated as leads. There are 46 statement rows,
44 individually adjudicated note subclaims, and 32 disputed-reading rows.
The complete proofs, counterexamples and current open arguments are in
`PROOFS.tex`; the second checks are in `research/SECOND_CHECKS.md`.
All work was done in one stream. “Second check” means a new derivation from
the hypotheses by the same model, not another reader or a formal certificate.

## 1. The object in his terms and in current terms

> « Construction de faisceaux de modules »

The cover names the construction of module sheaves from functors and an
application to prorepresentation along a section (94/002.1–15). The central
working object is a covariant functor from modules to sets. The problem is to
recover a finite module P for which the functor is naturally Hom(P,−).
The later sheets apply the criterion to proper Hom functors and to affine
restriction of scalars. The cover's final Ω¹-expression has an unidentified
following mark; its meaning is not supplied from the later argument.

**Our terminology.** “Finite” means finitely generated; over a noetherian
ring this is equivalent to finitely presented. A strict prorepresentation
is a filtered colimit of Hom(P_i,−) with finite P_i and surjective inverse
transition maps. Eventual stationarity means actual isomorphisms of the
transition maps beyond a stage, a stronger assertion than isomorphism of
the pro-object with a constant object. These distinctions decide H035.29.

A left exact set-valued functor on modules has a canonical module structure:
apply it to the addition, scalar and finite-product diagrams. This fact,
proved in H035.2, makes the subsequent tensor comparisons meaningful. Once
left exactness is removed, additivity and A-linearity must be stated. The
question mark attached to additivity in Remarque 18 is therefore substantive.

> « module de différentielles pour un C.M. »

The heading on 94/011.1 is retained as written. The parameter-quotient
property beneath it is the property of a canonical module of a
Cohen–Macaulay local ring. That identification is our reconstruction,
proved in H035.16. It is not a corrected reading of the word, and it would
be false if interpreted as ordinary Kähler differentials. The later
“faisceau fondamental” is used in this canonical-module sense, with the
normalization specified in the proofs.

> « foncteur constructible »

On 94/022 the proposed name refers to the non-left-exact conditions of
Theorem 12. It must not be identified without proof with a functor having
a finite presentation by Hom functors in Auslander's sense. That smaller
category has useful closure properties, but the full composition assertion
under the manuscript's axioms remains the main unresolved continuation here.

## 2. Where he writes about it, in page order

The source is Montpellier cote 94, catalogued as *Dualité des modules /
Construction de faisceaux de modules: notes manuscrites (s.d.)*, with the
catalogue qualification **[à partir de 1965]**. No exact date is written on
the relevant mathematical leaves. The inserted absolute-value typescript
has no established author or separate date in the supplied evidence.
The official [cote 94 PDF](https://grothendieck.umontpellier.fr/94.pdf) was
opened and the additional relevant pages were inspected personally.

| Scans | Content and status of the leaf |
|---|---|
| 002 | Cover: construction of module sheaves; prorepresentation along a section; unidentified invariant notation. |
| 003–005 | Restriction of scalars, faithfully flat descent, principal completion and noetherian induction: Lemme 1, Lemme 2, Proposition 3. |
| 005–007 | Complete-local criterion and strict prorepresentation: Proposition 4 and Lemme 5. |
| 008 | Remarque 5 bis: constructible rank and the flawed converse, repaired using an additional finite-value hypothesis. |
| 009–010 | Generic graded freeness, Tor vanishing and Hom base change; two distinct errors in the written Hom-complex argument. |
| 011 | Canonical-module reconstruction, regular and parameter quotients, generic existence; EGA/excellence margin. |
| 012 | Separate absolute-value typescript, outside H035. Included only because the supplied notes make mathematical claims about it. |
| 013 | Continuation of Corollaire 10, parameter Hom detection, cancelled Corollaire 11 and its reformulation note. |
| 015–017 | Rewritten Corollaire 11; Theorem 12 and its proof; Remarque 13. The missing strictness in the rewrite is separated from the strict system actually supplied to the theorem. |
| 018 | Proper Hom representability, quasi-coherent extension and arbitrary base change: Theorem 14. |
| 019–021 | Higher underived Ext/cohomology functors and generic regular-quotient comparisons: Lemmas 15–17. |
| 022 | Remarque 18, the prospective constructible-functor theory; Theorem 19 on affine restriction of scalars. |
| 023–024 | Finiteness refinements, closed immersions, cones, the Murre pointer and Remarque 21. |

The initial citations covered only scans 2–13. Targeted searches for the
names and notation in the supplied whole-folder transcription located
15–24; the folder was not read through indiscriminately. Scan 14 is an
intervening documentary report about local fields and is not imported into
the mathematical argument. The scan numbers above are PDF positions, not
the handwritten folio numbers.

Locators count main written horizontal rows from the top, including headings,
displays and cancelled rows; interline and marginal additions use “a” and “m”.
The convention and principal anchors are in `readings/LINE_INDEX.md`.
Every disputed locus also has a pixel crop in `readings/`, with coordinates
in `CROP_MANIFEST.tsv`. The original transcriptions have not been rewritten.

## 3. His statements, precise reconstructions and verdicts

Each quotation below is the manuscript's short phrase, on its own. The
following paragraph is this run's precise formulation. “False as written”
is accompanied by the counterexample and the strongest corrected version
proved here; it does not mean every surrounding conclusion fails. The
two open rows remain working items, with their reduction and failed
approaches preserved rather than presented as settled.

'''
for row in rows:
    text+=f"### {row['id']} — {row['locator']}\n\n"
    text+=f"> « {row['his_words']} »\n\n"
    text+=f"**Our precise formulation.** {row['statement']}\n\n"
    text+=f"**Reconstruction or textual qualification.** {row['reconstruction']}\n\n"
    text+=f"**Status:** {row['status']}. **Proof and check:** {row['proof_or_reference']}.\n\n"
    text+=f"**Literature:** {row['later']}\n\n"
    text+=f"**Date:** {row['date']}. **Confidence:** {row['confidence']}.\n\n"

text+=r'''## 4. Groundwork beside the manuscript

### The proof of the central criterion

**Our proof structure.** First recover finite representers after localizing
at each prime, using the completed-local condition and artinian Matlis
duality. Constructible residue rank then gives generic representation on
integral quotients, because Theorem 12(iv) supplies precisely the finite-value
hypothesis missing in Remarque 5 bis. The minimal-support argument produces
a strict system of finite modules representing the functor pro-objectwise.

Next choose a finite module Ω canonical on a **dense** open. Density matters
on a reducible base: it guarantees intersection with the merely nonempty
open furnished by (vi). On that intersection, finite F(Ω) and the parameter
comparisons make the strict system stationary. The repaired Corollaire 11
uses a commutative square whose right vertical map is injective by strictness;
surjectivity follows from the upper comparison. It does not assume base
change for each individual Hom stage. Finally Proposition 3's noetherian
induction and principal-completion gluing return a finite representer on A.

The proof passes the axioms to quotient rings, using exactness of noetherian
completion. It does not assume that arbitrary localization commutes with
completion. It uses the valid regular-embedding/Gor-2 version of the
canonical-module assertion, not the false CMU-only enlargement. Nor does it
use the false Z¹ two-Tor criterion. These distinctions are why the theorem
survives defects in several intermediate drafts.

### Standard inputs, with checked locators

| Input | Role | Opened source or proof |
|---|---|---|
| Finite-limit preservation and canonical linearity | Turns the set-valued functor into an A-linear functor and supplies the canonical tensor maps. | Direct diagrams, PROOFS.tex H035.2; no extra hypothesis hidden. |
| Flat modules as filtered colimits of finite free modules | Flat scalar extension for additive finitary functors. | [Stacks 058G, Theorem 10.81.4](https://stacks.math.columbia.edu/tag/058G). |
| Faithfully flat module descent | Descends local/completed representing modules and their finiteness. | [Stacks 023N, Proposition 35.3.9](https://stacks.math.columbia.edu/tag/023N); H035.3 gives the equalizer reduction. |
| Exactness and flatness of noetherian completion | Quotient inheritance and completed-module gluing. | [Stacks 00MB, Lemma 10.97.2](https://stacks.math.columbia.edu/tag/00MB); H035.4 gives compatible presentations. |
| Artinian Matlis duality | Finite representers from the injective cogenerator; parameter Hom detection. | [Stacks 08Z9, Proposition 47.7.8](https://stacks.math.columbia.edu/tag/08Z9). |
| Krull intersection | All parameter-power tests detect a zero kernel. | [Stacks 00IP, Lemma 10.51.4](https://stacks.math.columbia.edu/tag/00IP). |
| Canonical modules and CM duality | Interprets Ω and its regular/parameter quotients. | [Stacks 0DW3](https://stacks.math.columbia.edu/tag/0DW3), [0DW4](https://stacks.math.columbia.edu/tag/0DW4), and [0B5A, Lemma 47.16.7](https://stacks.math.columbia.edu/tag/0B5A); H035.16–18 give the quotient arguments. |
| Relative generic freeness | Handles coherent coefficients finite over finite-type algebras, not necessarily finite over the base. | [Stacks 051S, Lemma 10.118.2](https://stacks.math.columbia.edu/tag/051S); H035.11–12 and H035.37 give the nilpotent-filtration argument. |
| Proper formal functions in the pro-category | Makes higher underived Ext commute with the actual formal-module tests. | [Stacks 02OB, Lemma 30.20.4(1),(3)](https://stacks.math.columbia.edu/tag/02OB) and [02OC, Theorem 30.20.5](https://stacks.math.columbia.edu/tag/02OC); H035.34 spells out the spectral-sequence step. |
| Quasi-coherent approximation | Extends Hom representation from finite presentation to arbitrary quasi-coherent source. | [Stacks 01PJ, Lemma 28.23.6](https://stacks.math.columbia.edu/tag/01PJ). |

All uses have individual check events. Sources checked only as background
are labeled as such in `CHECK_EVENTS.tsv`; opening or reading a page is
not recorded as an independent proof of its contents.

### Corrections that change the mathematics

The most substantial false assertion before the main theorem is the
converse in Remarque 5 bis. The flat module Σ_p(1/p)Z has free rank-one
localizations at every prime and constant residue rank, but it is not finite
on any nonzero principal open. The proof on the page explicitly invokes
finite generation of F(N), which its earlier hypotheses do not provide.
Theorem 12(iv) repairs this without changing that theorem.

The two errors on scan 10 are independent. The Hom complex needs Q as its
coefficient, while the written P gives the wrong dimensions even over a
field. Separately, Tor₁ with cycles Z¹ is insufficient: the explicit
k[x,y]/(xy) example satisfies both written vanishings and fails base change.
Using the boundary module B¹, or the specified stronger Tor₂ condition,
repairs the criterion. The generic Hom theorem itself is true.

The CMU margin is false for a different reason. Cohen–Macaulayness of a
dense open in every integral closed subset does not provide a generic
canonical module. The explicit noetherian one-dimensional example in
H035.21 has non-Gorenstein local rings in every open; modulo its local
parameter t³, the socle has basis t⁴,t⁵. A finite generic rank-one canonical
module would be free on a smaller open, contradicting that socle dimension.
The valid uniform replacement is Gor-2; excellence implies it.

Other literal defects are kept separate: the zero quotient in Proposition 3,
zero f in Lemme 5(v), lost strictness in the rewritten Corollaire 11, “s∈S”
instead of the dense open in Lemme 17, the missing pushforward in the cone
formula, and coherent modules called vector bundles. The absolute-value
leaf has its own normalization, positive-exponent and nonzero-element
issues; those do not belong to the representability argument.

## 5. What became of these claims

### Published mathematical counterparts

The folder's loose dating does not establish that every sheet precedes or
follows a particular publication. The table identifies exact mathematical
counterparts and differences, not an undocumented chain of influence.

| Date | Opened source | Exact relevance |
|---|---|---|
| 1961 | [EGA III₁, 4.5.1–3, pp.138–139](https://www.numdam.org/item/PMIHES_1961__11__5_0.pdf) | Coherent Ext and formal completion. The pro-Artin–Rees argument in H035.34 retains the stronger underived coefficient formulation being checked here. |
| 1963 | [EGA III₂, 7.7.6–9, pp.69–71](https://www.numdam.org/item/PMIHES_1963__17__5_0.pdf) | Hom representation with a source-presentation hypothesis in 7.7.8; 7.7.9(iii) announces removing it. It is not an exact certificate for unrestricted Theorem 14. |
| 1965 | [EGA IV₂, 6.11.8 and Remarques 6.11.9, pp.162–163](https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf) | The exact margin reference establishes CMU consequences. It does not establish canonical-module existence. |
| May 1965 talk; 1966 volume | [Murre, exposition 294, Theorem 3, p.255](https://www.numdam.org/article/SB_1964-1966__9__243_0.pdf) | The cited closed condition Y_T=X_T under flat finite type and the adic condition, including properness. |
| SGA 3; checked 2009 revision | [Exposé VIII, Theorem 6.4 and Corollary 6.5, pp.18–19](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp8-8nov09.pdf) | A related closed-condition theorem for essentially-free morphisms. Its hypothesis is recorded as different. |
| 1994 preprint; 1997 publication | [Jaffe, section 7, pp.26–29 of the opened preprint](https://arxiv.org/pdf/alg-geom/9410009) | Proper flat and Dedekind positive cases, and a nonflat underived-cohomology obstruction to coherence. This prevents replacing all the manuscript's functors by the finite-Hom-presentation class. |
| 1997 lecture; full article cited there in 1998 | [Hartshorne, section 2, pp.88–89](https://www.mate.polimi.it/smf/vol67/hartshorne.pdf) | The finite-Hom-presentation category is abelian. Its composition closure follows by a finite presentation of the outer Hom argument. The lecture also distinguishes nonflat cohomology. |
| 2014 | [Hall, Theorems C–D p.4, Example 3.10 p.18, final author version](https://bpb-ap-se2.wpmucdn.com/blogs.unimelb.edu.au/dist/5/501/files/2021/05/coho_bc.pdf) | Matches the full proper Hom result, including quasi-coherent first argument and flat finitely presented target. Theorem E concerns derived tensor and must be distinguished from H035.34. |
| 2025 | [Lyu, Corollary 4.7 p.225, Lemma 6.1 and Theorem 6.2 p.230](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/formal-lifting-of-dualizing-complexes-and-consequences/5B440834E8251BAF3DA3752276F6C31B) | Gives the precise canonical-module spreading result used for the Gor-2 reconstruction. Remarks 7.7 and 7.9 p.233 explain why CMU and excellence must be handled with care in stronger duality questions. |

The exact six-axiom statement of Theorem 12 was not found as a matching
published theorem in the sources checked; it has a complete proof here.
This is not a novelty claim. The search covered Numdam, arXiv, MathOverflow,
EGA/SGA, collected-text indexes and author bibliographies. zbMATH Open was
attempted twice but was inaccessible. Failed searches and unmatched modern
terminology are not evidence that an assertion was never published.

### The remaining composition problem

For the explicit affine class in H035.39, every axiom except completion
is proved stable under composition. The generic condition can be upgraded
from a nonempty open to a dense open component by component, so reducible
bases no longer present an obstruction. For a finite module M over a
completion C, the remaining comparison is

\[
F(G(M))\longrightarrow\varprojlim_n F(G(M/I^nM)).
\]

It is not legitimate to apply F's completion axiom immediately: its input
G(M) must first be controlled over C, and the inner tower need not already
be its ordinary adic quotient system. Arguments (A)–(D) in H035.39 now prove
the entire assertion for **every countable noetherian base in the stated
class**, including principal completions with nonartinian levels. They also
prove it for arbitrary Dedekind domains and artinian rings. The proof uses
Matlis duality to make inverse limits of finite modules exact over complete
local rings, and completed localizations to detect pro-zero systems. Once
G(M) is finite, these arguments give the required pro-comparison. Thus
nonartinian principal-adic continuity is no longer a separate open gate.

Arguments (E)–(F) reduce the remaining sufficient finiteness question
further. Finiteness on all maximal-completed modules implies finiteness on
principal-completed modules. Locally, write R for the base, m for its maximal
ideal, k=R/m and D for its completion. Exact inverse limits show that G(M)
is intrinsically m-adically complete. It is finite if and only if
H(M)=G(M)/mG(M) is finite-dimensional over k. The functor H inherits the
maximal completion axiom, and the other archival conditions for this
residue-field-valued functor are automatic.

The precise remaining sufficient gate is therefore: if an additive,
finitary H:Mod(R)→Vect(k) has finite-dimensional values on finite R-modules
and satisfies H(M)=lim H(M/m^nM) for every finite D-module M, must H(M)
be finite-dimensional? The incomplete uncountable case remains unresolved
here. Countable R, complete R, and algebraizable-summand inputs are proved.
Failure of this finiteness property alone would not refute composition;
it would still require an outer functor whose comparison fails.

The half-exact functor results of Hall–Rydh, Theorems 3.3 and 3.7 and
Remark 3.8, pp.767–768 of their 2019 paper, do not supply the missing step:
half-exactness is not assumed in Remarque 18, and the completion injection
reported there tests finite modules over the original base. The exact
hypothesis checks are recorded in the research log.

The direct torsion-weight counterexample attempted over k[[x,y]] fails
the original hypothesis at p=(x), so it is explicitly rejected. Replacing
the class by coherent functors, assuming arbitrary finite inverse systems
are Mittag–Leffler, or applying flat base change to nonalgebraizable
formal modules does not close the argument. The exact failed steps and
next attacks are in `research/COMPOSITION_ATTEMPTS.md`. “Open” here means
unresolved in this run; no claim is made that it is an established open
problem in the literature.

## 6. Links to other catalogue objects

`LINKS.tsv` contains its header and no asserted relation. The supplied
catalogue places H038 (local cohomology and duality), H02M (Hilbert schemes,
norms, Tor and Ext), and H03A (scheme-valued functor gluing) nearby. That is
evidence of thematic proximity, not a checked “uses,” “same question,” or
generalization relation between the relevant passages. No cross-object
claim has been manufactured from the shared vocabulary.

H02X is a documentary object that includes the local-fields report in cote
94. It is not a supplied mathematical tag for the absolute-value assertions
on scan 12. Those rows are explicitly marked off object, with their correct
mathematical subject named and no invented tag.

## 7. Verdicts on the six supplied entries

Every entry was read in full, independently of its sweep placement.
`NOTES_VERDICTS.tsv` gives an anchor, mathematical verdict, placement and
reason for each of its 44 subclaims.

| Entry | Subclaims | Verdict in brief |
|---|---:|---|
| work:K94-01#1 | 14 | Broadly faithful descriptive overview, but it silently supplies “nonzero” in Proposition 3 and does not expose the missing hypothesis in 5 bis, the false Tor criterion, or the absolute-value defects. The inserted arithmetic leaf is outside H035. |
| work:K94-01#2 | 9 | Correctly identifies many missing proofs. The two-Tor item is false as written, so “unproved” is insufficient; the others receive proofs with their exact qualifications. |
| work:K94-01#3 | 3 | The possible question mark remains uncertain; the reformulation margin is confirmed. Its no-other-conjecture statement is confined to scans 2–13; the later programme is now included. |
| work:K94-01#4 | 7 | P/Q and nonzero root-of-unity corrections confirmed. The undefined coefficient is identified. Singular agreement is editorial; the final curl and cancelled-preposition claims remain uncertain on the ink. |
| work:K94-01#5 | 7 | Internal dependencies and exact EGA and Bourbaki pointers checked. The EGA citation does not justify the marginal enlargement. The unspecified valuations chapter remains unidentified. |
| work:K94-01#6 | 4 | Proof-order arrow and Tor linkage confirmed with the false criterion isolated. The s/n index and overwritten Hom definitions retain their uncertainty; no convention change is inferred. |

The supplied CHECKS.tsv contained no prior mathematical check rows. This
run's events distinguish computation, targeted proof checks, exact-source
matching, and background use. The model is GPT-6 Astra Pro; the environment
does not expose the reasoning-effort setting, so no “max” setting is claimed.

## 8. Our research results bearing on this object

'''
if not after_results:
    text+='The results attachment remains closed at this stage. This complete pre-results entry records the archive reading and mathematical assessment before those claims are consulted. A dated opening event and evidence-only comparison will be added in the next phase.\n'
else:
    with (root/'CONSEQUENCES.tsv').open() as stream: consequences=list(csv.DictReader(stream,delimiter='\t'))
    text+='The results attachment was opened only after the pre-results entry was written and frozen in research/ENTRY_BEFORE_RESULTS.md. Its opening time is recorded in progress.log. These comparisons concern the supplied runs’ claims; their source status is not adopted as a proof.\n\n'
    if consequences:
        text+='| Supplied result | Manuscript item | Relation | Evidence and check state |\n|---|---|---|---|\n'
        for row in consequences:
            text+='| '+' | '.join(row.get(k,'').replace('|','/').replace('\n',' ') for k in ['tag','statement_id','relation','evidence'])+' |\n'
    else:text+='No evidence-backed relation was found; CONSEQUENCES.tsv records that empty outcome.\n'
text+=f'\n---\n\nEntry generated at {stamp}. Detailed state and mandatory reviews: PROGRESS_LEDGER.md. All cited works and verification qualifications: references.bib.\n'
(root/'ENTRY.md').write_text(text)
if not after_results:
    frozen=root/'research/ENTRY_BEFORE_RESULTS.md'
    if frozen.exists():raise SystemExit('Pre-results entry already frozen; refusing to overwrite it.')
    frozen.write_text(text)
    digest=hashlib.sha256(frozen.read_bytes()).hexdigest()
    (root/'research/ENTRY_BEFORE_RESULTS.sha256').write_text(digest+'  ENTRY_BEFORE_RESULTS.md\n')
    with (root/'progress.log').open('a') as stream:stream.write(f'pre-results entry written and frozen {stamp} sha256={digest}\n')
print('Wrote ENTRY.md:',len(text.split()),'words; phase:', 'post-results' if after_results else 'pre-results')
