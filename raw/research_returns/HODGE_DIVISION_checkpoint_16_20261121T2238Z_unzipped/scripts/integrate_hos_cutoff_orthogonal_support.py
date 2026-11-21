"""Integrate whole-reviewed HOS13--16 and OL06--08; no numerical re-run."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json

R=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
paths={
 'HOS13-15':'agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_cutoff_section.tex',
 'HOS16':'agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_sharp_section.tex',
 'OL06-08':'agents/imprimitive/orthogonal_lowlevels/orthogonal_support_section.tex'}
frozen={
 'HOS13-15':'42ccec86bd4fa25e91c9156204e215e901f3b8ea6a175c9012ba2948dae72bba',
 'HOS16':'ce8fc689891738dbf571cdae6f92879bca88937129ac66bf278b6ec6f72cdd3f',
 'OL06-08':'fefeade2dbdf99e8c7ce67fc78eaa0a26c178f2711a7162229fab9573065f8a1'}
for k,p in paths.items():
 assert hashlib.sha256((R/p).read_bytes()).hexdigest()==frozen[k],k
def change(s,a,b):
 assert s.count(a)==1,(a,s.count(a))
 return s.replace(a,b)
q=R/'QUESTIONS.tsv'
rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert all(r['id'] not in ('Q2bs','Q2bt','Q2bu') for r in rows)
(R/'research/gates_before_hos_cutoff_orthogonal.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q2i'},indent=2)+'\n')
changes={
 'HOS13-15':('This is a new derivation, submitted for whole-proof review. The first',
 'This new derivation has passed whole-proof reviews by /root and\n/root/imprimitive, with independent exact arithmetic recorded separately.\nThe first'),
 'HOS16':('The argument is submitted for independent\nwhole-proof review; it does not assert existence at any surviving rank.',
 'The entire argument and invoked published proof have passed independent\nwhole-proof reviews by /root and /root/imprimitive; the separate exact\narithmetic also passes. It does not assert existence at any surviving rank.'),
 'OL06-08':('universal proof.  Independent final review is pending.  Actual',
 'universal proof. Whole-proof reviews by /root and /root/g34\\_eightfolds\npass, with independent exact arithmetic recorded separately. Actual')}
for k,(a,b) in changes.items():
 p=R/paths[k];p.write_text(change(p.read_text(),a,b))
p=R/'HODGE_DIVISION.tex';s=p.read_text()
for anchor,extra in [
 ('agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_section.tex',[paths['HOS13-15'],paths['HOS16']]),
 ('agents/imprimitive/orthogonal_lowlevels/orthogonal_lowlevel_section.tex',[paths['OL06-08']]),
 ('agents/g34_eightfolds/bireflection/higher_odd_symplectic_five_bibitems.tex',['agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_sharp_bibitems.tex']),
 ('agents/imprimitive/orthogonal_lowlevels/orthogonal_lowlevel_bibitems.tex',['agents/imprimitive/orthogonal_lowlevels/orthogonal_support_bibitems.tex'])]:
 a=r'\input{'+anchor+'}'
 s=change(s,a,a+'\n'+'\n'.join(r'\input{'+x+'}' for x in extra))
s=change(s,'higher $q=3$ factors remain open among these single-field cases.',r'''higher $q=3$ factors are further restricted by D-HOS-13--16.
The all-order-three carrier bound is $2a/9$. The complete prime-order
reduction and the published Larsen--Shalev--Tiep restricted-support
estimate give $\nu\ge\delta_*a$ for $n\ge284$, where
$\delta_*=189312302221/1024000000000>1/6$.
The compatible normalizer of a nonselfdual factor is scalar times inner;
tensor cycles have stronger support. Twelve genuine inertias would
force $e\le1536000000000/55936906663<28$, contradicting the factor
degree. Thus only $4\le n\le283$ remains in this higher characteristic-three
symplectic family; D-HOS-15 also supplies the independent coarser effective
cutoff $n<10^{30}$.''')
s=change(s,'ordinary self-dual characters of level below $10^{30}$.',r'''ordinary self-dual characters of level below $10^{30}$ at that stage.
D-OL-06--08 now closes this unbounded-dimension case. For every
$d\ge22$ and these nine fields, an ordinary irreducible character
extending to $O$ has full compatible-normalizer support at least
$7a/64$. Opposite abelian radicals, quadratic weight counts, reflection
commutators and finite-field descent give the complete bound, including
the possible character discrepancy between extensions to $O$.
The actual nontrivial multiplier budget forces $e\le64$, below the
factor degree. Together with D-OL-01--05 this leaves only
$d\le4\cdot10^{30}-3$ for every transitive orthogonal core.
This is a finite simple-factor parameter range, not an enumeration
of tensor powers, scalar extensions or actual sources.''')
s=change(s,'The remaining ordinary low-level natural dimension is unbounded;','At that stage the remaining ordinary low-level natural dimension is unbounded;')
p.write_text(s)
base=('D-HOS-13--15 proves all-order-three support2a/9 and a complete inner prime-order reduction. Nonselfdual higherSp(q3) compatible factor normalizers are scalar times inner. The previously checked explicit LarsenTiep estimate excludes all ranksn>=10^30, allowing mixed such ranks and factor permutations. ')
sharp=('D-HOS-16 sharpens the remaining higherSp(q3) nonselfdual ranks to4<=n<=283: the published LST2011 Th4.3.6 and Remark4.3.7 restricted mu2 support give delta*=189312302221/1024000000000>1/6 for n>=284, and the actual twelve-inertia budget gives e<=1536000000000/55936906663<28 against degree>=3^283. ')
orth=('D-OL-06--08 closes the unbounded orthogonal natural-dimension gate. Every ordinary O-extendible irreducible overq∈{2,3,4,5,7,8,9,11,13},d>=22 has full compatible-normalizer support7a/64. With OL01--05, transitive factors of d>=4*10^30-2 are ordinary,O-extendible,selfdual; nontrivial multiplier forces e<=64 against the factor-degree floor. Thus every remaining transitive orthogonal factor has d<=4*10^30-3. This bounds simple-factor parameters, not tensor multiplicities, scalar extensions or actual-source enumeration. ')
for r in rows:
 if r['id']=='Q2i':
  t=r['finding_ids_or_current_gate']
  t=change(t,'Nonselfdual higherq3 factors remain open. ',base+sharp)
  t=change(t,'Ordinary low-level naturald remains unbounded; no theta irreducibility/exhaustion or fullO extension is claimed. ','At this intermediate stage ordinary low-level naturald remained unbounded. ')
  t=change(t,'The unbounded naturald gate is now ordinary selfdual level<10^30 over exactlyq∈{2,3,4,5,7,8,9,11,13}. ',orth)
  r['finding_ids_or_current_gate']=t
new=[
 ['Q2bs','Prompt target2; higher characteristic-three symplectic cutoff','Can nonselfdual higherSp(q3) transitive sources have arbitrarily large natural rank?','refuted',base+'Whole root/peer proof, source and code readings PASS. This coarse cutoff is sharpened in Q2bt.'],
 ['Q2bt','Prompt target2; LST2011 restricted symplectic support','Can the surviving nonselfdual higherSp(q3) rank be at least284?','refuted',sharp+'Whole root/peer proof and complete published estimate/proof readings PASS; exact arithmetic independently reconstructed. No existence at the surviving ranks is asserted.'],
 ['Q2bu','Prompt target2; extendible low-field orthogonal normalizers','Can the residual ordinary selfdual orthogonal core have unbounded natural dimension?','refuted',orth+'Whole root/G34 proof, primary-passage and author-code readings PASS; independent finite supplements are separate from the universal proof.']]
rows.extend(dict(zip(fields,x)) for x in new)
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-HOS-13--15','targeted proof check','Root whole frozen proof, full author checker/JSON and all final unitarity clarifications read. PASS Siegel generation, exact quadratic weights, Heisenberg phase/trace, all prime-order cases, nonselfdual outer exclusion, tensor support and actual source budget. No new source theorem is re-proved.',paths['HOS13-15']),
 ('D-HOS-13--15 peer audit','targeted proof check','Root read entire imprimitive peer report SHA8c8b1a5c347aa16098dccf4618e7ae3a36a442a98459286f7a9dd066a4ed6c47. Whole proof/source/code PASS; independent full F19 carrier reconstruction0.607898250s,59802forms,2187carriers,4374powers,1458spectra. Initial unsupported .copy API error retained. Root does not claim whole peer-code reading.','agents/imprimitive/audit_symplectic_three_cutoff/PEER_AUDIT.md'),
 ('D-HOS-16','targeted proof check','Root whole frozen proof/bibliography/author checker/JSON PASS. Restricted mu2 support2n, correct radical sqrt(N/7), threshold284, delta fraction, degree ceiling and full source scope all verified. Author exact first PASS0.001372407s.',paths['HOS16']),
 ('LST2011 Theorem4.3.6 Remark4.3.7','used and rechecked in this run','Root fresh complete definition/constantp1907, theorem and entire proofpp1917-1923, and remark1923 read; original published renderedpp1918,1922,1923 visually checked. PDFSHAdbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e. Prop4.2.3 statement/setup separately read but not used here. No independent re-proof of source classifications.','agents/g34_eightfolds/bireflection/sources/LST2011_Waring_published.pdf'),
 ('D-HOS-16 peer audit','targeted proof check','Root entire imprimitive report SHA9ee67f208daa5e024f78ea2ca92192efcea4f53818036078e80d4fc07114fb84 read. Whole proof/source/code PASS; independent integer arithmetic0.002043289s. Source proof freshly read and rendered independently. Root does not claim whole peer-code reading.','agents/imprimitive/audit_symplectic_three_sharp/PEER_AUDIT.md'),
 ('D-OL-06--08','targeted proof check','Root entire frozen proof, exact full checkpoint14-to-frozen diff, all author checker283lines and full JSON/bibliography/source notes read. PASS radicals/generation, all weight orbits, counting, faithful full normalizer, O-extension character, linear/semilinear cases and actual source. Author final arithmetic17.721761447s; finite supplements not universal proof.',paths['OL06-08']),
 ('D-OL-06--08 primary passages','used and rechecked in this run','Root fresh Taylor full invoked Witt/decomposition/reflection-generation/perfectness/simplicity proofs pp57-58,138-140,157-163 and O2 dihedral Th11.4; TaylorVinroot2018 full Lem2.1/setup383; LiXia complete Table2.1/section14 locally (new web fetch failed); Liebeck2017 complete conventions/Th2.4ipp2-4 and rendered denominator sqrt(q)-1. Earlier GLT3.7 full165-167 retained. KTV fullOquotient/center/reality rechecked earlier20:55. Exact scopes preserved.','agents/imprimitive/orthogonal_lowlevels/SUPPORT_SOURCES.md'),
 ('D-OL-06--08 peer audit','targeted proof check','Root entire G34 report SHAf84c00526d2a27445e9a31e020ab5ed4c8fb98cf903619edaedf47d98f600b6c read. Full proof/source/author-code PASS. Independent arithmetic2.739600632s:40320 O6+2 via ordered bases,9468 GL2 field bases,695232 quadratic identities,71316 scalar cocycles; no author import. Root does not claim whole peer-code reading.','agents/g34_eightfolds/bireflection/ORTHOGONAL_SUPPORT_PEER_AUDIT.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:
  w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:
 f.write('\n## Finite symplectic and orthogonal simple-factor parameter gates\n\n'+now+' — Q2bs/Q2bt/Q2bu refuted; Q2i strictly reduced. '+base+sharp+orth+'These changes occur after review08. The base and sharp cutoff are integrated together; the final smaller gate supplies movement. Review/source maintenance is not separate movement. No formal hourly review is performed here.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
 f.write('\n## No unbounded q3 symplectic or orthogonal simple-factor range\n\n'+sharp+orth+'These are necessary restrictions on actual condition-A curve suppliers (cote16 scan050, as corrected SIGN_NEXT SN-C03/C04), with original-field inclusion, actual Shapiro/polarized variation and period rank9. They do not construct cycles. The condition-I division (scan049/cote44 Th4), Cayley-Hamilton inversion (scans048-049), lambda/K-theory, realizations, weights and motivic/L-function placements remain as in the common framework; Markman/Severn/032 remain conditional where invoked.\n')
out={'date_utc':now,'integrated':list(paths),'frozen_reviewed_sha256':frozen,'canonical_sha256':{k:hashlib.sha256((R/v).read_bytes()).hexdigest() for k,v in paths.items()},'new_rows':{'Q2bs':'refuted','Q2bt':'refuted','Q2bu':'refuted'},'strictly_reduced_main_gates':['Q2i']}
(R/'research/hos_cutoff_orthogonal_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
