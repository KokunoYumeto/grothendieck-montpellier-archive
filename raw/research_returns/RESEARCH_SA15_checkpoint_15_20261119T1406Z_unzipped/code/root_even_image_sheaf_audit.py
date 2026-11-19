"""Actual full root audit of the conditional even-image sheaf reduction."""
from pathlib import Path
import csv,datetime,json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_even_image_sheaf_audit.json';assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
 ('lem:ss-even-image-sheaf','PASS: full proof rederived. The nonsplit elliptic Frobenius extension, after positive twisting, gives equal delta-kernel/image and freeness over k[delta]/delta²; tensoring gives free A-module rankb/4. Root checked both rank-drop codimensions, independence of all four derivative vectors, reflexivity via depth, determinant O(-b), vanishing H0, and all four p-basis Cartier identities. Full Frobenius maps into I, lambda has constant unit Frobenius, K is stable, and normal extension gives a common nonzero degreeb determinant polynomial. No irreducibility/reducedness asserted here.'),
 ('lem:ss-even-one-loss-point','PASS: full tangent-P6 construction independently checked. Odd projection degrees make both tangent components generically nonzero; excluding factor flexes gives second-jet surjectivity. Two full first jets have rank6 off the coordinate/crossed exceptions and at least5 everywhere, giving the required rank5/rank4 global-singularity strata and rank4/rank3 secondary-contact strata. Sharp-source factors do not contain P6. Two odd sharp components with one simple cross-tacnode have defect5 and stable rankb-4. An ordinary remaining node makes delta1delta2s nonzero by the gradient determinant, so the point lies in Pcircle.'),
 ('thm:ss-even-full-group-if-unit-Hasse-irreducible','PASS: complete conditional proof rederived, with the unproved determinant hypothesis retained explicitly. Reflexive determinant allocation extends the Omega1 argument and implies the unique covector kernel is the only proper nonzero invariant subspace. One genuine loss-one point gives generic loss1 only under the irreducibility hypothesis. Purity survives the codimension>=9 exclusion. Restrictions of full transvections are transvections or identity on K; the actual GL8 block excludes all nonSL alternatives. The translation kernel is0orallK, and the already proved H1 vanishing excludes0 by its forbidden fixed line. Root requested explicit any-perfect-base-field scope for the arithmetic statement.')]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 writer=csv.writer(f,delimiter='\t')
 for sid,result in events:writer.writerow([sid,now,who,'independent re-proof',result])
with (w/'notes/ROOT_SEARCH_LOG_15.md').open('a') as f:
 f.write(f'''\n## {now}: post-freeze even-image sheaf reduction\n\nRoot read and independently rederived all three new conditional sheaf assertions, including the exact ranks/codimensions, reflexive determinant extension, global simple-tacnode construction, and conditional full-stabilizer argument. No exploratory pencil was used or claimed independently rerun. The exact Kantor--Seress primary theorem and the earlier Lang/purity, covector and H1 inputs had already been fully checked and were matched to the present hypotheses. The unit Hasse divisor's geometric irreducibility and reducedness remain an explicit hypothesis. The later all-even boundary-degree argument has been announced and saved but is not covered by this audit. These files remain outside the frozen CP15 paper pending post-save promotion.\n''')
result={'status':'PASS','actual_utc':now,'complete_statement_audits':len(events),
 'scope':'Conditional even-image sheaf reduction only; later all-even closure not audited here.'}
dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
