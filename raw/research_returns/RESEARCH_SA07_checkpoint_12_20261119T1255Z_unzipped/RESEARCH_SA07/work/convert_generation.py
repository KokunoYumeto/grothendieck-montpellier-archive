from pathlib import Path
import re, subprocess
base=Path('/workspace/scratch/f6dbb6638732')
g=(base/'work/agent_generation.md').read_text()
l=(base/'work/agent_lattices.md').read_text()
def part(text,name):
 m=re.search(r'^## '+re.escape(name)+r'\. ([^\n]+)\n(.*?)(?=^## |\Z)',text,re.M|re.S)
 title,body=m.groups()
 body=body.lstrip()
 body=re.sub(r'^\*\*Status:.*?\*\*\s*','',body,flags=re.S)
 body=re.split(r'^### Additional source checks',body,flags=re.M)[0]
 return title,body
mapping={'GEN-1':'A.4.9','GEN-2':'A.5.1','GEN-3':'A.5.2','GEN-4':'A.5.3','GEN-5':'A.5.4','LAT-1':'D.1.1','LAT-2':'D.1.2','LAT-3':'D.3.1','LAT-4':'D.3.2','LAT-5':'D.4.1','LAT-6':'D.4.2','LAT-7':'D.2.1','LAT-8':'D.5.1','LAT-9':'D.5.2','LAT-10':'D.5.3','LAT-11':'D.5.4','LAT-12':'D.6.1'}
def conv(s):
 for a,b in sorted(mapping.items(),key=lambda x:-len(x[0])):s=s.replace(a,b)
 s=s.replace('GEN2.','A5.1.').replace('\\unsure{5|4}',r'\{5\mid4\}')
 s=s.replace('T_\\ell,quad','T_\\ell,\\quad')
 s=s.replace('`code_generation/check_generation.py`','`code/check_generation.py`').replace('`code_generation/check_generation.out`','`code/check_generation.out`')
 s=s.replace('being developed in Part E','proved in E.1.2').replace("Part E is the parent task's location",'Part E supplies the results')
 s=re.sub(r'^### (.*)$',r'**\1.**',s,flags=re.M)
 out=subprocess.run(['pandoc','-f','markdown+tex_math_single_backslash+raw_tex','-t','latex','--wrap=preserve'],input=s,text=True,capture_output=True,check=True).stdout
 return out
summ={
'GEN-1':('Known; translation proved',r'For every elliptic curve over $\Qb$, the smallest algebraic subgroup containing a translated period locus is the full motivic group, in the category specified below.'),
'GEN-2':('Proved',r'The actual automorphism-cocycle image is Zariski dense exactly when the comparison point is generic over the same base field.'),
'GEN-3':('Proved counterexample',r'Passing from the actual cocycle image to its generated subgroup can change its Zariski closure.'),
'GEN-4':('Proved',r'Inversion converts the displayed right cocycle to a left cocycle; its graph is a homomorphism into the explicitly defined semidirect product.'),
'GEN-5':('Proved counterexample',r'There are genuine elliptic period comparisons over a transcendental field for which the actual image is not dense but its generated subgroup is dense. An augmented degree-one example has minimum field transcendence degree one and still has strictly different closures.'),
'LAT-1':('Proved',r'The integral product, restricted adelic ring and full product have the distinct maps and topologies described below. Betti comparison gives a dense integral submodule of the completed realization.'),
'LAT-2':('Proved bound; general equality gate retained',r'The relative tensor-comparison scheme has dimension $(n-1)\dim G$. This proves the stated componentwise bound; its joint product-ring interpretation requires the coordinate algebra specified below.'),
'LAT-3':('Proved',r'Every compact open adelic coset contains a full-measure set of points generic over $\Q$ in every local component, including the joint version for any fixed finite tuple.'),
'LAT-4':('Known inputs; application proved',r'For geometrically pairwise nonisogenous non-CM elliptic curves over a number field, Galois changes of the places attain the full bound at every prime.'),
'LAT-5':('Known criterion; examples proved',r'The connected affine groups having rational approximation in the finite adeles are characterized below. The determinant quotient proves that the full elliptic motivic groups do not have this property.'),
'LAT-6':('Proved equivalence and counterexamples',r'All-frame commensurability is equivalent to openness under rational approximation. Componentwise genericity has a different reverse implication, as the explicit group and motivic examples show.'),
'LAT-7':('Source gate; H5 formulation refuted',r'The supplied pages do not define $K$. The flag-fibre dimensions are five and four after fixing determinant; a concrete two-place example refutes automatic filtration-preserving linear commensurability.'),
'LAT-8':('Proved',r'The cocycle is the automorphism restriction of the fpqc descent datum of the comparison torsor. The change-of-place identity follows by typed composition.'),
'LAT-9':('Proved counterexample',r'Two conjugate CM elliptic curves can have rational and locally integral comparisons but no integral comparison compatible with their endomorphisms.'),
'LAT-10':('Universal assertion refuted; exact elliptic gate',r'The Tate motive $\Q(-2)$ refutes universal openness of the total-image closure. For a non-CM elliptic degree-one motive over a number field, that openness is equivalent to full period genericity.'),
'LAT-11':('Necessity proved; sufficiency refuted',r'The Tate quotient forces transcendence of $\pi$ for a generic comparison point. That condition alone does not imply genericity, even at minimum field transcendence degree in the stated degree-one category.'),
'LAT-12':('Scope recorded',r'The recovery question requires a specified category, coefficient ring and equivalence relation on places; the resolved cases are given in Part E.')}

def block(name,text):
 title,body=part(text,name)
 if name=='GEN-5':
  body=body.replace('The CM period theorem of Chudnovsky gives',r'The CM field calculation of A.4.3, using Chudnovsky \cite[\S2A, Theorem 1, p.343]{EllChudnovsky1978}, gives')
  old='abelian subvarieties and their\nprojectors do not acquire new parameters under algebraically closed\nbase extension.'
  new=r'''Here is the needed base-extension argument. For abelian varieties $A,B$ over an algebraically closed field $L$ and an algebraically closed extension $L'$, every homomorphism over $L'$ spreads over an integral finite-type $L$-scheme. A homomorphism between abelian varieties is rigid: its deformation fixing the origin is constant, as follows by applying the rigidity lemma to the difference of two fibres. The relative Hom scheme is therefore unramified with discrete fibres, and this family of homomorphisms is constant on a connected base. A closed $L$-point of the base gives the original homomorphism over $L$. Thus $\operatorname{Hom}_L(A,B)\to\operatorname{Hom}_{L'}(A_{L'},B_{L'})$ is bijective; injectivity is faithful base change. Apply this to the rational idempotent cutting out the elliptic factor, clear its denominator, and take the image of the resulting algebraic homomorphism. This produces the elliptic isogeny factor over $L=\overline{\mathbf Q}$.'''
  body=body.replace(old,new)
 if name=='LAT-5':
  body=body.replace('matrices, by the usual two-by-two identity.',r'''matrices by the explicit identity
\[
w(u)=E_{12}(u)E_{21}(-u^{-1})E_{12}(u)
=\begin{pmatrix}0&u\\-u^{-1}&0\end{pmatrix},\qquad
\operatorname{diag}(u,u^{-1})=w(u)w(-1).
\]''')
 cites={
 'GEN-1':r'\cite[Proposition 3.1; Theorem 5.13(ii); Proposition 5.14]{GenKSV2026}',
 'GEN-2':r'\cite[Definitions 2.3 and 2.9; Conjecture 2.12]{GenBostCharles}',
 'GEN-5':r'\cite[Proposition 2.21; Theorem 6.20 and Proposition 6.21]{GenDeligneMilne}',
 'LAT-1':r'\cite[Expos\'e XVI, Th\'eor\`eme 4.1, original p.233]{GenSGA4}',
 'LAT-4':r'\cite[\S4.4, Th\'eor\`eme 3, p.299; \S6.1, Th\'eor\`eme 6, p.324]{GenSerre1972}; \cite[\S5, Satz 4 and Korollar 2, pp.360--361]{GenFaltings1983}; \cite[Theorem 1.1 and Remark 1.2]{GenLombardo}',
 'LAT-5':r'\cite[Satz 1; Hilfss\"atze 2.3--2.5, pp.191--194]{GenKneser1965}; \cite[Theorem A, p.1140]{GenPlatonov1969}; \cite[\S\S2,5]{GenPlatonov1970}',
 'LAT-8':r'\cite[Theorem 3.2]{GenDeligneMilne}',
 'LAT-9':r'\cite[Theorem 3.13, p.24]{GenMilneCM2007}',
 'LAT-7':r'\cite[Theorem 12.14 and Corollary 12.16]{EllMilneMF}',
 }
 status,summary=summ[name]
 result='\\begin{result}{'+mapping[name]+'}{'+conv(title).strip()+'}{'+status+'}\n'+summary+'\n\\end{result}\n'
 if name!='LAT-12': result+='\\begin{proof}\n'
 result+=conv(body)
 if name in cites:result+='\nThe primary theorem locators used in this argument are '+cites[name]+'.\n'
 if name!='LAT-12':result+='\\end{proof}\n'
 return result
out='\\subsection{The subgroup generated by the elliptic period locus}\n\n'+block('GEN-1',g)+'\n\\subsection{The automorphism image and period genericity}\n\n'
for n in range(2,6):out+=block('GEN-'+str(n),g)+'\n'
(base/'output/RESEARCH_SA07/sections/A_generation.tex').write_text(out)
order=[('Integral realizations and the dimension bound',[1,2]),('The field on 18:45 and the filtration proposal',[7]),('Adelic genericity and elliptic open images',[3,4]),('Rational approximation and the margin equivalence',[5,6]),('Descent, change of place and the openness expectation',[8,9,10,11]),('Scope of place recovery',[12])]
out=''
for title,ns in order:
 out+='\\subsection{'+title+'}\n\n'
 for n in ns:out+=block('LAT-'+str(n),l)+'\n'
(base/'output/RESEARCH_SA07/sections/D.tex').write_text(out)
print('Created A_generation.tex and D.tex')
