# Reading and reproducing ALPOGE_BRIDGES

This guide accompanies the paper and registers. In a numbered checkpoint,
all files describe the state at that checkpoint; they are not a final
claim that every remaining question has been decided.

## The five principal deliverables

| File | Purpose |
|---|---|
| `ALPOGE_BRIDGES.tex` | Self-contained manuscript: adopted inputs, original questions, exact sources, complete checked deductions, counterexamples, and a separate part for remaining gates and unchecked source assertions. |
| `QUESTIONS.tsv` | Current question-by-question state, original locator, finding identifiers or remaining gate, and bridges used. The source-kind column distinguishes an original question from a current research inference. |
| `CHECK_EVENTS.tsv` | Actual check events. A primary-statement check, a complete proof reading, a computation, and a prior intake report are different events. The method field states what was done. |
| `LEDGER.md` | Dated work record and complete question snapshots at the required movement reviews. The historical snapshots remain intact when later results supersede them. |
| `IMPLICATIONS.md` | Consequences for each part of the programme, including the information still needed at the remaining gates. |

The optional supporting material in `research/` preserves the constituent
proof modules, source locators, computational certificates and scripts,
attempted routes, check records, and assembly documentation. It is there
to make the result inspectable and continuable, not to replace the
self-contained main manuscript.

## Entry points by original question

| Question or programme | Checked result to read first | Scope boundary to retain |
|---|---|---|
| Cote 14, Albanese-generated cycle relations | AQ-14-FORWARD/CONVERSE; CC-ALB01–02; BR-14-SEP | The integral relation agrees for projective, affine, quasiprojective and all smooth separated finite-type parameters over an algebraically closed field, in every characteristic. The finite-field rational-point reading has its own counterexample. |
| Cote 15, finite-field motives | CC-TATE01–05; CC-AG01–15; BR-15-PRIME-SUPPORT | The explicit classification applies to the abelian–Artin–Tate numerical category. Rational object descent has a finite all-slope test for each specified object; over the prime field its full multiplicity monoid has a computable generator. A rational neutral fibre functor remains obstructed by the supersingular quaternion example. |
| Cote 15, a specified arbitrary variety | CC-XC01–10; BR-EFF01–03 | Finite rational cycle certificates have a terminating intersection-trace verifier and supply one splitting valid for every ℓ different from the characteristic. Enumeration halts exactly on positive instances, and is proved to terminate for the stated Fermat, diagonal and squarefree-binary-form families. Universal termination and negative-membership decisions remain unproved. |
| Cote 18, periods and comparison | AQ-PERIOD-STRONG/GENERATION; KN-COMP01–04; BR-18-AD01 | The overly strong joint formulation is refuted; comparison theorems and adelic genericity have precise affirmative scopes. The full non-CM complex period question is retained separately. |
| Cote 123, Kostant's letter | CC-APG01–11; BR-123-WEDGE/OPPF4/OPPE8/OPPG2; CC-RK01–05 | The complex apposition classification, some/all-choice opposition, outer action, and subregular ranks have complete answers. The manuscript distinguishes Lie-algebra results from group results and central forms. |
| Cote 66, affine torsion comparison | BR-66-01–03 | The universal degree-zero test is exactly henselianity. The quantifier over all torsion sheaves is essential. |
| Cote 134-8, linear localization | F-SM-29–41 | The projective-generator and AB4 cases are proved; a weaker countable comparison criterion is also proved. The additive counterexample omits the full symmetric tensor structure; the stated tensor repairs and countable-scalar exact tensors are excluded, while the bare original tensor case remains a separate gate. F-SM39 proves the literal ordinary counit for the stated connective-chain module categories without scalar size restrictions. |
| Cote 136, admissible PD theories | AQ-136-COMPARISON/DP-MODEL/STRICT/RATIONAL/PLOCAL; subsequent scoped refinements | Strict equalization is refuted. Strict common sources and ordinary terminality are proved whenever only finitely many rational primes are nonunits. Over every ring, common sources are equivalent to connectedness by an admissible cospan construction. Connectedness over Z remains open. |
| Deligne's weights and monodromy | BR-WM-02; CC-WM01–03; CC-ST01–04; CC-RES01–02 | The finite exterior-power trace criterion retains the actual monodromy operator. The universal stable-curve decomposition and canonical exit construction do not assert purity of every ordinary singular-fibre group. |
| Abelian Artin–Tate arithmetic | BR-AT-01; AQ-FINITE; CC-F01/F01b | Primitive Dirichlet factors and integral twists are within the adopted theorem. Nonabelian Artin and general Hecke factors require additional analytic inputs. |
| Analytic RH criteria and classical consequences | BR-TR-01/02; the consequences chapter | Each classical result retains its exact analytic hypothesis and range. A zero-set spectral realization is distinguished from a geometric operator constructed from primes. |
| Masullo's route | F-SM-01–22 and the source-scope chapter | The normalized numerical identities and the exhibited operator counterexamples are checked. The remaining global-to-local kernel construction is not supplied by the numerical identity. |

Later findings can refine these entry points. `QUESTIONS.tsv` is the current
state register, while the dated entries in the ledger explain when a gate
changed. A result established without RH is identified as such; its
presence in this bridge study does not give it an artificial RH dependence.

## Check terminology and provenance

The adopted Alpöge declarations are used as theorems, as directed by the
task. Their exact names and targets are recorded in the source-scope
section and check register. The supplied declarations were inspected;
this run does not claim a fresh Lean kernel compilation of the entire
external proof archive.

The current model identifier is GPT-6 Astra Pro. The effort setting is not
exposed, and the records say so. Author and separate-reader complete
readings are recorded under the type of check actually performed; they
are not relabelled as independent re-proofs. A numerical experiment is
not a proof except where the finite exact certificate and its relation
to the proposition are supplied explicitly.

A finding identifier means that its statement and proof are established
in this run. It does not assert first publication. When a supplied intake
already reports a related result, the paper credits that report and
distinguishes it from the full proof checked here. An unavailable prior
proof is carried as unavailable, with its report-level status retained.

## Reproduction and continuation

The manuscript is assembled by `research/assemble.py` from the listed
proof modules. That script also normalizes the question and check-event
registers. It never creates a checkpoint. If it is used after extracting
a checkpoint, create a `deliverables/` directory and place the principal
deliverables there, because their paths are flattened to the ZIP root
for delivery.

`research/build_pdf.py` builds the TeX using the documented environment.
Compilation is a syntax/typesetting check. A PDF is included in a
checkpoint only after a separate completed visual QA record exists;
absence of a delivered PDF does not imply that the TeX has not compiled.
The TeX is the required paper format and contains the full deliverable.

`research/checkpoint.py N` makes a new immutable checkpoint only after
the elapsed-time boundary for that number. It refuses to overwrite a
previous checkpoint and excludes all earlier ZIPs. Each checkpoint
contains a SHA-256 manifest. The original supplied source packet and
downloaded third-party reference caches are not republished; their names
and exact source locators allow them to be restored separately.

`research/movement_review.py N evidence-file yes|no` records a due review
only after the mathematical decision and its evidence have been supplied.
It does not infer progress from changed text, a build, or file counts.
The review rule remains the one requested: an original open row must
change status, or a main question must have a strictly smaller proved
gate; two consecutive reviews without such movement end the work.

The fixed start time is in `research/RUN_START.txt`. Checkpoint numbers,
review dates, and no-movement counts must continue from the recorded
values after a restoration, rather than starting a new schedule.

The subsequent CC-AG14 example has exact descent multiplicities0 and every integer at least2; its abelian-threefold corollary uses classical Honda-Tate alone. AQ-136-PARTIAL-SOURCE supplies all horizontal conditions and integral vertical H0/H1 over Z, with higher vertical torsion still unresolved. F-SM40 proves the raw counit under the stated product-preserving interval condition.

The next checked addition, CC-AG15, proves the exact monoid3N for a p=163 threefold example and refutes a proposed norm-gcd shortcut. BR-15-PRIME-SUPPORT reduces the geometric generator search to finitely many cyclotomic prime towers, with heights still unbounded. AQ-136-COSPAN/CONNECTED-SOURCES/SEMILOCAL-SOURCES proves the new mixed semilocal strict common-source statement; this is an original-gate change after movement review03.
