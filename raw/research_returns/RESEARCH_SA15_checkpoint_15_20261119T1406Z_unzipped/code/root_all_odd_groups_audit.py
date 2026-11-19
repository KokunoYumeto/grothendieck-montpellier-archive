"""Record the actual full root proof and primary-source audit, no sample computation."""
from pathlib import Path
import csv,datetime,json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_all_odd_groups_audit.json'
assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
 ('lem:ss-all-odd-norm-factors','PASS: entire arbitrary-kernel assembly read and rederived. Balanced quaternion isogeny has graph kernel with both projections injective; exact symmetric norm line is L^d because geometric Pic0[2] vanishes. Pair-contact rank exceptions are finite and too small, triple Segre values are independent everywhere, invariant divisors lie in finite P2 loci. Both collision divisors are irreducible and distinct from D,Q. Source discriminant contributes no determinant factor. Normalization conductor proves the stable local quotient rank r-1. Over the generic D local ring, ordered nodal graph bundles are Frobenius-unit and the odd isogeny identifies ambient subbundles, giving exact D multiplicity2.'),
 ('thm:ss-all-odd-Hasse','PASS: every mixed witness identifies Q and its R_g with one target Hasse component; every uniform tangent triple joins its T_g,eta to the same component. A further target factor would pull back solely to D with degree<=6, contrary to d²>=9. The generic norm curve is sharp, so no factor pulls back identically. A smooth mixed witness ensures reducedness. The sharp-source simple-tacnode open in the irreducible R_g has exact target defect3 and hence relative stable rank9d²-2; semicontinuity proves generic loss1.'),
 ('thm:ss-all-odd-full-groups','PASS: entire proof and all invoked bundle/group reductions reread. Universal relative coherent bundle is Omega1 on P^(9d²-1), regular Frobenius extends across singular curves, determinant allocation plus exact absence of odd-degree invariant covectors gives irreducibility. Stable loss1 and strict henselian Lang finite part yield transvection inertia, purity and simply connected projective space yield generation. The actual natural GL8 block kills every invariant alternating form. Root actually viewed original Kantor-Seress Theorem3.6 printedp22 and checked all four alternatives; atq2 every nonSL alternative preserves such a form. Projective normality of each cubic and tensor multiplication give ambient restriction surjectivity for everyd. Arithmetic full image follows from geometric full image over any perfect base field.'),
]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,outcome in events:writer.writerow([sid,now,who,'independent re-proof',outcome])
with (w/'notes/ROOT_SEARCH_LOG_15.md').open('a') as f:
    f.write(f'''\n## {now}: all odd supersingular-product groups\n\nRoot read and independently rederived the full three-statement arbitrary-odd-degree assembly and reread the exact determinant-allocation, strict henselian Lang/purity and actual natural-block proofs. The primary Kantor--Seress original printed page22, Theorem3.6, was actually visually inspected from the retained original-PDF render. A fresh attempt to open https://pages.uoregon.edu/kantor/PAPERS/ksfinal.pdf through web retrieval failed because the57,682,627-byte response exceeded that endpoint's limit; this does not replace the actual primary-page inspection. The complete proof passes, including exact multiplicity2 on D and the strict degree inequality d²>=9>6. This closes the fixed supersingular product's full-image problem in every odd degree, without claiming the even-degree or arbitrary-X result. No new finite computation was used for this assembly.\n''')
result={'status':'PASS','actual_utc':now,'complete_statement_audits':len(events),
        'primary_source_actually_viewed':'Kantor-Seress2001, Theorem3.6, printedp22',
        'new_mathematical_computation':False}
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
