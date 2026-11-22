"""Record the actual full root proof and primary-source audit; no computation claimed."""
from pathlib import Path
import csv, datetime, json
w = Path(__file__).resolve().parents[1]
dest = w/'outputs/root_positive_index_audit.json'
assert not dest.exists()
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
 ('lem:DE-A3-positive-index-Prym', 'PASS: entire proof independently rederived after rereading the full previous nonproduct mixed proof. Integral dual polarization has local-local index a, so a+v2(m)>0 kills the actual height-two local-local 2-torsion. Its immersion into the connected smooth Prym gives a connected order-two subgroup of ker Verschiebung after Frobenius twist. Additivity of dimension and p-rank gives total defect at least two. No merely isogeny-level subgroup is substituted.'),
 ('lem:DE-A3-positive-index-descent', 'PASS: complete cyclic descent rederived. The ordinary etale kernel has order 2^a. Rescaling a generator lift by an nth root produces a genuine linearization in characteristic two without averaging. The polarization factorization and Cartier-dual multiplicative kernel give a(H)=0 and preserve the local-local index. Ample pullbacks are connected by the divisor sequence. The finite etale cyclic cover has a filtration of its F2 regular-representation sheaf by n trivial quotients, proving Euler-characteristic multiplication and hence Deuring-Shafarevich. Together with etale Hurwitz this multiplies the exact defect by n. Crew original pp36 and42 were actually viewed; exact AV quotient, duality, and descent passages were freshly read.'),
 ('thm:DE-A3-positive-index-bounds', 'PASS: apply the previously audited index-zero theorem only on the quotient B, pull its smooth curves back, and use openness of iterated Frobenius rank on the complete linear system. This proves lower bounds 9Dd²-2^a for odd d and 9Dd²-2^(a+1) for even d, with upper bound 9Dd²-2 in both cases. When a=1 and d odd the bounds agree. All perfect-field assertions are geometric after algebraic closure.'),
 ('rem:DE-A3-positive-index-gate', 'PASS: scope checked. The pullback construction alone cannot attain defect two for a>=2 odd degree or a>=1 even degree. No index-zero ample class on the original A is asserted; the descended H is on B. These limits do not refute sharpness.')
]
with (w/'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, outcome in events:
        writer.writerow([sid, now, who, 'independent re-proof', outcome])
with (w/'notes/ROOT_SEARCH_LOG_16.md').open('a') as f:
    f.write(f'\n## {now}: positive ordinary-index bounds on mixed nonproduct surfaces\n\nRoot read and independently rederived every assertion in A3_mixed_positive_index_bounds.tex and reread the entire previous mixed nonproduct polarization/Prym proof. Crew original https://www.numdam.org/item/CM_1984__52_1_31_0.pdf was opened; pp34-37 were read and original pp36 and42 actually viewed, including equation1.8.2 and the sheaf-filtration proof. The retained original Edixhoven–van der Geer–Moonen text was freshly read at Theorem4.38/Example4.40 pp65-66, Theorem7.5 and Proposition7.6 p100, and Theorem8.10/Corollary8.11 with proofs pp116-117. The proof passes in full; no new computational certificate is needed or claimed. It closes ordinary index one in odd degree and gives explicit two-sided bounds for every positive index. The remaining sharpness gate is a>=2 odd degree and every a>0 even degree.\n')
result = {'status':'PASS', 'actual_utc':now, 'complete_statement_audits':len(events), 'new_computation':False}
dest.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
