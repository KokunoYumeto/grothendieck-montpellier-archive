"""Integrate E833 after full mathematical and canonical-source reviews."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
proof='agents/sixfolds/rm_mixed_star_cubic_obstruction_section.tex'
sha='726986467b0ce44bf681cd650ff1ba7aeb0251faae582721f95c3098ba4a3552'
assert hashlib.sha256((R/proof).read_bytes()).hexdigest()==sha
def ch(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
q=R/'QUESTIONS.tsv';rs=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rs[0]);assert all(r['id']!='Q5ag' for r in rs)
(R/'research/gate_before_mixed_star_cubic.json').write_text(json.dumps({r['id']:r for r in rs if r['id']=='Q5i'},indent=2)+'\n')
p=R/'HODGE_DIVISION.tex';s=p.read_text();anchor=r'\input{agents/sixfolds/rm_reversed_elliptic_star_addendum_section.tex}'
s=ch(s,anchor,anchor+'\n'+r'\input{'+proof+'}')
s=ch(s,'General mixed-sign and multicenter configurations remain outside\nthese two statements.',r'''SF-E833 then removes the uniform-sign restriction: every actual
single-center square-zero star in its unit/free extension architecture
is excluded, even for a real center which is not an actual line class.
The compound-image argument handles singular adjusted-unit blocks
without positivity. The full cubic character forces both surviving
blocks to be scalar; their equal defect traces give
$u=(7k/2)\theta$, contradicting the scalar-unit lemma.
Multiple centers, different unit characters, signed virtual
multiplicities and unproved defect determinants remain outside
this conclusion.''');p.write_text(s)
gate=('SF-E833 excludes all actual single-center square-zero stars with positive unit/free multiplicities, arbitrary signs, arbitrary real center, arbitrary rational algebraic B and every coherent effective finite action in E825 scope. The actual extension may put any free sums in A and B, with B locally free; the intrinsic defect determinant is proved to be r*c1(L). Singular adjusted-unit blocks contradict compound-image support; invertible blocks make alpha=a*p+c*z. The nonzero unit cubic term gives two independent mixed-form equations forcing u=(7k/2)*theta, which contradicts E832 scalar lemma. Multiple centers, different unit characters, signed virtual multiplicities and unproved defect determinants remain outside. ')
for r in rs:
 if r['id']=='Q5i':
  s=r['finding_ids_or_current_gate']
  s=s.replace('General mixed-sign stars and multiple centers remain outside these statements. ','')
  s=ch(s,'Remaining: unstable bundles',gate+'Remaining: unstable bundles')
  s=s.replace('outsideE818/E821/E822/E823/E824/E825/E826/E827/E828/E829/E830/E831/E832/E832R','outsideE818/E821/E822/E823/E824/E825/E826/E827/E828/E829/E830/E831/E832/E832R/E833')
  r['finding_ids_or_current_gate']=s
rs.append(dict(zip(fields,['Q5ag','Prompt target5; mixed-sign actual unit/free stars','Can mixed signs in a single-center square-zero free configuration evade the reviewed uniform-sign obstruction and give a balanced weakly semiregular seed?','refuted',gate+'Root and independent G34 whole-proof reviews PASS; exact independent exterior-algebra supplement confirms the full cubic identities.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rs)
events=[
('SF-E833 canonical proof','targeted proof check','Root previously read the whole256-line frozen draft at2a74ada9; now read all273 canonical lines at4c1f347c and the complete conversion metadata. Parent-requested notation-only repair replaces H(V) with complementary invariant-form summands; corrected paragraph and metadata reread, finalSHA72698646. All14equations unchanged. Full mathematical PASS; no cohomology of a contractible tangent plane is asserted.',proof),
('SF-E833 independent audit','targeted proof check','G34 full draft/dependency/author-code/output/attempt review PASS21:10:42UTC. Root read entire report SHA96774170d0b0368a4f08702da93ec6619927bba4ac3f8c9152801598e6109fc2, entire independent checker and output. Own peer implementation first-run0.285877600s reconstructs full8-generator exterior algebra,8Hermitian variables,8cubic components and two rank4 component maps. No author helpers imported. Universal compound-image and actual sheaf/action proofs separately read.','agents/g34_eightfolds/bireflection/MIXED_STAR_CUBIC_PEER_AUDIT.md; agents/g34_eightfolds/bireflection/audit_mixed_star_cubic.py'),
('SF-E833 author exact supplement','computation or formal certificate','Root read entire author checker and full output/attempts. Successful13checks took0.203484884s. Initial raw SymPy structural equality failure retained; exact expanded difference is zero and no mathematical identity changed. No root rerun or finite-to-universal geometric inference claimed.','agents/sixfolds/rm_mixed_star_cubic_certificate.py; agents/sixfolds/rm_mixed_star_cubic_certificate_output.json; agents/sixfolds/rm_mixed_star_cubic_certificate_attempts.json'),
('SF-E825/E832 used by E833','used and rechecked in this run','The previously whole-reviewed exact defect ring map and determinant condition apply to the displayed locally split sequence even with either free sum empty. E832 scalar spectral lemma and invariant compound identification reused exactly. No additional finite-action preservation, positivity, slope or rationality of the star center is required. Published BF/supplied S21 statuses unchanged.','agents/sixfolds/rm_free_summand_overlap_section.tex; agents/sixfolds/rm_elliptic_star_character_obstruction_section.tex')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:f.write('\n## Mixed-sign single-center gate removed\n\n'+now+' — Q5ag refuted; Q5i strictly reduced. '+gate+'Full root and peer readings complete. This is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:f.write('\n## Cubic Chern character obstruction\n\n'+gate+'The condition-A supplier alternatives (cote16 scan050) lose another actual coherent K-theory architecture. The argument combines the lambda-ring exterior-square character with its cubic component and the intrinsic defect determinant, within the common EGA/SGA and Hochschild framework already located. It supplies no cycle and no general nonexistence theorem for arbitrary unstable objects; condition-I positivity, Cayley-Hamilton inversion and motivic/L-function scope remain unchanged.\n')
p=R/'research/frameworks.tex';p.write_text(ch(p.read_text(),'SF-E811--832R concern','SF-E811--833 concern'))
out={'date_utc':now,'integrated':['SF-E833'],'reviewed_draft_sha256':'2a74ada9fb1a9894ffc7c1f402e8eeb4d470af5a7d6d63923951055b99f4b58f','canonical_sha256':sha,'new_rows':{'Q5ag':'refuted'},'strictly_reduced_main_gates':['Q5i']}
(R/'research/mixed_star_cubic_integration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
