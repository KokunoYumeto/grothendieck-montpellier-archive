"""Integrate two fully written, whole-reviewed strict reductions."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
proofs={
 'OL':'agents/imprimitive/orthogonal_levels/orthogonal_level_section.tex',
 'E828':'agents/sixfolds/rm_equal_hull_equivariance_section.tex'}
frozen={'OL':'889ddcc6a70b196139c30678ac6d4a72c8a11a4a58f85b33e53bdfe8df6b2ed9',
 'E828':'4ce0701b2979fe95d69a35fb7c68362d0b53e840f8ba05367ea59fee0c00b6cd'}
for k,p in proofs.items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==frozen[k]
def change(text,old,new):
 assert text.count(old)==1,(old,text.count(old))
 return text.replace(old,new)

q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert all(r['id'] not in ('Q2bn','Q5ab') for r in rows)
(R/'research/gates_before_ol_equal_hull.json').write_text(json.dumps({r['id']:r for r in rows if r['id'] in ('Q2i','Q5i')},indent=2)+'\n')
p=R/proofs['OL'];s=p.read_text()
s=change(s,'The complete author proof and exact arithmetic certificate\nare being checked; independent review is not yet claimed.',
 'The complete proof, invoked sources and author arithmetic certificate\nhave been read by /root and /root/g34\\_eightfolds. Both whole-proof\nreviews pass. Separately authored exact arithmetic checks also pass;\ntheir actual scopes and timings are retained in the check register.')
p.write_text(s)

p=R/'HODGE_DIVISION.tex';s=p.read_text()
for anchor,addition in [
 ('agents/imprimitive/unitary_nonweil/linear_nonweil_section.tex',proofs['OL']),
 ('agents/sixfolds/rm_diagonal_yoneda_obstruction_section.tex',proofs['E828']),
 ('agents/imprimitive/unitary_nonweil/unitary_nonweil_bibitems.tex','agents/imprimitive/orthogonal_levels/orthogonal_level_bibitems.tex')]:
 a=r'\input{'+anchor+'}';s=change(s,a,a+'\n'+r'\input{'+addition+'}')
s=change(s,'remain outside these exclusions.\n\nFor alternating cores,',r'''remain outside these exclusions.
D-OL-01--03 gives a separate effective orthogonal reduction at natural
dimension $d\ge10$. In the transitive setting every factor degree is
less than $q^{(2\cdot10^{29})d}$, and every descended ordinary character
has level $\ell<10^{30}$. A genuinely spin factor, or in odd
characteristic a character which does not extend to the special
orthogonal group, must have $d<2\cdot10^{30}$. The mixed-core
degree obstruction uses full-normalizer support $3e/16$ and $e\le24$.
The remaining ordinary low-level natural dimension is unbounded;
no theta irreducibility or full orthogonal extension is asserted.

For alternating cores,''')
s=change(s,'divisor or filtration types remain open.\nRank-deficient unit matrices,',r'''divisor or filtration types remain open.
SF-E828 closes the apparent equal-hull exception: same-slope free
line blocks remain actual invariant subobjects even when one has the
unit hull's Chern class, and averaging the existing splitting gives
an actual equivariant unit complement. Thus the E826/E827 conclusions
retain their Ext and cap hypotheses but no longer require those two
Chern classes to differ. A nonsplit positive HN factor and several
distinct flat isomorphism types within one Chern-class block remain
outside this statement.
Rank-deficient unit matrices,''')
p.write_text(s)
ol=('D-OL-01--03 further forces every transitive orthogonal factor of naturald>=10 to have degreea<q^((2*10^29)d), and every descended ordinary character to have level<10^30. Genuinely spin factors, or odd-characteristic characters not extending toSO, have d<2*10^30. The separate arbitrary-mixed all-above-degree-barrier theorem has full-normalizer support3/16 and sourcee<=24. Ordinary low-level naturald remains unbounded; no theta irreducibility/exhaustion or fullO extension is claimed. ')
eh=('SF-E828 removes the unequal-hull-Chern-class restriction in E826/E827: distinct-Chern-class same-slope free line blocks are canonical invariant subobjects even when one has c1(L), and averaging the actual ordinary retraction gives an honest equivariant unit complement. All prior Ext/cap and actual split-positive-factor assumptions remain. Nonsplit positiveHN factors and multiple flat isomorphism types inside one Chern-class block are outside. ')
for r in rows:
 if r['id']=='Q2i':r['finding_ids_or_current_gate']=change(r['finding_ids_or_current_gate'],'Other small-field higher-rank Lie cores remain.',ol+'Other small-field higher-rank Lie cores remain.')
 if r['id']=='Q5i':
  r['finding_ids_or_current_gate']=change(r['finding_ids_or_current_gate'],'Remaining: unstable bundles',eh+'Remaining: unstable bundles').replace('outsideE818/E821/E822/E823/E824/E825/E826/E827','outsideE818/E821/E822/E823/E824/E825/E826/E827/E828')
newrows=[
 ['Q2bn','Prompt target2; orthogonal degree, level and cover gate','Can a transitive orthogonal source violate the explicit degree/level barrier or retain genuinely spin or SO-nonextendible factors at arbitrarily large natural dimension?','refuted',ol+'Whole root and G34 proof/source audits PASS; exact arithmetic separately reconstructed.'],
 ['Q5ab','Prompt target5; equal-hull free-block equivariance','Can a same-slope free line of the unit hull Chern class evade the actual equivariant diagonal obstruction merely through off-diagonal action?','refuted',eh+'Whole author, root and imprimitive mathematical reviews PASS; no numerical premise.']]
rows.extend(dict(zip(fields,x)) for x in newrows)
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)

events=[
 ('D-OL-01--03','targeted proof check','Root read complete354-line proof, bibliography, source log and entire author checker. Whole mathematical PASS, including cover faithfulness/noninflation distinction, induced SO character, actual commutators, arbitrary tensor normalizers, transitive degree gate and all exponent steps. Status paragraph alone updated at integration.',proofs['OL']),
 ('D-OL-01--03 published inputs','used and rechecked in this run','Root freshly read full published GLT2024 Def3.2ii/Lem3.3-4 proofs pp160-161, Th3.7 pp165-167, Th1.5iii p154/proof167, Prop6.3 pp193-194, Prop7.3 pp198-200, and rendered both exponent pages. Accepted LT5.5 proof and spin support p30 read; HHM35/4 retained checked source status. No classification reproof claimed. Published PDF SHAad6f1d3bf9e0acc60220f9098033513b521f96668967002914da7d5a91ced957.', 'agents/imprimitive/orthogonal_levels/SOURCES.md'),
 ('D-OL-01--03 root arithmetic','computation or formal certificate','Independent universal rational identities PASS at20:39:07UTC in0.025412343s. No author code imported. Exact sigmaM, trace/source constants, level inequality, barrier polynomial, and source-exponent gaps. No group enumeration; no rerun of61900 author boundary cases claimed. Pre-execution transcription of the quadratic coefficient and odd-spin exponent was corrected against the frozen proof.', 'research/root_orthogonal_level_check.py; research/root_orthogonal_level_checked.json'),
 ('D-OL-01--03 independent audit','independent re-proof','G34 whole-proof/source/author-code review PASS at20:37:49UTC, frozen889ddcc6. Root read complete report. Independent exact arithmetic PASS0.044676667s,21900 boundary pairs plus enormous residues and universal identities. Auditor structural-equality implementation failure retained separately; no author defect. Root does not claim a fresh whole reading of the peer code.', 'agents/g34_eightfolds/bireflection/ORTHOGONAL_LEVELS_PEER_AUDIT.md'),
 ('SF-E828','targeted proof check','Root read complete151-line draft, full157-line canonical conversion and independent peer report. PASS Hom-to-unit vanishings including same Chern class and flat twists, actual type preservation, canonical evaluation images, honest conjugation action and averaging of an existing retraction. No canonical complement or equivariant structure invented.',proofs['E828']),
 ('SF-E828 independent audit','independent re-proof','Imprimitive complete mathematical audit PASS20:29:12UTC at draftd57b98f4. Root read full report SHA7b7ba6b5440440d51214356e1b050d91976cb9a4282814c2eb8fdab0d5d6dc9d. No numerical premise; prior Ext and actual split-positive-factor hypotheses retained.','agents/imprimitive/audit_equal_hull/PEER_AUDIT.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:
 f.write('\n## Orthogonal level/cover barrier and equal-hull equivariance integrated\n\n'+now+' — Q2bn and Q5ab refuted; both Q2i and Q5i strictly reduced. '+ol+eh+'All complete new proofs have root and independent peer readings. This integration occurs after formal review08 and is not counted retroactively in it. No stopping review is performed here.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
 f.write('\n## A bounded orthogonal level and an intrinsic equal-hull splitting\n\n'+ol+'This narrows the actual finite-monodromy condition-A supplier gate; it gives no new detector without an actual cycle supplier.\n\n'+eh+'This strengthens the necessary obstruction for the balanced-RM alternative in the supplied categorical framework. The EGA/SGA, realization, lambda-ring and K-theoretic placements remain those of the common framework. Condition-I division, Cayley-Hamilton inversion, and motivic/L-function limits are unchanged; Markman, Severn and032 remain conditional.\n')
p=R/'research/frameworks.tex';s=p.read_text();p.write_text(change(s,'SF-E811--827 concern','SF-E811--828 concern'))
canonical={k:hashlib.sha256((R/v).read_bytes()).hexdigest() for k,v in proofs.items()}
out={'date_utc':now,'integrated':['D-OL-01--03','SF-E828'],'frozen_reviewed_sha256':frozen,'canonical_sha256':canonical,'new_rows':{'Q2bn':'refuted','Q5ab':'refuted'},'strictly_reduced_main_gates':['Q2i','Q5i']}
(R/'research/orthogonal_levels_equal_hull_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
