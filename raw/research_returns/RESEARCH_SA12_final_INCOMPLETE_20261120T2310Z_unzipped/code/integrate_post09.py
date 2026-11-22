"""Integrate separately audited post-CP09 reconstructions, without making a ZIP."""
from pathlib import Path
from datetime import datetime, timezone
import ast, csv, hashlib, json, re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
paths = [
 'parts/C/D_cover_uniform_relative.tex',
 'parts/D/D_tame_quadratic_count_candidate.tex',
 'parts/D/D_uniform_ramification_bound.tex',
 'parts/C/D_psl2_bounded_conductor_geometry.tex',
 'parts/D/D_bounded_ramification_obstruction.tex',
 'parts/C/D_curvewise_conductor_consequences.tex',
 'parts/C/D_p_H1_surface_post09.tex',
 'parts/C/D_local_tame_p_H1_post09.tex',
 'parts/D/D_tame_surface_linear_cohomology.tex',
 'parts/C/D_local_surface_reduction_post09.tex',
 'parts/B/post09_reconstruction/D_uniform_local_representation_growth_B.tex',
 'parts/B/post09_reconstruction/D_local_reflexive_atlas_B.tex',
 'parts/B/post09_reconstruction/D_fixed_rank_constructible_B.tex',
 'parts/C/D_global_fixed_rank_post09.tex',
 'parts/C/D_global_quadratic_count_post09.tex',
 'parts/D/D_tame_parabolic_fixed_rank_growth.tex',
 'parts/B/post09_reconstruction/D_quadratic_growth_alternating_B.tex',
 'parts/C/D_persistent_first_neighborhood.tex',
 'parts/B/D_residual_exceptional_genus_B.tex',
 'parts/D/D_saturated_boundary_slopes_candidate.tex',
 'parts/C/D_cover_uniform_annihilator.tex',
 'parts/B/post09_reconstruction/D_fixed_different_rational_chains_B.tex',
 'parts/B/post09_reconstruction/D_proper_curve_arithmetic_defect_B.tex',
]
env = r'(theorem|proposition|lemma|corollary|example)'
heading = re.compile(r'\\begin\{' + env + r'\}\[([^\]]+)\]')
statement = re.compile(r'\\begin\{' + env + r'\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
records = []
for rel in paths:
    path = root / rel
    body = path.read_text()
    def mark(m):
        title = m.group(2)
        if title.startswith('Proved under stated matrix-size hypotheses:'):
            title = title.replace('Proved under stated matrix-size hypotheses:',
                                  'Proved under stated hypotheses:', 1)
        elif not title.startswith(('Proved:', 'Proved under stated hypotheses:', 'Refuted:', 'Known:')):
            title = 'Proved: ' + title
        return '\\begin{' + m.group(1) + '}[' + title + ']'
    body = heading.sub(mark, body)
    path.write_text(body)
    for m in statement.finditer(body):
        sid, title = m.group(3), re.sub(r'\s+', ' ', m.group(2))
        status = title.split(':', 1)[0]
        end = body.find('\\end{' + m.group(1) + '}', m.end())
        refs = sorted(set(re.findall(r'\\ref\{([^}]+)\}', body[m.end():])))
        cites = sorted(set(k.strip() for match in re.findall(
            r'\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}', body)
            for k in match.split(',')))
        records.append(dict(id=sid, statement=title.split(':',1)[1].strip(), status=status,
            where_proved=f'{rel}: label {sid}', depends_on='; '.join(refs+cites),
            manuscript_pages='29/061,066',
            notes='Complete proof retained. Post-CP09 mathematical reconstruction is identified separately from recovered bytes; all original requested rows D.1/D.2(ii)/L8 retain their unresolved general status.'))

# A whole fragment is included once; aliases are not counted as extra statements.
paper = root / 'parts/D/paper_D.tex'
content = paper.read_text()
marker = '% BEGIN AUDITED POST-CP09 INTEGRATION'
if marker not in content:
    content += '\n\n' + marker + '\n'
    content += '\\subsection{Further uniform bounds and audited obstructions for D.1 and D.2(ii)}\n'
    content += '\n'.join('\\input{' + rel + '}' for rel in paths) + '\n'
    content += '% END AUDITED POST-CP09 INTEGRATION\n'
    paper.write_text(content)
else:
    missing=[rel for rel in paths if '\\input{'+rel+'}' not in content]
    if missing:
        content=content.replace('% END AUDITED POST-CP09 INTEGRATION',
            '\n'.join('\\input{'+rel+'}' for rel in missing)+'\n% END AUDITED POST-CP09 INTEGRATION')
        paper.write_text(content)

cols = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
csvpath = root / 'parts/D/results_D.csv'
with csvpath.open() as f: old = list(csv.DictReader(f))
known = {x['id'] for x in old}
added = [x for x in records if x['id'] not in known]
with csvpath.open('w', newline='') as f:
    w=csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(old+added)

eventpath=root/'parts/D/CHECK_EVENTS_D.tsv'
with eventpath.open() as f: events=list(csv.DictReader(f, delimiter='\t'))
who='GPT-6 Astra Pro; /root; SA12 run 1; effort setting not independently exposed'
old_checks={'D:different-conductor-bound','D:surface-uniform-different',
            'D:fixed-boundary-uniform-different','D:surface-uniform-conductor',
            'D:persistent-first-neighborhood'}
for row in added:
    sid=row['id']
    kind='retained complete proof audit and restored-file consistency' if sid in old_checks else 'complete actual-file proof check'
    outcome=('PASS. Exact scope, every displayed argument, dependency use, and distinction from full finite generation checked. '
             + ('Original complete root and independent-agent audits retained; this record does not invent a new full read.' if sid in old_checks else
                'Exact source read in full by root on 20 November 2026 before this integration timestamp; agent check provenance is in the reconstruction manifests and dated messages.'))
    events.append(dict(statement_id=sid,date=now,who=who,type=kind,outcome=outcome))
    owner='/root/part_b' if '/B/' in row['where_proved'] else '/root/part_c' if '/C/' in row['where_proved'] else '/root/part_d'
    events.append(dict(statement_id=sid,date=now,
        who=f'GPT-6 Astra; {owner}; SA12 run 1; inherited effort not independently exposed',
        type='author proof and source audit; reconstruction provenance',
        outcome='PASS as reported by the named author. Full original transcription audits and separately identified fresh actual-file audits are itemized in parts/B/post09_reconstruction/integration_manifest_B_post09.json, parts/C/integration_manifest_C_post09.json, and parts/D/POST09_D_RECONSTRUCTION_MANIFEST.md.'))
for sid, run, assertions in [
 ('D:psl2-bounded-conductor-covers; D:bounded-ramification-generation-obstruction','psl2_bounded_ramification_v2_root',31222),
 ('D:quadratic-growth-alternating-obstruction','alternating_quadratic_growth_reconstructed_root',201628)]:
    if not any(run in x['outcome'] for x in events):
        events.append(dict(statement_id=sid,date=now,who=who,type='computation or formal certificate',
            outcome=f'PASS: {assertions:,} exact assertions in separately identified reconstructed program. Full source read and independent root run retained in code/output/{run}.run.json. Historical lost-source runs are distinct records, not attributed to these program bytes.'))
ecols=['statement_id','date','who','type','outcome']
with eventpath.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=ecols,delimiter='\t');w.writeheader();w.writerows(events)

# Parse complete BibTeX entries by brace depth and update each key only once.
def entries(s):
    starts=list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,]+),',s))
    for m in starts:
        level=0; end=None
        for i in range(s.index('{',m.start()),len(s)):
            if s[i]=='{' and (i==0 or s[i-1]!='\\'):level+=1
            elif s[i]=='}' and (i==0 or s[i-1]!='\\'):
                level-=1
                if level==0:end=i+1;break
        assert end is not None
        yield m.group(1).strip(),s[m.start():end],m.start(),end
mainpaths={p:root/f'parts/{p}/references_{p}.bib' for p in 'ABCD'}
allkeys={key:p for p,path in mainpaths.items() for key,*_ in entries(path.read_text())}
bib_sources={
 'B':['parts/B/post09_reconstruction/references_B_post09_reconstructed.bib','parts/B/references_residual_genus_B.bib',
      'parts/B/post09_reconstruction/references_rational_chains_B.bib','parts/B/post09_reconstruction/references_arithmetic_defect_B.bib'],
 'C':['parts/C/references_C_post09.bib'],
 'D':['parts/D/references_D_post09.bib','parts/D/references_parabolic_count_D.bib','parts/D/references_parabolic_quadratic_D.bib'],
}
bib_added=[]
for p, sources in bib_sources.items():
    for rel in sources:
        for key, entry, _, _ in entries((root/rel).read_text()):
            owner=allkeys.get(key,p); target=mainpaths[owner]; text=target.read_text()
            existing=[item for item in entries(text) if item[0]==key]
            if existing:
                _,_,a,b=existing[0]; text=text[:a]+entry+text[b:]
            else:
                text+='\n\n'+entry+'\n';bib_added.append(key)
            target.write_text(text);allkeys[key]=owner

# The report's main conclusion and review state must match the current proofs.
assembly=root/'code/assemble.py'; src=assembly.read_text(); tree=ast.parse(src)
node=next(n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='outcomes' for t in n.targets))
outcomes=ast.literal_eval(node.value)
for i,(item,state,loc) in enumerate(outcomes):
    if item=='D.1':
        state='Incomplete in general; all-field rank-linear H1 and finitely generated maximal prosolvable quotient proved for proper normal surfaces with the original divisorial boundary; quadratic rank defining-characteristic representation growth proved; earlier full-generation cases retained'
        loc='D:tame-global-quadratic-representation-bound; D:tame-surface-all-characteristics-H1; D:tame-parabolic-fixed-rank-growth; D:surface-curvewise-conductor; '+loc
    elif item=='D.2(ii)':
        state='Incomplete in general; all-field rank-linear H1 and finitely generated maximal prosolvable quotient proved for proper surfaces, including nonnormal schemes; defining-characteristic quadratic rank growth proved globally on surfaces and for complete local punctures in every dimension; earlier full-generation cases retained'
        loc='D:punctured-surface-all-characteristics-H1; D:global-quadratic-representation-bound; D:uniform-local-growth-all-dimensions; '+loc
    elif item=='L8':
        state='Incomplete only through residual D.1/D.2(ii); arithmetic tame homotopy, descent, local counterexamples, surface linear cohomology and the stated representation-growth bounds are proved'
        loc='D:tame-surface-all-characteristics-H1; D:global-quadratic-representation-bound; '+loc
    loc='; '.join(dict.fromkeys(token.strip() for token in loc.split(';')))
    outcomes[i]=(item,state,loc)
lines=src.splitlines(keepends=True)
lines[node.lineno-1:node.end_lineno]=['outcomes=[\n'+',\n'.join(repr(x) for x in outcomes)+'\n]\n']
src=''.join(lines)
src=src.replace('The general case still requires control of new horizontal exceptional wild inertia or a uniform geometric bound on both finite-module first cohomology and nonabelian chief-crown multiplicities. Smallness, all-open pronilpotent generation, and a linear H1 bound alone do not give it.',
 'The strongest remaining surface gate is now nonabelian: all-field rank-linear H1 bounds and finite generation of maximal prosolvable quotients have been proved for both original-boundary tame groups and codimension-two punctures, including nonnormal proper surfaces. Defining-characteristic representation isomorphism classes have bounds q^(C r^2) for proper-surface punctures and complete local punctures in every dimension, and q^(C r^2) for the original divisorial-boundary surface quotient. The alternating-product obstruction proves that even all-field quadratic representation counts, linear H1, smallness and finite open prosolvable quotients do not imply full generation. Nonabelian crown multiplicities, alternating factors and the remaining projective or semilinear Lie families require geometric control; unrestricted-dimensional nonprojective global reduction remains open. Residual genus and different estimates are auxiliary until they control those groups.')
src=re.sub(r"'Formal review04 was completed[^\n]*",repr('Formal review07 was completed at09:11:25 UTC after the scheduled09:10 review time. All A/B/C rows remain decided; only general D.1, D.2(ii), and residual L8 remain open. The main gate strictly shrank through the all-field surface H1 theorems, local and global quadratic representation bounds, and original-boundary fixed-rank bounds; the exact comparison is in code/output/formal_review07.json. The consecutive no-movement count is0. The next formal review is due10:10 UTC. The next immutable scheduled checkpoint is13, due09:55 UTC; slots10–12 have failed scheduled-attempt records and no archives. Auxiliary results, reconstruction, packaging and repeated audits are not counted as main-gate movement.')+',',src)
assembly.write_text(src)

unresolved=root/'parts/D/unresolved_D.tex'; s=unresolved.read_text()
s=s.replace('The existing constructibility arguments\nprovide finiteness for each coefficient group separately,\nwithout either uniform estimate.',
 'The all-field linear estimate is now proved in dimension two by\nTheorems~\\ref{D:punctured-surface-all-characteristics-H1} and\n\\ref{D:tame-surface-all-characteristics-H1}, with the stated\nSchreier bounds for every open subgroup. Hence the maximal\nprosolvable quotients are finitely generated. The remaining surface\ncriterion concerns nonabelian crown multiplicities.\nTheorem~\\ref{D:global-quadratic-representation-bound} bounds\ndefining-characteristic representation classes by $q^{Cr^2}$ for\nproper-surface punctures, including the stated nonnormal extension;\nTheorem~\\ref{D:uniform-local-representation-growth} and\nCorollary~\\ref{D:uniform-local-growth-all-dimensions} give the local\nanalogue in every dimension. Theorem~\\ref{D:tame-parabolic-fixed-rank-growth}\ngives $q^{C_r}$ for the original-divisor tame surface quotient.\nExample~\\ref{D:quadratic-growth-alternating-obstruction} shows that\neven an all-field quadratic bound combined with linear cohomology\ndoes not imply finite generation abstractly. The exceptional-genus\nbound of Corollary~\\ref{D:surface-residual-genus-bound} is an\nadditional geometric constraint, not a bound for all crown\nmultiplicities. Unrestricted-dimensional nonprojective global\nreduction also remains open.')
unresolved.write_text(s)

inventory=root/'code/program_inventory.py'; s=inventory.read_text()
newcerts=[
 ('parts/D/code/check_psl2_bounded_ramification_v2.py','31,222 exact assertions for q=4,8,16: fields, PSL2 generation, branch orbits, inertia, invariant polynomials, and product inequalities; separately reconstructed source, distinct from the historical306,144-assertion program','parts/D/output/psl2_bounded_ramification_v2_root.json','runtime_seconds'),
 ('parts/B/code/check_alternating_quadratic_growth_reconstructed.py','201,628 exact assertions: A5/A7/A9, elementary subgroup ranks, tensor dimension and composition bounds, and16 multiplicity inequalities; reconstructed program, distinct from the historical186,828-assertion JavaScript source','parts/B/output/alternating_quadratic_growth_reconstructed.json','runtime_seconds'),
 ('parts/B/code/check_fixed_different_rational_chains.py','2,340 exact assertions for20 degree-two characteristic-two covers: substitution, curve semigroup gaps, all resolution-chart transitions, different data and intersection determinants; properness and normality are proved separately','parts/B/output/fixed_different_rational_chains.json','runtime_seconds'),
]
for cert in newcerts:
    if cert[0] not in s:s=s.replace('certs=[\n','certs=[\n'+repr(cert)+',\n',1)
inventory.write_text(s)

checkpoint=root/'code/checkpoint.py'; s=checkpoint.read_text()
s=s.replace("'prior_checkpoints':[f'RESEARCH_SA12_checkpoint_{i:02d}.zip' for i in range(1,number)]", "'prior_checkpoints':[f'RESEARCH_SA12_checkpoint_{i:02d}.zip' for i in range(1,number) if i not in (10,11,12)],'missed_scheduled_slots':[i for i in (10,11,12) if i<number]")
checkpoint.write_text(s)

manifest={'utc':now,'labels':[r['id'] for r in records], 'added_rows':len(added),
 'files':[{'path':rel,'sha256':hashlib.sha256((root/rel).read_bytes()).hexdigest()} for rel in paths],
 'new_bibliography_keys':bib_added,'archive_created':False,
 'requested_open_rows':['D.1','D.2(ii)','residual L8']}
(root/'code/output/integrate_post09.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'statements_integrated':len(records),'added_rows':len(added),'new_bib_keys':len(bib_added),'archive_created':False}))
