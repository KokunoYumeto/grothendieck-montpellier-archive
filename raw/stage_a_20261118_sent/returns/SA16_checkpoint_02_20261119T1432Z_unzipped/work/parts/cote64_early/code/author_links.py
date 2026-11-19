"""Authored verified links, plus lossless extraction of prior-context lead fields."""
import csv,json,re
from pathlib import Path
from author_records import items
ROOT=Path(__file__).resolve().parents[1]
S=ROOT.parents[2]/'sources'/'SA16_notes'/'pro'
I={int(x['id'].split('-')[-1]):x for x in items}
rows=[]
def link(kind,fr,to,what,evidence,ns,status='both endpoints checked'):
 rows.append({'kind':kind,'from':fr,'to':to,'what':what,'evidence':evidence,
              'note_ids':';'.join(src for n in ns for src in I[n]['sources']),'verification':status})
link('folder','64/27–28; MPL_64_002-039_transcription.tex:998–1132','64/42–43; MPL_64_040-077_transcription.tex:108–157','End(M0)=A⊕W and trace kernel recur before the geometric development.','Both full passages read; finite_groups.py checks identical planes, trace and nonsplit W extension. C-SA16-233.',[233])
link('folder','64/26–29; MPL_64_002-039_transcription.tex:945–1173','64/66–69; MPL_64_040-077_transcription.tex:638–732','Zero-sum lift torsor is used for relative full level4 frames and octahedral faces.','Both passages read;16 lifts,96 frames and two lifts per face recomputed. C-SA16-231/235/241/286.',[231,235,241,283,286,287])
link('folder','64/33–36; MPL_64_002-039_transcription.tex:1331–1556','64/45–53; MPL_64_040-077_transcription.tex:168–343','Finite six-vertex octahedron becomes a geometric six-axis divisor on a conic.','Both endpoints read; structured group has24 direct symmetries. Bare characteristic5 failure isolated separately. C-SA16-240/262/263.',[240,262,263,265])
link('folder','64/54–57; MPL_64_040-077_transcription.tex:348–418','64/58–62; MPL_64_040-077_transcription.tex:424–542','Three four-point objects I,K,F_t and their Klein twists acquire the genus-one involution interpretation.','Both endpoints read; supplement§7 proves I=K∧F_t and fixed-locus classification. C-SA16-260/273.',[260,269,273])
link('folder','64/54; MPL_64_040-077_transcription.tex:348–360','64/63–65; MPL_64_040-077_transcription.tex:545–631','Canonical Klein group of a four-divisor produces the intrinsic doubling quotient.','Both endpoints read; three explicit involutions and F_t identities recomputed. C-SA16-271/277/280.',[271,277,280])
link('folder','64/71–74; MPL_64_040-077_transcription.tex:744–811','64/75–77; MPL_64_040-077_transcription.tex:816–910','Tame tangent-power construction specializes to the elliptic quadratic tangent root and pinning.','Both endpoints read. General arbitrary-G target is false as written; quadratic case is separately proved. C-SA16-289/291/293/298.',[289,291,293,298])
link('folder','64/76–77; MPL_64_040-077_transcription.tex:848–910','64/78–79; MPL_64_078-115_transcription.tex:6–48','Promise to specify Q0 is fulfilled, then orientation data enter the rigidified triple.','Both endpoints read directly; side relation s_i′=i s_i and D_Q0=μ4*. C-SA16-297 ↔ continuation C-SA16-501.',[297,298])
link('folder','64/75–77; MPL_64_040-077_transcription.tex:816–910','64/80–82; MPL_64_078-115_transcription.tex:65–135','Orientation-twisted tangent root is formulated relatively over Z[1/2].','Both endpoints read; scan81 formula27 has O(2). Scan80 formula23 omits a tensor power, handled in continuation C-SA16-502.',[295,296,298])
link('folder','64/66–69; MPL_64_040-077_transcription.tex:638–732','64/93; MPL_64_078-115_transcription.tex:382–391','The zero-sum level4 lifts are explicitly requested to produce canonical Legendre pinning.','Both endpoints read. C-SA16-286 supplies finite data; later question is continuation C-SA16-535, not solved by counts alone.',[283,286,288,298])
link('folder','64/74–75; MPL_64_040-077_transcription.tex:806–843','64/94; MPL_64_078-115_transcription.tex:397–414','Quadratic root groupoid is restated as μ2-torsor twisting after a reference root is chosen.','Both endpoints read; exact local μ2 root classification matches Stacks03PK and AntieauMeierProp4.5.',[293])

link('published work','64/4–5,8–19; MPL_64_002-039_transcription.tex:64–795','SGA1 V Theorem4.1 (retyped p104); VIII Theorem2.1 (p158); IX Proposition4.1 (p182)','Finite groupoid dictionaries extend to finite étale sheaves by effective descent.','Published endpoints opened and read. Exact object dictionaries are our equivariant constructions, not claims that SGA1 states the five-square model.',[213,217,221,235])
link('published work','64/24,37–38,55–62; transcript locators in SA16-228/244/260/273','SGA1 XI §4, after Proposition4.3, retyped pp227–228','Associated bundles and extension of torsor structure group supply the contracted products used here.','Opened formula E(P)=(P×E)/G and its effective-descent construction. The exact D8 cup computation is separate.',[228,244,260,273])
link('published work','64/71–74; MPL_64_040-077_transcription.tex:744–811','SGA1 XIII §2.0–2.1, retyped pp276–279','Tame local inertia and the sheaf of tame torsor classes are the published framework.','Read cyclic tame inertia, Definition2.1.1/2.1.2 and base-change2.1.5. This does not validate arbitrary independently chosen i.',[289,290,291])
link('published work','64/75; MPL_64_040-077_transcription.tex:816–843','EGAII Proposition4.1.6, Proposition4.2.3 and Theorem4.2.4, printed pp72–74; Stacks01OA §27.21','Projective bundle and determinant-line calculation underlying the tangent orientation formula.','Both published endpoints read directly, including the EGA invertible-quotient universal property and base-change §4.2.8–10. The orientation tangent identity is independently proved in supplement§10.',[295])
link('published work','64/27–32; MPL_64_002-039_transcription.tex:998–1325','BrauJones2016 proof of Lemma3.1, equation26 and invariant-plane table, pp7–8','Split GL2(Z/4) congruence sequence and its two invariant planes.','Author PDF opened, exact matrix formulas compared with all16 F2 matrices and96 mod4 matrices. Does not independently supply exact canonical torsor packaging.',[233,234,235,237,238,239])
link('published work','64/45–53; MPL_64_040-077_transcription.tex:168–343','Beauville2010 Proposition1.1; proof of Theorem4.2, case3','Field normalizer of a Klein subgroup and rationality of finite PGL2 subgroups.','Author offprint opened. Prime-to-characteristic convention prevents citing the S4 classification unqualified in characteristic3.',[261,262,267])
link('published work','64/48–53; MPL_64_040-077_transcription.tex:228–343','Hua2026 §42, Theorem42.1 and Counterexample42.2, printed pp194–195','Characteristic5 failure of the bare six-point stabilizer.','Exact field argument opened. Relative correspondence and μ4 refinement explicitly listed as unproved; no formal verification claimed.',[263,265,267])
link('published work','64/63–65; MPL_64_040-077_transcription.tex:545–631','Milnor2004 Theorem3.1 and local-degree equation3, pp3–5','Multiplication descends to a Lattès map; local degrees explain iteration multiplicities.','Primary preprint opened. The universal normalized formula and arbitrary-base hypotheses are independently checked here.',[277,280,282])
link('published work','64/74–77; MPL_64_040-077_transcription.tex:806–910','AntieauMeier2020 Definition4.4, Proposition4.5, Lemma4.7, pp14–16','Legendre atlas as a μ2-torsor and the twisted S3 action.','Primary preprint opened at exact statements and proof. This is the ordinary Legendre mechanism, not the later special μ4 normalization.',[293,296,298])
link('published work','64/66–77; MPL_64_040-077_transcription.tex:638–910','ConradLevel Definition2.7, Remark2.8, Proposition3.2, pp6–8','A suitable level4 point canonically gives a Legendre structure; negating it negates the differential.','Author handout read directly. Remark2.8 excludes a natural ordinary S3 action; later symmetric comparison remains narrower than existence.',[286,287,293,298])
link('published work','64/37–38; MPL_64_002-039_transcription.tex:1581–1633','MerkurjevScavia2024 §1.1 equations1.3–1.4 and Example1.4, pp3–4','Cup-product obstruction for lifting two characters to U3(F2)=D8.','Exact primary cocycle equations opened; site-general formulation independently explained in supplement§5.',[244,245])

# Metadata extraction is lossless, not a claim verdict or inferred mathematical link.
leadrows=[]
entry_to_item={e:x for x in items for e in x['sources']}
for package in ('MPL_64_002-039','MPL_64_040-077'):
 path=S/f'{package}_notes.md'
 text=path.read_text()
 matches=list(re.finditer(r'^### (.+)$',text,re.M))
 for n,m in enumerate(matches,1):
  end=matches[n].start() if n<len(matches) else len(text)
  block=text[m.start():end]
  fields=[]
  for label in ('Context searched and compared','Results-state relation','Context comparison','Register bearing'):
   fm=re.search(r'\*\*'+re.escape(label)+r':\*\*\s*(.*?)(?=\n\n|\n\*\*|\Z)',block,re.S)
   if fm: fields.append(label+': '+fm.group(1).strip().replace('\n',' '))
  e=f'{package}#{n}'
  if not fields: continue
  it=entry_to_item[e]
  raw=' | '.join(fields)
  lead={'kind':'our projects','from':'; '.join(f"{v['file']}:{v['start']}-{v['end']} (scan {v['scan']})" for v in it['lines']),
        'to':raw,'what':'Prior-run contextual comparison preserved as a lead; see its note heading: '+m.group(1),
        'evidence':f"Attached {path.name}, physical lines {text[:m.start()].count(chr(10))+1}–{text[:end].count(chr(10))+1}; local manuscript endpoints were read in this run. The cited context archive and register are not supplied; no claim of rechecking those external endpoints is made.",
        'note_ids':e,'verification':'prior context lead only; external endpoint not verified'}
  leadrows.append(lead)
rows.extend(leadrows)
for name,data in [('links.tsv',rows),('context_leads.tsv',leadrows)]:
 with (ROOT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(data)
print(len(rows), 'link rows, including',len(leadrows),'prior-context leads')
