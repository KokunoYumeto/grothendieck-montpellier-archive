#!/usr/bin/env python3
"""Serialize manually selected mathematical alarms and checked comparisons.
Context paragraphs are mechanically retained only as quarantined provenance.
No textual reading or verdict is inferred by this program.
"""
import pathlib,json,csv,re,datetime
r=pathlib.Path(__file__).resolve().parents[1];work=r.parents[1];base=work.parent
items=json.loads((r/'items.json').read_text());ib={x['id']:x for x in items};claims=json.loads((r/'claims.json').read_text());cb={x['id']:x for x in claims}
readings=[]
def R(scan,line,reading,alt,evidence,weight='high',confidence='medium'):
 readings.append(dict(cote='29',scan=str(scan),line=line,reading=reading,alternative=alt,evidence=evidence+' No scan was inspected and no reading is changed.',weight=weight,confidence=confidence))
R(95,'Pro: Cor3.3; item247','de G double-prime dans Ker u-prime','Check G-prime versus G-double-prime and the direction of the dual map','The contravariant diagonalizable dual sequence in SGA3VIII3.3 fixes domains; the printed double prime creates a type mismatch.')
R(95,'Pro: Cor3.2–3.3 blank connectors','blank homomorphism slots','Determine arrow directions only from the ink; published dual sequence is a comparator','Kernel/cokernel arguments reverse arrows. A blank carbon-copy connector is not a license to insert the modern direction.','medium','low')
R(96,'Pro49–51; K29-07:51–64','extension triviale','Check whether trivial refers to splitting or only to an action/trivialization','The finite formal elliptic degree-one example has pi2(E)=0 and a nonsplit central inertia extension; either the assertion is wrong or its intended qualifier matters.')
R(96,'Pro49–51; item208','finite mu_n inertia for the projective-line boundary','Check a nonzero-degree assumption and the exact n','coker(d:T→T) is finite for nonzero d but equals T for d=0; the zero-degree case is not removed by changing notation.')
R(98,'Pro88–94; K29-07 arithmetic paragraph','sans doute / n’est en général pas / possible fini','Collate the whole negation and whether fini or abélien occurs','The two attached witnesses differ. Abelianization cannot prove whole-group finiteness, and a totally real tame S3 example refutes universal abelianity for its allowed ramification set.','high','low')
R(98,'Pro inserted abelianization product','product (Z/ell Z)^* without an infinite-place qualifier','Check whether real-place tameness or a diagonal-sign quotient was specified','Allowing ramification at infinity and imposing total reality produce different arithmetic abelianizations; no convention is silently supplied.')
R(100,'Pro henselian marginal insertion and branch product','connected-cover condition and D_i/Y_i subscripts','Collate the exact connectedness quantifier and which components meet Z','The semiglobal reduction uses extension and connectedness of finite covers, not merely a pointwise henselian local ring.','high','low')
R(101,'Pro154–206 cohomology display','mu_n versus mu_underlined_n; quotient Gamma versus G','Check all coefficient and quotient labels','A tuple of inertia exponents and an extension by their product is a different coefficient object from one cyclic mu_n; the lifting class lives over the quotient group.')
R(101,'Pro Chern-class comparison','desired equality with c1(O(D_i)) mod n_i','Check sign, O(D_i) versus O(−D_i), and the transition convention','Changing a local-equation transition to its inverse changes the Kummer Čech cocycle sign. The Codex201 gerbe continuation can fix the convention only after both formulas are collated.')
R(103,'Pro218–241 extension/cancellation','normal inertia and cancelled commutation/product assertion','Check cancellation boundaries and barred inertia symbols','Normal subgroups need not commute (Q8 gives a finite test). The cancellation cannot be erased by restoring the product coefficient from context.')
R(103,'Pro canonical isomorphisms and extension ending','I versus bar I; 1−1 at sequence end','Check the inertia quotient and final endpoint','The cohomology class depends on the actual abelian kernel after quotienting; an unbarred group can have the wrong type.','high','low')
R(104,'Pro242–264 semidirect-product phrase','multiplication by q on Z in a semidirect product','Possibly an ascending presentation or Z[1/q], rather than an automorphism action on Z','For q>1, multiplication by q is not an automorphism of Z. The valid GL(V) conjugacy lemma is unaffected.')
R(104,'Pro bottom inequality','N-prime > N-double-prime','Check > versus ≥ and the intended eigenvalue-orbit exponents','The finite permutation proof needs a positive difference between powers; all symbols can be checked against that exact argument.','medium','low')
R(105,'Pro269–284','exact à gauche versus contextual exact','Retain à gauche; check the crossed constant/sheaf qualifiers','The long exact cohomology sequence gives left exactness after H1-vanishing, not unrestricted exactness in degree2.')
R(107,'Pro diagram; item255','Z=Spec complete local ring with pi1(Z)=Zhat²','Check whether a punctured complement or deleted coordinate divisors were intended','The unpunctured strictly henselian complete local spectrum has trivial finite étale covers; the two-inertia model belongs to the normal-crossing complement.')
R(108,'Pro ideal-product proof','Q∩Q′(Q+Q′) without parentheses','Check grouping around the intersection factor','The proof uses (Q∩Q′)(Q+Q′)⊂QQ′; without grouping a reader can infer a different ideal expression. The supplied reading is retained.','medium')
R(108,'Pro final map','product sign versus plus sign','Check × versus +','The Chinese remainder target is a ring product; the direct-sum notation is harmless only for underlying finite additive groups.','medium')
R(110,'Pro monic-factor proof a)','B at opening, then ideals of A and J+J′=A','Check A/B substitutions','The comaximality equation must be in the ambient polynomial algebra used at that step; mixed ring names obscure the CRT decomposition.')
R(110,'Pro quotient and monic ideal labels','B/R versus A/R and (P)/(R)','Collate the overwritten ring and polynomial letters','The finite-projective rank and characteristic-polynomial proof depends on the precise quotient.','high','low')
R(117,'Pro622–630','normalisé de U-bar where compactified X-bar may be intended','Check the base of normalization','Normalization of the base compactification in the covering function field gives the extension; normalizing the wrong open object does not. Both witnesses are retained.')
R(117,'Pro quotient structure-sheaf expression','p-bar(O_Xbar-prime)^G without pushforward symbol','Check p_* and invariant placement','The quotient construction needs the invariant direct-image algebra on the base, not an untyped application of p.','high')
R(120,'C29-06 extension argument','schematically dense/separated uniqueness used near extension claim','Check whether existence and uniqueness are separately asserted','Schematic density and separatedness compare two existing extensions; they do not create an extension.')
R(121,'C29-06 determinant display','det N=±p^r','Check square-matrix qualification and characteristic-zero convention','Invertibility on the prime-to-p Tate lattice requires a square matrix and determinant a unit at every ell≠p; in characteristic0 this means±1.')
R('122–123','C29-06 Remords','conjugate inertia groups versus conjugate homomorphisms','Check the common Tate-sheaf trivialization and chosen paths','The Remords upgrades subgroup information to maps only after the specified coefficient identification; an omitted choice changes the statement.')
R(124,'Pro641–649; C29-07 cover','ensembles / schémas versus other subtitle','Collate the subtitle without inferring mathematical content from the cover','This determines the documentary heading, not the hypotheses of the finite group-scheme theory.','low','low')
R(125,'C29-06 incipit/date; item228','18.(6|8).1959','18August1959 is supported by the published correspondence, but the ink must decide the glyph','The exact Tate incipit and subsequent group-scheme passage occur in the published18August1959 letter; this does not date every adjacent leaf.','medium','high')
R(129,'Pro first homotopy paragraph','underlined Pi1 versus plain Pi1','Check where the relative progroup/local-system notation is underlined','A relative group-scheme local system, a geometric group and an ordinary profinite group are not interchangeable.')
R(131,'Pro relative torsor definition','cancelled plat/séparable, inserted étale for G','Retain the surviving finite étale qualification; collate cancelled words','The relative representability question differs substantially for finite flat infinitesimal G. The insertion changes the category.')
R(131,'Pro universal direct-image hypothesis','universellt versus universelle','Check that f_*O_X=O_S is asserted after every base change','Pointed rigidity/representability arguments use the universal form, not only equality on the initial base.')
R(131,'Pro Cas fini?? and bracket cas à fibres finies','finite structural group versus finite fibres of the functor','Collate which finiteness is questioned','A fixed finite G does not automatically give the exact quasi-finiteness conclusion of the relative moduli functor.','high','low')
R(132,'Pro English I-6 second paragraph','such a vector is in T','Check f(v)∈T versus v∈V or v∈f^−1(T)','The source introduced v in V and T⊂W; the literal membership has the wrong ambient vector space.')
R(133,'Pro criterion(v)','algebraically closed field extensions versus contextual separable extensions','Preserve algebraically closed in both fields and collate k/K capitals','The condition compares geometric fibres and is not the same as invariance under every separable extension of arbitrary fields.')
R(135,'Pro marginal neighbourhood model','compatibility only over local schemes versus actual neighbourhood extension','Collate the inserted neighbourhood clause and overlap maps','The set consisting of a generic point and one closed point of A1 gives the obstruction to inferring openness from local-scheme data alone.')
R(135,'Pro final paragraph','Je vais pour du moins ramener au local versus contextual Je ne suis pas sûr','No replacement without the scan','The attached witnesses do not support the contextual quotation. Its presence would change documentary self-flag classification, not prove the gluing lemma.','medium','low')
R(137,'Pro corrected implication','admissibility preserved by arbitrary base change; faithfully flat descent','Collate the direction and faithful-flat qualifier','The source itself cancels an implication and replaces it; descent uses uniqueness of the infinitesimal kernel, while arbitrary-base descent is not automatic.')
R(138,'Pro final minimality formula','P′ torsor under G, followed by P′×_G G′','P′ under G′ and extension P′×_(G′)G, if the intended subgroup is G′⊂G','The contracted product must extend the smaller structural group to the larger one; the literal formula has the direction reversed.')
R(139,'Pro definition/proposition of pointed-torsor functor','Z with superscript0/1/none, and point xi/a','Collate each occurrence separately','The notation must distinguish a pointed isomorphism-class functor from an unpointed cohomology set. A conventional H1 notation is not silently substituted.','high','low')
R('139–143','equalizer/reduction proof and restart','R asserted H-torsor before flatness; later closure axiom','Check whether the missing flatness/category qualification was inserted or is a genuine gap','The alpha_p equalizer and cusp examples meet reduced-base conditions but break unrestricted variable-base flatness; the later constant-k category is not refuted.')
R(148,'K29-09 uniform completion proof','V relation on W rather than X; W² rather than tilde-W²','Collate ambient X/W and completion tildes','The entourage-composition argument must relate pairs of Cauchy filters; changing ambient space makes the containment ill-typed.')
R(152,'K29-09 deleted Bpi passage','H0=Hom(pi_s,E)','Possibly Hom from the one-point trivial pi-object','Equivariant Hom from the regular pi-set gives E, whereas H0 is E^pi. Cancellation is preserved.')
R(156,'K29-09 frame-torsor margin','G orbits where H stabilizer quotient is intended','Check G/H lettering','Recovering an n-sheeted cover from its S_n-frame torsor uses the stabilizer S_(n−1), not the full S_n quotient.')
R(157,'K29-10 free-locus theorem','cas fini qualification','Check whether finite étale is the intended scope','The doubled-origin étale involution has a two-point nonopen free locus; the finite étale case is valid.')
R(159,'K29-10 line109','ramifié','Possibly non ramifié','The construction is a covering/fundamental-group category; ramified and unramified objects have different descent and fibre-functor behavior. This is a hypothesis alarm, not a chosen correction.','high','low')
R(160,'K29-10 classD example','plats affines','Possibly fidèlement plats affines when used as covering epimorphisms','An affine non-surjective flat open immersion is not a cover; effective descent needs the relevant surjectivity condition.')
R(162,'K29-10 proper image statement','conoyau finite','Finite index, unless the image is known normal','For nonnormal subgroups the set of cosets has finite cardinality but there is no quotient group with the indicated kernel.')
R(162,'K29-10 nodal example','Zhat deprived of its p-component','Check an unstated prime-to-p convention or the deletion','Ordinary étale cyclic graph covers of a nodal rational curve exist in every degree, includingp.')
R(176,'K29-11 pi2 spectral-sequence display','H1 identified with a limit of H2; i/j indices','Check degree and transition indices in the whole diagram','The low-degree cohomology exact sequence does not permit this degree change without an additional suspension or shifted complex.')
R(180,'K29-11 margin','résolu / affirmative','Collate the exact margin and its attachment','A marginal word cannot resolve all fpqc effectivity cases unless one knows which statement it qualifies.','high','low')
R(183,'K29-11 Set-functor criterion','ordinary continuous maps from the inverse limit','Check whether a uniform-continuity or finiteness qualifier is present','The Baire-space counterexample meets all three written assumptions. Uniform continuity would repair this example, but is a reconstruction and is not inserted into the text.')
R(186,'K29-11 last definitions','pi2 versus pi1 glyph in the category-valued programme','Collate the index with the preceding half-cosimplicial construction','A fundamental-category construction and a second-homotopy group have different types.','medium','low')
R(187,'K29-11 normalization proof','normalization of the base maps to X','Check direction or a missing open-subscheme qualifier','For a strict open immersion X⊊Y with Y normal, Y does not generally map to X overY. The intended finite-type theorem has a different normalization proof.')
def tsv(path,rows,fields):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
tsv(r/'readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
links=[]
def L(kind,fr,to,what,evidence,notes=''):
 links.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=notes))
# Explicit comparisons whose two supplied ends were read by root/peer.
L('folder','29/88–94: formal tame tube; review29a SA12-64','29/96–98: SA12-205,207,208','Homotopy sequence, Chern class and the claimed trivial extension','Both transcription ends read; finite formal elliptic cover refutes splitting, while P1 degree-zero needs a separate infinite kernel.','MPL_29_095-140#1 N001,N003,N004')
L('folder','29/101,103: SA12-212–214','29/201: K29-02 gerbe of local equations','Chern classes and the lifting/root-gerbe continuation','Both ends read; late-review Čech calculation records the transition/sign convention. Root gerbe and divisor root stack are distinct.','MPL_29_095-140#1 N008–N010')
L('folder','29/67: generic linear section','29/113–114: SA12-262','Geometric irreducibility inserted in the later Bertini formulation','Both ends read by29a/root; the earlier missing geometric qualifier is not silently imported backwards.','MPL_29_095-140#1')
L('folder','29/45: finite-type character Hom discussion','29/131: SA12-246,253','Finiteness in a relative torsor functor','Earlier end read by29a and root cross-review; later end read by root. Shared finiteness question is not a representability proof.','MPL_29_095-140#3 N049')
L('folder','29/71: universal f_*O=O Picard hypotheses','29/131: SA12-246,254','Universal direct image of O used in a different moduli question','Both supplied ends read; no transfer of the Picard theorem to the pointed-torsor functor.','MPL_29_095-140#3 N050')
L('folder','29/90: vanishing of H1 on a universal tame procover','29/105,176: SA12-216,285','H1-vanishing and the H2/pi2 programme','Both ends read by29a/root. The later Hurewicz identification remains additional mathematics.','MPL_29_095-140#1 N012')
L('folder','29/125–130: finite group-scheme letter','29/137–143: SA12-229–237','Restarted admissibility and minimality argument','Both complete passages read. Category closure and fixed-field versus variable-base maps are explicitly distinguished.','MPL_29_095-140#2 N017–N033')
L('folder','29/165–172: discrete torsors/minimality','29/179–186: SA12-287–292','Component descent, progroups and the Set-functor limit claim','Both passages read. The valid group-homomorphism theory is not the false ordinary continuous-Set-map criterion.','Codex K29-10; K29-11')
L('folder','29/117,119–121: inertia maps','29/122–123: Remords','Subgroup conjugacy refined to homomorphism conjugacy','Both ends read; common Tate-module trivialization retained.','MPL_29_095-140#1 N013,N014')
# Exact published comparisons; use claim IDs for complete hypotheses and bibliographic keys.
for nums,to,what in [
 ([233],'EGAIV4 17.4.1(d),17.4.9,17.5.1','Reused EGA draft; final17.4.10 is different'),
 ([230,231,232],'SGA3VIII 3.2–3.5,section4','Exact diagonalizable-group typescripts'),
 ([248],'Grothendieck–Serre correspondence,18August1959,printed91ff','Exact letter incipit and finite-infinitesimal programme'),
 ([227,228],'SGA3XI3.1,3.5–3.8','Related representability and gluing criteria, scope limited'),
 ([261,262,267,269],'SGA3X6.1–6.3','Representable discrete torsors and component-nerve presentation'),
 ([210,270],'Bourbaki195 A§2 and A§3 Proposition3.1','Proobjects, minimal objects and strictness; ordinary limits distinguished'),
 ([210],'SGA4I8.3.3(iii),8.13.2–4','Two different prorepresentability criteria, visually read'),
 ([209],'SGA7I1.1–1.3; Serre–Tate1968 appendix reference','Monodromy context and elementary eigenvalue lemma'),
 ([245],'Deligne1980 4.2.7–4.2.8; Orgogozo2006 11.2–11.4; Illusie2006 5.2','Characteristic-two question settled with exact dates'),
 ([244],'SGA7XVIII6.1,6.6–6.7; Esnault–Kindler2016 Theorem1.1','Tame Lefschetz and boundary hypotheses'),
 ([240,242,243],'SGA1X2.10–2.11 and X1.8–1.10','Bertini/connectedness mechanism and base-field limitations'),
 ([252,258,259],'SGA1X1–2,especially2.5','Homotopy sequences, proper image and full nodal graph factor')]:
  cc=[cb[f'CL-SA12-{n}'] for n in nums];fr='; '.join(f"29/{','.join(map(str,c['scans']))} {c['id']}" for c in cc)
  L('published work',fr,to,what,'Exact source passages read; detailed scope and proof level recorded in claims, reference annotations and CHECK_EVENTS.',','.join(dict.fromkeys(i for c in cc for i in c['items'])))
# Preserve every source context paragraph, without promoting unavailable packets to evidence.
src=base/'source/SA12_notes/pro/MPL_29_095-140_notes.md'
note=None;buf=[]
for line in src.read_text().splitlines():
 m=re.match(r'#### (N\d+)',line)
 if m:note=m.group(1)
 if line.startswith('**Context and relation:**'):
  n=int(note[1:]);parent=1 if n<=15 else 2 if n<=35 else 3 if n<=50 else 4
  L('our projects',f'MPL_29_095-140#{parent} {note}', 'Earlier context packets and named research runs (not supplied)',line.removeprefix('**Context and relation:**').strip(),'Quarantined lead. This exact note paragraph and its local transcription were read; the named external context packet/result was not attached and is not independently certified here.',f'MPL_29_095-140#{parent} {note}')
tsv(r/'links.tsv',links,['kind','from','to','what','evidence','note_ids'])
tsv(r/'project_leads.tsv',[x for x in links if x['kind']=='our projects'],['kind','from','to','what','evidence','note_ids'])
events=[];today='2026-11-19';who='GPT-6 Astra Pro; inherited effort; root SA12 consolidation'
def E(s,typ,outcome):events.append(dict(statement_id=s,date=today,who=who,type=typ,outcome=outcome))
for i in items:E(i['id'],'used and rechecked in this run','Read source entry/lead and actual transcription, distinguished author text/earlier interpretation/current reconstruction. '+i['check']+': '+i['check_reason'])
proof_ids=[201,202,203,204,206,209,210,211,212,214,221,222,223,224,225,226,228,234,235,236,237,238,249,250,252,253,254,255,258,259,261,267,269,270,271,273,274,275]
computation_ids=[202,203,204,206,209,212,223,224,225,226,234,235,254,270,274]
refuted={203:'Retain the normal-bundle H2 extension class; pi2=0 does not imply a split extension.',224:'Restrict to a category in which the equalizer is finite flat and the required torsor reductions exist; variable-base maps cannot be admitted without this.',236:'Use the punctured complement of the normal-crossing divisor for the rank-two inertia expression; the unpunctured strictly henselian spectrum has trivial pi1.',255:'The finite étale version is valid; the arbitrary nonseparated étale version is false.',259:'Ordinary étale pi1 of the rational nodal curve is full Zhat, including its p-component.',270:'Use uniformly continuous maps to discrete sets, or a finite compact inverse system; ordinary continuity is insufficient.'}
refinements=[]
for c in claims:
 E(c['id'],'used and rechecked in this run','Actual transcription read and exact literature scope searched. '+c['status_on_pages']+'. '+c['fate'])
 n=int(c['id'].split('-')[-1])
 if n in proof_ids:E(c['id'],'independent re-proof' if n in [202,203,204,206,209,210,212,214,221,222,223,224,225,226,228,234,235,236,237,238,249,250,253,254,255,259,270,271,273] else 'targeted proof check',c['computation']+' See independent_checks.md and explicitly cited peer checks; referenced deep theorems are used as inputs, not claimed independently reproved.')
 if n in computation_ids:E(c['id'],'computation or formal certificate',('Exact finite torsion and grading calculation in programs/torsion_grading_checks.py and outputs/torsion_grading_checks.json; general proof in torsion_grading_checks.md.' if n==274 else 'Exact calculations in programs/exact_checks.py and outputs/exact_checks.json; general mathematical scope is established separately in the written proof.'))
 if n in refuted:
  rid='REF-'+c['id'];refinements.append(dict(id=rid,refutes=c['id'],statement=refuted[n]));E(c['id'],'refuted, with the refined statement’s id',rid+': '+refuted[n])
refs=json.loads((r/'reference_verification.json').read_text())
for b in refs:E(b['key'],'carried as background without fault found' if b['note']=='unverified' else 'used and rechecked in this run','Reference verification status '+b['note']+'. '+b['annote']+' Verification of metadata/statement is not a full proof check unless explicitly stated.')
tsv(r/'CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
(r/'refined_statements.json').write_text(json.dumps(refinements,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'readings':len(readings),'links':len(links),'project_leads':sum(x['kind']=='our projects' for x in links),'events':len(events),'refinements':len(refinements)}))
