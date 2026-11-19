"""Authored refinements after reading the exact Samuel primary statements."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=R/'scripts/build_claims.py'
s=p.read_text()
block='''# Exact primary matches found by backward tracing; no source text is amended.
for c in C:
    n=int(c['id'].split('-')[-1])
    if n==492:
        c.update(statement='The supplied fragment lacks the preceding derivation definitions. Samuel’s printed counterexample has B=k[x,y,z] in characteristic 2, Dx=y^4, Dy=x^2 and Dz=xyz; the divisor (z) does not descend from the constant field. This antecedent is an external reconstruction, not text supplied on scan 36.', fate='Samuel1962Derivations, §3, p.3-11, matches every surviving step: specialization z=0, Db/b=−xy and differentiation. The missing definitions were checked on the published page image. The archival statement remains class F because its own antecedent is absent.', present_status='As of 2026-11-19: the likely published source is exactly identified and its contradiction verified, but its antecedents are not silently inserted into the transcription.', refs=['Samuel1962Derivations'], confidence='high', computation='scripts/calculations.py; outputs/calculations.txt; CALC-24; proof_notes.md')
    if n==494:
        c.update(statement='Let B be a local UFD of characteristic 2 and D a derivation with constant fraction field K and [Frac(B):K]=2. If D(B) generates the ideal (Dx,Dy), for x,y in the maximal ideal, every logarithmic derivative in that ideal equals Du/u for a unit u of B.', **{'class':'E'}, fate='Exact matches: Samuel1962Derivations §4 Lemma 3 and Samuel1964TIFR, chapter III §5 Lemma 5.1. The two-generator unit construction is independently checked, including gcd normalization and the formula u=1+cx+dy+(cd+alpha)xy.', present_status='As of 2026-11-19: established under the printed local factorial and degree-two constant-field hypotheses; CALC-23 checks the characteristic-two identity.', refs=['Samuel1962Derivations','Samuel1964TIFR'], confidence='high', computation='scripts/calculations.py; outputs/calculations.txt; CALC-23; proof_notes.md')
    if n==496:
        c.update(statement='For A=k[[U,V,Z]]/(Z^2−U^(2i+1)−V^(2j+1)) in characteristic 2, the divisor class group contains an additive subgroup isomorphic to k^N, where N counts pairs 0≤a<i, 0≤b<j with (2j+1)a+(2i+1)b≥2ij. This vector-space structure is noncanonical.', **{'class':'E'}, fate='Exact matches: Samuel1962Derivations §6(b) Proposition 3 and Samuel1964TIFR chapter III §5 Theorem 5.2. The published proof was checked through the logarithmic-derivative quotient, weight filtration, recursive integration and splitting as F_2-vector spaces; the monomial count is recomputed.', present_status='As of 2026-11-19: established for the stated field case. In particular N(2,2)=1. This replaces the initial broad-method-only literature match.', refs=['Samuel1962Derivations','Samuel1964TIFR'], confidence='high')
    if n==497:
        c.update(statement='For the same invariant ring A, U=X^2 is prime, A[U^(-1)] is a Dedekind domain and localization preserves its class group. For infinite k and i=j=2 this gives an infinite ideal class group.', fate='The prime and dimension assertions are independently proved. Samuel1964TIFR Theorem 5.2 supplies the exact subgroup theorem, while Samuel1961Factoriels §1 supplies the class-group localization framework.', present_status='As of 2026-11-19: the infinite-class-group example is established; its formerly unmatched input C-SA14-496 now has an exact opened primary proof.', refs=['Samuel1962Derivations','Samuel1964TIFR','Samuel1961Factoriels'], confidence='high')
    if n==514:
        c.update(statement='Let K be a Noetherian UFD and F an irreducible weighted-homogeneous polynomial of positive weight q. For a positive integer c coprime to q, K[X_1,...,X_n,z]/(z^c−F) is factorial if c≡1 modulo q, or if every finite projective K-module is free.', **{'class':'E'}, fate='Exact matches: Samuel1964TIFR chapter I §8 Theorem 8.1, including both alternatives and the free extension descent proof; Samuel1964Mechants §III Proposition 2. No broader theorem is substituted for the two alternatives.', present_status='As of 2026-11-19: established with precisely the printed alternatives. The proof and its descent hypotheses were read and checked.', refs=['Samuel1964TIFR','Samuel1964Mechants'], confidence='high')
    if n==515:
        c.update(statement='For a field K and pairwise coprime positive integers a,b,c, the ring K[X,Y,Z]/(Z^a−X^b−Y^c) is factorial.', **{'class':'E'}, fate='Samuel1964TIFR chapter I §8, Example (1) after Theorem 8.1, supplies the same trinomial family. The field hypothesis printed in this exercise is retained. Weighted degree bc and coprimality with a give the criterion; X^b+Y^c is irreducible when gcd(b,c)=1.', present_status='As of 2026-11-19: established for the printed field case; no claim about arbitrary exponents or a larger coefficient-ring class is needed.', refs=['Samuel1964TIFR','Samuel1964Mechants'], confidence='high')
    if n==518:
        c.update(fate='Exact match: Samuel1964TIFR chapter I §8 Theorem 8.2 (Klein–Nagata), with characteristic not 2 and at least five variables. The localization and scalar-extension proof was read and independently checked.', refs=['Samuel1964TIFR'], confidence='high')
    if n in (503,565):
        c['refs']=['Samuel1961UFD','Samuel1964Mechants','Samuel1964TIFR']
        c['fate'] += ' Samuel1964Mechants §III Proposition 1 explicitly says i,j,k>0; its positive range corroborates the repair without deciding the archival ink.'
    if n in (494,496,497,514,515,518):
        c['page_status_detail']=c['present_status'].removeprefix('As of 2026-11-19: ')
'''
if '# Exact primary matches found' not in s:
    s=s.replace('def save():\n',block+'def save():\n')
    p.write_text(s)
p=R/'scripts/build_bibliography.py';s=p.read_text()
block='''ref('Samuel1962Derivations','incollection','Pierre Samuel','Classes de diviseurs et dérivées logarithmiques',1963,'https://www.numdam.org/item/SD_1962-1963__16_1_A3_0.pdf','Primary PDF opened. Page3-11 checked visually; §4 Lemma3 and §6(b) Proposition3 read and matched. The exact unit-logarithmic lemma and N(i,j) family are identified.',booktitle='Séminaire Dubreil-Pisot',volume='16',number='1, exposé3',pages='1--30',circulation='Talk dated1962-11-19; seminar volume1962–1963. The surviving bibliography cites1965 publications, so the date of the surviving revision is not identified with the talk date.')
ref('Samuel1964TIFR','book','Pierre Samuel','Lectures on Unique Factorization Domains',1964,'https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr30.pdf','Official TIFR full PDF opened. ChapterI §8 Theorems8.1/8.2 and examples, §9 recurrence; chapterIII §5 Lemma5.1 and Theorem5.2 proof read. The current typeset file has occasional typographical errors, so identities were independently checked.',series='Tata Institute of Fundamental Research Lectures on Mathematics',volume='30',publisher='Tata Institute of Fundamental Research',editor='M. Pavman Murthy, notes',circulation='Title page1964; first circulation not separately established. Current official retypesetting is not a date for the archived draft.')
ref('Samuel1964Mechants','article','Pierre Samuel','Méchants anneaux de séries formelles',1964,'https://www.numdam.org/item/ASCFM_1964__24_3_109_0.pdf','All three article pages opened and read; §III Propositions1–2 exactly supply positive exponents and both weighted-cyclic alternatives.',journal='Annales scientifiques de l’Université de Clermont-Ferrand2, Série Mathématiques',volume='24',number='3',pages='109--111',circulation='Publication1964; earlier first circulation not independently established. Its São-Paulo citation date differs from the later seminar bibliography, and no priority date is inferred.')
'''
if "ref('Samuel1962Derivations'" not in s:
    s=s.replace('tags={\n',block+'tags={\n')
    s=s.replace('pages106–110 read using OCR','pages106–116 read using OCR')
    p.write_text(s)
print('Exact primary refinements inserted into reproducible builders.')
