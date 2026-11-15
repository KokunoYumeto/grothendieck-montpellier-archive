"""Finalize the reviewed section handoffs and enforce one paragraph per section."""
from pathlib import Path
import re,json
P=Path(__file__).resolve().parents[1]
p=P/'guide_sections/134_6_tail_by_134_5_6.tex'
s=p.read_text()
oldhead=r'\paragraph{\S105, continuation. Abelian pairings, algebraic topoi and an unfinished universal property (pp.\ 399--406).}'
newhead=r'\paragraph{\S105. Duality of presheaf topoi\newline and tentative additive generalizations (pp.\ 394--406).}'
opening=r'''Dated 12 August with a handwritten addition of 13 August, subsection D explicitly limits its heading to topoi of the type $A^\wedge$ and tentative generalizations. Proposition~3 states the free-cocompletion property of the Yoneda inclusion $\varepsilon_A:A\to A^\wedge$: restriction gives (33), an equivalence between cocontinuous functors $A^\wedge\to\mathcal M$ and arbitrary functors $A\to\mathcal M$, when $\mathcal M$ has small inductive limits. The quasi-inverse sends $i$ to $i_!$, computed in (35) by the inductive limit of $i(a)$ over $A_{/F}$, and (36) gives its right adjoint $i^*(x)=(a\mapsto\mathrm{Hom}(i(a),x))$. The following remark literally assumes a pseudocotopos, where the witness says pseudotopos. Formula (37), however, writes $i\mapsto i^*$ as a covariant functor between the ordinary Hom categories without an opposite. Natural transformations reverse under this assignment, and the explicit opposite in (6), p.\ 385, rules out treating the missing variance mark as an unstated convention; the formula is preserved literally rather than mathematically amended (p.\ 394). The universal property adjoins arbitrary inductive limits while disregarding any that may already exist in $A$. Its projective-limit dual is (38), whose restriction map visibly includes $F\circ\varepsilon_A^o$, with the F and composition sign omitted by the witness. Thus $\mathcal M$-valued cosheaves on $A^\wedge$ identify with functors $A\to\mathcal M$, while $\mathcal N$-valued sheaves identify with functors $A^o\to\mathcal N$, equivalently presheaves on the chaotic site. If $\mathcal M$ has both kinds of small limits, combining these descriptions for $B=A^o$ gives (39), identifying cosheaves on $A^\wedge$ with sheaves on $B^\wedge$ with the same values. The final word canonically on p.\ 395 is cancelled; diagram (40) then explains the comparison through $\mathrm{Hom}(A,\mathcal M)=\mathrm{Hom}(B^o,\mathcal M)$ and a chosen quasi-inverse supplied by projective limits. Its dual, with $\mathcal N=\mathcal M^o$, is canonically quasi-inverse to the comparison for B, using the ordinary opposite-category identity (6). The source leaves the two inner Hom arguments at the end of p.\ 396 blank, whereas the witness supplies them (pp.\ 395--396). Case~1 takes sets as coefficients. Formula (41) and its symmetric counterpart identify each presheaf topos with the set-valued cosheaves on the other, through the separately cocontinuous pairing (42), denoted $F*G$ in (43). Two applications of Proposition~3 give (44), so the pairing is determined on representables by $a*b^o=\mathrm{Hom}_A(b,a)=\mathrm{Hom}_B(a^o,b^o)$ in (45). Its symmetry compares the pairing for $(A,B)$ with the pairing for $(B,A)$; it is not an undeclared symmetry inside one fixed pair of categories. Formula (47) gives the evaluation identities $a*G\simeq G(a)$ and $F*b^o\simeq F(b)$ (pp.\ 396--398). The remarks postpone further development of this set-valued duality but sketch the opposite-variance bi-sheaf (48), associated with mutually adjoint contravariant functors. The pairings are proposed as the cross-Hom sets in a category $\mathcal E(A)$ combining $A^\wedge$ and $(B^\wedge)^o$ along A, with $\mathcal E(A)^o\simeq\mathcal E(B)$. Their compatibility is to be expressed through composition and associativity; full details are not supplied here. The later discussion on pp.\ 404--405 returns to this construction, as the marginal pointers anticipate (p.\ 398). Case~2, opened at the foot of p.\ 398, takes abelian-group coefficients and uses the abelianization results (12) and (14) of \S104. '''
if oldhead in s:
 s=s.replace(oldhead,newhead,1)
 first='This continuation begins with Case~2, introduced on p.\\ 398. '
 assert first in s
 s=s.replace(first,opening,1)
 p.write_text(s)
else:
 assert newhead in s,'Unexpected section 105 heading; do not duplicate its opening.'
# Blank lines inside an entry would create additional paragraphs. Preserve all wording,
# formulae, headings and explicit local line breaks while joining each section body.
files=['134_5_6.tex','134_6_middle_by_134_5_6.tex','134_6_tail_by_134_5_6.tex']
counts={}
for name in files:
 f=P/'guide_sections'/name;text=f.read_text();parts=re.split(r'(?m)^(\\paragraph\{[^\n]*\}\n)',text)
 prefix=parts[0].rstrip();out=[prefix] if prefix else [];sections=[]
 assert len(parts)%2==1
 for i in range(1,len(parts),2):
  heading=parts[i].rstrip();body=parts[i+1]
  # These authored guide entries contain no displays or verbatim blocks.
  assert not re.search(r'\\(?:begin|\[|par\b)',body),heading
  lines=[l.strip() for l in body.splitlines() if l.strip()]
  assert not any(l.startswith('%') for l in lines),heading
  out.append(heading+'\n'+' '.join(lines));sections.append(re.search(r'\\S(\d+)',heading).group(1))
 f.write_text('\n\n'.join(out)+'\n');counts[name]=sections
assert r'\S90. Existence and perfection of test functors,\newline' in (P/'guide_sections/134_5_6.tex').read_text()
(P/'records/GUIDE_COVERAGE_134_5_6.json').write_text(json.dumps({'section_entries':counts,'body_paragraphs_per_entry':1,'shared_section_evidence':{'102':['records/PAGE_REVIEW_134_7_8.tsv: ps_134-6_060','records/PAGE_REVIEW_134_5_6.tsv: ps_134-6_061--063'],'104':['records/PAGE_REVIEW_134_5_6.tsv: ps_134-6_066--074','records/HANDOFF_104_105_tail_134_3_4.md: p393'],'105':['records/HANDOFF_104_105_tail_134_3_4.md: pp394--398','records/PAGE_REVIEW_134_5_6.tsv: ps_134-6_081--088']}},indent=2)+'\n')
print('Final guide entries:',sum(map(len,counts.values())),counts)
