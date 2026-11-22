"""Promote the reviewed hook/mixed three-tail exclusions and derived integers."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,io,json,re
R=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
items=[
 {'ids':'D-HK301--03','row':'Q2cp','proof':'agents/g34_eightfolds/bireflection/hook_three_section.tex',
  'frozen':'6f3918af33aa3f23c2c89d4ac445635a64c00bd981a0d7f5557636a7eb5c6130',
  'peer':'agents/imprimitive/audit_hook_three/PEER_AUDIT.md',
  'peer_sha':'6a713469b3bb89a39902b3a2c6797f31b7e287db42e45e84de9d51d220efecb3',
  'old':'New author derivation D-HK301--03.  Independent whole-proof\nreview is pending.',
  'new':'New author derivation D-HK301--03. The complete author, root and\nseparate /root/imprimitive whole-proof and primary-source reviews have\npassed, with distinct exact spectrum reconstructions.'},
 {'ids':'HD-MT301--03','row':'Q2cq','proof':'research/alternating_mixed_three_tail_section.tex',
  'frozen':'3073a8ef70d698db8d7ff748ba7df56c1352e24fa1dfbdb1c3c61d54f783f8a8',
  'peer':'agents/g34_eightfolds/bireflection/MIXED_THREE_TAIL_PEER_AUDIT.md',
  'peer_sha':'1686bd1bbcd1ea158036d1da30df23e0a77d2542f80732335be000ed1916221b',
  'old':'New root derivation HD-MT301--03. Complete author and peer\nreviews are pending.',
  'new':'New root derivation HD-MT301--03. Complete root and separate\n/root/g34\\_eightfolds whole-proof, source and checker reviews have\npassed, including a distinct exact cyclic and actual-flag reconstruction.'},
 {'ids':'HD-ALT-10','row':'Q2cs','proof':'research/alternating_four_tail_integer_cutoffs_section.tex',
  'frozen':'3bcc1ca3a7e59f91cb9e46618d5fb8d05244a503a588c69610960e364485b75a',
  'peer':'agents/sixfolds/audit_alternating_four_tail/PEER_AUDIT.md',
  'peer_sha':'7e95f4d7ad019dcddc1387d34ddceca819ed88379bc5ec5522ee435584bd0f60',
  'old':'Root derivation HD-ALT-10; complete review and promotion of its\nthree-box premises remain pending.',
  'new':'Root derivation HD-ALT-10. Complete root and separate\n/root/sixfolds whole-proof reviews have passed. Its three-box\npremises are now promoted after their own complete peer audits.'}
]
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
for item in items:
 assert sha(item['proof'])==item['frozen'],item['proof']
 assert sha(item['peer'])==item['peer_sha'],item['peer']
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert not any(r['id'] in ('Q2cp','Q2cq','Q2cs') for r in rows)
archive=R/'research/frozen_remaining_three_tails';archive.mkdir(exist_ok=False)
for item in items:
 p=R/item['proof'];before=p.read_text();assert before.count(item['old'])==1
 (archive/p.name).write_bytes(p.read_bytes())
 after=before.replace(item['old'],item['new'])
 if item['ids']=='D-HK301--03':after=after.replace('{HK:GarsiaGoupil2009}','{HD:GarsiaGoupil2009}')
 assert re.findall(r'\\\[(.*?)\\\]',before,re.S)==re.findall(r'\\\[(.*?)\\\]',after,re.S)
 p.write_text(after);item['canonical']=sha(item['proof'])
 item['display_count']=len(re.findall(r'\\\[(.*?)\\\]',after,re.S))
hookbib=R/'agents/g34_eightfolds/bireflection/hook_three_bibitems.tex'
oldbib=hookbib.read_text();(archive/hookbib.name).write_text(oldbib)
assert oldbib.count('\\bibitem{HK:GarsiaGoupil2009}')==1
hookbib.write_text(oldbib.split('\\bibitem{HK:GarsiaGoupil2009}')[0])
main=(R/'HODGE_DIVISION.tex').read_text()
anchor=r'\input{research/alternating_two_row_three_tail_section.tex}'
assert main.count(anchor)==1
main=main.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+i['proof']+'}' for i in items))
anchor=r'\input{research/alternating_two_row_three_tail_bibitems.tex}'
assert main.count(anchor)==1
main=main.replace(anchor,anchor+'\n'+r'\input{research/alternating_three_tail_character_bibitems.tex}'+'\n'+r'\input{agents/g34_eightfolds/bireflection/hook_three_bibitems.tex}')
old='main non-Eisenstein problem has at least three boxes off its long\nrow or column and satisfies the exact ALT07/ALT08 shape bounds.'
new='main non-Eisenstein problem now has at least four boxes off its long\nrow or column and satisfies the exact ALT07/ALT08 shape bounds.'
assert main.count(old)==1;main=main.replace(old,new)
anchor='identity exceeds the permitted moving-rank budget.\nThe scalar single-factor'
addition='''identity exceeds the permitted moving-rank budget.
D-HK301--03 and HD-MT301--03 exclude the other two three-box
labels, $(n-3,1,1,1)$ and $(n-3,2,1)$, in the same single-factor
and all-count scopes. Thus all three-box tails disappear from
the remaining non-Eisenstein ordinary transitive gate.
The derived HD-ALT-10 gives $n\\ge20h-2$: respectively
$38,78,118,198,358,838,1318,3238$ in the eight non-Eisenstein
class-number-one fields. These are necessary source inequalities,
not existence or dominance statements.
The scalar single-factor'''
assert main.count(anchor)==1;main=main.replace(anchor,addition)
(R/'HODGE_DIVISION.tex').write_text(main)
hook=('D-HK301--03 excludes the ordinary hook (n-3,1,1,1) for all n>=15: '
 'one factor over every original imaginary quadratic field and every transitive tensor count over non-Eisenstein original fields. '
 'The new all-eigenvalue estimate is nu(Wx)>=A ind(x)+B with A=(n^2-9n+8)/6, B=(n^2-2n-1)/8 and character floor -(n-1)^2/8. '
 'Actual n-letter and nt-letter quotient Riemann--Hurwitz budgets give strict contradictions, retaining the full B and exact weighted-cycle error. '
 'The label (97,1,1,1) passed the previous necessary shape gate and is now excluded; no actual source was asserted. ')
mixed=('HD-MT301--03 excludes the ordinary mixed label (n-3,2,1) in all n>=15 with the same one-factor/all-transitive-count field scopes. '
 'Its all-eigenvalue bound has A=(n^2-8n+8)/3, B=n(n-3)/3 and character floor -n/3. '
 'The actual natural quotient budgets exceed 2a+6 and 2e+6. The previous necessary profile (97,2,1) is excluded. '
 'Together with HD-AT301--03 and the earlier standard/two-box closures, every remaining non-Eisenstein ordinary long label has tail k>=4. ')
derived=('HD-ALT-10 derives n>=20h-2 from k>=4 and ALT07/08, with the actual inducing degree floor retained. '
 'For Q(i), Q(sqrt(-2)), Q(sqrt(-7)), Q(sqrt(-11)), Q(sqrt(-19)), Q(sqrt(-43)), Q(sqrt(-67)), Q(sqrt(-163)), '
 'the necessary integers are 38,78,118,198,358,838,1318,3238. The endpoint (n-4,4) satisfies only the stated necessary numerical conditions. '
 'This is a derived presentation, explicitly not separate movement or a source-existence claim. ')
mainrow=next(r for r in rows if r['id']=='Q2i');oldmain=dict(mainrow)
for r in rows:
 r['finding_ids_or_current_gate']=r['finding_ids_or_current_gate'].replace('Otherthree-box andlargertailsremain. ','')
mainrow['finding_ids_or_current_gate']+=' '+hook+mixed+derived
newrows=[('Q2cp','ordinary hook-three alternating source','Can the ordinary hook-three label supply the actual rank-nine source in any transitive tensor count?','refuted',hook),
 ('Q2cq','ordinary mixed-three alternating source','Can the ordinary mixed-three label supply the actual rank-nine source in any transitive tensor count?','refuted',mixed),
 ('Q2cs','derived integer presentation after all three-box exclusions','What effective integral lower degrees follow from k>=4 and the accepted field shape bounds?','proved',derived)]
for rid,source,question,state,finding in newrows:
 rows.append(dict(zip(fields,[rid,'Prompt target2; '+source,question,state,finding+'Complete root and separate peer whole-proof audits PASS.'])))
out=io.StringIO();writer=csv.DictWriter(out,fields,delimiter='\t');writer.writeheader();writer.writerows(rows);q.write_text(out.getvalue())
(R/'research/gate_before_remaining_three_tails.json').write_text(json.dumps(oldmain,indent=2)+'\n')
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 w.writerow(['D-HK301--03; HD-MT301--03 integration',now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION','targeted proof check',
  'Complete root author-proof/checker/output readings plus both entire final peer reports read. Hook peer determinant/Ramanujan reconstruction PASS6830classes48606rootorders; one auditor-only structural SymPy equality failure corrected by exact expansion and retained. Mixed peer independent triangular inversion PASS22517classes193333entries plus90actualflagcases670200points136388orbits; no failure. Shared cyclic/weighted authorship disclosed. Root has not whole-read either peer program. Only status/bibliography keys changed; all20hook and14mixed displays identical. Q2cp,Q2cq refuted; Q2i strictly reduced after review11.',
  '; '.join(i['peer'] for i in items[:2])])
 w.writerow(['HD-ALT-10',now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION','targeted proof check',
  'Root actually read full new proof, every author checker line, full first PASS output and full sixfolds peer report. Exact monotonicity/positive cubic/endpoints/field table PASS. Author5896inequalities0.046937184s23:37:29UTC; peer257922pairs and actual8hookproducts0.080975055s23:38:56UTC. No assertion failure. Peer conditional k>=4 premises now discharged by separately accepted three-box audits. Root has not whole-read peer program. Q2cs proved; DERIVED ONLY, not separate movement.',items[2]['peer']])
with (R/'LEDGER.md').open('a') as f:
 f.write('\n## Every ordinary three-box tail excluded\n\n'+now+' — Q2cp and Q2cq refuted; Q2i strictly reduced after formal review11. '+hook+mixed+'\n\n'+derived+' No formal review or checkpoint occurs in this integration.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
 f.write('\n## Complete three-box-tail removal and necessary integers\n\n'+hook+mixed+derived+' These are obstructions for actual finite-cover local systems and their representation lambda-rings/K-theory. They shrink condition-A suppliers (cote16, scan050; SIGN_NEXT SN-C03/C04), retaining the established EGA/SGA/FGA, schemes-over-Z and motivic projector frame. They supply no condition-I cycle and add no Markman, Severn or032 premise.\n')
rec={'date_utc':now,'strict_rows':['Q2cp','Q2cq'],'derived_only_row':'Q2cs','main_gate':'Q2i','after_review':11,'objects':items,'math_displays_unchanged':True}
(R/'research/remaining_three_tails_integration.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))
