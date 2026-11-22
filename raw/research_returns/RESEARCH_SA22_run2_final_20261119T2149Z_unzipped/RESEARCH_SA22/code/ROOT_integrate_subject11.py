#!/usr/bin/env python3
"""Integrate the independently audited subject11 statements and exact scope."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re

root=Path(__file__).resolve().parents[1]
stamp=datetime.now(timezone.utc).isoformat()
fragments=[
 'notes/C_Greenberg_finite_uniform_fragment.tex',
 'notes/ROOT_complete_Greenberg_points.tex',
 'notes/C_Witt_localization_fragment.tex',
 'notes/B_Suzuki_Greenberg_fragment.tex',
]
for name in fragments:
 assert (root/name).exists(),name

p=root/'sections/part_B.tex'; text=p.read_text()
old=r"\subsubsection{11. A scoped N\'eron theorem and the historical category question}"
new=r"\subsubsection{11. Piecewise structures and the relative N\'eron construction}"
assert old in text or new in text
text=text.replace(old,new)
text=text.replace(r'We retain that comparison separately in Question~\ref{U:thesis-programmes};',
                  r'The following theorems give the directly relevant finite-partition and relative-cohomology comparisons;')
start=text.index(r'\paragraph{The original partition construction.}')
end=text.index(r'\input{notes/C_constructible_group_algebraization.tex}',start)
text=text[:start]+r'''\paragraph{The original partition construction and the scope of the answer.}
Original cote~43, folios~91,93,95--96 (PDF pages one higher), gives a
complete discrete valuation ring with perfect residue field, finite
surjective descent on the target, and a functor
$\mathcal N:\mathcal C(S)\to\mathcal C'(k)$ explicitly named after
N\'eron. Its formula is a colimit over finite constructible partitions,
applying the valuation-ring construction to each piece before evaluating
the sheaf \cite[folio~95]{A567_GrothendieckCote43}.
The next folio proposes a relative-cohomology interpretation but marks
injective preservation for verification and crosses out an argument.
We do not attribute a completed proof to that proposal. Folio~85
separately defines a localization at integral radicial surjections;
this does not identify it with the finite-piecewise category below.

EGA~I connects its constructible-topology scheme to N\'eron reduction
\cite[I, 7.2.14, pp.~338--339]{ROOT_EGAI1971}; the precise relation to
Olivier's universal absolutely flat construction is recorded by
\cite[8.3, p.~581]{ROOT_Ferrand2003}.
We answer the catalogue's expressly permitted strongest-proved-statement
alternative by the complete category and group-object comparisons,
finite and complete Greenberg realizations, exact infinite obstruction,
and perfect-test relative cohomology below. Every test category is
specified. We do not assert the lexical identity of every occurrence of
``morcel\'es'', define the still unverified historical ``flasque''
qualification by guesswork, or identify all historical and modern sites.

''' + text[end:]
anchor=r'\input{notes/C_absolute_flat_piecewise_comparison.tex}'
if r'\input{notes/C_Greenberg_finite_uniform_fragment.tex}' not in text:
 text=text.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+name+'}' for name in fragments))
p.write_text(text)

p=root/'sections/unresolved.tex';text=p.read_text()
pat=r'\\begin\{question\}\[B\.3, subject 11:.*?\\end\{question\}\s*'
match=re.search(pat,text,re.S)
if match:
 backup=root/'notes/subject11_previous_unresolved_formulation.tex'
 if not backup.exists():backup.write_text(match.group(0))
 text=text[:match.start()]+text[match.end():]
p.write_text(text)

p=root/'RESEARCH_SA22_paper.tex';text=p.read_text()
text=text.replace('\\part{Unresolved obligations and audit}',
                  '\\clearpage\n\\part{Unresolved obligations and audit}') if '\\clearpage\n\\part{Unresolved obligations and audit}' not in text else text
p.write_text(text)

p=root/'notes/C_Witt_localization_fragment.tex';text=p.read_text()
text=text.replace('For every ring $A$,','For every commutative ring $A$,')
p.write_text(text)

fields=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
p=root/'B_results.csv';rows=list(csv.DictReader(p.open()))
next_id=max(int(r['id'].split('.')[1]) for r in rows if re.fullmatch(r'B\.\d+',r['id']))+1
for r in rows:
 if 'B:perfect-Greenberg-cohomology' in r['where_proved']:
  r['notes']=r['notes'].replace('Full primary proofs read by B/C/root.',
    'Full primary proof audits by B/C; root independently checked the exact statements, derived typing, cited Sections7--8/10 and the complete used Suzuki2018/Begueri proofs.')
 if re.search(r'label B:subject11$',r['where_proved']):
  r['notes']='Ordinary smooth-test abelian Neron-model theorem, BLR1.3Theorem2. Subject11 is answered under B.3\'s strongest-statement alternative by this and the separately numbered piecewise-category, finite/complete Greenberg and relative-cohomology theorems. This ordinary mapping functor alone is not identified with the historical partition functor.'
details={
 'B:finite-Greenberg-piecewise':('Proved under stated hypotheses','Equal-characteristic finite truncation; algebraically closed k; separated finite-type X, possibly nonreduced; finite reduced test partitions. Exact realization in the absolutely flat category and product/group preservation proved.'),
 'B:uniform-partition-obstruction':('Refuted','Explicit singleton-idempotent series refutes an infinite-limit/finite-partition interchange. Injectivity, every truncated quotient and proper dense completion are proved. Infinite argument, not a finite-computation claim.'),
 'B:finite-cover-partition-obstruction':('Refuted','Obstruction persists under every finite surjective cover of the specified reduced affine finite-type site, hence after sheafification in sets or additive abelian groups. No assertion about ring epimorphisms or the entire historical site.'),
 'B:complete-Greenberg-points':('Known','Arbitrary R-scheme; complete DVR with perfect residue field, perfect test algebra in mixed characteristic. Explicit derivation from corrected BGA17.5/18.2 and Bhatt2014Theorem4.1/Remark4.6; completeness and relative typing checked; no finite-partition interchange.'),
 'B:Witt-localization-witness':('Proved under stated hypotheses','Universal ghost-polynomial identity; corrected explicit nonlocalizable vector in polynomial/perfect domains. Source coordinate convention checked; original illustrative tuple belongs to the localization. Existing147-check certificate supplements the full infinite proof.'),
}
pattern=re.compile(r'\\begin\{(theorem|proposition|lemma)\}\[[^\n]*\]\\label\{([^}]+)\}(.*?)\\end\{\1\}',re.S)
added=[]
for name in fragments:
 source=(root/name).read_text()
 for m in pattern.finditer(source):
  label=m.group(2)
  if label not in details or any('label '+label==r['where_proved'].split(', ')[-1] for r in rows):continue
  status,note=details[label]
  refs=set(re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',source))
  cites=[]
  for c in re.findall(r'\\cite\w*(?:\[[^\]]*\]){0,2}\{([^}]+)\}',source):cites.extend(c.split(','))
  depmap={
   'B:finite-Greenberg-piecewise':'C:absolute-flat-piecewise; BBertapelleGonzalezAviles2022; BStacks',
   'B:uniform-partition-obstruction':'C:absolute-flat-piecewise',
   'B:finite-cover-partition-obstruction':'B:uniform-partition-obstruction; C:absolute-flat-piecewise; BStacks',
   'B:complete-Greenberg-points':'BBertapelleGonzalezAviles2022; ROOT_BhattAlgebraization2014',
   'B:Witt-localization-witness':'BBertapelleGonzalezAviles2022',
  }
  deps=depmap[label]
  rows.append(dict(zip(fields,[f'B.{next_id:02d}',' '.join(m.group(3).split()),status,
      name+', label '+label,deps,'66/002; cote43/091,093,095,096',note])))
  next_id+=1;added.append(label)
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)

event_fields=['statement_id','date','who','type','outcome']
p=root/'ROOT_CHECK_EVENTS.tsv';events=list(csv.DictReader(p.open(),delimiter='\t'))
who='GPT-6 Astra (OpenAI), inherited reasoning effort, run /root, ChatGPT Pro mode'
for label,(status,note) in details.items():
 if not any(e['statement_id']==label and 'ROOT_subject11_integration_audit' in e['outcome'] for e in events):
  events.append(dict(zip(event_fields,[label,stamp,who,'targeted proof check',
      'PASS: '+note+' Exact root source/proof scope is recorded in notes/ROOT_subject11_integration_audit.md; B/C independent audits retained.'])))
events.append(dict(zip(event_fields,['B:perfect-Greenberg-cohomology',stamp,who,'targeted proof check',
 'PASS: exact final site/functor/coefficient typing and retained unit/bounded-output hypotheses checked. Root read cited definitions, exact theorems, Sections7--8/10 and Suzuki2018/Begueri used proofs; B/C read full Mac Lane-resolution source proof. See notes/ROOT_subject11_integration_audit.md.'])))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,event_fields,delimiter='\t');w.writeheader();w.writerows(events)

p=root/'notes/B_gate_audit.md';old=p.read_text()
if not old.startswith('# Part B gate audit — current scope update19:'):
 historical=root/'notes/B_gate_audit_before_review03.md'
 if not historical.exists():historical.write_text(old)
 current='''# Part B gate audit — current scope updateACTUAL_TIMEUTC,19November2026

**Current task-level residuals:2.** They are the necessary original Gabber1994 and Fujiwara1995 passages, hypotheses and used proof dependencies. The overall report remains INCOMPLETE. The mathematical scoped results and general counterexamples are proved; opened modern replacement proofs do not satisfy the separately explicit original-source request.

Subject11 now has a complete answer under B.3's expressly permitted strongest-proved-statement alternative. The five category/group-object theorems are joined by the exact finite Greenberg partition comparison, the infinite uniform-partition counterexample and its finite-surjective sheafification strengthening, complete Greenberg points for arbitrary schemes, and the typed perfect-test relative-cohomology theorem with smooth and finite-flat calculations. Each new mathematical statement has a full proof or exact derivation from opened primary theorems, and independent audits. The additional Witt-coordinate lemma corrects an illustrative source vector without disputing the valid localization inequality or corrected point theorem.

The ordinary BLR mapping property is retained at its actual smooth-test scope. It is not equated with the historical partition functor. The unverified lexical identity of every occurrence of morcelés, the undefined flasque qualification, and an equivalence with the entire handwritten site remain explicit historical limits. The prompt does not impose their complete retrospective recovery in addition to its strongest-statement alternative. Removing that additional obligation is a scope correction, not mathematical movement. The new substantive category/functor answers are assessed separately at the scheduled review.

Current proof and scope records: notes/ROOT_subject11_integration_audit.md, notes/B_literal_catalogue_scope.md, notes/C_subject11_literal_scope_20261119.md, notes/B_Suzuki_Greenberg_derived.md and the independent C/B audits. Original-source attempts include notes/ROOT_original_source_followup_1917.md and notes/A567_GabberFujiwara_IRDB.md, in addition to the earlier B/C logs. No unavailable source is marked opened.

## Historical audit through18:35UTC and subsequent dated research entries

The following prior descriptions are preserved as chronological evidence. Their former residual counts and completion wording are superseded by the current two-row account above.

'''
 p.write_text(current.replace('ACTUAL_TIME',datetime.fromisoformat(stamp).strftime('%H:%M'))+old)

out={'updated_utc':stamp,'added_component_rows':added,'subject11':'strongest-proved-statement alternative fulfilled at explicit scope','remaining_required_rows':2,'formal_review':'not recorded by this integration program'}
(root/'logs/ROOT_integrate_subject11.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
