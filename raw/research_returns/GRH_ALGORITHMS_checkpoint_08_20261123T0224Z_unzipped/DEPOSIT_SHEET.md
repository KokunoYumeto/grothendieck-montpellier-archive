# Deposit sheet — not filed

**Title:** Deterministic finite-field constructions after Alpöge, Bach, von zur Gathen, Lenstra, Mumford, and Pila.

**Author line:** Empty in the manuscript, for completion at filing.

**Subject:** Computational algebra and analytic number theory; deterministic finite-field constructions; exact Riemann-hypothesis inputs; complex multiplication and finite-etale algorithms.

**Keywords:** Dirichlet GRH; finite fields; irreducible polynomials; cyclotomic cofactors; Teichmüller units; complex multiplication; theta functions; Frobenius; deterministic factorization; effective Chebotarev; class groups; average algorithms.

## Exact manuscript abstract

```latex
Bach, von zur Gathen and Lenstra constructed nonresidues from
smooth cyclotomic values, and Pila used Frobenius polynomials of
abelian varieties to find roots of unity. We prove an unconditional
deterministic construction of \(\mathbb F_{p^r}\) with bit cost
polynomial in the odd prime \(r\), \(\log p\), and the part of
\(\Phi_{\operatorname{ord}_r(p)}(p)\) coprime to \(2r\).
Combining Pila's method with Mumford's theta equations and granting
Alp\"oge's Dirichlet GRH also gives a bound polynomial in
\(\log p\) for every fixed prime degree and fixed valuation
\(v_r(p^{\operatorname{ord}_r(p)}-1)\). Exact CM height bounds,
algebraic recognition, marked good reduction and arithmetic over the
full residue algebra supply the geometric construction. The first
bound is uniform in its displayed numerical parameters; the second
has an exponent depending on the fixed degree and valuation. A
bound polynomial uniformly in \(r\) and \(\log p\) remains
open by these methods. We also trace eighteen classical algorithmic
statements to their exact Riemann hypotheses, prove the pure-field
zeta equivalence and Lenstra's Teichm\"uller reduction, and separate
Tang's polynomial-time interfaces from their zero-free inputs.
Character-product and quadratic-value estimates give short auxiliary
searches outside \(O(\sqrt P\log\log P)\) primes at fixed
degree. The mathematics and text were produced by GPT-6 Astra in
ChatGPT Pro mode; the cofactor and fixed-parameter constructions, principal
reductions and average theorems received statement-alone re-proofs
by the same model, earlier proofs received targeted checks by
Claude Opus 5.5 at effort high, and no human has checked this paper.
```

## Eight opening requirements and their locations

| Requirement | Place in the manuscript |
| --- | --- |
| Title names the mathematical problem and the sources of the programme | Title: deterministic finite-field constructions, after Alpöge, Bach, von zur Gathen, Lenstra, Mumford, and Pila. |
| Abstract begins with the earlier work and ends with production/check provenance | Abstract, first and last sentences. |
| Complete statements and their meaning | Section1, beginning with the unconditional cofactor theorem and the fixed-parameter CM theorem, followed by the older algebraic and average statements. Each specifies its inputs and uniformity. |
| Why the question matters | Section1 explains deterministic construction and factorization interfaces, and what rational Dirichlet GRH settles. The cofactor and fixed-parameter results remove precise remaining input classes. |
| Credit divided by exact scope | Section1 and the classical table; the cofactor proof cites BGL's projection and commutator, the CM construction identifies Pila and Mumford's contributions, and Tang's interfaces retain their distinct analytic inputs. |
| Context and neighbouring work | Classical table with exact source locators; comparison with Sze; Tang/OpenAI/Cureton–Thorner audit; CM height, recognition, reduction and theta-equation sources at their uses. |
| Scope stated beside conclusions | Section1 distinguishes numerical-cofactor uniformity, fixed-parameter polynomial bounds and the unsolved fully uniform gate. Individual CM and finite-menu statements retain their fixed-data hypotheses. |
| Mechanism before proofs | Section1 and the first paragraphs of the construction sections explain primary projection, the separating commutator, CM Frobenius support, and finite-product arithmetic. |

## Main statements in the opening

The following are the unique LaTeX labels of the opening statements, for editorial navigation only; they are not permanent registry identifiers:

- `cor:two-primary-cyclotomic-cofactor`
- `thm:fixed-wild-cm`
- `cor:fixed-wild-prime-degree-field`
- `thm:dirichlet-ninth-root-cubic`
- `thm:kummer`
- `thm:teich`
- `thm:nonresidue`
- `thm:tangfront`
- `thm:quasipoly`
- `thm:fixed-r-almost-all-auxiliary`
- `thm:almost-all-small-tate`
- `thm:aa-12r`
- `cor:aa-finite-field-algorithms`

## Authors and the work carried here

| Source authors | Contribution and scope used |
| --- | --- |
| Alpöge | Dirichlet GRH is the named analytic input A, not a certified theorem proved in this paper. |
| Bach, von zur Gathen, and Lenstra | Cyclotomic projection, smoothness-based nonresidues, and the rational-function/commutator root-extraction mechanism; exact author-page locators distinguish the specialization proved here. |
| Sze | Related deterministic root-extraction procedures; the full field-group cofactor and primitive-root inputs are compared explicitly with the smaller cyclotomic cofactor. |
| Lenstra and Adleman | Teichmüller and finite-field construction framework, number-field algorithms, and exact representation interfaces. |
| Mumford | Theta structures, moduli and projective equations, and the line-bundle ampleness criterion. |
| Pila | Deterministic Frobenius-polynomial computation and the CM root-of-unity programme. |
| Serre and Tate; Milne | Potential good reduction, CM type and Frobenius-support statements, with their integral and rational hypotheses kept distinct. |
| von Känel and Kret; Pazuki; Colmez; Wei | Effective CM/Faltings/theta-height bounds and the precise conditional or unconditional form used. |
| Lamzouri, Li, and Soundararajan | Dirichlet-GRH least-prime-in-a-coset bound for the small quadratic auxiliary input. |
| Kannan, Lenstra, and Lovász; Buchmann and Lenstra | Certified algebraic recognition and prime-local maximal-order computations. |
| Tang | The distinct uniform polynomial factoring and presentation algorithms, credited as Tang's theorem. |
| OpenAI; Cureton and Thorner | Prime-field and zero-free inputs to Tang's route; the official and separately revised zero-free texts are distinguished. |
| Miller; Bach; Hooley; Koiran; Solovay and Strassen; and the remaining table authors | The eighteen classical theorem/stage transfers, each tied to its exact zeros and primary-source locator. |

The bibliography gives the complete APA citations. The source inventory records original-byte hashes where obtained, exact inspected locations, and explicit unsuccessful byte-retrieval cases. No author has been contacted.

## Exact manuscript method note

```latex
The mathematics and text were produced by GPT-6 Astra in ChatGPT Pro mode.
Independent statement-alone re-proofs of the cofactor construction, the fixed-parameter construction and its ninth-root case, principal algebraic reductions and average theorems used the same model; the configured effort was not exposed
in their records. These were not different-model or formal checks.  Earlier project records describe targeted checks
by Claude Opus 5.5 at effort high; those checks concern the earlier
consequences, not Tang's later algorithm.  No human has checked this paper.
Our text is dedicated to the public domain under
\href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0~1.0}.
The accompanying programs and records are in the
\href{\workbenchurl}{zeta and $L$-functions workbench}; the permanent
record address is \url{\recordurl}.
```

## Release and filing state

This is an unfiled research draft. Permanent WB number, permanent page and deposited version are reserved for the registry to assign. No publication, push or external message is authorized or performed. The author line remains empty. Our text and programs are dedicated under CC0 1.0.

The main fixed-parameter and both cofactor statements have complete same-model statement-only reproofs, with exact seals and author-exposure chronology in the workbench. Further statements have the individual targeted checks recorded in CHECK_EVENTS.tsv. The source proofs of large named external inputs are background rather than independently certified theorems. No human has checked the paper.

The newest build status is in workbench/research/root. Final all-page visual inspection, the complete two final readings, the final format1 migration and the final version manifests remain completion tasks until their explicit records say otherwise. This sheet does not claim that they have already occurred.
