"""Merge current research contributions without erasing unresolved parent tasks."""
from pathlib import Path
import csv, datetime, json
root=Path(__file__).resolve().parents[1]
fields=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
rows=list(csv.DictReader((root/'RESEARCH_SA14_SA19_results.csv').open()))
rows=[r for r in rows if r['id'] not in ['A2V-cross','A2W-cross','A2Y-cross','A2Z-cross']]
by={r['id']:r for r in rows}
def put(r):
    if r['id'] in by: by[r['id']].update(r)
    else: rows.append(r);by[r['id']]=r
for owner in ['bce','dgj','fhi']:
    for r in csv.DictReader((root/'work'/owner/'results.csv').open()):
        if owner=='bce':
            ident=r['id'];ident=('SA14-'+ident) if ident.startswith('H') else ident
            part=ident[:1] if ident[:1] in 'BCE' else None
            where='work/bce/section_'+part+'.tex' if part else 'work/bce/additional_leads.tex'
            if r['source']:where+='; '+r['source']
            r=dict(id=ident,statement=r['statement'],status=r['status'],where_proved=where,depends_on='',manuscript_pages_settled=r['cote_scan'],notes=r['proved_result_or_precise_gate'])
        else:
            if not r['where_proved'].startswith(('work/','sections/')):
                r['where_proved']='work/'+owner+'/'+r['where_proved']
            if r['id'] in ['A2V-cross','A2W-cross','A2Y-cross','A2Z-cross']:r['id']=r['id'].removesuffix('-cross')
        put(r)
mapping={'D1-positive':'D1','D1-negative':'D1','D1-family':'D1','D2-flatness':'D2','D2-specialization':'D3','D2-Igusa':'D4-versal','G2':'G2b','G3-Albanese':'G3','G3-principal':'G3','H-Ga':'H2','H-all':'H1','I-2d':'I2','F':'F-full','I-all':'I-full','J2-isomorphism':'J2a','J2-positivity':'J2b','SA14-H9':'E2','SA14-H6':'SA14-H6','SA14-H10':'SA14-H10-main','SA14-H11':'SA14-H11-affinity-general','E4-311Igusa':'D4-versal'}
for dest,src in mapping.items():
    if dest in by and src in by and dest!=src:
        original=by[dest]['statement'];r=by[src].copy();r.update(id=dest,statement=original);put(r)
for ident,status,note in [
 ('B2','Refuted as a fibre-type-only criterion; fixed-family iff proved','Identical regular base and abstract geometric fibre types give opposite extension properties; no criterion from those data alone exists. The exact deformation-sensitive Cl/Pic kernel criterion is proved for regular base and normal integral geometric fibres. R2 is not necessary and requires the original lci hypothesis for sufficiency.'),
 ('E4','Undecided','E4.T proves Pic-tau closedness without projectivity for proper flat finitely presented geometrically integral families over arbitrary scheme bases. E4.S settles the fibrewise smoothness/defect claims; E4.Curve proves full Pic schematicity for smooth proper geometrically connected curves. Remaining mathematical gate: full Pic schematicity for geometrically integral nonnormal families and normal higher-dimensional families over arbitrary bases. The scan310 finite-component iff retains an explicitly recorded reading/scope uncertainty; multiplication nonopenness is already refuted by E4.H.'),
 ('K','Current register complete; final audit pending','Every current A-J and lead row is numbered with status and proof location. Final completeness requires resolution or the user-defined stopping review for every remaining research gate.'),
 ('E4-311canonicalArtin','Refuted by an explicit dual-number Igusa deformation','D4a gives k=Fbar2, R=k[epsilon]/epsilon^2 and ordinary Serre-Tate parameters q12=1+epsilon, all other qij=1. A compatible abelian Picard-variety subgroup would force 1=q12 by Katz morphism lifting. Pic-tau remains flat. Root, BCE and FHI targeted audits passed; the uncertain manuscript notation is retained.'),
 ('E4-311canonicalReduced','Refuted','Part D3 cyclic shear gives an explicit reduced trait base with no embedded abelian subgroup having the fibrewise Picard varieties; kernel lengths of (F^2,2) change from 2 to 4.'),
 ('E4-311NS','Refuted','Part D4 product Igusa family has ordinary generic NS torsion Z/2 and supersingular special NS torsion zero; the component-group assertion is false.'),
 ('C2','Proved','Full excellent henselian comparison proved by principal finite determination, blow-up and Stein factorization, conductor descent, and approximation; independent proof audit passed.'),
 ('C4','Proved in original cone scope; arbitrary-local extrapolation refuted','The source fixes the local cone at its vertex and then compares punctured Picard groups. That statement is proved modulo bounded p-groups. A characteristic-three factorial local hypersurface with henselian/completed punctured Pic Z refutes the arbitrary-local extrapolation; different intrinsic etale-local NS definitions are stated separately.'),
 ('E1','Refuted as stated; intended valuative version proved','A normal total-space elliptic degeneration refutes the literal assertion. The version with geometrically normal fibres is proved over a trait. Arbitrary-base representability questions are distinct E4 rows.'),
 ('SA14-H1','Proved','For normal projective X the geometric-generic Pic-tau restriction kernel is finite connected unipotent; its tangent space is H1(L^-1). A3 gives an explicit nonzero example in dimension two.'),
 ('SA14-H3','Refuted as recalled; target undecided','Bhatt-de Jong local theorem is injectivity up to p-power torsion, not the recalled isomorphism; no global solution follows.'),
 ('SA14-H4','Undecided','This lead is the boxed injectivity assertion A2, not A3. The surviving p-torsion kernel in dimensions three and four is still unresolved.'),
 ('SA19-H3','Undecided','All dimensions are proved for separated complete graded algebras with a basis of open left ideals; all surfaces are proved for arbitrary jointly continuous topology. The original scan43:66 was visually checked: it specifies separated complete graded topological algebras, without an open-left-ideal hypothesis. The remaining gate is the full universal property in that broader category in dimensions at least three.'),
 ('SA19-H4','Refuted','The actual ordinary local Jacobian of k[s,t]_(s,t) has an explicit nonsplit Z/p extension and is not projective; higher Ext vanishing for the curve pro-Jacobian is separately proved in Serre category and on the perfect etale site.')]:
    if ident in by:by[ident].update(status=status,notes=note)
for ident,statement,where,pages in [
 ('SA14-H1','Generic Pic-tau restriction kernel and existence of its nonzero infinitesimal part','sections/A.tex, a:generic-unipotent and a:very-ample-example','57:99-100'),
 ('SA14-H3','Universal surjectivity without cohomological vanishing and recalled local analogue','sections/A.tex, A1r and tested approaches','57:97'),
 ('SA14-H4','Boxed universal injectivity in dimension at least four','sections/A.tex, A2b and A4b','57:97')]:
 if ident in by:by[ident].update(statement=statement,where_proved=where,manuscript_pages_settled=pages)
for ident,statement,where,note in [
 ('R3g','The generic smooth hyperplane restriction kernel is finite connected','sections/A.tex, a:generic','Proof uses Kummer Lefschetz, the p-torsion dlog injection, and the incidence variety; targeted independent check by fhi.'),
 ('R3u','The generic hyperplane restriction kernel is infinitesimal unipotent for normal projective X','sections/A.tex, a:generic-unipotent','Rational dlog handles normal X; Raynaud Proposition6.2.3 excludes mu_p; Cartier duality proves unipotence. Root independently checked the source and proof.'),
 ('A3','There exists a smooth projective surface with a very ample L and nonzero H1(L^-1); the least requested dimension is two','sections/A.tex, a:very-ample-example','Explicit characteristic-two Raynaud surface followed by 556 simultaneous ninth-root covers; h0(L)=562 and h1(L^-1)=1. Complete GF(2) basis and finite transition certificate included; three targeted independent audits passed.'),
 ('A3R','Every positive two-parameter Raynaud polarization with negative H1 fails very ampleness','sections/A.tex, a:raynaud-all','Connection lemma gives vanishing for a>=ell; fibre semigroup excludes a<ell. This family exclusion is compatible with the separate A3 cover construction.'),
 ('A3f','Direct Raynaud fibre polarizations in the stated degree range are not very ample','sections/A.tex, a:fibre','Semigroup pole orders force the fibre map to factor through Frobenius; finite check covers 518 pairs, while the proof treats all coprime pairs.'),
 ('A3n','A very ample negative-H1 example requires q_nil>=h0(L)>=5 on a surface','sections/A.tex, a:nilpotence','Opened Enokizono Th4.20 with E=0; low projective embeddings have H1(O)=0.'),
 ('A3s','An A3 surface is of general type, satisfies explicit numerical bounds, and has no smooth W2 lifting','sections/A.tex, a:generaltype','Opened Terakawa Th1.6, corrected Zhang Th3.1, and Langer Cor11.2; very ampleness forces degree at least3 on a genus-one fibre.')]:
    put(dict(id=ident,statement=statement,status='Proved',where_proved=where,depends_on='Part A proof and cited primary sources',manuscript_pages_settled='57:99-100',notes=note))
put(dict(id='A2D',statement='For fixed nontrivial p-torsion M and very ample L, smooth hyperplanes trivializing M form a finite determinantal locus, and a nonempty locus requires h1(M)-h1(M(-L))>=h0(L)-2',status='Proved',where_proved='sections/A.tex, a:determinantal; work/root/A2_determinantal.tex',depends_on='dlog injection in R3g; A2 finite p-group reduction for final corollary',manuscript_pages_settled='57:97',notes='Complete conormal and maximal-minor proof; BCE independent targeted audit passed. Gives a finite fixed-pair test, not a universal exclusion or a counterexample.'))
put(dict(id='A2V',statement='A Cartier-fixed regular one-form vanishing along a smooth ample divisor has order pa and a nonzero exact tangential leading term, yielding a Frobenius kernel on H1(Y,O_Y(-aY))',status='Proved necessary condition',where_proved='sections/A.tex; work/dgj/A2_cartier_leading.tex',depends_on='conormal sequence; Cartier exact sequences; dlog injection; A2 finite p-group reduction only in dimension at least three',manuscript_pages_settled='57:97',notes='Also forces h0(Omega_X)>=h0(O_X(pY)) and a nonnormal associated mu_p torsor. The affine model dlog(1+t^p x) disproves naive p-squared order iteration. Root independent audit and finite coefficient checks passed. Full A2 global extension/exclusion remains unresolved.'))
put(dict(id='A1Q',statement='Picard restriction for quasi-F-split smooth ample targets, and for every smooth Fano threefold target',status='Known; derivation proved',where_proved='sections/A.tex, a:known-targets; work/root/A1_known_targets.tex',depends_on='Petrov2025 Cor4.10; Kawakami-Tanaka PartI Th6.3 and PartII Th7.2; Serre duality; A4c',manuscript_pages_settled='57:97',notes='Quasi-F-split targets give injectivity for ambient dimension at least3 and isomorphism for dimension at least4. A smooth Fano threefold target gives an isomorphism in every p, including2. Exact target hypotheses and duality indices independently audited by DGJ; no unrestricted A1 or A2 conclusion.'))
put(dict(id='A2P',statement='A smooth ample relative Frobenius p-multisection of a projective-line bundle cannot kill p-torsion from its base',status='Proved construction exclusion',where_proved='sections/A.tex; work/root/A2_multisection_exclusion.tex',depends_on='projective-bundle canonical formula; divisor adjunction; A2Z conductor duality',manuscript_pages_settled='57:97',notes='For a quotient F*E to N the normal line is Q^p and the relative canonical line Q^(p-1). Normalization of a mu-p torsor would make the latter anti-effective, contradicting ample normal bundle. Positive-dimensional smooth projective base, quotient convention and full relative-Frobenius inverse section explicit. DGJ independent equation/conductor audit passed. Does not settle A2.'))
for ident,where in [('B2','sections/B.tex, B2 exact obstruction and paired projective families'),('C2','sections/C.tex, Theorem C2.G'),('C4','sections/C.tex, cone comparison and general-local counterexample'),('E1','sections/E.tex, E1 literal counterexample and intended valuative theorem'),('E4','sections/E.tex, individual questions 57:308-315'),('K','sections/K.tex, complete current numbered register')]:
    if ident in by: by[ident]['where_proved']=where
for ident in ['F','F-full']:
    if ident in by: by[ident]['notes']='For complete normal local surfaces with algebraically closed residue field, the unrestricted conjecture remains. In equal characteristic F8/F9b settle every geometric quotient with normal pro-p kernel over the full tame quotient. F10 proves finite abelian inertia using Krishna–Majumder2026v2; F10c gives all-prime rank-linear H1 bounds for abelian monodromy, and F11 proves uniform finite generation of metabelian quotients. F12 gives the characteristic-p bound for metabelian coefficients; F12b settles pro-p closed second derived subgroup. F13 proves a fixed log-conductor bound after one fixed cover. F13c/d remove unramified character order and reduce the remaining coefficient-prime-not-p estimate to a degree-linear tame-generator bound for cyclic covers of uniformly bounded p-power degree (F13.6). F13e bounds refined-Swan zero length, but not cleanup complexity. F13.5/F13.6, further solvable and nonsolvable wild quotients, and mixed characteristic remain unresolved. The actual wild kernel is not assumed pro-p.'
for ident in ['A2','SA14-H4']:
    if ident in by: by[ident]['notes']='Universal point injectivity and its least dimension remain undecided. The kernel in dimension at least three is a finite p-group; for each nonzero order-p class its bad smooth hyperplanes form the finite determinantal locus A2D. A2V forces a Cartier-exact leading term and Frobenius kernel on negative H1 of the hyperplane, with vanishing order divisible by p and a nonnormal mu_p torsor. A2W forces rank(d:H0Omega1->H0Omega2)>=n-1. A2Y additionally requires noninjective Frobenius on H1(O_Y) and no smooth W2 lifting of Y. In dimension3 the target is of general type by applying A3s to L^a. No global realization or universal exclusion of this remaining gate is proved.'
for ident in ['I-full','I-all','SA19-H3']:
    if ident in by: by[ident]['notes']='All dimensions are proved for separated complete graded algebras with a basis of open left ideals; all surfaces are proved for arbitrary jointly continuous topology. The original43:66 specifies the broader category without the open-left-ideal hypothesis. I7b now proves open dense differential-image quotients for whole source columns over arbitrary regular local rings. Remaining: construction and continuity of the entire adjacent-arrow family and its endpoint assembly in arbitrary complete targets, in dimension at least3.'
with (root/'RESEARCH_SA14_SA19_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
events=list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
seen={tuple(r.items()) for r in events}
for owner in ['bce','dgj','fhi']:
    for r in csv.DictReader((root/'work'/owner/'CHECK_EVENTS.tsv').open(),delimiter='\t'):
        if owner=='bce' and r['statement_id'].startswith('H'):r['statement_id']='SA14-'+r['statement_id']
        if r['type']=='proved or rechecked in this run':r['type']='used and rechecked in this run'
        key=tuple(r.items())
        if key not in seen:events.append(r);seen.add(key)
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
out=['INCOMPLETE','','| Item | Status | Statement / current gate |','|---|---|---|']
for r in rows:out.append('| '+r['id']+' | '+r['status']+' | '+(r['where_proved']+'; '+r['notes']).replace('|','\\|')+' |')
out += ['', '## Authorship and verification','', 'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). The model effort setting is inherited and not exposed. We claim no priority. We read the supplied diplomatic transcriptions. No manuscript images were attached; selected original scans 57:309–315 and 43:64–66 were subsequently retrieved from the official Montpellier PDFs and visually inspected, with remaining handwriting uncertainties retained. Check events record the actual level of verification. Each outcome is scoped to the exact formulation proved or refuted. Distinct stronger variants retain separate unresolved rows.', '', '## Sources, calculations, corrections and remaining gates','', 'The detailed contribution reports below are retained in full; cited sources are marked opened or not opened in the bibliography. The source-download manifests and finite computations are included with their code and outputs. No finite calculation is represented as proof of a universal assertion.']
for owner in ['bce','dgj','fhi']:
    p=root/'work'/owner/'report.md'
    if p.exists():out+=['', '### Contribution '+owner,'',p.read_text()]
for note in ['A_research_06_to_07.md','A_research_07_to_08.md']:
    p=root/'work'/'root'/note
    if p.exists():out+=['','### Main-question attempts and exact source scopes','',p.read_text()]
p=root/'work'/'bce'/'A2_group_purity_counterexample.md'
if p.exists():out+=['','### Rejected purity shortcut','',p.read_text()]
out+=['','## Main Part A audit','','A3 is proved affirmatively: the fully specified characteristic-two surface in Theorem a:very-ample-example has a very ample bundle L with h1(L^-1)=1, h0(L)=562, and h1(O)=565. Dimension two is the least dimension in the requested range. The construction first gives an ample globally generated Raynaud polarization Q, then takes 556 simultaneous ninth roots of a generic basis of H0(Q^9). The complete basis over GF(2), transition equations, exact ranks, run time and outputs are in code/certify_A3.py, code/A3_Q9_basis.json and code/certify_A3_output.json. Smoothness and very ampleness have full proofs and three independent targeted AI checks.','','A1 reduces to dimension four and remains unresolved. A2, including its least universal injectivity dimension, remains unresolved. SA14-H1 is the generic infinitesimal unipotent-kernel statement and is proved, including the normal case and nonzero example. SA14-H4 is the boxed A2 injectivity claim; earlier checkpoint mappings of these two lead labels are corrected here. A nonzero infinitesimal kernel is not a counterexample on geometric points.','','The Bhatt–de Jong local theorem gives injectivity up to p-power torsion. Lauritzen–Rao gives very ample nonvanishing in degree 3r−4, not degree one. Direct positive two-parameter Raynaud polarizations are excluded by A3R, but the simultaneous-root cover lies outside that family. The homogeneous and Cech searches retain their exact scopes; unsaturated graded dimensions are not equated with sheaf cohomology. Historical undecided A3 notes are superseded by the complete construction.','','## Typesetting','','The integrated LuaLaTeX build diagnostics are in code/paper_build_diagnostics.json. The first checkpoint recorded the failed dependency setup. The private build environment has since been repaired. Each delivered PDF is subject to the 2pt overflow limit and sampled visual inspection, recorded below.']
for qa in sorted((root/'code').glob('visual_qa_*.json')):
    out+=['', '### '+qa.name, '', '```json', qa.read_text().strip(), '```']
out+=['','## Superseded and excluded material','','The initial section stubs are superseded by the integrated sections. Agent work files remain as the contribution audit trail. Externally downloaded primary-source PDFs and rendered QA images are excluded from checkpoints; locators and retrieval logs are retained. No original manuscript statement is silently corrected.']
(root/'RESEARCH_SA14_SA19_report.md').write_text('\n'.join(out)+'\n')
ledger=root/'PROGRESS_LEDGER.md'
with ledger.open('a') as f:
    f.write('\n## Working snapshot '+now+'\n\nThis is a checkpoint update, not the three-hour formal progress review.\n\n| Open row | Status | Current gate |\n|---|---|---|\n')
    for r in rows:
        if any(s in r['status'].lower() for s in ['undec','unsettled','unresolved','pending','progress','scope-dependent','delegated']):
            f.write('| '+r['id']+' | '+r['status']+' | '+r['notes'].replace('|','\\|')+' |\n')
print(json.dumps(dict(time_utc=now,results=len(rows),events=len(events)),indent=2))
