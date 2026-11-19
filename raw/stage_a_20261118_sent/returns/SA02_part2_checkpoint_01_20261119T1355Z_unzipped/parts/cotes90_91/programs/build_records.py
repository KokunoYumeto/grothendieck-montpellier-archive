"""Serialize manually researched records. No mathematical verdict is inferred by code."""
from pathlib import Path
import csv,json,re,hashlib

ROOT=Path('/workspace/scratch/95cd10054c54')
OUT=ROOT/'SA02_work/parts/cotes90_91'
PKG='MPL_90+91_002-018'
PRO='source/SA02_texts/pro/'+PKG+'_transcription.tex'
NOTE='source/SA02_notes/pro/'+PKG+'_notes.md'

def dump(name,data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

def table(name,headers,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(headers);w.writerows(rows)

passages={}
for file in [ROOT/PRO]+sorted((ROOT/'source/SA02_texts/codex').glob('K9*_transcription.tex')):
    lines=file.read_text().splitlines();cote=None;starts=[]
    for i,line in enumerate(lines,1):
        m=re.search(r'\\cotefile\{(\d+)\}',line)
        if m:cote=m[1]
        m=re.search(r'\\scanpage\{(\d+)\}',line)
        if m:starts.append((cote,int(m[1]),i))
    for j,(c,s,a) in enumerate(starts):
        b=starts[j+1][2]-1 if j+1<len(starts) else len(lines)
        passages.setdefault((c,s),[]).append(f'{file.relative_to(ROOT)}:L{a}–L{b}')

def loc(cote,scans,pro=True):
    result=[]
    for s in scans:
        c,s=(str(cote),s) if not isinstance(s,str) or '/' not in s else s.split('/')
        ls=passages.get((c,int(s)),[])
        result+=ls if not pro else sorted(ls,key=lambda z:('/pro/' not in z,z))
    return result

items=[];entries=[]
def I(n,source_n,kind,cote,scans,words,statement,reconstruction,check,reason,verdict='kept'):
    if isinstance(source_n,int):source_n=[source_n]
    ident=f'SA02-{n}'
    items.append(dict(id=ident,sources=[f'{PKG}#{x}' for x in source_n],kind=kind,cote=str(cote),scans=scans,
                      lines=loc(cote,scans),his_words=words,statement=statement,reconstruction=reconstruction,
                      check=check,check_reason=reason))
    for j,k in enumerate(source_n):
        entries.append([f'{PKG}#{k}',ident,verdict if j==0 else 'merged into '+ident,reason])

I(500,1,'other','90,91',['90/2','91/2','91/3'],'[Editorial citation key, not an authorial mathematical statement]',
  'The Pro notes distinguish source witnesses, external project excerpts and modern references. The stated archival evidence is a mixed sequence, not a continuously dated treatise.',
  'The present run checks actual supplied sources. Unseen context packets and findings cards remain external leads; their earlier verdicts are not adopted. The 11 September 1967 letter dates that letter only.',
  'agrees','Citation conventions are retained; external endpoints are unavailable and are not counted as checked links.')
I(501,2,'unproved claim',90,[2],'Cond. équivalentes a) b) c) d)',
  'For a flat module M over a nonfield Dedekind domain A, the manuscript equates finite saturation of every finite submodule, exclusion of each A^(p), absence of K in each M_p, and a union of finite saturated submodules; separating A-linear forms suffice and are asserted necessary for countably generated M.',
  'The equivalence is false: over Z, M=sum over primes p of (1/p)Z has all local p-heights bounded by one, but saturation of Z is the nonfinite module M. The surviving a–d and countable projectivity implications are separated in CL-SA02-501.',
  'understates','The note identifies the hypotheses but stops at an unproved package; a hypothesis-checked counterexample refutes b,c⇒a,d. Pro/Codex ambiguity in the word before module does not rescue this example.','corrected')
I(502,3,'self-flagged step',90,[4],"faire l'argument",
  'Under finite saturation for B, the coordinate coalgebra of a flat affine group over a Dedekind domain, each finite submodule lies in a finite saturated subcoalgebra. The two one-sided coaction conditions must survive saturation.',
  'Saturation is a kernel with torsionfree quotient; flatness gives the required tensor intersections. This implication uses the finite-saturation hypothesis itself, not the false equivalence in the preceding lemma.',
  'agrees','The deferred parenthesis is explicit. Unequal tildes are retained as a reading issue; the saturation argument is independently supplied.')
I(503,4,'unpursued implication',90,[6],'N engendre l’algèbre B',
  'If the group is also of finite type and its coordinate module has the preceding finite-saturation property, a finite projective stable algebra-generating submodule yields a faithful linear representation after every base change.',
  'Faithfulness means trivial kernel on every algebra-valued point; it does not imply surjectivity or faithful flatness onto the entire general linear group.',
  'agrees','The proof explicitly tests points over arbitrary A-algebras, and the finite-type assumption is present.')
I(504,5,'unproved claim',90,[6],'syst. projectif strict',
  'Every affine group scheme over a field is an inverse limit of finite-type affine group schemes with faithfully flat transition maps.',
  'Finite Hopf subalgebras and faithful flatness over Hopf subalgebras, rather than finite subcoalgebras alone, are needed for this reconstruction.',
  'agrees','The correction from inductive to projective and the explanation of strictness are explicit; topological-group limits on 91/98–102 are distinct.')
I(505,6,'unproved claim',90,[8,10],'i-admissible',
  'For a directed union B=colim B_i of finite projective saturated subcoalgebras, finite B-comodules factor through a B_i; comodules over B_i correspond to modules over U_i=B_i^∨, with the stated restriction transitions.',
  'Factorization for a finite module uses finitely many coaction coefficients and preservation of injectivity by the saturated stages; coassociativity and counit give the U_i action.',
  'agrees','The dual-algebra mechanism and admissible categories are on the page. The first unclear category label is not used to change the definition.')
I(506,7,'unproved claim',90,[10,12],'projectif de t.f.',
  'A finite comodule over these Dedekind coalgebra stages is a quotient of a comodule finite projective over the base. A relative variant assumes ordinary finite quasi-coherent modules have finite locally free covers.',
  'A finite U_i-module admits a surjection U_i^r; U_i is finite projective as an A-module. The relative continuation must specify which S or S′ is the base.',
  'agrees','The finite-type input is written here, unlike the broader sentence on 90/16; the change of base letter remains a reading alarm.')
I(507,8,'reading question',90,[10],'si G est de t.f.',
  'The identification of the module criterion with nonempty fibres of every irreducible component is explicitly restricted to G of finite type over the Dedekind base.',
  'This is a scope correction to the quoted external finding, not an authentication of its unseen counterexample or a proof of the equivalence. Components after base extension and the module condition must be matched exactly.',
  'agrees','The finite-type phrase is explicit. An external refutation deleting it does not address this written assertion.')
I(508,[9,45],'withdrawn in the same text',90,[6,14],'fidèlement plat',
  'The cancelled 90/14 proposition claims that the representation on a finite stable generating module maps G faithfully flatly onto Aut(N). The live 90/6 conclusion is only faithful representation.',
  'The earlier run’s test G_m acting on span(1,t,t^-1) gives diag(1,z^-1,z), a proper closed subgroup of GL_3. Its algebra map kills an off-diagonal coordinate, so it cannot be faithfully flat.',
  'agrees','The whole stronger proposition is deleted. The counterexample is rechecked and applies to that withdrawn wording only.')
I(509,10,'unproved claim',90,[14,18,20,22,24],'un plus petit sous-module',
  'Under the stated finite locally free coalgebra-stage hypotheses, a quasi-coherent submodule F of a G-equivariant E has a smallest stable quasi-coherent envelope in E; flat base change is claimed to commute with it. Later versions use a G-linearized relatively ample invertible sheaf.',
  'Different base, quasi-compactness and resolution hypotheses belong to different versions. Mere flatness of the coordinate coalgebra is insufficient; the finite-stage/projectivity hypotheses are retained.',
  'agrees','The envelope is nontrivial for an arbitrary submodule, not a submodule already known G-stable. The note correctly distinguishes this.')
I(510,[11,44],'reading question',90,[10,12,16],'tt O_X-G-module',
  '90/16 asserts a finite locally free equivariant quotient for every equivariant module although its hypothesis supplies such covers only for finite-type modules.',
  'The earlier run’s counterexample is S=X=Spec(k), G trivial, E a countably infinite direct sum of k. Every map from k^r has finite-dimensional image. The finite-type formulation is the plausible repair, not an emendation.',
  'agrees','The literal unrestricted conclusion is false; the point example checks every stated hypothesis and does not attack 90/10–12.')
I(511,12,'withdrawn in the same text',90,[14,18,20],'Si S qu. cpt qu. sép.',
  'The drafts place quasi-compactness and quasi-separatedness on different objects; one version involving S is deleted, and a later version requires covers by finite locally free base modules.',
  'No single theorem is obtained by combining selected clauses from all drafts. Each surviving version is tracked with its hypotheses; scan order supplies no date.',
  'agrees','The cancellation and revised hypotheses are visible in the transcriptions and cannot be silently combined.')
I(512,13,'unproved claim',90,[20,22],'ils sont adjoints',
  'For the relatively ample line bundle, the graded-section functor E↦⊕_n f_*(E⊗L^n) is left exact; graded sheafification is exact, left adjoint to sections, and its counit identifies the original quasi-coherent sheaf. Sections are therefore fully faithful in the specified setting.',
  'This is the standard section/sheafification adjunction for the ample construction; it is unrelated merely by terminology to an external Lefschetz graded-ring programme.',
  'agrees','The two exactness assertions concern different functors and are not contradictory.')
I(513,14,'unpursued implication',90,[22],'d’où par minimalité lui est égal',
  'The stable envelope of a graded submodule is the direct sum of the stable envelopes of its homogeneous pieces; functoriality with respect to multiplication then makes it a graded module over the section algebra.',
  'The equality follows from two containments and minimality. Algebra-module stability is a second step, not a consequence of grading alone.',
  'agrees','The bracketed proof supplies this distinction; no missing index is silently added to the transcription.')
I(514,15,'self-flagged step',90,[24],'Rédiger mieux',
  'After twisting a finite-type F, finitely many sections generate it. The finite stable hull of their degree piece generates the proposed sheaf envelope, giving finite generation.',
  'The equality with the minimal envelope uses stable generation and the two containments; the chosen sections and the ample-generation hypothesis must be retained.',
  'agrees','The rewriting request is explicit and is not evidence of a disproved argument.')
I(515,16,'reading question',90,[14,18],'F′ de F; F′ de E',
  'The first version places a containing stable envelope inside F; the later version places it in E and contains F.',
  'The latter is the coherent mathematical formulation. The former is listed for scan review and is not edited.',
  'agrees','The two witnesses differ exactly in the ambient module.')
I(516,17,'unproved claim',90,[3,5],'le th. de Hartshorne',
  'A flat local morphism of noetherian local rings with geometrically reduced fibres has connected generic fibre, and remains connected after deleting a closed subset above a proper closed base subset, when the base is geometrically unibranch, or unibranch with primary residue extension.',
  'The reused EGA sheets include a punctured-spectrum reduction using depth. Missing inequality signs, the Japanese replacement and the formal-fibre corollary are kept separate.',
  'agrees','This is an independent EGA strand on the reused pages, not an equivariant-generation step.')
I(517,18,'withdrawn in the same text',90,[7,9,15],'séparés inutile !',
  'Under the hypotheses of the preceding EGA completion result, base change is fully faithful on all étale schemes. The separated target case is followed by descent of the open graph in the general case.',
  'The extension from separated targets uses descent of the graph and descent of isomorphisms; it does not claim equivalence or essential surjectivity.',
  'agrees','Both the obsolete separated formulation and the general graph argument are supplied.')
I(518,19,'withdrawn in the same text',90,[9],'il est possible que',
  'A cancelled remark inserts characteristic zero of the residue field, but stops after “induit” without the asserted conclusion.',
  'No essential-surjectivity or equivalence claim can be recovered. Only a cancelled expectation and the need for a continuation are established.',
  'agrees','An incomplete sentence is not turned into a conjecture with an invented conclusion.')
I(519,20,'unpursued implication',90,[11,13,17,19,21,23,25],'Les démonstrations sont les mêmes',
  'The reused EGA drafts construct ordinary and strict henselization and discuss universal properties, finite/integral semilocal base change, faithful flatness, regular fibres, reducedness, normality, associated primes and unibranchness.',
  'Ordinary and strict henselization differ in their residue extension and the relevant unibranch/geometrically-unibranch condition. Their individual theorem statements are split in the claims map.',
  'agrees','Parallel passages are genuine; local hypotheses are not literally identical and are not flattened into one theorem.')
I(520,21,'self-flagged step',90,[13,19,21],'?; peu clair; mélange !',
  'The draft queries a reduction involving (18.8.7.1) and proof transitions between filtered Artinian rings and finite/profinite spectra.',
  'The uncertain marginal words remain uncertain. A noetherian profinite Hausdorff space is finite by compactness and discreteness; the corresponding ring assertion still needs its stated flat/injective transition hypotheses.',
  'agrees','The question marks are recorded, while proof checks separate topological finiteness from algebraic finite length.')
I(521,22,'withdrawn in the same text',90,[23,25],'la forme hybride',
  'A semilocal/hybrid universal property is deleted and criticized in a margin. The subsequent local henselian adjunction is a different, completed formulation.',
  'No mixed source/target category is supplied by inference. The cancelled fragment is unidentifiable as a complete theorem.',
  'agrees','The overall deletion remains part of the item; a later categorical analogy does not reinstate it.')
I(522,23,'unproved claim',91,[5],'Dans le cas d’un monomorphisme',
  'For a monomorphism Y→X with X flat of finite type over a locally noetherian S, the relative section/equality subfunctor is analyzed by eight representability tests; flatness supplies the injectivity needed in the Artinian base test.',
  'The closed immersion specialization has a direct published counterpart in Murre’s Theorem 3; not every unfinished general monomorphism variant follows automatically.',
  'agrees','The numbered tests and flatness argument are actually on the page; the criterion as a whole is not proved there.')
I(523,24,'withdrawn in the same text',91,[6],'Théorème … Pour',
  'A deleted draft begins with a flat finitely presented source and a finitely presented closed subscheme, then stops before its conclusion.',
  'It is not evidence that the noetherian hypotheses of the preceding theorem were removed.',
  'agrees','The fragment remains distinct from the live theorem.')
I(524,25,'unproved claim',91,[7],'En fait; ess. libre',
  'For closed subschemes the local extension condition is strengthened toward properness of the equality functor, and the generic condition is reduced to essential freeness.',
  'The argument points to EGA IV §11; it must retain schematic density and the chosen open neighbourhood, rather than only pointwise equality.',
  'agrees','The stronger condition and the unfinished reduction are both present; the lower cancelled corollary is not a live theorem.')
I(525,26,'reading question',91,[8],'voisinage … de la fibre spéciale',
  'Condition L is compared with commutation with adic limits, but the neighbourhood phrase and valuation reduction contain uncertain words.',
  'The later source Murre distinguishes the closed-fibre neighbourhood condition from the generic condition; it motivates scan review, not emendation.',
  'agrees','Neither later condition R nor constructible-topology terminology decides the unclear word.')
I(526,27,'withdrawn in the same text',91,[8,9],'tout sous-groupe ouvert',
  'Condition R in the live formulation says that over every local S-scheme an open subgroup containing the special fibre is the whole group. The additional “closed” and the name π0-rigid are deleted. A DVR testing reduction is stated under finite-type/noetherian hypotheses.',
  'The open-and-closed test on 91/8 and the live open-only definition are separate formulations.',
  'agrees','The note correctly keeps the deleted word and scope of testing visible.')
I(527,28,'unproved claim',91,[8],'fibres connexes',
  'Connected fibres suffice for the asserted condition, as does a family of finite S-schemes whose geometric-fibre translates by the identity component cover G.',
  'The family is not stated finite and its members are schemes, after a correction from groups. The precise hypotheses inherited by the second assertion are retained.',
  'agrees','The manuscript is broader than a finite family of subgroup schemes; the raised sign still requires scan review.')
I(528,29,'withdrawn in the same text',91,[9,10],'fermé si G est séparé sur S',
  'For u:H→G, with H flat finite type satisfying R and the locally noetherian assumptions of the surrounding criterion, the centralizer is a subscheme; it is closed when G/S is separated.',
  'The all-closed formulation on 91/9 is deleted. Target separatedness supplies the closed diagonal in the equality condition.',
  'agrees','The live corollary contains the repair; no claim of unconditional closedness survives.')
I(529,30,'unproved claim',91,[10],'Transp; Norm',
  'The page distinguishes an inclusion transporter from an equality/isomorphism transporter and deduces a normalizer under further flatness, R and immersion assumptions.',
  'The uncertain decoration is not silently identified. The two functors must be distinguished by containment versus equality after conjugation.',
  'agrees','Different hypotheses and conclusions are written; a generic transporter label would lose scope.')
I(530,31,'self-flagged step',91,[11],'Il faudrait également moduler',
  'The author requests variants removing noetherian assumptions and a corresponding modification of the preceding theorem.',
  'Later finite-presentation inserts are evidence for individual variants, not a proof of a universal removal.',
  'agrees','This is an explicit task; the displayed theorem still assumes a locally noetherian base.')
I(531,32,'unpursued implication',91,[11,12],'commute aux limites projectives adiques',
  'For finite-type X over locally noetherian S and coherent F, the flatness subfunctor is represented by an unramified locally finite-type scheme exactly under the adic commutation test; properness suffices.',
  'The manuscript’s flatness and faithful-flatness variants and E/F letter changes are tracked separately. Murre §3(A), Theorem 2 and Corollary 1 are an exact comparator for the coherent-flatness formulation.',
  'agrees','The published comparison is reopened and checked; it is not substituted for the manuscript wording.')
I(532,33,'reading question',91,[12],'fibre générique',
  'The literal condition L says generic fibre and the margin specifies a singleton associated-point condition with an uncertain adjacent adjective.',
  'A special-fibre neighbourhood and one associated prime agree with Murre’s corresponding tests. This is mathematical evidence for scan review only.',
  'agrees','Generic/special reverses the local condition and is a high-weight unresolved reading.')
I(533,34,'reading question',91,[12],'f′ imm; imm|mono',
  'The factorization corollary alternates immersion and a doubtful immersion/monomorphism reading; it relates a faithfully flat factor followed by an inclusion to flatness of a kernel-pair projection.',
  'Murre §3(A), Corollary 2 has a monomorphism. The exact hypothesis on X/S and both projection labels must be retained.',
  'agrees','The published theorem supplies a comparator without deciding the strokes.')
I(534,35,'unproved claim',91,[13],'le quotient X/R',
  'A factorization, when it exists, is unique as the fpqc sheaf quotient by the kernel pair; existence is reduced to the flatness locus and descent of finite-presentation data.',
  'The quotient-category statement and existence are separate. Arbitrary image factorizations are not asserted.',
  'agrees','The proof mechanism is visible but compressed; modern algebraic-space images cannot be identified with schemes without further hypotheses.')
I(535,36,'unproved claim',91,[14],'formellement principal homogène',
  'For the finitely presented formally principal homogeneous object in the corollary, a unique base subfunctor S′→S is asserted so that P→S′ is faithfully flat and a torsor.',
  '“Formally principal homogeneous” is a pseudo-torsor condition, not an assertion that sections already exist. The topology is the fpqc/fppf quotient context.',
  'agrees','The cancelled noetherian wording is preserved; no arithmetic μ2 classification is inferred.')
I(536,37,'unproved claim',91,[14],'N=Ker u … plat',
  'A finitely presented group homomorphism with flat kernel has the represented quotient G/N and its monomorphism to the target under the preceding factorization hypotheses.',
  'Murre’s application gives the finite-type locally noetherian version. The finite-presentation extension must be checked by descent, not attributed to that wording unchanged.',
  'agrees','The quotient assertion is written without a construction; the exact published specialization is distinguishable.')
I(537,38,'unproved claim',91,[16,17,18,19,20,21,22,23,24,25,31,32],'représentable par morphismes non ramifiés',
  'For proper flat X,Z over S, a map i:Z→X and a separated finite-presentation target Y, precomposition Hom(X,Y)→Hom(Z,Y) is represented by unramified morphisms on the open locus where the infinitesimal restriction is injective, equivalently M_v→M_u is surjective.',
  'The Pro range gives only the start; Codex 19–25 continues the proof with admitted compatibilities and a second obstruction construction. The dated letter on 31–32 restates the result.',
  'understates','Later supplied Codex leaves were absent from the old note’s evidence. They must be incorporated; they do not by themselves erase every proof gap.','corrected')
I(538,39,'unproved claim',91,[16,19,20,23,24,25],'Modules cohérents M_u,M_v',
  'The deformation Hom functors in a base module J are corepresented by coherent base modules, compatibly with base extension; precomposition induces M_v→M_u.',
  'The coherent Hom functor represented by a vector-type affine scheme is related but not identical until its additivity identifies the corepresenting module. This identification is part of the reconstruction.',
  'agrees','The critical module construction is explicitly asserted; a fibre-dimension argument alone would not establish base-change compatibility.')
I(539,[40,47],'unpursued implication',91,[16,17],'par Nakayama',
  'Once M_v→M_u is constructed, its surjectivity locus is the complement of the support of its finitely presented cokernel and is universal under base change.',
  'The earlier run’s presentation-matrix test is rechecked: if A^n→A^m→C→0, the locus C=0 is the union of principal opens of all maximal m×m minors, with the usual conventions for m=0 and n<m.',
  'agrees','This proves the open-locus step conditionally on the modules; it is not a proof of the entire Hom theorem.')
I(540,41,'unproved claim',91,[16,17],'réduction … immédiate',
  'The author asserts reductions to Artinian or noetherian bases, with a possible reservation in the margin. Pro and Codex differ in the local adjective.',
  'Limit descent must carry X,Z,Y,i and the module map, including the surjectivity condition. The uncertain “sans doute” is not a secure independent objection.',
  'agrees','The reductions are asserted rather than proved and remain attached to their specific finite-presentation hypotheses.')
I(541,[42,48],'self-flagged step',91,[18,19,20,21,23,24,25],'Nous admettrons',
  'The lift problem over a nilpotent ideal compares pseudo-torsors with their acting Hom groups. Codex 19–21 admits compatibility equalities; 23–25 revises the obstruction quotient.',
  'The earlier run’s algebraic square is valid when V→U is surjective and J→J_t injective: Hom(U,J)=Hom(V,J)×_{Hom(V,J_t)}Hom(U,J_t). Nonemptiness of the pseudo-torsors is an additional issue. The later quotient must use the image of the kernel of the compatibility map.',
  'understates','The old assertion of no supplied continuation is corrected by reading Codex 19–25. A group-square identity does not establish existence of a point in an empty pseudo-torsor.','corrected')
I(542,43,'unpursued implication',91,[16,26,31,32],'Énoncer plutôt en termes de',
  'The margin asks for a relative-product version and suggests that a nearby hypothesis can be omitted when Z→X is surjective; the later section-functor theorem and letter are related formulations.',
  'The marginal attachment is unresolved. In particular, the separatedness conclusion on 26 cannot hold for arbitrary nonseparated P; the letter includes separatedness explicitly.',
  'agrees','The relative formulation is real; the exact omitted hypothesis must not be guessed.')
I(545,46,'idea of the earlier run','90,91',['90/2','90/10','91/8','91/9'],'toutes ses fibres sont non vides; U=G_T',
  'For R=k[t]_(t), G=Spec(R)⊔Spec(k(t)) is the open subgroup of constant C2 retaining only the generic point of the nonidentity component. It is flat affine finitely presented, fails R, and B=R×K has a nonfinite saturated hull of 0×R.',
  'The component misses the special fibre. This simultaneously illustrates the two obstructions and is consistent with the finite-type component criterion; it does not refute it.',
  'agrees','The earlier run’s construction and every relevant hypothesis are independently checked.')
I(548,49,'idea of the earlier run',91,[16,17,35,36],'[Editorial modern comparison]',
  'Modern proper-flat-source Hom functors are algebraic spaces locally of finite presentation when the target is separated and finitely presented. This supplies an ambient setting for the manuscript’s unramified restriction map.',
  'Scheme representability of the ambient Hom functor and representability of the restriction morphism are different. The nonprojective obstruction on 35 and elementary nonfinite section example on 36 reinforce this distinction.',
  'agrees','The Stacks hypotheses and target category are reopened and checked; no blanket scheme theorem is inferred.')
I(549,50,'other',91,[16,18,114,120,136,142],'[Editorial comparison of Hom functors]',
  'The deformation Hom groups, geometric morphism functors, categorical Ind/Pro Hom formulas and affine spaces of polynomial lifts are four distinct constructions in the supplied cote.',
  'The actual Codex endpoints were read. Common notation does not identify their hypotheses or provide a transfer of representability.',
  'agrees','The earlier caution is retained and the endpoints now present in the source archive are checked.')
I(550,51,'other','90,91',['90/2','90/14','91/3','91/81','91/124'],'[Editorial planning comparison]',
  'The planning labels K_G(X), nonprojective representability and Greenberg–Néron concern genuine themes of these pages. Other context projects about residues, Lefschetz rings, arithmetic sections or S19 are not established by the passages.',
  'This is a bounded thematic mapping. External project endpoints are absent and are recorded as unverified leads only.',
  'agrees','Planning vocabulary is not promoted to mathematical results.')
I(551,52,'other','90,91',['90/2','90/10','90/14','91/9','91/16','91/19','91/25'],'[Editorial five-finding table]',
  'The five Hua cards named in the Pro notes concern components, saturated subcoalgebras, equivariant envelopes, condition R and relative unramified Hom.',
  'Only their quoted descriptions are supplied, not the underlying cards or verdicts. The manuscript finite-type phrase and the later Codex continuation correct source-bounded descriptions; no external project status is authenticated.',
  'understates','The table’s own caution is sound, but this run can add the supplied continuation and a counterexample to Lemma1. External finding endpoints remain unverified.','corrected')
I(552,53,'other','90,91',['90/6','90/21','91/8','91/14'],'[Editorial three-open-entry table]',
  'LM7 E.23, FLAGGED_149 B9 and LM1 D.11 are named in the prior context table as open. These pages contain no proof or counterexample to their exact external arithmetic formulations.',
  'Their inherited status is reported only as the earlier run’s claim, not retained as a verified present status. Their unsupplied source endpoints are explicitly unverified.',
  'overstates','“Retain Open” cannot be a current independent verdict without the underlying sources; the records are kept solely as contextual leads.','corrected')

assert len(entries)==53
assert len({r[0] for r in entries})==53
entries.sort(key=lambda r:int(r[0].split('#')[1]))
dump('items.json',items)
table('entries.tsv',['entry_id','item_id','verdict','reason'],entries)
table('passage_index.tsv',['cote','scan','locator'],[(c,s,l) for (c,s),ls in sorted(passages.items()) for l in ls])
print(f'Stage1 serialized: {len(entries)} source entries; {len(items)} manually authored items.')
