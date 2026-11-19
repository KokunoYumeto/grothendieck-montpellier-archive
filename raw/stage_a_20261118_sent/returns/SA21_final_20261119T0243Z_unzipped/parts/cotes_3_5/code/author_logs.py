"""Record actual research actions and their limited epistemic strength."""
from pathlib import Path
import json,csv,datetime,collections
O=Path(__file__).resolve().parents[1];date='2026-11-19';who='GPT-6 Astra Pro; effort inherited; run /root/cotes_156_3_5'
C=json.loads((O/'claims.json').read_text());original=sum([json.loads((O/f'claims_{i}.json').read_text()) for i in (3,4,5)],[])
G=collections.defaultdict(list)
for x in original:G[x['search_group']].append(x['id'])
S=[]
def s(k,source,query,groups,result,refs='',limits='Negative search is not proof of absence.'):
 S.append([k,date,source,query,';'.join(sum([G[g] for g in groups],[])),result,refs,limits])
s('S01','web searches; primary backward references','Alexandroff Diskrete Räume1937 pdf; Stong finite topological spaces1966 pdf; Birkhoff rings of sets1937; Grothendieck Esquisse topologie modérée §5 pdf',['alexandrov','poset','lattice','stratification','betweenness'],'Located original metadata, Stong and Birkhoff sources. Full-text Alexandroff access failed; no exact full figure calculus match.','Birkhoff1948;Stong1966;Alexandroff1937;Esquisse1984')
s('S02','web search and primary references','Kochen Specker1967 partial Boolean algebra original pdf; Stone1937 Boolean rings topology regular open; Galois connection orthocomplemented lattice polarity Birkhoff1940; Quillen Higher K theory I1973 Theorem A',['partial_boolean','boolean','stone','orthogonality','quillen'],'Located primary Kochen–Specker, Birkhoff and Quillen material; exact locators in source_checks.md.','KochenSpecker1967;Birkhoff1948;Quillen1973')
s('S03','zbMATH Open/arXiv/MathOverflow/Numdam indexed searches','site:zbmath.org "Vers une géométrie des formes"; site:arxiv.org Grothendieck tronçons multistrates subdivision; site:mathoverflow.net Grothendieck figures topology; site:numdam.org Grothendieck topologie modérée',['custom','subdivision','betweenness'],'No exact general figure-axiom continuation identified. MO project-specific recent material used only as leads; Hua exact later results checked separately.','Malgoire2002;CSG2026;Hua2026','Indexed search coverage only; not exhaustive database corpus access.')
s('S04','web search','"Grothendieck" "tronçon" "topologie"; "partial Boolean algebra" "closure" "relativization"; "coarsest topology" "closed subset" "finer topology" extension; "Alexandrov" "preorder" "final topology" "initial"',['intervals','topology','partial_boolean','alexandrov','extension_topology'],'No exact full moderated-closure or closed-subspace-extension match. Standard partial Boolean and Alexandrov ingredients located.','KochenSpecker1967;Borges1967;WaasWoolfYokura2026')
s('S05','web search','"On stratifications and poset-stratified spaces" arxiv; "Quillen" "Higher algebraic K-theory I" pdf; "least topology" "closed subspace" extension finer; site:numdam.org Grothendieck EGA "locaux fermés"',['stratification','alexandrov','extension_topology','quillen'],'Opened exact modern stratification source and Quillen. No exact match for V least extension in retrieved topology-extension literature.','WaasWoolfYokura2026;Quillen1973;Borges1967')
s('S06','web and zbMATH indexed search','"Grothendieck" "tronçons" "topologie" "T0"; "Grothendieck" "multistrates" "admissible"; "Grothendieck" "algèbre des figures" "modérées"; site:zbmath.org "Diskrete Räume" Alexandroff',['custom','intervals','topology','subdivision','poset','alexandrov'],'No exact tronçon separation or full admissible-figure result found. Unrelated combinatorial/linguistic hits rejected.','Alexandroff1937')
s('S07','strong web search; EGA/SGA','"Grothendieck" "modérées" "algèbre de Boole"; "Grothendieck" "figures" "raffinement" "sous-figure"; site:numdam.org EGA I "localement fermé"; SGA4 IV "sober" "topological" Grothendieck',['custom','stratification','topology','subdivision'],'Found institutional2002 notice, EGAI metadata and modern SGA translations. No exact SA21 later publication; unreliable translated sobriety wording not imported.','Malgoire2002','EGA full web PDF exceeded size limit. Original SGA check delegated to parent; no original-passage claim made here.')
s('S08','web search','"moderated" "partial Boolean algebra" closure Grothendieck; "finite union" "intervals" "partial order" "complement"; "coarsest topology" "closed subspace" finer topology extension; "Grothendieck" "contrée" "ombre"',['custom','partial_boolean','intervals','extension_topology'],'No exact match. Partial-order interval generalizations and simple topology extensions are related but hypotheses differ.','Borges1967;Birkhoff1948')
s('S09','zbMATH/arXiv/MathOverflow; strong web search','site:zbmath.org "partial Boolean" closure; site:arxiv.org "Grothendieck" "subdivision" "figures"; site:mathoverflow.net "Grothendieck" "tronçons"; "Grothendieck" "Esquisse" "topologie modérée" pdf',['custom','partial_boolean','subdivision'],'Partial Boolean functions are a different topic; polynomial subdivision results rejected. Opened original Esquisse excerpt; MO historical leads remain project-dependent.','Esquisse1984;CruzMorales2021')
s('S10','web search','"Grothendieck" "two orders" subdivision figures; "Grothendieck" "multistrates" "ombre"; "orthogonality" "lower ideals" "ortholattice"; "preorder" "closed subset" "topology extension"',['custom','poset','subdivision','orthogonality','lattice','extension_topology'],'No exact two-order calculus or extension characterization found. Unrelated algebraic orders/utility extensions rejected.','Birkhoff1948;Borges1967')
s('COUR','Numdam/arXiv; backwards bibliography','Betweenness partially ordered reconstruction order reversal; Courcelle Betweenness partial orders; Altwegg1950 Zwischenbegriff geordneten Mengen; Bankston road systems betweenness',['betweenness','elementary'],'Courcelle primary finite/countable scope, Bankston distinction and backward author references checked; no exact cone-stable relational axiom system located.','Courcelle2020;Bankston2013','Altwegg/Lihová references remain leads, not cited theorems without opening.')
s('BK','primary book and bibliography','Birkhoff1948 chapters I.11, IV.5–6, IX.4–5, X.3, XI.3, XI.5; backward Stone references',['elementary','intervals','topology','boolean','poset','lattice','orthogonality','stone'],'Relevant primary passages read and exact scope recorded.','Birkhoff1948','Full book downloaded for targeted reading; no assertion of reading the entire book.')
s('ST','primary paper','Stong1966 pp325–327 Propositions1–6',['alexandrov','poset'],'Rendered primary pages and visually read minimal-neighborhood/order/component statements.','Stong1966','Finite-space scope preserved.')
s('KS','primary paper','Kochen–Specker partial Boolean algebra pp65–66',['partial_boolean','boolean'],'Rendered primary pages, checked definitions and compatible contexts.','KochenSpecker1967','No inference about moderated closure enrichment.')
s('WWY','arXiv primary article','Waas–Woolf–Yokura Proposition2.6; Proposition3.3; Corollary3.4; Proposition3.9',['alexandrov','stratification'],'Opened exact statements and their proofs/hypotheses.','WaasWoolfYokura2026','Related quotient theorem; no blanket resolution of manuscript.')
s('QUI','primary paper','Quillen Higher algebraic K-theory I Theorem A and dual form',['quillen'],'Opened exact theorem and compared poset comma categories.','Quillen1973','No automatic universal-base-change conclusion.')
s('BORG','primary paper','Borges On Extensions of Topologies1967 §§1–2, Lemma2.1',['extension_topology'],'Opened primary paper and rejected as exact match for the stronger prescribed-closed-subspace statement.','Borges1967','T1/simple-extension scope differs.')
s('ESQ','primary published excerpt','Esquisse d’un Programme end§5 and§6 pp32–35',['stratification','subdivision'],'Read exact predecessor passages; publication1997 versus composition1984 kept distinct.','Esquisse1984','Conceptual link, not classA later theorem.')
s('HUA','primary preprint and public code','hexagon2611.00125v2 §§78–79; repository Folder156_3.lean and Folder156_4.lean',['betweenness','orthogonality'],'Exact limited matches found and mathematically checked. Full relevant Lean source read; figure certificate independently executed.','Hua2026;HuaLean3;HuaLean4','No Lean execution; project-reading dependence; first-circulation day unverified.')
s('ZB-ACCESS','direct zbMATH','https://zbmath.org/?q=an%3A0018.09105',['alexandrov'],'Tool inaccessible; indexed database search and primary bibliographic metadata used.','Alexandroff1937','Access limitation recorded, not silently represented as successful database review.')
with (O/'search_log.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['search_id','date','source','queries_or_locators','claim_ids','result','opened_refs','limits']);w.writerows(S)
E=[]
targeted={3:[4,5,6,7,8,9,10,12,13,17,18,19,21,22,23,25,27],4:[1,2,3,4,6,11,12,20,27,29,30,31,32,33,39],5:[1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,21,22,23,24,25,27,28,29]}
refuted={3:[1,15,20,24,26],4:[26,28,34,39],5:[8,20,26]}
cert={3:[1,4,7,12,19,22,26,27],4:[26,28,34,35,39],5:[8,20,24,26]}
refinements={
 (3,1):('R-SA21-3-001','The bare compatibility data do not determine a cut from its compatible complement. No general positive repair is proved; the three-point obstruction does not refute later strengthened network axioms.'),
 (3,15):('R-SA21-3-015','The universal T0/sobriety answers and the implication from closed points to total order are false for the displayed abstract tronçon axioms. No necessary-and-sufficient replacement axiom is claimed.'),
 (3,20):('R-SA21-3-020','Only the abstract partial-Boolean generalization is refuted: an underlying meet can exist for incompatible elements. The question for a realized Mod(L) is not settled by this example.'),
 (3,24):('R-SA21-3-024','Only the abstract closure-algebra generalization is refuted: identity closure can make every element clopen without making all pairs compatible. No counterexample for a specified geometric realization or new sufficient hypothesis is claimed.'),
 (3,26):('C-SA21-3-027','The correct finite-generation statement uses nonempty membership-vector classes; a boundary subdivision may generate a strictly finer algebra.'),
 (4,26):('C-SA21-4-027','The checked repair uses completely join-prime generators, not ordinary complete join-irreducibility; the later VI strengthening is recorded separately.'),
 (4,28):('R-SA21-4-028','Under the already assumed least-containing-member condition, x↦A_x is injective exactly when the family separates points. Without separation it identifies precisely points with identical membership profiles.'),
 (4,34):('C-SA21-4-035','Complete orthocomplementation survives; distributivity fails in the fully checked figure countermodels. The countermodel statement itself is valid.'),
 (4,39):('R-SA21-4-039','C1–C4 with identity subdivisions do not force strict virtual-support separation. The author’s least-element example, independently checked on a two-element chain, is valid; no strengthened universal separation theorem is supplied.'),
 (5,8):('R-SA21-5-008','The universal connectedness claim and the transcribed union-product construction fail in the stated set-family model. No replacement construction or restriction restoring connectedness is proved here.'),
 (5,20):('R-SA21-5-020','Retention of outside closed strata alone does not imply unchanged outside residuals or a bijective outside target map. No new sufficient strengthening of condition d is claimed.'),
 (5,26):('C-SA21-5-027','The corrected least-extension characterization requires preservation of closures of every subset of the complement U, in addition to the prescribed topology on T.'),
}
# These records describe a valid counterexample or a limited-scope obstruction.
# Attach the refutation to the false embedded substatement, not to the valid record.
refute_subjects={
 (3,20):'C-SA21-3-020#abstract-generalization',
 (3,24):'C-SA21-3-024#abstract-closure-generalization',
 (4,39):'C-SA21-4-039#withdrawn-universal-separation',
 (5,26):'C-SA21-5-026#withdrawn-four-test-characterization',
}
for x in C:
 ch=int(x['cote'].split('-')[1]);n=int(x['id'].split('-')[-1])
 if n in targeted.get(ch,[]):typ='targeted proof check';out='Specific order/set argument checked; see proof_checks.md and claim present_status. Scope is the stated hypotheses, not all suggested generalizations.'
 else:typ='carried as background without fault found';out='Statement, provenance and page status fully read; this event alone is not a proof verification. Specific refutations/certificates are separate rows below.'
 if (ch,n)==(4,35):
  typ='independent re-proof';out='Valid current-run countermodel: the five-cycle and seven-element constructions and their figure axioms are checked in proof_checks.md. The manual identity-subdivision argument is separate from the executed finite certificate. C-SA21-4-034 is the conjecture refuted, not this countermodel statement.'
 if (ch,n)==(5,26):
  typ='independent re-proof';out='The author’s three-point counterexample to the four weak tests is valid and independently checked. The refuted embedded characterization is separately identified below; the counterexample itself is not refuted.'
 E.append([x['id'],date,who,typ,out])
 if n in refuted.get(ch,[]):
  refine,scope=refinements[(ch,n)]
  E.append([refute_subjects.get((ch,n),x['id']),date,who,'refuted, with the refined statement’s id',refine+'; '+scope+' Localized statement and scope: proof_checks.md, Named refinements and scoped obstructions.'])
 if n in cert.get(ch,[]):E.append([x['id'],date,who,'computation or formal certificate','Executed Python finite certificate in code/computations.py; outputs/computations.json. Symbolic explanations separately identified; no Lean compiler.'])
for (ch,n),(rid,statement) in refinements.items():
 if rid.startswith('R-SA21-'):
  E.append([rid,date,who,'used and rechecked in this run','Named scope/refinement of the existing check for '+f'C-SA21-{ch}-{n:03}'+': '+statement+' This records the already established result; no additional positive repair is inferred. See the exact identifier in proof_checks.md.'])
for key,scope in [('Birkhoff1948','Targeted primary passages BK-1..4 read and used; standard implications checked where explained.'),('Stong1966','Propositions1–6 pp325–327 visually read; finite scope preserved.'),('KochenSpecker1967','pp65–66 partial algebra definitions read and matched, not whole hidden-variable theorem reproved.'),('Courcelle2020','§2 cardinality restriction and Theorem3.5–3.6 statements checked; no claim to reprove entire paper.'),('Bankston2013','§3.1 relation distinction checked; road and strict betweenness not conflated.'),('Quillen1973','Theorem A statement and dual form checked against poset principal ideals; theorem carried as established background.'),('Borges1967','§§1–2 inspected; exact-match claim rejected.'),('WaasWoolfYokura2026','Proposition2.6 and§3 exact hypotheses checked.'),('Esquisse1984','Primary end§5 and§6 pp32–35 read as conceptual predecessor.'),('Hua2026','Only§§78–79 targeted mathematical comparison; current-run finite figure check extends the encoded hypothesis verification.'),('HuaLean3','Full raw source read; theorem statements compared; not compiled.'),('HuaLean4','Full raw source read; figure axioms C1–C3 absent from formal model; not compiled.')]:
 E.append([key,date,who,'used and rechecked in this run',scope])
for key in ['Alexandroff1937','Malgoire2002','CSG2026','CruzMorales2021']:
 E.append([key,date,who,'carried as background without fault found','Opened metadata/notice/abstract only; no mathematical theorem certified from unseen text.'])
with (O/'check_events.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(E)
(O/'outputs/logs_output.json').write_text(json.dumps({'search_groups':len(S),'check_events':len(E),'claim_count':len(C),'note':'Actions distinguished from source reading; negative search bounded.'},indent=2)+'\n')
print('Saved',len(S),'search records and',len(E),'check events.')
