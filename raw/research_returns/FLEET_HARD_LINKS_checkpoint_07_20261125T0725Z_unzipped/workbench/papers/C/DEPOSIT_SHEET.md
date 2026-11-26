# Deposit sheet — C

Status: current paper verified and frozen at 46 pages; the wider research task continues. Not deposited. Author line intentionally blank. The owner assigns the permanent registry number, public page and commit.

## Title

#SAT modulo p and Artin–Mazur height, after Katz and Stienstra

## Current abstract

The following is the editable LaTeX abstract of the accompanying source; its mathematics and scope match the PDF built from it.

```latex
A companion counting construction, following Katz's coefficient formula,
realizes the number of satisfying assignments modulo a prime as the
Hasse--Witt scalar of a smooth Calabi--Yau hypersurface.
Starting from this construction and Stienstra's logarithm, we identify
its second height test with a count of balanced local assignments,
or equivalently with a count of cyclic orbits.
The resulting height-two decision is modular-counting complete at every
fixed prime, even on the locus where the first scalar vanishes.
At a fixed prime, exact-height decision lies in modular counting with
the requested height supplied in unary and allowed to grow.
Logically equivalent formulas with the same integer satisfying count
can have different height-two status. A binary example also gives
parity-counting completeness at height three. When the prime is part
of the input, even the promised height-two oracle recovers exact
counting through polynomially many queries.
We give exact point-count tests, including the extra precision needed
at two, a finite stopping rule, and polynomial-space computation of
unrestricted exact height. We analyze the existing quasi-Frobenius-splitting
matrix criterion of Kawakami, Takamatsu and Yoshikawa and its implementation
by Batubara, Garzella and Pan; a separate dense implementation takes time
exponential in the number of variables times the logarithm of the prime. A matching complexity
classification for the unrestricted function remains open.
The mathematics and text were produced by GPT-6 Astra (ChatGPT Pro mode);
separate readings by the same model and exact computations are recorded,
and no human has checked the paper.
```

## Subject and keywords

Arithmetic geometry; Calabi–Yau hypersurfaces; Artin–Mazur height; Hasse–Witt scalar; counting complexity; Frobenius slopes.

## Method and checking note

Mathematics and text: GPT-6 Astra (ChatGPT Pro mode; runtime label GPT-6 Astra Pro). Separate workers used the same model and inherited reasoning settings; no unexposed effort level is invented. CHECK_EVENTS.tsv distinguishes statement-only reproof, targeted proof check, exact computation/certificate, and source verification. No human has checked the papers. No Lean proof of these new statements is claimed. Original text and programs are dedicated under CC0 1.0. Intended workbench: https://github.com/KokunoYumeto/arithmetic-geometry-complexity-workbench . Permanent record placeholder: https://github.com/KokunoYumeto/mathematics-workbenches .

## Eight opening requirements

| Requirement | Location in this paper |
|---|---|
| 1. Field-recognizable title and credit | Title block; the programme/source is identified immediately in the abstract and Section1 |
| 2. Source, result, scope and production/check note | Abstract, first through last sentences |
| 3. Full main statements and meaning | Section1 named main theorems and the paragraphs immediately following them |
| 4. Why the question matters | Section1 opening question and consequences; A gives the explicit border transfer, B the size conjecture, C the height-stratum/counting distinction |
| 5. Exact division of credit | Section1 source/context subsection; exact theorem/page locators in references and proof citations |
| 6. Earlier and neighboring work | Section1 source comparisons and cited context; no source proof is assumed beyond its explicitly cited statement |
| 7. Scope and remaining obstruction | Section1 after the main theorems, and the closing What remains open section |
| 8. Proof overview | Section2, explicitly headed Proof overview, before the main proof sections |

## Authors whose work carries the arguments

Katz (coherent Frobenius coefficient); Artin and Mazur (formal groups); Stienstra (integral logarithm); Vlasenko (valuation height test); van der Geer and Katsura (finite-height bound); Lauder and Wan (finite trace formula); Hesse, Allender and Barrington (uniform integer division); Valiant and Vazirani (isolation); Mumford and Atiyah (theta parity); Chebotarev/Tao (prime-order Fourier minors); Grenié and Molteni (effective Chebotarev under specified GRH); the cited counting and parity companion manuscripts (hypersurface and pencil constructions).

The source list records exact locations used, not an assertion that the authors have seen or endorsed this text. The full expert and newcomer readings and all 46 final-page visual inspections are recorded in the workbench, including an incremental expert check of the last method and layout edits.

Additional carried authors: Tatsuro Kawakami, Teppei Takamatsu and Shou Yoshikawa (Fedder criterion); Ryan Batubara, Jack J. Garzella and Alex Pan (fixed matrix algorithm); Fuetaro Yobuko (height comparison).

Recent computational context: R. Batubara, J. J. Garzella, Y. Huang, and M. Mellberg, whose 2026 controlled-reduction and explicit Newton-strata results are cited as context, not as a premise of the complexity proofs.
