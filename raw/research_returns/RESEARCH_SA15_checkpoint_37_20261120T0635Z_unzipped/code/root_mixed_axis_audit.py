"""Record full root proof audit of corrected mixed axis norms and seed certificate."""
from pathlib import Path
import csv,datetime,json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_mixed_axis_audit.json'
assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
 ('lem:root-mixed-six-three-cartier','targeted proof check','PASS: root authored the complete universal seed proof, independently derived the p-basis Cartier pairing and exact semilinear dual orientation, and constructed two exact verifiers with distinct polynomial-arithmetic implementations. The fixed source has two independent kernel sections and an F²16minor c5, hence stable rank16 for every ordinary parameterc!=0. Intersecting with the smooth open and taking stable parts of the universal divisor sequence gives genus19,p-rank17,relative16. Independent OC audit has passed; RD audit requested.'),
 ('rem:root-mixed-six-three-certificate','computation or formal certificate','PASS: exact six-trial search0.0044763490004697815s, with all vectors/ranks retained; independent p-basis/table/matrix reconstruction and polynomial-domain determinant0.18401811700459803s. Initial .rem software-domain coercion failure0.040903039000113495s is fully retained as code/mixed_6_3_cartier_verify_failed_v1.py and its outputs. Monic pseudo-remainder repaired only the implementation. The invalid ordinary-axis transfer direction is explicitly recorded and not used.'),
 ('lem:DE-A3-axis-nodal-norm','independent re-proof','PASS: full proof read. For a second-axis kernel, the degree3 chord has at least one nonzero derivative and the two transverse derivatives vary independently, so its tangency determinant cuts every coefficient fibre. For a first-axis kernel, degree6 evaluation on two first jets is surjective. Triple values have rank3 except the finite multiplication-by3 collinearity locus, where rank2; both incidence dimensions are16<17. Proper incidence, etale immersion and finite translated intersections give birational nodal images. N²=36 gives18(n-1) nodes, including even etale kernels. Both norm-class directions are checked by pullback.'),
 ('cor:DE-A3-mixed-thin-vone','independent re-proof','PASS: every oddn has an etale isogeny from a supersingular source to the prescribed supersingular target. The universal(6,3) sharp open intersects the axis nodal open. Normalization adds18(n-1) unit graph classes, giving full stable rank18n-1 and relative18n-2. Translation fixes the Pic0 discrepancy, and openness plus the existing even ordinary-factor bound gives equality for a generic smooth target. Scope is exactly a congruent2mod4,b1,d1; the seed is separately independently audited.'),
 ('rem:DE-A3-mixed-axis-scope','targeted proof check','PASS: the ordinary-axis proposal would yield(6,3n) and is invalid for the required class. The corrected supersingular-axis etale construction yields(6n,3) only for oddn; no4-divisiblea conclusion is claimed.')]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_15.md').open('a') as f:
    f.write(f'''\n## {now}: mixed(6,3) seed and corrected axis geometry\n\nA universal coefficient vector was found in six exact trials. Its twice-iterated Frobenius16minor is the polynomial c5, so the proof applies to every nonzero ordinary Weierstrass parameter. Both complete programs and all outputs, including the first symbolic verifier's domain-coercion failure, are retained. The full geometric seed proof uses the previously checked Cartier, stable divisor-sequence and very-ample Bertini inputs. Root separately read and independently proved the entire axis-kernel pair/triple incidence argument and normalization transfer. An initial ordinary-axis transfer proposal was incorrect: its norm class is(6,3n). The repaired supersingular-axis transfer gives(6n,3) for oddn and closes only a congruent2mod4 in the thin strip;4-divisiblea remains open.\n''')
result={'status':'PASS','actual_utc':now,'events':len(events),'scope':'Seed plus corrected odd supersingular-axis transfer; no4-divisiblea assertion.'}
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
