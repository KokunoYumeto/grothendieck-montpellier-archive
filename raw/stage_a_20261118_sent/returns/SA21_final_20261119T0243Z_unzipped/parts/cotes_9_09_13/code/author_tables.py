"""Manual reading alarms and links, with both endpoints inspected."""
from pathlib import Path
import csv,json
ROOT=Path(__file__).resolve().parents[1]
R=[];L=[]
def r(scan,line,reading,alternative,evidence,weight='high',confidence='high'):
 R.append(['156-9',scan,line,reading,alternative,evidence,weight,confidence])
r(72,'J156-9-09:273','uncertain membership/negated-membership signs and α|x','Use matching positive membership signs for relational transposition, then negate both sides to obtain orthogonality','The following text explicitly passes to negation; the current asymmetric signs cannot encode the transpose relation.')
r(73,'J156-9-09:288–307','ΣA*, ΣE and ΣA′ mixed in Lemma2','Check whether the domain/codomain labels are ΣE and ΣE′','The formulas act on support lattices of the two fixed disjoncteurs, not support lattices of an introduced subset A.','medium')
r(76,'J156-9-10:85','all structures of disjunction on E correspond to graphs','Check for the qualifier anti-reflexive, already used on line81','General disjoncteurs also require a marked subset E0 of isolated graph vertices; the same page supplies that extra datum.','medium')
r(77,'J156-9-10:123–135','cosuppE(A)=cosupp(A*) with ambient set suppressed; M/A uncertainty','cosuppE(A)=E0 union cosuppE*(A intersect E*), with E*=E minus E0','Left-hand sides contain all universal zero points, while right-hand sides inside E* cannot contain them. The support-lattice isomorphism removes and then reattaches E0.')
r(79,'J156-9-10:197','A subset ΣE','A element ΣE','The following intersection with CA is a statement about one closed subset A of E, not an arbitrary family of closed subsets.','medium')
r(79,'J156-9-10:206','relation d’ordre canonique pulled back from ΣE','relation de préordre unless σE is injective; check whether order is being used in a broad convention','Two points with identical perpendiculars are distinct but comparable in both directions. This may be a terminology convention, not a transcription error.','medium','medium')
r(83,'J156-9-11:73–75','uncertain direction of the diagram inequality','A≤β α(A)','The closure construction gives extensivity; the opposite direction is the conclusion to be proved.')
r(84,'J156-9-11:107','injection or surjection for ΣE→P(E′)','injection','The target is all subsets; surjectivity onto all P(E′) would force a Boolean restriction and is not equivalent to join density.')
r(85,'J156-9-11:131','lower x′,y′ quantified without explicit membership in E′','x′,y′∈E′, with x′≤x,y′≤y','Without membership in the chosen subdisjoncteur, the criterion holds tautologically by taking x′=x,y′=y and cannot characterize density.')
r(86,'J156-9-11:177','Compte tenu de prop.1','prop.2','The general faithful join-dense representation is Proposition2 on scans81–84; Proposition1 is the canonical L→ΣL case.','medium')
r(89,'J156-9-11:268,274','exists/nexists and x/x′ uncertainties','no pair exists; then quantify x∈A','Disjoint direct images require the negation of an existing incident pair; the source variable belongs to A⊆E.')
r(90,'J156-9-12:46–47','A′ or A in barα; B or A′ in barβ','barα acts on A⊆E and barβ on A′⊆E′','The identities must be typed in their respective domains; both are used in the next proof.')
r(93,'J156-9-12:150','β_*(A′)⊥A′ or A; superscript on barA','β_*(A′)⊥A and β_*(A′)⊥barA','The live proof compares a subset of E with its E-closure; the primed ambient set would be ill-typed.')
r(94,'J156-9-12:215','Sup indexed in ΣE or ΣE′','Sup in ΣE','β maps E′ to ΣE; the join must be formed in its codomain.')
r(99,'J156-9-13:59','(iv b)','(v b), or the renumbered (ii)b','Scan95 inserts the pointwise clause and scan97 explicitly names it v b); condition(iv) has no b part.','medium')
r(101,'J156-9-13:107–109','(x,x′)⊥(y,y′) iff x⊥x′ or y⊥y′','x⊥y or x′⊥y′','The printed formula compares elements belonging to different factors. The corrected coordinate pairing is needed for the claimed row/column property; ink remains undecided.')
def l(fr,to,what,evidence='Both endpoint passages read in the supplied transcriptions; relationship checked.',notes=''):
 L.append(['folder',fr,to,what,evidence,notes])
l('156-9 scan65 J156-9-08:276–283','156-9 scan66 J156-9-09:5–7','The injection counterexample to complement commutation continues: surjectivity, hence bijectivity, is required. It does not refute closure commutation for powersets.')
l('156-9 scan66 J156-9-09:16–39','156-9 scan67 same:49–81','Insufficient inclusion is strengthened to equality after closure, and orthogonality preservation is strengthened to faithfulness.')
l('156-9 scan68 J156-9-09:98–104','156-9 scan63 J156-9-08:168–190','Explicit reference to manuscript p59, formulas(*) closure commutation and(**) complement commutation. The two formulas have different hypotheses.')
l('156-9 scan63 J156-9-08:168–190; scans68–69 J156-9-09:98–137; scan75 J156-9-10:42','156-9 scans95–97 J156-9-12:225–355','Corrected Proposition4 answers the earlier closure question; crosslink MP-SA21-9-08 and MP-SA21-9-10.','Both ends read; the generator condition is explicitly inserted and acknowledged.','')
l('156-9 scan68 J156-9-09:93–98','156-9 scans81–84 J156-9-10:257–273; J156-9-11:6–94','The question whether the strong conditions imply an isomorphism is resolved by applying the later faithful join-dense representation theorem.','Both ends read; application is this run’s inference, not an explicit backward citation.')
l('156-9 scan70 J156-9-09:182–201','156-9 scans95–96 J156-9-12:272–276,305–320','The γ-closed criterion and maximal normalized pretranspose are formalized in Proposition4.')
l('156-9 scans72–73 J156-9-09:250–337','156-9 scans95,97 J156-9-12:253–257,335–355','The generator equality corrects both the arbitrary-function lemma and the raw/support adjoint equivalence.')
l('156-9 scan74 J156-9-10:4–14','156-9 scan73 J156-9-09:286–337','The symbol barβ in Cbarβ denotes the closed perpendicular fiber introduced on73, not union extension; no spurious extra-C reading alarm is raised.')
l('156-9 scan75 J156-9-10:44','156-9 scan104 J156-9-13:182','The early morphism definition via transpose commuting with C is retained in the later morphism/comorphism terminology.')
l('156-9 scan79 J156-9-10:193–206','156-9 scan76 same:53–85','Spat3 uses Disj2; the compatible preorder is pulled back from singleton supports.')
l('156-9 scan82 J156-9-11:14–17','156-9 scan87 same:187–193; scan82 same:19–39; scan84 same:90–94','The b′ forward reference to manuscript p83 and explicit inverse-formula reminders are discharged at these exact places.')
l('156-9 scan86 J156-9-11:177','156-9 scans81–84 J156-9-10:257–273; J156-9-11:6–94','The representation reference written prop1 mathematically points to prop2; numeral is left for scan review.')
l('156-9 scan87 J156-9-11:183–187','156-9 scan82 same:19–39','Corollaries explicitly use the inverse maps from Proposition2.')
l('156-9 scan89 J156-9-11:249–275','156-9 scans99–100 J156-9-13:84–93','The composition reminder is realized by normalized composition and the support-category equivalence.')
l('156-9 scan90 J156-9-12:32–69; scan91 same:98','156-9 scans92–93 same:104–167','Inserted closure clauses of Proposition3 are proved after the deferred note; the circular draft is cancelled.')
l('156-9 scan92 J156-9-12:133','156-9 scan90 same:16–47','The phrase lemme1 refers to the statement renamed Proposition3; it is not the old arbitrary-generator Lemma1 of scan72.')
l('156-9 scan94 J156-9-12:201–219','156-9 scans95–97 same:225–355','Question of which maps admit a transpose receives the corrected complete criterion.')
l('156-9 scan98 J156-9-13:12; scan99 same:46–77','156-9 scan95 J156-9-12:253–276; scan97 same:335–355','The corollary checks Proposition4; ivb on99 is an old or erroneous label for the added pointwise condition.')
l('156-9 scan99 J156-9-13:84; scan101 same:112','156-9 scan98 same:3–23','Both p94 references point to normalized correspondences and the closed-fiber relation set, respectively.')
l('156-9 scan104 J156-9-13:160–184','156-9 scans105–106 J156-9-14:8–77','The next folder expands the set graph-factorization characterization: disjointness corresponds to injective target projection, complement to bijective target projection.')
l('156-9 scan104 J156-9-13:184','156-9 scan105 J156-9-14:6; scan107 same:83','The author sets aside the general factorization question and proceeds without such a decomposition. This is evidence of the local change of focus only.')
for name,head,rows in [('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],R),('links.tsv',['kind','from','to','what','evidence','note_ids'],L)]:
 with (ROOT/name).open('w') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(head);w.writerows(rows)
out={'readings':len(R),'links':len(L),'publication_links':0,'project_links':0,'note':'No exact published Grothendieck endpoint or context-project lead was identified in these five folders; no generic resemblance entered as an exact link.'}
(ROOT/'outputs/author_tables_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
