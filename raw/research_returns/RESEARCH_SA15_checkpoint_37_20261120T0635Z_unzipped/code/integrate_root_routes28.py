"""Integrate previously audited route lemmas without altering their mathematics."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
history=w/'notes/root_routes28_before_integration'
assert not history.exists();history.mkdir()
for rel in ['code/consolidate.py','notes/root_references.bib','notes/late_source_census.json','notes/rational_monodromy_residual_obstruction.tex']:
    p=w/rel;shutil.copy2(p,history/p.name)

trans=w/'notes/post_CP27_freeze_transvection_route.tex'
marked=w/'notes/marked_normalization_triple_collision_obstruction.tex'
rational=w/'notes/rational_monodromy_residual_obstruction.tex'
assert sha(trans)=='c09cfe84e5f20ca4939a2a7306263769932949c4648bbedbed6c54e3a9d71709'
assert sha(marked)=='d2140b03e1a5597cc95659633ccf3af9fed61c88b3a01eb5db5683118665c3ed'
assert sha(rational)=='5b5a77cfa6dd1472b8b38ed2da4fd38dd5eb32f5e681cd07b9daf55ae2f22402'
t=trans.read_text().replace('\\subsection*{','\\subsection{',1)
t=t.replace('The two elementary lemmas are supplied with complete proofs for independent\nreview.','The two elementary lemmas have complete direct proofs and an independent\nproof audit.')
t=t.replace('\\paragraph{Algebraic criterion.}',r'''\begin{lemma}[One conjugacy class of transvections]
\label{lem:root-single-transvection-class}
\status{Proved; complete direct proof and independent audit passed.}''')
t=t.replace('\\emph{Proof.}',r'\end{lemma}'+'\n'+r'\begin{proof}',1)
t=t.replace('\\paragraph{Local corank-one inertia.}',r'''\end{proof}
\begin{lemma}[Local corank-one Lang inertia]
\label{lem:root-corank-one-Lang-inertia}
\status{Proved; complete direct proof and independent audit passed.}''')
t=t.replace('\\emph{Proof.}',r'\end{lemma}'+'\n'+r'\begin{proof}',1)
t=t.replace('\\paragraph{Precise unresolved geometric step.}',r'\end{proof}'+'\n\n'+r'\paragraph{Precise unresolved geometric step.}')
t=t.replace('The opened primary comparison was Brumer and Kramer, arXiv:1701.01890v1,','The opened primary comparison was Brumer and Kramer~\\cite{BrumerKramer2018LargeImage}, arXiv:1701.01890v1,')

m=marked.read_text().replace('\\subsection*{','\\subsection{',1)
start='Let $R$ be a strictly henselian discrete valuation ring'
assert start in m
m=m.replace(start,r'''\begin{proposition}[Trivial inertia with marked constant-rank normalization]
\label{prop:root-marked-normalization-inertia}
\status{Proved; complete direct proof and independent audit passed.}
Let $R$ be a strictly henselian discrete valuation ring''',1)
m=m.replace('\\emph{Proof.}',r'\end{proposition}'+'\n'+r'\begin{proof}',1)
m=m.replace('\\paragraph{Effect on the proposed triple-packet route.}',r'\end{proof}'+'\n\n'+r'\paragraph{Effect on the proposed triple-packet route.}')
m=m.replace('it is outside its frozen paper and\noutcome table.','it was outside that frozen paper and\noutcome table and is now included with its exact limited hypotheses.')

r=rational.read_text().replace('Proved by a direct argument; independent audit requested.','Proved; complete direct proof and independent audit passed.').replace('Proved by a direct argument and an exact finite supplement; independent audit requested.','Proved; direct proof, full independent audit and exact finite supplement passed.')
rational.write_text(r)
section=w/'sections/A_route_limitations.tex'
assert not section.exists()
section.write_text(t+'\n'+m+'\n'+r+'\n')
con=w/'code/consolidate.py';c=con.read_text()
needle="   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')"
assert needle in c
c=c.replace(needle,"   out.write('\\n\\\\input{sections/A_route_limitations}\\n')\n"+needle,1)
con.write_text(c)

bib=w/'notes/root_references.bib';b=bib.read_text()
entries=r'''
@article{BrumerKramer2018LargeImage,
 author={Brumer, Armand and Kramer, Kenneth},
 title={Large 2-adic Galois image and non-existence of certain abelian surfaces over {Q}},
 journal={Acta Arithmetica},
 volume={183},
 pages={357--383},
 year={2018},
 doi={10.4064/aa170514-20-2},
 url={https://arxiv.org/pdf/1701.01890},
 note={Opened original arXiv:1701.01890v1, 7 January 2017, 19 pages: introduction; Theorem 2.1.1 and Proposition 2.1.2 statements; full final reduction of Theorem 2.1.1 on printed p.3 and full Proposition 2.3.4 proof on printed p.5. Published metadata checked separately. Symplectic and arithmetic comparison only; no theorem imported into the fixed characteristic-two hypersurface family. The full Honda-system argument and cited classification proof were not freshly read.}
}
@article{DAddezio2023Parabolicity,
 author={D'Addezio, Marco},
 title={Parabolicity conjecture of {F}-isocrystals},
 journal={Annals of Mathematics},
 volume={198},
 number={2},
 pages={619--656},
 year={2023},
 doi={10.4007/annals.2023.198.2.3},
 url={https://arxiv.org/pdf/2012.12879},
 note={Opened original arXiv:2012.12879v4, 8 February 2023, 30 pages, and official journal metadata. Read introduction printed pp.2--4; complete statement and final proof of Theorem 4.4.12 on printed pp.23--24; complete Proposition 5.1.4 and Theorem 5.1.6 statements and proofs on printed p.25. Deeper dependencies, including Theorem 4.1.3, Proposition 4.3.2 and Corollary 4.3.6, were not fully audited in this pass. Rational-isocrystal comparison only; no residual full-image theorem is imported.}
}
'''
for key in ['BrumerKramer2018LargeImage','DAddezio2023Parabolicity']:
    assert ('{'+key+',') not in b
bib.write_text(b+'\n'+entries)

late=w/'notes/late_source_census.json';rows=json.loads(late.read_text())
keys={row['key'] for row in rows}
for row in [
 {'key':'DAddezio2026UnobtainedLead','author':"D'Addezio, Marco (search-snippet attribution only)",'year':'2026','title':'Crystals and the parabolicity conjecture; reported arXiv:2610.15521','access':'Not obtained; unverified primary-search lead only','locators_and_limits':'Primary snippet reported11October2026. Both abstract and PDF open attempts returned DisabledError. No original theorem or proof obtained or used; metadata are not asserted as independently verified.','url':'https://arxiv.org/abs/2610.15521'},
 {'key':'ShimuraUnitRoot2026UnobtainedLead','author':'Author list not verified','year':'2026','title':'Local monodromy of unit root F-isocrystals from Shimura varieties; reported arXiv:2607.10054','access':'Not obtained; unverified primary-search lead only','locators_and_limits':'Primary snippet reported11July2026. Both abstract and PDF open attempts returned DisabledError. A further exact-ID arxiv-domain search returned no results. No theorem or proof obtained or used; neither authors nor bibliographic metadata are asserted as independently verified.','url':'https://arxiv.org/abs/2607.10054'}
]:
    assert row['key'] not in keys;rows.append(row)
late.write_text(json.dumps(rows,indent=2)+'\n')

events=[
 ('lem:root-single-transvection-class','2026-11-19T23:02:09.930804+00:00','independent re-proof','Complete independent monodromy-reviewer rederivation of the one-conjugacy-class argument; exact original SHA c09cfe84e5f20ca4939a2a7306263769932949c4648bbedbed6c54e3a9d71709. Numbered CP28 integration changes presentation only. Global branch/conjugacy assumptions remain unproved.'),
 ('lem:root-corank-one-Lang-inertia','2026-11-19T23:02:09.930804+00:00','independent re-proof','Complete independent Lang lifting and additive inertia proof; no cyclicity inferred. Same exact audited original and presentation-only CP28 integration.'),
 ('prop:root-marked-normalization-inertia','2026-11-19T23:06:59.619400+00:00','independent re-proof','Complete independent Artin-Schreier, marked-torsor gluing and trivial-inertia proof; exact original SHA d2140b03e1a5597cc95659633ccf3af9fed61c88b3a01eb5db5683118665c3ed. Constant rank and rational marked sections are essential; no arbitrary triple-family claim.'),
 ('prop:root-rational-residual-obstruction','2026-11-19T23:20:43.652552+00:00','independent re-proof','Reduction/descent reviewer fully rederived compact openness, Zariski density over Qp and Qpbar, and absolute irreducibility. Exact candidate SHA 5b5a77cfa6dd1472b8b38ed2da4fd38dd5eb32f5e681cd07b9daf55ae2f22402; independent_rational_residual_parabolic_audit.json. No geometric realization or main-gate movement.'),
 ('ex:root-rational-residual-parabolic','2026-11-19T23:20:43.652552+00:00','independent re-proof','Complete all-prime block-parabolic proof and exact unchanged finite-code rerun0.12095284799579531s; all64512 matrices checked, no fixed vectors/covectors, proper natural GL3 block. Author output unchanged; every mathematical field agrees.'),
 ('ex:root-rational-residual-parabolic','2026-11-19T23:19:39.731542+00:00','computation or formal certificate','Author exact finite run0.12337379300151952s: code/check_rational_residual_parabolic.py and outputs/rational_residual_parabolic.json. Parametersp2,r3,s2;64512 matrices,GL5order9999360,14 elementary transvections. Finite group verification only, no geometric or infinite-density inference.')
]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label,utc,kind,detail in events:
        wr.writerow([label,utc,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); root with named independent reviewer',kind,detail])
record={'status':'AUDITED ROOT ROUTES INTEGRATED','actual_utc':stamp,
        'preserved_inputs':str(history.relative_to(w)),
        'section':str(section.relative_to(w)),'section_sha256':sha(section),
        'new_labels':[e[0] for e in events[:-1]],
        'scope':'Presentation-only numbering of three previously independently audited elementary statements plus two newly audited rational/residual statements. No main-gate movement.'}
(w/'outputs/root_routes28_integration.json').write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/checkpoint28_changes.md').open('a') as f:
    f.write('\n### Audited route limitations integrated\n\nThe two transvection lemmas, the marked-normalization inertia proposition and the two rational/residual statements are now numbered in sections/A_route_limitations.tex. The original exploratory notes and exact audited hashes are preserved. Their full independent audits are explicitly mapped to the new labels in CHECK_EVENTS.tsv. The rational/residual proof passed the reduction/descent independent audit at23:20:43.652552UTC; the literal isolated finite checker reran in0.12095284799579531s against author0.12337379300151952s, with every mathematical output field equal and author bytes unchanged. These results close proposed inference routes only and are not counted as main-gate movement. The two opened primary comparisons now have passage-specific bibliography entries; failed recent leads remain explicitly unverified in the source census.\n')
print(json.dumps(record,indent=2))
