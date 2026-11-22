#!/usr/bin/env python3
"""Integrate independently audited no-torus and regular-model stabilization."""
from pathlib import Path
import csv
import datetime
import json
import time

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
aux=(base.parent/'D'/'B_aux_no_torus.tex').read_text()
aux=aux.replace('\\subsubsection{Statement B.2r:', '\\subsubsection*{Statement B.2r (Proved):')
(base/'B_aux_no_torus.tex').write_text(aux)
regular=(base/'B2_regular_model_stabilization.tex').read_text()
path=base/'paper_B.tex'
paper=path.read_text()
assert 'Statement B.2r ' not in paper and 'Statement B.2s ' not in paper
paper=paper.replace('proved in B.2h over perfect fields and in B.2o in dimension at most two;\nover imperfect fields in dimension at least three it remains a separate\nunresolved strengthening.',
    'proved in B.2h over perfect fields and in B.2s whenever a proper regular\nbirational model exists, in particular in dimension at most three.  The\nremaining arbitrary-field scope is stated separately in B.2-U.')
path.write_text(paper+'\n\n'+aux+'\n\n'+regular)

path=base/'results_B.csv'
with path.open() as stream:
    reader=csv.DictReader(stream);fields=reader.fieldnames;rows=list(reader)
for row in rows:
    if row['id']=='B.2-U':
        row['statement']='Additional weak upper-cone replacement over imperfect fields without a known proper regular birational model'
        row['depends_on']='B.2h every perfect field; B.2s every field with a proper regular birational model and every dimension-at-most3 case; B.2q refutes strong cofinality'
        row['notes']='The regular-model case is now proved by iterative bad-valuation generic-fibre cuts and bounded exponent. The residual scope has dimension at least4 and no regular model supplied. A general Galois alteration extension is written and being audited separately; it has not yet been promoted.'
rows.extend([
dict(id='B.2r',statement='Normal proper Picard groups and finite-constant Weil restrictions of proper groups have no geometric torus; every finite-type commutative group with no geometric torus has largest abelian subgroup and bounded-exponent quotient',status='Proved',where_proved='paper_B.tex Statement B.2r',depends_on='Tanaka2015D Lemma2.2(2); Kelly2018D Corollary20; MilneAG2022B Theorems5.39/8.27; stable multiplication images',manuscript_pages='29/075',notes='All fields and all nonreduced parameter schemes included. Weil restriction allows arbitrary finite constant extensions. No unsupported smoothness of a single multiplication image is assumed.'),
dict(id='B.2s',statement='Weak upper-cone Picard stabilization holds over every field whenever the function field has a proper regular birational model; in particular in transcendence degree at most3',status='Proved',where_proved='paper_B.tex Statement B.2s',depends_on='B.1g; B.2d; B.2r; ACMV2026 Albanese duality; iterative bad-valuation generic-fibre cuts; CossartPiltant2019B Theorem1.1',manuscript_pages='29/075',notes='No filteredness is assumed. Maximal centre dimension converts every later restriction into a finite-field base bundle; each cut strictly lowers excessive ambient abelian dimension. Bounded exponent and one Jacobian give a maximal finite order. Root/C/D actual-file audits pass.')])
with path.open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields);writer.writeheader();writer.writerows(rows)

with (base/'CHECK_EVENTS_B.tsv').open('a') as stream:
    stream.write('B.2r\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_d\tproved\tD wrote the complete auxiliary package, directly opening TanakaLemma2.2(2), KellyCor20 and MilneTheorems5.39/8.27. The initial single-image smoothness shortcut was replaced by stabilization of closed multiplication images.\n')
    stream.write('B.2r\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b and /root, actual-file reading\ttargeted proof check\tB and root independently read the complete auxiliary proof. B reopened Tanaka and Kelly primary locators. Arbitrary test schemes and the finite-product extension for all finite l/k were verified. No gap found.\n')
    stream.write('B.2s\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_b\tproved\tWrote the complete regular-model theorem from the iterative bad-valuation route suggested by C, including coefficient-kernel descent, all-parameter Picard restriction, finite abelian-dimension descent and maximal finite-order conclusion.\n')
    stream.write('B.2s\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_c, actual-file reading\ttargeted proof check\tC read the complete214-line initial proof and checked every generic-fibre restriction, nonconstant-to-Pic detection and final rank bound; suggested explicit image dominance and iteration relabelling, both added. This event does not claim C independently reopened Cossart-Piltant.\n')
    stream.write('B.2s\t2026-11-20\tGPT-6 Astra (OpenAI), /root/part_d, actual-file reading\ttargeted proof check\tD read the complete proof, checked valuation persistence, maximal centre dimension, normal generic fibres, coefficient subgroup gluing, strict cuts and N-torsion rank. Suggested defining A0 by the largest abelian subgroup to avoid an unstated imperfect-field reduction rule; adopted.\n')
    stream.write('B.2s\t2026-11-20\tGPT-6 Astra (OpenAI), /root, actual-file reading\ttargeted proof check\tRoot read the214-line theorem and full auxiliary package, checked the valuation and group-scheme chain, and requested explicit F-flat base change and A0 wording; both added. Root independently opened Cossart-Piltant arXivv2 Theorem1.1 pp3--4 and verified arbitrary-field dimension3 resolution.\n')

path=base/'unresolved_B.tex'
text=path.read_text()
text=text.replace('B.2o proves it over every field in transcendence degree at most two.\n+Only imperfect ground fields and transcendence degree at least three',
                  'B.2s proves it whenever a proper regular birational model exists,\nin particular over every field in transcendence degree at most three.\nOnly imperfect ground fields without such a supplied model')
# Preserve exact replacement even if the source has no patch-style plus.
text=text.replace('B.2o proves it over every field in transcendence degree at most two.\nOnly imperfect ground fields and transcendence degree at least three\nremain.',
                  'B.2s proves it whenever a proper regular birational model exists,\nin particular over every field in transcendence degree at most three.\nOnly imperfect ground fields without such a supplied model, necessarily\nin transcendence degree at least four, remain.')
text += '\n\\paragraph{Current extension under audit.}\nThe regular-model proof in B.2s resolves its image bound by imposing\nrestrictions from one geometrically bad divisorial valuation at a time.\nA regular Galois alteration with finite semilinear constants appears\nto furnish the same argument in all dimensions: invariant abelian\nsubgroups are realized by an abelian torsor after translation killing\nand a fixed Frobenius twist.  The complete auxiliary descent proof is\nbeing independently audited; no general conclusion is assumed here.\n'
path.write_text(text)
path=base/'corrections_B.tsv'
text=path.read_text().replace('remains open only in dimension at least3 over imperfect fields.',
                            'is proved whenever a proper regular model exists, in particular through dimension3; the remaining imperfect-field alteration extension is being audited separately.')
path.write_text(text)
with (base/'notes.md').open('a') as stream:
    stream.write('\n## 2026-11-20 04:05 — weak stabilization under a regular model\n\nB.2r and B.2s are checked and integrated. The weak upper-cone claim holds over arbitrary fields whenever a proper regular birational model exists, hence for all dimensions at most3 by the primary Cossart–Piltant2019 Theorem1.1. The key finite induction is on the dimension of the largest abelian subgroup of a fixed ambient Picard group: an excessive subgroup has a geometrically bad divisor in its rational Albanese graph; maximizing that valuation\'s allowed centre gives one fixed generic-fibre restriction annihilating all future Picard images but not that subgroup. No filteredness or fixed list of all bad divisors is assumed. At the end the ambient quotient has bounded exponent; the fixed Jacobian bounds finite orders. The all-dimensional extension via an equivariant alteration with semilinear constants is under actual-file audit.\n')
with (base/'sources'/'search_log.md').open('a') as stream:
    stream.write('\n## 2026-11-20 04:05 — no-torus and regular-model inputs\n\n- Reopened Tanaka arXiv1502.01381v4, Lemma2.2(2), pp6–8: normalization of the reduction after any field extension of a normal variety is a universal homeomorphism.\n- Reopened Kelly July4,2018 manuscript, Corollary20 p9: finite universal homeomorphism admits a fixed Frobenius factorization when the structure-sheaf kernel is nilpotent. The proof is applied to all Picard parameter schemes by Frobenius on both factors.\n- Opened Cossart–Piltant arXiv1412.0868v2 (January8,2019), Theorem1.1 pp3–4, and compared the earlier2014 author draft. Arbitrary-field quasi-excellent dimension-at-most3 regular resolution is explicit. Publication metadata confirmed in the primary Journal of Algebra page.\n- MilneAG2022 Theorem5.39 is the faithfully-flat-onto-image theorem; Theorem8.27 is Barsotti–Chevalley. D reopened the exact pages.\n')
record=dict(operation='integrate_regular_stabilization_B',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),statements=['B.2r','B.2s'],elapsed_seconds=time.perf_counter()-started)
(base/'code'/'output'/'integrate_regular_stabilization_B.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
