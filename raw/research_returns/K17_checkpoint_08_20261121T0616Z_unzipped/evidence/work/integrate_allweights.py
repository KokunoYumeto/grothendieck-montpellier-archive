from pathlib import Path
import csv

base=Path(__file__).resolve().parent.parent
work=base/'work'
pkg=base/'K17_package'

def replace_file(name, replacements):
    p=work/name
    s=p.read_text()
    for old,new in replacements:
        if old not in s:
            raise RuntimeError(f'Missing replacement in {name}: {old[:70]}')
        s=s.replace(old,new)
    p.write_text(s)

replace_file('build_paper.py',[
('weight $32$ and at $691$ in weight $12$. At $2$ it holds through\nweight $18$ by an exact compact-group computation; the all-weight\nassertion and the remaining irregular-prime cases retain explicit gates.',
 'weight $32$ and at $691$ in weight $12$. At $2$ a central-extension\nparity induction constructs adapted Newton generators in every odd\nweight and proves integral free generation in all weights. A separate\nlocalized Steinberg-homology argument reduces the $K_{12}$ gate to\ntwo specified ranks. The other remaining cases retain explicit gates.'),
("(work/'k_polynomial_section.tex').read_text()+'\\n'+r", "(work/'k_polynomial_section.tex').read_text()+'\\n'+(work/'k12_rank_reduction.tex').read_text()+'\\n'+r"),
('What remains integral at','The integral comparison at'),
("s += '\\n'+(work/'pro2_integral_section.tex').read_text()+'\\n'+(work/'pro2_integral_newton_section.tex').read_text()", "s += '\\n'+(work/'pro2_integral_section.tex').read_text()+'\\n'+(work/'pro2_integral_newton_section.tex').read_text()+'\\n'+(work/'pro2_integral_class2_section.tex').read_text()+'\\n'+(work/'pro2_integral_allweights_section.tex').read_text()"),
('two nonzero trace products and their gcd, or a different integral\ncohomology calculation. The available primary literature checks and\nthe exact trace-product reduction are documented in the evidence notes.',r'''two nonzero trace products and their gcd, or the two localized
Steinberg-homology vanishings in Proposition~\ref{prop:k12-two-ranks}.
The formerly missing rank-$11$ term is now eliminated. The remaining
terms are $H_4(\mathrm{GL}_9;\mathrm{St}_9)$ and
$H_3(\mathrm{GL}_{10};\mathrm{St}_{10})$ over $\mathbb Z[1/13!]$.
Neither of these two computations is claimed here.'''),
(r'''\paragraph{OPEN-2-LATTICE: integral odd generation at $2$.}
The exact outer-filtration comparison and compact-group calculation
prove integral odd generation through weight $18$. The all-weight gate
is attainment of the explicit Newton minimum in every primitive odd
weight. Proposition~\ref{prop:newton-basis} then supplies the complete
compact basis and Hall-generation argument; no independent stability
hypothesis remains. No all-weight proof or counterexample is asserted.''',r'''\paragraph{The former OPEN-2-LATTICE gate is closed.}
Theorem~\ref{thm:2-allweights} constructs every adapted Newton lift
by an integral parity correction. Proposition~\ref{prop:newton-basis}
then proves free generation in all weights, and
Proposition~\ref{prop:outer-sat} identifies the actual outer filtration.
The earlier finite and class-two computations remain separate checked
results; neither is extrapolated to obtain the theorem.'''),
("'vandiver_kernel_bibliography.tex']", "'vandiver_kernel_bibliography.tex','k12_rank_bibliography.tex']")
])

replace_file('tripod_section.tex',[
('What remains integral at','The integral comparison at'),
('Choosing odd classes whose rational images form the standard free generating system gives an injective integral free source. Equality with the actual lattice, weight by weight, is the remaining saturation question. We obtained neither a checked all-weight proof nor a counterexample for this surjectivity at $2$.',r"Choosing odd classes whose rational images form a free generating system gives an injective integral free source. Equality with the actual lattice requires an additional argument. Theorem~\ref{thm:2-allweights} below supplies that argument in every weight: it constructs primitive adapted odd generators, proves integral freeness, and uses the exact outer-filtration comparison. It does not prescribe unit values for a separately normalized Soul\'e family."),
('This suggests finite-weight lattice calculations; it supplies no integral free basis by itself.','This explains the denominators in the finite-weight lattice calculation. The subsequent parity induction uses actual group commutators to remove them where needed and supplies the integral free basis.'),
('take $q=149$ and $z=16$, with $z$ of exact order $37$.',r'take $q=149$ and $\zeta=107$, whose square root in the order-$37$ subgroup is $16$. The half-exponent normalization is corrected in Hart--Harvey--Ong, \S7, p.~13; the detailed certificate above uses exactly that correction.')
])

replace_file('pro2_integral_section.tex',[
('Lie algebra. This is a finite-range result; the all-weight\nintegral generation assertion remains open in this run.',r'''Lie algebra. This is an independently checked finite-range result;
Theorem~\ref{thm:2-allweights} below proves the all-weight assertion
by a separate induction.'''),
('in the Iwasawa algebra. The unproved step in an all-weight\nargument is integral correction of every lower decomposable\nweight and stability of the resulting Hall family under $D$.\nThe scalar Newton determinant does not alone prove that step.',r'''in the Iwasawa algebra. Passing to all weights requires integral
correction of lower decomposable terms. The scalar Newton determinant
does not alone perform that correction; the following compact-basis
reduction and parity induction supply it.''')
])

replace_file('pro2_integral_newton_section.tex',[
('This proposition is conditional: the infinite attainment\nhypothesis is not established by the finite calculation above.',r'''This proposition isolates a sufficient lifting hypothesis. The finite
calculation above does not establish it; Theorem~\ref{thm:2-allweights}
below establishes it in every weight.'''),
('The remaining all-weight question is therefore the existence\nof these lifts, or equivalently attainment of the Newton\nminimum in every odd weight.',r'''The all-weight problem is therefore reduced to the existence
of these lifts, or equivalently attainment of the Newton
minimum in every odd weight. This gate is closed by
Theorem~\ref{thm:2-allweights} below.''')
])

replace_file('pro2_integral_class2_section.tex',[
('That higher-length lifting question requires its own\nargument.',r'''The higher-length lifting is supplied by the separate induction
in Theorem~\ref{thm:2-allweights}.''')
])

replace_file('k_groups_section.tex',[
('and does not state the integral\nand higher-codimension input required by that route.\nNo new specified degree vanishing is claimed from the\nexistential constants extracted here.',r'''and does not state the integral
and higher-codimension input required by that route.
Proposition~\ref{prop:steinberg-two-local} extracts the localized
integral consequence of its proof; Proposition~\ref{prop:k12-two-ranks}
thereby leaves only ranks $9$ and $10$ in the $K_{12}$ homology gate.
No new specified degree vanishing is claimed from the
existential constants extracted here.''')
])

p=pkg/'QUESTIONS.tsv'
with p.open() as f:
    reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
byid={r['id']:r for r in rows}
byid['Q2-NEWDEG']['finding_ids_or_current_gate']='VK-POLY-CERT; K17-K12-TWO-RANKS; OPEN-K-NUM'
byid['Q2-NEWDEG']['detail']='No new degree certified. Alternatives: complete integral trace polynomials, or H4(GL9;St9) and H3(GL10;St10) over Z[1/13!] both zero. K17-ST2-LOCAL eliminates the formerly missing rank11 term.'
byid['Q4-GEN2'].update(state='proved',finding_ids_or_current_gate='K17-2-ALL; K17-2-NEWTON-BASIS; K17-OUT-SAT',detail='Integral parity correction constructs actual adapted Newton lifts in every odd weight; compact free basis and weighted Magnus comparison prove the entire actual integral graded Lie algebra free on primitive odd classes. No prescribed Soulé normalization asserted.')
byid['Q4-GEN2-FINITE']['detail']='Independent exact computation through weight18, with full rerun through14 and two-way matrix checks through18. The separate K17-2-ALL theorem now proves all weights.'
byid['Q4-NEWTON-BASIS']['detail']='Every scalar Newton minimum suffices for compact basis and integral Hall generation. K17-2-ALL now supplies infinite attainment by actual commutator corrections.'
new=[
['Q2-ST2-LOCAL','BMPSW Prop8.5/Lem8.7/Lem8.9 pp57-59','Does the integral proof give localized Steinberg H2 vanishing?','proved','K17-ST2-LOCAL','For n>=3, H2(SLn;Stn) and H2(GLn;Stn) vanish over Z[1/(n+1)!].'],
['Q2-K12-TWO-RANKS','DEKM Remark6.6 p19; new localized resolution deduction','Can the K12 homology gate be reduced from three ranks to two?','proved','K17-K12-TWO-RANKS','Ranks9 and10 in Voronoi degree12 remain sufficient over Z[1/13!]; both vanishings are still unproved here.'],
['Q4-CLASS2','B3 integral at2; exact Newton-wedge parity calculation','Does the actual class-two quotient have free odd integral generation in all weights?','proved','K17-2-CLASS2','Symbolic parity identity and actual commutator correction prove every weight of the class-two quotient independently of the subsequent full theorem.'],
['Q4-ALLWEIGHTS2','B3 integral at2; parity and central extensions','Can every adapted odd Newton lift be constructed integrally?','proved','K17-2-ALL','Yes. c=-1 on H_ab yields twice the even tail in a previous derived subgroup; integral correction and triangular Frattini action close the induction.']]
for vals in new:
    if vals[0] in byid: raise RuntimeError('Duplicate new question')
    rows.append(dict(zip(fields,vals)))
with p.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(rows)

p=pkg/'IMPLICATIONS.md';s=p.read_text()
s=s.replace('K4=0 and K8=0 are cited established results, not consequences first proved by this run.', 'K4=0 and K8=0 are cited established results, not consequences first proved by this run. A separate integral-homology route has now become smaller: K17-ST2-LOCAL proves H2(GL_n;St_n) vanishes over Z[1/(n+1)!], eliminating rank11. K17-K12-TWO-RANKS shows that H4(GL9;St9) and H3(GL10;St10) vanishing over Z[1/13!] would suffice for K12=0. These are the two remaining homology computations.')
old='At2, K17-OUT-SAT proves exact agreement of the original outer filtration with its rational pullback. The compact-group calculation K17-2-FINITE18 then proves integral odd generation through weight18. K17-2-NEWTON-BASIS reduces the all-weight problem to attainment of the explicit Newton minimum in every primitive odd weight. Once those lifts exist, the compact free basis and integral Hall generation follow without a separate stability assumption. The finite computation does not establish infinite attainment.'
new='At2, the integral question is now proved in every weight. K17-OUT-SAT identifies the original outer filtration with its rational pullback. K17-2-ALL constructs an actual element in each odd weight2i+3 with the exact Newton abelian class. Complex conjugation acts as minus identity on the whole cyclotomic abelianization, so twice each unwanted next-even tail has a lift in a previously constructed commutator subgroup. The factor5^m(5-1)/2 is integral and removes it; triangular Frattini action propagates generation. K17-2-NEWTON-BASIS then supplies a compact free basis and free integral Hall generation. Thus the arithmetic integral Deligne–Ihara statement holds over Z2 for primitive generators. This does not prescribe unit values for a differently normalized Soulé family. The finite-weight18 calculation and the all-weight class-two identity remain independent checked intermediate results.'
assert old in s;s=s.replace(old,new)
s=s.replace('- The pro2 field equality and the odd-prime Vandiver implication are separate checked deductions from established inputs;', '- The pro2 field equality, all-weight primitive integral generation over Z2, and the odd-prime Vandiver implication are separate checked deductions from established inputs;')
p.write_text(s)

print('Integrated all-weight2 and two-rank K12 statements and current gates.')
