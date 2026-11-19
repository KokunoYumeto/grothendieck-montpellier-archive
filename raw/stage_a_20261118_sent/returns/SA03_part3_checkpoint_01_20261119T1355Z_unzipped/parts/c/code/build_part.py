"""Render explicitly authored editorial decisions; no heading/keyword classification.

Only line-indexing, serialization and integrity checks are mechanical. All verdicts,
claims, mathematical qualifications and mappings below were written after reading
the complete indexed notes and the indicated Pro and Codex transcriptions.
"""
from pathlib import Path
import csv,json,re
P=Path(__file__).resolve().parents[1]
ROOT=P.parents[2]
T='source/SA03_texts/pro/MPL_91_099-143_transcription.tex'
N='source/SA03_notes/pro/MPL_91_099-143_notes.md'
D='source/SA03_notes/pro/MPL_91_099-143_doubts.md'
PK='MPL_91_099-143'
tx=(ROOT/T).read_text().splitlines()
starts=[(int(m.group(1)),i+1) for i,l in enumerate(tx) if (m:=re.search(r'\\scanpage\{(\d+)\}',l))]
bands={s:(a,starts[j+1][1]-1 if j+1<len(starts) else len(tx)) for j,(s,a) in enumerate(starts)}
def loc(scans): return [f'{T}:{bands[s][0]}-{bands[s][1]}' for s in scans]
items=[]; entries=[]; claims=[]; problems=[]; events=[]
def I(n,src,kind,scans,words,statement,reconstruction,check,reason,verdicts=None):
    iid=f'SA03-{n}'
    items.append(dict(id=iid,sources=[f'{PK}#{s}' for s in src],kind=kind,cote='91',scans=scans,lines=loc(scans),his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for j,s in enumerate(src):
        verdict=(verdicts or {}).get(s,'kept' if j==0 else 'merged')
        entries.append(dict(entry_id=f'{PK}#{s}',item_id=iid,verdict=verdict,reason=reason))
    return iid

I(401,[1],'other',[], '',
  'Editorial citation key for earlier context excerpts; no mathematical assertion by the manuscript author.',
  'The full research returns named by the key are not among the supplied files. Their reported statuses cannot be adopted as verified results.',
  'agrees','Read the key and its scope paragraph. Retain as provenance metadata, with no phantom claim.')
I(402,[2],'conjecture',[99,101],'catégorie géométrique (?)',
  'Does the proposed finite-type category of schematic objects over a noetherian base have the listed finite-limit, quotient and descent properties?',
  'Pro reads pro-schématique; K91-08 reads quasi-schématique. Neither identification with a topos nor a definition of the exact category is supplied here.',
  'overstates','The question is real, but the category word is disputed between transcriptions. Retain the question; do not silently identify it with the category of schemes or a Grothendieck topos.',{2:'corrected'})
I(403,[3],'self-flagged step',[101],'donc aux ... finies ???',
  'The sheet asks whether the specified base-change operation preserves finite colimits after listing finite limits, effective equivalence-relation quotients, descent epimorphisms and distributive coproducts.',
  'An exact/extensive-category or topos comparison is a modern reconstruction; the dual list and its arrows must be interpreted in the intended slice category.',
  'agrees','The final question is supported. Distributivity over coproducts alone does not prove preservation of all finite colimits.')
I(404,[4],'withdrawn in the same text',[101],'Tout morphisme se factorise',
  'The epimorphism–monomorphism factorization item is cancelled; an adjacent kernel-pair diagram and lower primed list remain.',
  'No later theorem is inferred from the residual diagram.',
  'agrees','Both the cancellation and surviving alternatives were read. A withdrawn draft is not a live theorem.',{4:'withdrawn'})
I(405,[5,47],'reading question',[100,102],'K est dense dans H',
  'The reused typescript proves inverse-limit subgroup, density, kernel and projection statements; the marginal 2|? at the subgroup paragraph is undecided.',
  'For the open-surjection theorem, homomorphisme sur must retain its topological quotient-map sense; mere continuous algebraic surjectivity would be weaker.',
  'agrees','The two entries concern the same reused inverse-limit proof material. The possible handwritten question mark is not counted as a certain authorial doubt.')
I(406,[6,7],'reading question',[104,105,106],'base formée d’ouverts rétrocompacts',
  'The constructible topology and its restriction to locally constructible subspaces are developed under explicit quasi-compact and retrocompact basis hypotheses.',
  'Modern patch topology terminology is used only with the stated spectral/local spectral hypotheses. The E|F variable in the restriction lemma remains a reading flag.',
  'agrees','The restriction lemma supplies the precise local-to-global dependency, so the two entries are merged without removing the letter ambiguity.')
I(407,[8],'reading question',[106],'pt générique',
  'The margin links compactness in the constructible topology to existence of generic points of irreducible closed subsets and a T0 qualification.',
  'K91-08 reads uniqueness under T0 where Pro suggests a converse. The mathematical proof gives existence from patch compactness and uniqueness from T0; no converse is assigned to the author.',
  'overstates','The generic-point argument is supported, but the purported converse rests on a conflicting reading.',{8:'corrected'})
I(408,[9],'self-flagged step',[107],'Nature locale de la notion ??',
  'The questioned notion is a local intersection of constructible subsets, compared with closedness and compactness in the patch topology.',
  'We call this proconstructibility only where the displayed equivalences support it. The uncertain coined word is left unchanged.',
  'agrees','Retain the locality question and distinguish local compactness as a space from closedness in an ambient patch space.')
I(409,[10],'reading question',[108],'hyp.',
  'Pro reads a warning that the retrocompact pullback hypothesis is too restrictive; K91-08 reads that it is always verified for a scheme morphism.',
  'The latter statement is mathematically correct: pullback of a quasi-compact open immersion is quasi-compact. This is evidence for ink review, not authority to change the transcription.',
  'misreads','A definite authorial self-criticism cannot be retained when the independent transcription reverses the statement. The note is corrected to a conflict flag.',{10:'corrected'})
I(410,[11],'withdrawn in the same text',[109],'il f. et s. que',
  'The upper corollary is cancelled, while lower basis criteria for quasi-compactness and retrocompactness remain live.',
  'The surviving proof uses finite unions of basis opens and quasi-compactness of intersections; it is recorded separately from the cancelled formulation.',
  'agrees','Retain the revision history and the live criterion rather than treating the whole page as withdrawn.')
I(411,[12,13],'reading question',[110],'transforme les parties constructibles',
  'The positive constructible-image N.B. in Pro conflicts with the negative K91-08 reading; the following corollary characterizes constructible-image maps by openness in the patch topology.',
  'Spec k(t) → Spec k[t] is a quasi-compact affine map whose image is the nonconstructible generic singleton. This rejects the unqualified positive reading, not a securely established authorial assertion. The alleged les vérifier also conflicts with sont vérifiées.',
  'misreads','Both note entries depend on unstable readings in the same hypothesis block. Merge as a conflict audit; retain the valid corollary separately in the claims map.',{12:'corrected',13:'merged'})
I(412,[14],'unproved claim',[111],'Alors X^{cons} est compact',
  'An affine scheme has compact Hausdorff constructible topology; a quasi-separated scheme has locally compact patch topology; a quasi-compact quasi-separated scheme has compact patch topology.',
  'Here compact is topological compactness, and the inserted quasi-separated qualification is essential to the stated affine-basis argument.',
  'agrees','The note accurately preserves the quasi-separated insertion and the absence of a proof of affine compactness on this leaf.')
I(413,[15],'unproved claim',[111,115],'un monomorphisme q. cpt',
  'A proconstructible subset of a quasi-compact quasi-separated scheme is the image of a quasi-compact monomorphism.',
  'Construct the absolutely flat envelope and restrict to the closed subset in its patch spectrum; the resulting closed subscheme followed by the envelope map is a monomorphism. This proof is ours, with Olivier as a published counterpart.',
  'agrees','The strengthened monomorphism assertion is explicit. It is not replaced by the much weaker image of an arbitrary morphism.')
I(414,[16],'unproved claim',[113],'partition globale',
  'Geometric applications are residue-field-compatible maps locally induced on reduced locally closed pieces; constructibility is local on a locally constructible cover and is transitive.',
  'For a quasi-compact quasi-separated domain the patch-open covering argument reduces a covering to finite data. The unresolved X|E subject prevents an unrestricted global assertion for arbitrary E.',
  'agrees','Keep all three assertions and their quasi-compactness qualification. No general commutation with inverse limits follows.')
I(415,[17],'unproved claim',[114],'foncteurs pleinement fidèles',
  'The page asserts that constructible applications between specified pairs give exactly natural transformations of their Cons functors on affine constructible models.',
  'This is restricted Yoneda for the category generated by the chosen models, conditional on the asserted affine model/refinement properties; the ambiguous ambient category is not silently enlarged.',
  'agrees','The displayed comparison is genuinely an isomorphism claim. Its missing category definitions are stated as an identification limit.')
I(416,[18,19],'unproved claim',[115],'A^{cons}',
  'For affine X=Spec A, the filtered direct limit over finite reduced locally closed affine constructible partitions of the products of section rings yields an absolutely flat envelope with patch spectrum.',
  'The universal pointwise-inverse ring T(A) is an external identification proved in the narrative, not an extra formula supplied by the manuscript. A partition of all of compact patch X by nonempty constructible pieces is necessarily finite.',
  'agrees','The bottom direct-limit expression and refinement maps fix the direction; keep the initial unsure sign as an ink flag. The published comparison is Olivier, not the w-local cover.')
I(417,[20],'withdrawn in the same text',[116],'quasi-compact',
  'The entire compactness draft on this leaf is cancelled.',
  'Its neighbouring surviving compactness results are on111 and122; sequence in the archive is not proof of chronology.',
  'agrees','A fully cancelled draft is indexed as withdrawal and is not promoted into another live claim.',{20:'withdrawn'})
I(418,[21],'title, date or page count',[118,124],'Greenberg; Néron',
  'The six numbered programme headings culminate in a disputed Néron-spaces line; scan124 is a title sheet.',
  'Pro reads a problem to pose; Codex may read thick points. Six headings are not a page count, and these leaves provide no manuscript date.',
  'overstates','The programme survives, but the explicit problem-heading reading is not secure. Retain as programme metadata and a scan flag.',{21:'corrected'})
I(419,[22,23],'unproved claim',[118,120],'Ind(Cons cpt)',
  'The diagrams propose adjunctions between schemes, constructible models, compact reduced schemes and flasque ind/pro objects, and write the usual inverse/direct-limit Hom formulas.',
  'The absolutely flat reflection and its opposite scheme adjunction are identified. Claims about the undefined flasque categories remain conditional; exchanging lim and colim without a fixed finite partition is not justified.',
  'agrees','The two sheets are stages of one categorical construction. Finite-type labels and bottom Cons|Ens are preserved rather than erased.')
I(420,[24],'unpursued implication',[122],'il est affine',
  'A quasi-compact scheme whose underlying Zariski space is Hausdorff is affine; a reduced such scheme is the spectrum of an absolutely flat ring.',
  'The page’s compact means quasi-compact and topologically Hausdorff. It does not assert that every proper scheme is affine.',
  'agrees','Read the finite affine clopen-cover and disjoint refinement proof; the earlier note’s compact terminology needs this explicit modern explanation.')
I(421,[25,26,27,28,29],'self-flagged step',[126,128],'(Ép); (Ép)′; (Ép)″; (Ép)‴; ???',
  'Four proposed thickness conditions for points of eventually affine inverse systems are compared: eventual fibre genericity, a dense-open pullback condition, constructibility of the point closure, and a constructible open part of it.',
  'Maximal in the fibre is interpreted in the generalization order, i.e. a generic point, not a closed point. Only separately proved implications are accepted; the ML/countability and ambient constructibility ambiguities remain.',
  'agrees','These entries all audit the same implication diagram. The noetherian insertion and local ideal fragment are retained as distinct subclaims and reading flags; the full equivalence is not asserted.')
I(422,[30],'unproved claim',[131],'corps résiduel k parfait',
  'Valuation-ring points and proper extension of a generic rational map are used to construct a point map between Greenberg objects.',
  'Modern Greenberg functor notation ordinarily includes completeness and chosen unramified lifts. Completeness is not explicit on the retained page. The V-point/K-point comparison must not inherit an accidental bar on X.',
  'agrees','The point construction is present. Its domain of definition and properness hypotheses are retained, without granting a morphism of schemes from a pointwise map.')
I(423,[31,32],'unproved claim',[131],'promorphisme d’indice fini',
  'Under a dominant generically separable generic-fibre map to a proper target, the page claims existence at a thick point, thickness of its image, a residue-field inclusion and a finite-index promorphism near the closure.',
  'The meaning of finite index and the full thickness hypotheses are not defined on this leaf. The residue-field assertion cannot be strengthened from the stated subfield relation to equality.',
  'agrees','The small insertions belong to the same Proposition1. They preserve existence and étale qualifications; the proposition is not upgraded to an established modern theorem.')
I(424,[33,34],'unproved claim',[132],'bornée',
  'Proposition2 claims constructible images on finitely partitioned X_K-simple pieces with a bounded invariant involving the valuation extension.',
  'Simple, the ell|d invariant, and finite index require recovery before an exact modern theorem can be matched. Greenberg approximation and motivic change-of-variables results are partial comparisons with different hypotheses.',
  'agrees','The earlier H-G finding is an external candidate, not proof of this exact statement. Merge its audit with the bounded assertion and preserve all missing definitions.')
I(425,[35],'unproved claim',[134],'abus de langage ici !',
  'The unit functor A↦A((t))× is the union of affine stages Γ_n recording a Laurent series and its inverse, both bounded below by −n.',
  'The minus sign is required by the equations and by Γ0. Coefficient convolution defines the stages; each equation involves finitely many variables.',
  'agrees','The stage construction is clear despite the i<−n|i<n ambiguity. Its representability and the scope of the notational caution are treated separately.')
I(426,[36,37],'reading question',[135],'n′ ≥ n',
  'The reduced valuation-stratum model Γ′_n→Γ_n is a closed immersion surjective on topological spaces; later stage maps preserve the underlying spaces but change nilpotent structure for strict increases.',
  'The last nonisomorphism statement requires n′>n. At n′=n the map is the identity. This is a proposed ink/inequality correction, not a changed transcription.',
  'overstates','The theorem’s scheme-theoretic comparison survives; the equality boundary as transcribed is false and flagged.',{36:'kept',37:'corrected'})
I(427,[38],'idea of the earlier run',[134,135],'a(t)b(t)=1',
  'The dual-number Laurent unit 1+εt^(−1), inverse 1−εt^(−1), lies in Γ1 and not in the zero-valuation power-series copy Γ′1 on dual-number points.',
  'This witnesses nilpotent structure. It does not refute topological surjectivity of Γ′1→Γ1, since a surjective closed immersion need not be surjective on every ring-valued point functor.',
  'agrees','Retain and rerun the earlier-run example, carefully separating topological surjectivity from functorial surjectivity.')
I(428,[39,40],'unproved claim',[136],'Hom_{ProSch/S}',
  'The comparison from pro-morphisms of eventually affine inverse systems to morphisms of their limits is asserted when target stages have finite presentation and source stages are quasi-compact.',
  'A verified modern theorem assumes quasi-compact quasi-separated source stages; the page only inserts quasi-compact. This additional hypothesis is our safe reconstruction, not silently attributed to the manuscript.',
  'agrees','Merge the proposed Greenberg application with the underlying Hom theorem; a point map alone does not supply stage morphisms or a uniform finite partition.')
I(429,[41],'unproved claim',[138],r'V_i=\mathfrak m^i/\mathfrak m^{i+1}',
  'Polynomial evaluation on a nilpotent ideal with m^(N+1)=0 depends on degree≤N; linear coefficients act on successive graded pieces, and a unit Jacobian gives invertible coordinate change on m^n.',
  'The quotient-algebra and evaluation-set interpretations are kept distinct. Local-ring determinant ∉m is equivalent to unit; det merely nonzero is not.',
  'agrees','Retain the nilpotence and localness hypotheses and the undecided determinant symbol.')
I(430,[42,44],'reading question',[140,142],'t ↦ a_0+a_1t+a_2t^2',
  'The translation/composition calculation for quadratic coordinate changes has constant, linear and quadratic terms, plus explicit cubic and quartic remainders.',
  'The linear cross coefficient is 2a′2a0a1; dropping remainders is valid for nilpotent evaluation under the stated filtration, or for augmentation-preserving jets, but not for every quotient substitution.',
  'agrees','The unfinished scan140 calculation and scan142 expansion are one computation, so they are merged and rerun symbolically.')
I(431,[43],'reading question',[142],r'\mathcal T_{X_0}',
  'The affine-space rows suggest torsors of lifts under a tangent/derivation module, but the displayed module is not defined here.',
  'For a smooth algebra and a square-zero ideal, differences between two lifts are derivations; that is the precise verified reconstruction. It does not identify every unexplained symbol on the page.',
  'agrees','Retain as an undeclared-object flag with a conditional modern comparator, not an invented theorem of the manuscript.')
I(432,[45],'idea of the earlier run',[142],'det ≠ 0',
  'The notation det≠0 cannot mean mere nonzero determinant over every base ring: t↦2t is not an automorphism of Z[t]/(t³).',
  'The open subscheme D(det) may be the intended functorial convention, in which case det is required to be a unit. The diagnostic rejects only the literal elementwise interpretation.',
  'agrees','Rerun the earlier-run test and keep the scheme-open interpretation available.')
I(433,[46],'idea of the earlier run',[142],'t+ε',
  'For A=Q[ε]/(ε³), t↦t+ε fails to preserve (t³), since (t+ε)³=3εt²+3ε²t modulo ε³,t³.',
  'This does not obstruct translation on the nilpotent ideal itself; it distinguishes the evaluation action from automorphisms of the naive truncated polynomial algebra.',
  'agrees','Retain and rerun the earlier-run counterexample with every quotient relation checked.')
I(434,[48],'other',[119,121,123],'algèbre extérieure',
  'The reused typescript develops exterior algebra of a direct sum, component decompositions, nilpotence, intersection criteria and the ordered basis of wedges.',
  'Printed page90 is scan119, page92 scan123 and page93 scan121; chronological order of archive scans is not the printed argument order.',
  'agrees','Retain the genuine algebra results as reused typescript material rather than presume new Grothendieck discoveries.')
I(435,[49],'idea of the earlier run',[119,121,123],r'\bigwedge(M\oplus N)',
  'The earlier run proposes transporting a Lefschetz-ring comparison through the natural exterior direct-sum isomorphism.',
  'The supplied leaves provide that map but no Lefschetz operator, polarization, or theorem about the WG2 project. The project comparison remains an unverified lead.',
  'agrees','The algebraic map is checked; the cross-project conclusion is neither asserted nor upgraded.')
I(436,[50],'other',[127],'dρ+ρd',
  'The cohomology-vanishing exercise uses an operator homotopic to zero that is invertible on the cochain complex.',
  'The sufficient chain-homotopy statement is clear. The Lie algebras, representation and invertibility hypotheses are missing from this isolated exercise fragment; general Lie-cohomology vanishing is not claimed.',
  'agrees','Keep the exercise as a source fragment with a fully stated conditional proof, not an unconditional vanishing theorem.')
I(437,[51],'other',[129],'p-dérivation',
  'The reused exercises treat restricted enveloping algebras, restricted PBW bases, universal properties and restricted derivations in characteristic p.',
  'PBW basis statements require the Lie algebra to be free over the base as specified; centrality of x^p−x^[p] and associative commutators prove the displayed structural claims.',
  'agrees','The characteristic and freeness conditions are retained; the exercise context is kept distinct from manuscript conjectures.')
I(438,[52,53],'other',[139,141],'1+X_1^p',
  'The formal law F(X,Y)=(X1+Y1+X1Y1, X2+(1+X1^p)Y2) in characteristic p is noncommutative but has abelian Lie algebra.',
  'The p=2 quadratic-quotient calculation is the earlier run’s diagnostic, not a separate general theorem. Associativity follows from Frobenius, and noncommutativity first occurs in degree p+1.',
  'agrees','Merge the exercise with the exact earlier-run truncation test while labelling their provenance separately.')
I(439,[54],'reading question',[139,141],'groupe symplectique formel à 2n variables',
  'The symplectic matrix Lie algebra satisfies XᵀJ+JX=0 and has dimension n(2n+1); for n=1 it has dimension3.',
  'Variables in the textbook phrase denotes the degree of the matrix representation: scan141 similarly calls GL(n) a group in n variables and explicitly gives dimension n². It need not mean formal coordinate dimension.',
  'overstates','The dimension computation is correct, but its use as an ink-error suspicion is weakened decisively by the neighbouring GL convention.',{54:'corrected'})
I(440,[55],'reading question',[141],'v → D(v∘F)',
  'A formal group homomorphism induces the tangent map at the identity; its Jacobian follows the explicitly stated row/column convention.',
  'Apply the derivation at the identity and then extend the resulting tangent vector invariantly. Without evaluation, D(v∘F) is a function on the source, not a scalar-valued derivation on the target.',
  'agrees','Retain the missing evaluation and n/m inconsistency as reading/convention questions, without reversing the author’s row convention.')
I(441,[56],'other',[143],'U=(I−R^{-1}S)^{-1}(I+R^{-1}S)',
  'The reused exercise gives the Cayley chart between skew matrices S and the orthogonal group, the inverse S=R(U−I)(U+I)^{-1}, and the induced formal composition.',
  'Work over a field of characteristic≠2 with invertible symmetric R, on the determinant-open chart. The final off-leaf continuation and blank textbook references are not supplied.',
  'agrees','Both rational inverse maps and the orthogonality identity are checked; the continuation remains outside the supplied source.')
I(442,[57],'idea of the earlier run',[131],'propre sur V',
  'The earlier run proposes comparing the span X(V′)→X(K′), X(V′)→X(k′) with FLAGGED149 point/fundamental-group constructions.',
  'Only the left-hand manuscript span is available. Full FLAGGED149 definitions and maps are absent, so no claim of equivalence or change of problem status is justified.',
  'agrees','Keep the lead in the separate our-projects table, with explicit endpoint unavailability.')
I(443,[58,59,60],'other',[99,100,101,102,107,110,118,124,126,128,131,132,134,135,136,138,142], '',
  'Editorial planning, open-entry status and proposed task lists summarize earlier notes and external registers.',
  'These are not additional authorial claims. They duplicate the mathematical items already indexed; named project sources not supplied here remain unchecked.',
  'agrees','All three sections were read through their tables and final paragraphs. Merge as editorial context and preserve their proposed links and directions without phantom claims.')

def write_items():
    (P/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    with (P/'entries.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(sorted(entries,key=lambda r:int(r['entry_id'].split('#')[1])))
    note=(ROOT/N).read_text().splitlines(); hs=[i+1 for i,l in enumerate(note) if l.startswith('### ')]; hs.append(len(note)+1)
    with (P/'reading_log.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['entry_id','source_file','line_start','line_end','reason'])
        for item in items:
            for eid in item['sources']:
                q=int(eid.split('#')[1]);w.writerow([eid,N,hs[q-1],hs[q]-1,'Read entire indexed entry before writing the explicit verdict.'])
                for s in item['scans']:w.writerow([eid,T,*bands[s],'Read cited passage in full, including cancellations, insertions and margin; compared the note’s claim with this text.'])
        w.writerow(['all assigned entries',D,1,len((ROOT/D).read_text().splitlines()),'Read the complete doubts table; no scan available, so no reading is decided.'])
        for k in ['K91-08','K91-09','K91-10']:
            for typ,ext in [('SA03_notes','notes.md'),('SA03_texts','transcription.tex')]:
                p=f'source/{typ}/codex/{k}_{ext}'; w.writerow([k+' lead (no verdict row)',p,1,len((ROOT/p).read_text().splitlines()),'Read complete independent transcription/lead; used to expose conflicts, not to overrule the frozen Pro source.'])

write_items()
if __name__=='__main__':
    assert len(entries)==60 and len({e['entry_id'] for e in entries})==60
    print(f'Explicitly authored items: {len(items)}; indexed verdicts: {len(entries)}; all entry numbers1–60 covered.')
