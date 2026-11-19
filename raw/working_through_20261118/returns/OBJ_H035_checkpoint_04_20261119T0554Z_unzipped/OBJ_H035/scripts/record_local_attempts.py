"""Record unsuccessful local attacks and precise literature scope checks."""
from pathlib import Path
from datetime import datetime, timezone
import csv

root=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).isoformat()
attempts=root/'research/COMPOSITION_ATTEMPTS.md'
text=attempts.read_text().replace('not substituted silently for the manuscript. The results ZIP remains closed.',
    'not substituted silently for the manuscript. The results ZIP was opened only after the full entry was frozen; it contains no result rows.')
text=text.replace('## Next attacks\n','## Historical next attacks at 04:26 UTC (superseded by (A)–(F))\n',1)
text+=f'''\n\n## {stamp} — Further local attacks; no additional gate reduction

1. **Countable descent.** A finite formal presentation uses only countably many
   coefficients, but the given functor need not descend to a countable subring
   with finite values there. Restriction or scalar extension also has not been
   shown to preserve the required completed-module comparisons. A countable
   coefficient description of M is therefore not a countable cover of H(M)
   by the evaluation images required by Baire. No descent theorem is claimed.

2. **Countably many evaluation types for a fixed M.** It would suffice to find
   a countable collection of finite R-modules whose evaluation images span
   H(M). Truncating the formal relation matrix does not produce actual maps
   from those approximations to M. The needed factorization, even modulo m
   on Hom, has not been established. Mittag–Leffler-module theorems found in
   Datta–Epstein–Tucker concern additional purity/flatness properties; their
   complete-base equivalences do not establish this assertion over R.

3. **Matlis-dual tensor targets.** For finite D-module T and its Matlis dual
   E_T, the functor N↦soc(N⊗_R E_T) is finitary and has finite-dimensional
   values on finite R-modules. It also has finite-dimensional values on finite
   D-modules: duality identifies those values with the vector-space dual of
   Hom_D(N,T)/m Hom_D(N,T). Hence it cannot provide an infinite-output example.
   More seriously, it need not satisfy completion. Take R=k[t]_(t),
   D=k[[t]], T=D and E_T=k((t))/k[[t]]. Then D⊗_R E_T=E_T and its socle is k,
   whereas (D/t^n)⊗_R E_T=0 since E_T is t-divisible. The proposed completion
   comparison is k→0. This is a rejected candidate, with the failed axiom
   explicit, not a counterexample to the manuscript.

4. **Formal coefficient annihilators.** Functors built from the kernel of a
   formal coefficient acting on N⊗_R D have finite values on finite R-modules
   after suitable reductions. On a formal input their expression involves
   D⊗_R D, not just D. The canonical completion comparison has not been
   verified. This candidate remains only an attempted construction; no
   calculation is claimed to disprove or establish its full axioms.

5. **Half-exact finiteness theorems.** Hall–Rydh (2019), Theorems 3.3 and 3.7
   and Remark 3.8, pp.767–768, require half-exactness. Their reported Flenner
   completion injection starts with a finite module over the original base.
   Neither point supplies the missing arbitrary additive-functor conclusion
   on a nonalgebraizable finite D-module. Ogus's primary lecture-note proof
   of the half-exact Nakayama lemma, Theorem 2, pp.1–2, confirms exactly where
   half-exactness is used. Flenner's original paper was not opened and is
   not cited as a checked theorem certificate.

6. **Direct composition without finite output.** There is a useful boundary
   check: an inner functor whose values are all k-vector spaces cannot itself
   create a completion counterexample. The restriction of any additive
   finitary outer F to Vect(k) is F(k)⊗_k−. Since F(k) is finite-dimensional,
   it commutes with inverse limits. Thus F(H(M))→lim F(H(M/m^nM)) is an
   isomorphism whenever the corresponding comparison for H is one, even if
   H(M) were infinite-dimensional. This confirms why the finite-output gate
   is sufficient rather than equivalent to composition. It is a side case,
   not a new reduction of the current general gate.

7. **Endomorphism finiteness and pure injectivity.** A finite D-module is
   finite over its endomorphism ring, and its linear compactness suggests
   pure-injective methods. Preservation of these finiteness properties by
   an arbitrary bounded finitary additive functor has not been proved.
   Results for finitely presented interpretation functors would reintroduce
   the stronger coherent-functor assumption. No such substitution is made.

The current gate remains exactly the local residue-field finite-output
question recorded at 05:29. The next substantive attacks are a direct
comparison for the outer functor on the linearly compact inner output, and
an explicit bounded noncoherent functor built from finite-module categories.
Both must retain the completed-module quantifier, not merely algebraizable
inputs.
'''
attempts.write_text(text)

bib=r'''
@article{Hall2017,
 author={Hall, Jack}, title={Openness of versality via coherent functors},
 journal={Journal für die reine und angewandte Mathematik}, volume={722},
 year={2017}, pages={137--182}, doi={10.1515/crelle-2014-0057},
 url={https://bpb-ap-se2.wpmucdn.com/blogs.unimelb.edu.au/dist/5/501/files/2021/05/openness_published_final.pdf},
 note={verified}, addendum={Opened published author copy. Section 5, Lemma 5.1 and Examples 5.2--5.3, pp.154--155; Proposition 6.13 p.161 concerns deformation-theory composition, not the whole archival module-endofunctor class.}
}
@article{HallRydh2019,
 author={Hall, Jack and Rydh, David}, title={Artin's criteria for algebraicity revisited},
 journal={Algebra \& Number Theory}, volume={13}, number={4}, year={2019},
 doi={10.2140/ant.2019.13.749},
 url={https://msp.org/ant/2019/13-4/ant-v13-n4-s.pdf},
 note={verified}, addendum={Opened whole-issue primary PDF, article beginning p.749. Definition 3.2 and Theorem 3.3 p.767; Theorem 3.7, Remark 3.8 and Proposition 3.9 p.768. Half-exactness and the original-base finite-module hypothesis are retained. The DOI landing page was inaccessible; the printed DOI was verified in the PDF.}
}
@misc{OgusBaseChangeNotes,
 author={Ogus, Arthur}, title={Cohomology and Base Change},
 howpublished={Math 256B course notes, 2017 course directory},
 url={https://math.berkeley.edu/~ogus/Math_256B-2017/Notes/basechange.pdf},
 note={verified}, addendum={Opened all five pages. Theorem 2, pp.1--2, is a primary proof of the half-exact Nakayama lemma. No independent date on the PDF is asserted.}
}
@article{DattaEpsteinTucker2026,
 author={Datta, Rankeya and Epstein, Neil and Tucker, Kevin},
 title={Mittag-Leffler modules and intersection flatness},
 journal={Forum of Mathematics, Sigma}, volume={14}, year={2026},
 eid={e87}, doi={10.1017/fms.2026.10204},
 url={https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/mittagleffler-modules-and-intersection-flatness/EAE22B6C98269DA183E62520265AD1F2},
 note={verified}, addendum={Opened primary HTML, published 3 June 2026. Definition 3.2.3, Proposition 3.2.7 and Theorem 4.3.12 checked for scope; complete-local and flatness hypotheses do not give the needed evaluation factorization over the incomplete base. No page number is invented for the HTML.}
}
'''
with (root/'references.bib').open('a') as stream:stream.write(bib)
with (root/'research/SEARCH_AUDIT.md').open('a') as stream:
    stream.write(f'''\n\n## {stamp} — Half-exactness, purity, and local-output searches

Primary texts opened: Hall2017 section 5 and Proposition 6.13; HallRydh2019
section 3; OgusBaseChangeNotes Theorem 2; DattaEpsteinTucker2026 Definition
3.2.3, Proposition 3.2.7 and Theorem 4.3.12. Exact locators and URLs are in
references.bib. These were hypothesis checks, not certificates of the
archival composition assertion. The half-exact results have an extra
exactness assumption; the Mittag–Leffler-module results have complete-base
and, for the broader equivalences, flatness assumptions. Distinguish the
module property from Mittag–Leffler inverse systems.

Queries also included additive functors with bounded finite values and
completion; functors and Baire; endonoetherian functors; Tor finiteness on
finite inputs; and countable evaluation types. Search snippets for
Schoutens, Flenner, and module-theoretic preenvelopes were leads only.
The original Flenner and Ogus–Bergman papers were not inspected. Jaffe's
section 7 was reopened to retain its algebra-functor scope and the
underived-cohomology obstruction to a coherent-functor substitution.
No theorem matching the remaining gate was found in these inspected loci;
this is not evidence of nonexistence elsewhere.
''')
events=[
 ('Hall2017','used and rechecked in this run','Sections 5–6 checked; coherence and deformation-theory composition do not identify the archival class'),
 ('HallRydh2019','used and rechecked in this run','Theorems 3.3,3.7 and Remark 3.8 retain half-exactness and finite original-base inputs; Proposition 3.9 matches flat scalar extension'),
 ('OgusBaseChangeNotes','used and rechecked in this run','Theorem 2 proof checked: half-exactness enters both short exact sequences; no application to arbitrary additive H'),
 ('DattaEpsteinTucker2026','carried as background without fault found','Definition 3.2.3, Proposition 3.2.7 and Theorem 4.3.12 inspected for hypotheses; not applied to the unresolved factorization'),
 ('H035.39','targeted proof check — rejected candidate and side case','Socle of tensor with Matlis dual fails completion in the displayed DVR example; residue-field-valued inner functors give composition by finite tensor; general gate unchanged')
]
with (root/'CHECK_EVENTS.tsv').open('a',newline='') as stream:
    writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
    for key,how,outcome in events:
        writer.writerow([key,stamp,'GPT-6 Astra Pro; effort not exposed; OBJ_H035 single-stream run',how,outcome,'research/COMPOSITION_ATTEMPTS.md: further local attacks; research/SEARCH_AUDIT.md; references.bib'])
with (root/'progress.log').open('a') as stream:
    stream.write(f'local attempts and source scope checks recorded {stamp}; no new gate movement since 05:29\n')
print('Recorded seven local attacks and four primary-source scope checks at',stamp)
