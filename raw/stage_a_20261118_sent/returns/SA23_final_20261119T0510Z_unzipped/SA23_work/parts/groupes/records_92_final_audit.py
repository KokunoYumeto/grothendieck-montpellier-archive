"""Final manual occurrence audit and attachment of executed calculations."""

# Scans 63–65 were read in the first full pass and re-read in this audit.
# Their earlier formulations are occurrences of the later doctrine questions.
extra_occurrences={
 43:[occurrence(4,[63,64],'476–479;492–503','bounded construction proposed, with a universe-bound question')],
 44:[occurrence(4,[65],'512–538','change-of-doctrine comparison announced')],
 49:[occurrence(4,[63,64],'481–483;509','amalgamated 2-sums and generalized exactness queried')],
 50:[occurrence(4,[63,64],'470–472;492–509','equality is explicitly distinguished from invertibility')],
 51:[occurrence(4,[63,64],'466–485;490–503','necessary/sufficient, smallness and full-faithfulness steps explicitly conjectural')],
}
for p in problems:
    n=int(p['id'].rsplit('-',1)[1])
    p['occurrences'].extend(extra_occurrences.get(n,[]))
for c in claims:
    n=int(c['id'].rsplit('-',1)[1])
    extra={82:'476–479',88:'466–479',90:'470–472;483–485;492–509',91:'476–485;490–503',102:'512–538'}.get(n)
    if extra:
        c['lines'].append(f'{source_file(4)}:{extra}')
        c['scans']=sorted(set(c['scans']+[63,64] if n!=102 else c['scans']+[65]))
for i in items:
    if i['id']=='SA23-921':
        i['lines'].append(f'{source_file(4)}:462–538')
        i['scans']=sorted(set(i['scans']+[63,64,65]))

addclaim(114,921,4,[64],'506–509',
 'Paraphrase: characterize algebraic theories intrinsically; preservation of 2-limits is the only visible necessary condition and is probably insufficient.',
 'A representable pseudofunctor Hom_Delta(R,-) preserves existing weighted bilimits. A converse requires a specified doctrine and size/accessibility hypotheses; the page does not state a sufficient intrinsic criterion.',
 'open on the pages; the author explicitly doubts sufficiency',
 'The weighted-bilimit universal property, tested at R, is exactly the required preservation equivalence. For a sufficient comparison theorem in a specified setting, a pseudofunctor from a finitely bi-accessible 2-category with weighted bilimits to Cat, preserving weighted bilimits and bifiltered bicolimits, has a left biadjoint. Evaluating that biadjunction at the terminal category gives a representing object. This adds hypotheses that the manuscript has not established for its arbitrary Delta.',
 'Di Liberti–Osmond Theorem 5.2.3 (printed theorem number; online section 6.2) gives the exact conditional biadjoint result. It does not identify the page’s arbitrary large doctrine with that setting.',
 ['DiLibertiOsmond2025'],'C')
claims[-1].update(status_category='open on the pages',status_assignment='Manually assigned after reading the explicit doubt at physical line 507.',record_origin='source assertion',reconstruction_boundary='The necessary preservation property and the question are on the page. The sufficient accessible comparison theorem and its representing-object consequence are modern reconstruction with explicit hypotheses.')
addproblem(71,'An intrinsic criterion for represented algebraic theories',
 [occurrence(4,[64],'506–509','live question; proposed necessary condition explicitly doubted as sufficient')],
 'Can algebraic theories be characterized intrinsically, perhaps by commuting with 2-limits?',
 'Representability implies preservation of weighted bilimits. Under the precise bi-accessibility hypotheses of C114, bilimit and bifiltered-bicolimit preservation give a sufficient criterion.',
 'The source’s unrestricted converse remains unspecified. Di Liberti–Osmond 5.2.3 supplies a modern conditional comparison, not an identification of all its doctrines.',
 ['DiLibertiOsmond2025'],worth='Worth a bounded comparison in one chosen doctrine: verifying bi-accessibility and the required preservation hypotheses turns the broad question into an exact theorem test.')
addproblem(72,'Does basis generation survive amalgamated 2-sums?',
 [occurrence(4,[63],'481–485','explicit proof obligation'),occurrence(7,[101,102],'263–307','repeated fixed-basis amalgamation and representation questions')],
 'If each I→R_lambda generates in the chosen doctrine, must the amalgamated 2-sum under I also be generated, and does the indicated small J detect transformations fully faithfully?',
 'For a fixed small bounded doctrine, one can formulate the amalgamated envelope and test its generation through the actual free-construction stages. The unrestricted large-doctrine formulation needs a stopping bound and the correct meaning of generation.',
 'C090 records the fixed-basis 2-pullback/amalgamation universal property; C091 and C101 separate generation from mere detection of transformations. Kelly’s bounded envelope theorem and the checked finitary doctrine results supply exact restricted settings, not the page’s missing general proof.',
 ['Kelly1982','DiLibertiOsmond2025'],worth='Worth a single bounded worked construction after fixing the doctrine and morphisms; the false faithful-basis implication prevents treating the general question as already settled.')

search('Bi-accessible bipresentable 2-categories biadjoint functor theorem weighted bilimits solution set; intrinsic representation of category-valued theories',[114],
 [dict(url='https://link.springer.com/article/10.1007/s10485-024-09794-9',locators='Theorem 5.2.3 and proof; online section 6.2, lines 1453–1466',match='Exact sufficient theorem includes preservation of bifiltered bicolimits and finitely bi-accessible domain/codomain with weighted bilimits; necessity follows directly from the bilimit universal property.')],
 limits='The page’s arbitrary Delta is not proved to satisfy these hypotheses. The source has inconsistent online section numbering, so the printed theorem number is retained. No unconditional converse is claimed.')
checked_ref('DiLibertiOsmond2025','Read Theorem 5.2.3 and its proof; retain both weighted-bilimit and bifiltered-bicolimit preservation, plus finite bi-accessibility. Apply its left biadjoint at 1 only under those hypotheses.','targeted proof check')
checked_ref('StacksLocalization','Read the complete proof of Lemma 4.27.9, tag 05Q2, and its right-fraction dual Lemma 4.27.17. The Hom formula uses filtered colimits commuting with finite limits; it does not establish arbitrary-product preservation.','targeted proof check')
checked_ref('Liu2013','Read Theorem 2.2.1 and its proof on printed p. 666, together with the base hypotheses on p. 661. Crystalline weights {0,1}, not merely Hodge–Tate or arbitrary filtered F-crystals, occur in the theorem.','targeted proof check')

# The explicit source sign notation must not be silently interpreted as +/-1.
readings.append(['161-1','13','420–437','epsilon(L) to sign(sigma); L tensor 2','epsilon(L) to permutation parity 0 or 1; L tensor n','An exponent +1 or -1 gives the same scalar when epsilon squared is 1 and cannot distinguish odd and even permutations. The adjacent-transposition calculation fixes the mathematical convention, but only ink can settle the written symbol.','high','high'])
readings.append(['161-2','63–64','476–507','necessary (?) / probably sufficient / intrinsic 2-limit criterion','retain distinct conjectural stages','The same passage asks operation generation, size of a transfinite presentation, full faithfulness on J, and an intrinsic criterion. These are separate obligations, not a single proved representation theorem.','high','high'])

calc=json.loads((BASE/'computations/check_groupes.output.json').read_text())
by_claim={}
for result in calc:
    for cid in result['claims']:by_claim.setdefault(cid,[]).append(result['check'])
for c in claims:
    c['computation']['proof_certificate']='SA23_work/parts/groupes/computations/proof_certificates.md#'+c['id'].lower()
    if c['id'] in by_claim:
        c['computation']['code']='SA23_work/parts/groupes/computations/check_groupes.py'
        c['computation']['output']='SA23_work/parts/groupes/computations/check_groupes.output.json'
        c['computation']['checks']=by_claim[c['id']]
        c['computation']['limit']='Executed exact finite or symbolic checks verify the named examples and identities only. The unrestricted claim depends on the separately recorded analytic proof and its hypotheses.'
        events.append([c['id'],DATE,WHO,'recomputed with code','All assertions passed in check_groupes.py; output sections: '+', '.join(by_claim[c['id']])+'. General validity is not inferred from finite samples.'])

# Item-level check events summarize actual mathematical work, not source reading.
for i in items:
    cs=[c for c in claims if i['id'] in c['items']]
    events.append([i['id'],DATE,WHO,'manual consolidation with linked proof checks','Linked claims: '+', '.join(c['id'] for c in cs)+'. Their individual records give the proof/counterexample, exact-source match and unresolved hypotheses; this row is not an additional independent proof.'])

# Correct a preliminary arithmetic slip in the internal reading ledger.
ledger=BASE/'analysis_1612_07.md'
txt=ledger.read_text().replace('the product closure of 2 has cardinalities 2^n and misses 3','the product closure of 2 has even cardinalities 2m (including 0) and misses 1 and 3')
ledger.write_text(txt)
