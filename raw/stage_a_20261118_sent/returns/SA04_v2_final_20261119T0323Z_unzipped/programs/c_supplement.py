"""Write manually authored reading, reference, link and search registers for part C."""
from pathlib import Path
import csv,json,re,sys
import c_build as c
OUT=c.OUT; DAY=c.DAY

def tsv(name,fields,rows):
    with (OUT/name).open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

reading_rows=r'''
93|221|P93:15|Characteristic-zero hypothesis is questioned.|Retain the circled question; formal de Rham exactness needs characteristic zero in ordinary power series.|The coefficient of x^(p-1)dx cannot be a derivative in characteristic p; C-SA04-414.|High: changes exactness.|High mathematical diagnosis; ink unresolved.
93|221|P93:26|Logarithmic derivative appears closed without a retained group qualification.|A commutative-group premise may precede this fragment; otherwise use Maurer-Cartan with its bracket.|The bracket identity in analysis.md §2.1 distinguishes the cases; C-SA04-401.|High, but preceding context absent.|Medium.
93|227|P93:153-161|Annihilating operator gives zero on an open arc.|Closed cycle, or an endpoint-difference term, would give a valid statement.|Product family, dx, D=1, endpoints0,1 gives1; C-SA04-406. This may be a mathematical slip rather than mistranscribed ink.|High.|High diagnosis; no palaeographic conclusion.
93|229|P93:181|A lift can make two arbitrary sections horizontal.|Require disjoint sections or matching tangent velocities at intersections.|a(s)=0 and b(s)=s force incompatible velocities; C-SA04-409.|High.|High diagnosis; ink unresolved.
93|230|P93:208-220|The relative-closed to absolutely-closed implication is deleted.|Preserve the deletion rather than restoring the implication.|s dx pulled back by x=t has differential ds wedge dt; C-SA04-411.|High for status attribution.|High deletion in transcription; scan not inspected.
93|232|P93:270-271|The target differential-form degree is doubtful.|The next differential after degree1 should land in degree2.|The complex and the following ker(d1) map require consecutive form degrees.|High for types.|Medium.
93|235|P93:384-393|u,v,h,k have conflicting domains and additive/multiplicative formulas.|The additive repair is u(p+g)-u(p)=d_H k(g), with u in closed degree0 and k in degree minus1.|Every term is then well typed and the torsor roof works; C-SA04-421. This is an audit reconstruction.|High.|High type alarm; exact ink unresolved.
93|235-236|P93:416,427-432|G and Gbar are captioned degrees0,1, then mapped to H^-1,H^0.|Degrees minus1,0 resolve Z in degree0.|Local splitting of the extension makes the degree calculation explicit.|High.|High.
93|236|P93:442-449|A boxed universal isomorphism O to RHom(Kprime,Kdoubleprime).|A morphism, with the preceding quasi-isomorphism only on the resolution of O.|Rank2 inputs give rank4 Hom; C-SA04-423, refined421.|High.|High mathematical; sign/arrow ink unresolved.
93|234|P93:363-373|The contracting-homotopy formula may be confused in contextual notes with Cartier.|Cartan contraction is the operation; retain the displayed chain degrees.|The identity is L_D=d i_D+i_D d in the square-zero setting.|High conceptual distinction.|High.
161-5|10|P93:690|Red M=I_alg omits a neutral-component marker.|M=(I_alg)^0 is the plausible qualified comparison.|A finite ramified quadratic character has trivial Hodge-Tate cocharacter but nontrivial finite inertia image; C-SA04-431.|High.|High diagnosis; missing ink not assumed.
161-5|16|P93:898|Strict valuation threshold.|Do not replace < by <=.|2x+x^2 at x=-2 cancels at the boundary; C-SA04-438.|High.|High.
161-5|17|P93:963|Lubin bibliography says1961.|Located publication is1967; could be a printed typo or a transcription discrepancy.|Opened Annals publisher record, vol85 pp296-302, DOI10.2307/1970443.|Medium bibliographic.|High external date; ink unresolved.
161-5|21|P93:1062|Weight-zero summand lacks a clear C subscript.|Restore a C-scalar-extension marker only if the scan supports it.|The displayed decomposition lives in a C-vector space.|Medium.|Medium.
161-5|23|P93:1127-1135|Superscripts naming the Hodge-Tate category and its two-weight part are doubtful.|Keep the two category levels distinct without choosing the letters.|The generating category at1145 has more objects than the Barsotti-Tate image.|High for domain.|Medium.
161-5|23-24|P93:1115-1124,1191|K and L reverse roles in the field tower and scalar extension.|Determine the field convention locally before normalizing the formula.|A tensor product over the larger field cannot be formed from the displayed smaller-field vector space without extra structure.|High.|Medium.
161-5|23|P93:1148|Geometric-base-point fibre could be read with Omega coefficients.|The Tate-module fibre is a finite-dimensional Qp representation; later coefficient extension is separate.|The source distinguishes the two fibre functors.|High.|High.
161-5|24|P93:1189,1195|Frobenius isomorphism and grading are inserted beside a deleted filtration.|Preserve the edited list; do not merge it with the cancelled version.|The requested tensor-extension axioms depend on which list is current.|High.|Medium.
161-5|24|P93:1201|Internal Hom operation is inserted.|Retain its variance and duality requirements.|Tensor compatibility alone does not specify the requested extension.|High.|High.
161-5|25|P93:1247-1285|Datum5 is cancelled and replaced by a torsor condition.|Keep the replacement and cancelled list as separate textual stages.|Treating both as simultaneous axioms invents a target category.|High.|High.
161-5|25|P93:1292|Right-action formula has a possible order reversal.|Check the order of group multiplication and conjugation on the scan.|A right action and a left action obey different composition orders.|High.|Medium.
161-5|26|P93:1318,1344|The dual mark is doubtful; the frozen Tate twist is positive.|Preserve the positive sign and leave the dual unresolved.|Duality reverses Hodge-Tate weights; external conventions do not decide this ink.|High.|Medium.
161-5|26|P93:1363-1365|Uniqueness of j ends with Du moins si.|Do not omit the unfinished qualification.|No complete normalization condition survives; C-SA04-452.|High.|High.
161-5|27|P93:1423,1430|Field descent and Frobenius descent have ambiguous directions.|Record them as distinct structures until the symbols are resolved.|The coefficient fields and semilinearity differ.|High.|Medium.
161-5|27-28|P93:1438-1447|Gamma, pi, Z and the group of S/Omega points are uncertain.|Determine the extension and subgroup, and do not assume pi is normal.|The quotient-H1 expression requires a normal subgroup and a defined quotient action.|High.|Medium.
161-5|29|P93:1489-1495|Injectivity and neutral-fibre triviality are juxtaposed.|Keep the two questions separate.|Other fibres require twisting; C-SA04-458.|High.|High mathematical.
161-5|29|P93:1497|Torsor is deleted in favour of homogeneous space.|Preserve the replacement.|Stabilizer A^Gamma need not be trivial.|High.|High.
161-5|29|P93:1521-1551|Integral-model labels and generic/integral point groups are uncertain.|Identify the model and the point field separately.|Integral points need not equal all generic points.|High.|Medium.
161-5|29|P93:1543|T(Qp) and T(K) can be confused.|For T=Res(K/Qp)Gm, T(Qp)=Kstar and T(K)=(K tensor K)star.|Separable quadratic K gives the latter as two Kstar factors; C-SA04-461.|High.|High.
98|2|P98:2-8|Cover XVII versus contextual XVIII.|Retain XVII pending scans.|The published norm exposé is XVII, but mathematical fit cannot decide an extra stroke.|Low mathematical, medium bibliographic.|Low palaeographic.
98|3|P98:27-38|Antisymmetric tensor terminology.|Distinguish the alternating image from the full sign-eigenspace.|In characteristic2 their dimensions differ,1 versus3 for rank2; C-SA04-464.|High.|High diagnosis; word ink unresolved.
98|7,11-13|P98:144-205,279-356|Cor/Cn norm-section label versus contextual Can.|Keep the doubtful abbreviation.|The operation is identified mathematically but its letters are not.|Low.|Low palaeographic.
98|11-13|P98:296-347|A single numerical degree includes the empty target.|A degree predicate or locally constant rank convention would avoid contradiction.|Empty pullback forces1=2 under the literal axioms; C-SA04-471. This need not be a transcription error.|High.|High mathematical.
98|14|P98:359-363|Final contracted-product sentence ends in compos.|Leave its completion open.|No fully quantified composition theorem is written after the interruption.|Medium.|Low palaeographic.
98|16|P98:405|Phi_A(X)=Hom_G(X,E).|Second argument A.|The represented object is A and E is a free-variable mismatch; C-SA04-478.|High.|High type diagnosis.
98|22|P98:540|Initial bullet or0 in the Picard-Brauer diagram.|An initial0 requires vanishing of the incoming Picard differential.|The real-conic cover has nonzero d2, while the finite field-cover case has Pic=0.|High.|Medium reading; high mathematical.
98|22|P98:542-546|H3 prime and final E4^(4,0) labels.|Retain the filtered H3 term and E4 correction.|The low-degree spectral sequence has further filtration and possible d4 contributions.|High.|High mathematical.
98|24|P98:601|Trivial local coefficients is deleted.|Keep defined local coefficients, including monodromy.|Circle reflection and the Klein bottle give nontrivial sign action; C-SA04-485.|High.|High.
98|24|P98:613|Action described by a doubtful phrase involving pi0 of the fibre.|Do not read this as depending only on the permutation of components.|O(2) modulo a reflection is connected but has degree minus1 action on H1.|High.|Medium.
98|27|P98:651|Faint bounded-cycle/Chow refinement.|Determine whether polynomial data or further restrictions are retained.|Pure O(n) quotients of O² have fixed cycle but unbounded Hilbert polynomial.|High.|Low palaeographic, high conditional counterexample.
98|27|P98:660|Generic length one suggests a global embedding in the support structure sheaf.|A generic identification or a refined subsheaf construction may be intended.|O(n) has rank1 but Hom(O(n),O)=0 for n>0.|High.|Medium.
98|30|P98:714|Extension composée or commune, versus contextual universelle.|Retain the alternatives separately.|Independent and aligned embeddings produce different point modules; the universal-field question is different.|High.|Medium.
98|30-33|P98:717-761|Phi/Cl for the field-equivalence class set versus contextual gothic F.|Do not substitute a letter solely from its meaning.|The role of the class set is clear; the alphabet is not.|Low.|Low palaeographic.
98|31|P98:726|Corollary3 versus contextual Corollary5.|Keep the frozen3.|This is numbering of the universal-field statement, not the later Tor corollary.|Low.|Low palaeographic.
98|34|P98:766-790|Example letters, insertion arrows, and cancelled final i).|Keep the current ordering and deletion.|Reordering the examples is exposition, not a scan correction.|Low.|Medium.
98|36|P98:850|Second Hom argument appears F where the operation has inputs F,G.|Use G as the mathematical candidate.|The finite-presentation kernel computes Hom(F,G), not Hom(F,F).|High.|High diagnosis.
98|39-43|P98:917-921,970,1005-1007|Tor/Ext structure-sheaf subscripts S,Y,X and Hom base A/B conflict.|Use the actual ambient ring B, respectively the structure sheaf on the module scheme, in the mathematical reconstruction.|Changing the ring changes Tor/Ext; C-SA04-503–510.|High.|High type diagnosis, ink unresolved.
98|40|P98:926|L_i free over B_i is used as a B-flat resolution.|Check whether B rather than B_i was intended; otherwise the written proof is invalid.|B=k[x], B_i=M_i=k misses Tor1; polynomial C_i resolutions give a labelled repair.|High.|High mathematical; no ink decision.
98|42|P98:988-992|Length and N/N+1 bounds in the marginal finite-free resolution condition.|Retain a free truncation through N+1 and the terminal-cokernel flatness condition in the repaired theorem.|The Ext comparison in degrees≤N requires the next differential; the multiplication-by-t example tests the cokernel.|High.|Medium.
98|43|P98:1015|A-flat versus contextual A-free; all degrees versus range≤N.|A-flat terms suffice; all degrees refers to the finite complex, Ext only to≤N.|The descending cycles-and-boundaries proof establishes the distinction.|High.|High source-comparison diagnosis.
98|44|P98:1054|Familles virtuelles versus contextual universelles.|Keep the doubtful adjective.|A parameter family containing classes does not automatically represent a universal functor.|Medium.|Low palaeographic.
98|6|P98:135|f(B) is the trace on f(B) of f(D).|The second f(B) should be f(A).|The quotient-subspace criterion requires a relatively open subset of f(A).|Medium.|High mathematical.
98|19|P98:470|Coefficient sum starts at i=1 after basis f0,...,fn.|Start at i=0.|The missing coefficient contributes to the expansion; C-SA04-527.|High.|High.
98|19|P98:472-476|First full-rank prefix supposedly determines a nonzero vector up to scale.|Stop one equation before full rank.|The full-rank homogeneous system has only zero; basis1,t certifies C-SA04-523.|High.|High.
98|19|P98:483-484|Pencil utile au cas non singulier? and Nouveau!/Revoir!, versus contextual Prouver!.|Retain the uncertainty and unknown author.|The surviving words do not justify a definite proof command.|Medium attribution.|Low palaeographic.
98|21|P98:524|Function (f+c fprime)g equals divisor X_c-Y.|Apply a principal-divisor operator to the whole product.|The neighbouring equations compare divisors; C-SA04-526.|High.|High type diagnosis.
98|23|P98:574|Power series has lower limit infinity.|Lower limit0.|The preceding monomial enumeration and following c0,...,cN require0; C-SA04-524.|High.|High.
98|25|P98:635|Historical ample is defined through birational/biholomorphic linear-system map.|Compare with modern ample and very ample rather than replacing the word.|Point separation alone does not establish tangent separation or a closed immersion.|Medium.|High terminological, not a decided reading.
'''
readings=[]
for row in reading_rows.strip().splitlines():
    vals=row.split('|'); assert len(vals)==8,vals
    vals[2]=vals[2].replace('P93:',c.P93+':').replace('P98:',c.P98+':')
    readings.append(dict(zip(['cote','scan','line','reading','alternative','evidence','weight','confidence'],vals)))
tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)

# Every record below has an actually opened primary URL, except the explicitly
# unverified Spencer attempt. Metadata-only openings do not certify a proof.
refrows=r'''
KatzOda1968|article|Katz, Nicholas M. and Oda, Tadao|On the differentiation of de Rham cohomology classes with respect to parameters|1968|Journal of Mathematics of Kyoto University|8|199--213|https://www.its.caltech.edu/~matilde/GaussManinKatzOda.pdf|10.1215/kjm/1250524135|Full primary PDF opened; section2 Theorem1 and section3 checked; communicated19April1968; introduction records Mumford1966--1967 seminar. Web title metadata was wrong, actual PDF title checked.|verified
Katz1970|article|Katz, Nicholas M.|Nilpotent connections and the monodromy theorem: applications of a result of Turrittin|1970|Publications mathematiques de l'IHES|39|175--232|https://www.numdam.org/item/PMIHES_1970__39__175_0.pdf||Full primary PDF opened; Theorem10.0 arithmetic hypotheses and Theorem14.1 checked.|verified
EGAIII2|article|Grothendieck, Alexander|Elements de geometrie algebrique III: Etude cohomologique des faisceaux coherents, seconde partie|1963|Publications mathematiques de l'IHES|17|5--91|https://www.numdam.org/item/PMIHES_1963__17__5_0.pdf||Primary PDF downloaded and read after web-reader size failure; section7.7, especially7.7.5--7.7.7 checked. Written with the collaboration of Jean Dieudonne.|verified
EGAIV4|article|Grothendieck, Alexander|Elements de geometrie algebrique IV: Etude locale des schemas et des morphismes de schemas, quatrieme partie|1967|Publications mathematiques de l'IHES|32|5--361|https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf||Primary PDF downloaded and read after web-reader size failure;16.8.4 and16.11.2 checked. Written with the collaboration of Jean Dieudonne.|verified
SGA4XVII|incollection|Deligne, Pierre|Cohomologie a supports propres, Expose XVII|1973|Theorie des topos et cohomologie etale des schemas, SGA4 tome3, Lecture Notes in Mathematics305|||https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf||Primary retypesetting opened and checked against numbered statements6.3.1--6.3.15; seminar1963--1964, publication1973. Expose author Deligne; seminar directed by Artin, Grothendieck and Verdier.|verified
Ferrand1998|article|Ferrand, Daniel|Un foncteur norme|1998|Bulletin de la Societe mathematique de France|126|1--49|https://www.numdam.org/article/BSMF_1998__126_1_1_0.pdf|10.24033/bsmf.2319|Primary PDF opened; polynomial-law representation2.5.1 and determinant norm3.1.1--3.1.2 checked.|verified
Grothendieck1961IV|incollection|Grothendieck, Alexander|Techniques de construction et theoremes d'existence en geometrie algebrique IV: les schemas de Hilbert|1961|Seminaire Bourbaki, expose221|6|249--276|https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf||Primary PDF opened; May1961 talk; section1 operations, Proposition1.2 properness, Proposition1.3 field qualifications, Theorem2.1 checked with erratum.|verified
Grothendieck1962Err|incollection|Grothendieck, Alexander|Erratum a l'expose no221|1962|Seminaire Bourbaki|7|302|https://www.numdam.org/item/SB_1961-1962__7__302_1.pdf||Complete one-page primary erratum opened; sufficiency restored in Theorem2.1.|verified
Serre1967|incollection|Serre, Jean-Pierre|Sur les groupes de Galois attaches aux groupes p-divisibles|1967|Proceedings of a Conference on Local Fields||118--131|https://link.springer.com/chapter/10.1007/978-3-642-87942-5_10|10.1007/978-3-642-87942-5_10|Publisher record opened; full offprint read in supplied transcription cote161-5 scans3--17. Conference1966; source footnote dates text December1966.|verified
Serre1979|incollection|Serre, Jean-Pierre|Groupes algebriques associes aux modules de Hodge-Tate|1979|Asterisque|65|155--188|https://www.numdam.org/article/AST_1979__65__155_0.pdf||Primary PDF opened; Rennes conference July1978, publication1979;1.3 Theorem1,1.4 Theorem2 and Corollary3, sections2 and5, Theorem7 checked.|verified
Sen1972|article|Sen, Shankar|Ramification in p-adic Lie extensions|1972|Inventiones mathematicae|17|44--50|https://link.springer.com/article/10.1007/BF01390022|10.1007/BF01390022|Publisher record opened; exact comparison theorem checked through Fontaine--Ouyang A.85 and Gross1979, not subscription full text.|verified
Sen1973|article|Sen, Shankar|Lie algebras of Galois groups arising from Hodge-Tate modules|1973|Annals of Mathematics|97|160--170|https://annals.math.princeton.edu/1973/97-1/p06|10.2307/1970879|Publisher metadata opened; theorem checked via Serre1979, not full original article.|verified
Gross1979|incollection|Gross, Benedict H.|Ramification in p-adic Lie extensions|1979|Asterisque|65|81--102|https://www.numdam.org/article/AST_1979__65__81_0.pdf||Primary PDF opened; ramification-filtration comparison and mixed/equal-characteristic distinction checked.|verified
FontaineOuyang|misc|Fontaine, Jean-Marc and Ouyang, Yi|Theory of p-adic Galois Representations|n.d.|Author book draft|||https://www.imo.universite-paris-saclay.fr/~fontaine/galoisrep.pdf||Primary author draft opened; section5.1 and AppendixA.4 TheoremA.85 with assumptions read. No publication date inferred from a search crawler.|verified
Fontaine1979|incollection|Fontaine, Jean-Marc|Modules galoisiens, modules filtres et anneaux de Barsotti-Tate|1979|Asterisque|65|3--80|https://www.numdam.org/article/AST_1979__65__3_0.pdf||Full primary PDF opened; introduction0.1--0.4, sections3.4--3.6 Theorem3.6.5, and6.5 checked. Admissible-category scope retained.|verified
Liu2013|article|Liu, Tong|The correspondence between Barsotti-Tate groups and Kisin modules when p=2|2013|Journal de Theorie des Nombres de Bordeaux|25|661--676|https://www.numdam.org/article/JTNB_2013__25_3_661_0.pdf||Primary PDF opened; Theorem2.2.1 and perfect-residue/finite-ramified-extension hypotheses checked. Received11June2012.|verified
Gunton2021|article|Gunton, Cody|Semistable abelian varieties and maximal torsion 1-crystalline submodules|2021|Journal de Theorie des Nombres de Bordeaux|33|39--81|https://www.numdam.org/item/10.5802/jtnb.1151.pdf|10.5802/jtnb.1151|Primary PDF opened; section1.2 Tate-curve noncrystalline example checked.|verified
deJongICM1998|incollection|de Jong, A. J.|Barsotti-Tate Groups and Crystals|1998|Documenta Mathematica, Extra Volume ICM1998|II|259--265|https://ems.press/content/book-chapter-files/27155||Primary PDF opened; section3 Theorem2 p261 gives integral-noetherian-normal-domain generic-Hom extension. Theorem1 has a different p-basis hypothesis.|verified
deJong1998|article|de Jong, A. J.|Homomorphisms of Barsotti-Tate groups and crystals in positive characteristic|1998|Inventiones mathematicae|134|301--333|https://link.springer.com/article/10.1007/s002220050266|10.1007/s002220050266|Publisher record and author bibliography opened; exact extension statement checked in author's ICM report.|verified
deJongErratum|article|de Jong, A. J.|Erratum to: Homomorphisms of Barsotti-Tate groups and crystals in positive characteristic|1999|Inventiones mathematicae|138|225|https://link.springer.com/article/10.1007/s002220050348|10.1007/s002220050348|Publisher record opened and author's ErratumTate.dvi downloaded/read. Corrects Lemma2.1(iii) and Definition2.2; author says no other changes necessary. Later digital date2018 is not print year.|verified
KatzSerreTate|incollection|Katz, Nicholas M.|Serre-Tate local moduli|1981|Surfaces algebriques, Lecture Notes in Mathematics868||138--202|https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf||Primary PDF opened; section1 general theorem, Theorem2.1 ordinary deformation,3.7 and4.3 Gauss-Manin comparison checked.|verified
SerreBourbaki1968|incollection|Serre, Jean-Pierre|Groupes p-divisibles|1968|Seminaire Bourbaki, expose318|10|73--86|https://www.numdam.org/item/SB_1966-1968__10__73_0/||Primary metadata and bibliography opened; reference4 records Woods Hole1964 mimeographed Lubin--Serre--Tate notes.|verified
MilneDocuments|misc|Milne, James S.|Historical documents: Woods Hole notes|n.d.|Author archive|||https://www.jmilne.org/math/Documents/index.html||Opened as documentary witness for the1964 notes only; no unrelated historical opinions used.|verified
Springer1973|book|Springer, Tonny A.|Jordan Algebras and Algebraic Groups|1973|Ergebnisse der Mathematik und ihrer Grenzgebiete|75||https://link.springer.com/book/10.1007/978-3-642-61970-0|10.1007/978-3-642-61970-0|Publisher and frontmatter opened; frontmatter explicitly says reprint of1973 edition. Full classification proof not inspected.|verified
Lubin1967|article|Lubin, Jonathan|Finite subgroups and isogenies of one-parameter formal Lie groups|1967|Annals of Mathematics|85|296--302|https://annals.math.princeton.edu/1967/85-2/p06|10.2307/1970443|Publisher metadata and author's bibliography opened; corrects source bibliography's1961 date, not its ink.|verified
HochschildSerre1953|article|Hochschild, Gerhard and Serre, Jean-Pierre|Cohomology of group extensions|1953|Transactions of the American Mathematical Society|74|110--134|https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/hochschild-serre.pdf|10.1090/S0002-9947-1953-0052438-8|Primary paper opened; introduction and construction read; received22March1952 and Lyndon antecedent distinguished from1953 publication.|verified
SerreGC|book|Serre, Jean-Pierre|Galois Cohomology|1997|Springer|||https://link.springer.com/book/10.1007/978-3-642-59141-9|10.1007/978-3-642-59141-9|Publisher metadata only opened; English translation1997. ChapterI section5 located bibliographically; proof here is independent and compared with Conrad AppendixB.|verified
Conrad2012|article|Conrad, Brian|Finiteness theorems for algebraic groups over function fields|2012|Compositio Mathematica|148||https://math.stanford.edu/~conrad/papers/cosetfinite.pdf||Primary author PDF opened; AppendixB.1--B.3 twisting and torsor descriptions checked, especially B.2 and discussion before Lemma6.4.2.|verified
Rydh2008II|misc|Rydh, David|Families of zero cycles and divided powers II: The universal family|2008|Author preprint|||https://davidrydh.se/papers/famzerocyclesII-20080411.pdf||Version11April2008 opened; section3 norm and section6 Hilbert--Chow checked. Remark7.6 broader proposed generalization is not used as theorem.|verified
MilneAV|incollection|Milne, James S.|Abelian Varieties|1986|Arithmetic Geometry||103--150|https://www.jmilne.org/math/xnotes/AVs.pdf||Author corrected version2January2022 opened; original numbering retained. Theorem7.1, Propositions8.1,9.1,9.2, Remark9.3 and dual-variety construction checked.|verified
Michor2006|misc|Michor, Peter W.|Topics in Differential Geometry|2006|Author draft|||https://deferentialgeometry.org/papers/Topics%20in%20Differential%20Geometry.pdf||Draft dated21February2006 in footer; section4.26 logarithmic derivative and section22 curvature formula opened.|verified
Crainic2023|misc|Crainic, Marius|Quotients in the year 2023|2023|Author course notes, Utrecht|||https://webspace.science.uu.nl/~crain101/topology-2023/quotients-2023.pdf||Primary course PDF opened; Definition0.1, Proposition0.2 and Theorem0.4 checked. Background comparator, not attribution of reused typescript.|verified
Spencer1969|article|Spencer, Donald C.|Overdetermined systems of linear partial differential equations|1969|Bulletin of the American Mathematical Society|75|179--239|https://www.ams.org/bull/1969-75-02/S0002-9904-1969-12129-4/S0002-9904-1969-12129-4.pdf|10.1090/S0002-9904-1969-12129-4|Primary PDF access failed; bibliographic lead only. No exact formal-exactness theorem attributed on this basis.|unverified
'''
refs={}
for line in refrows.strip().splitlines():
    k,typ,author,title,year,journal,volume,pages,url,doi,annote,note=line.split('|')
    refs[k]=dict(type=typ,author=author,title=title,year=year,**({'journal':journal} if typ=='article' else {'booktitle':journal} if typ=='incollection' else {'howpublished':journal}),volume=volume,pages=pages,url=url,doi=doi,annote=annote,note=note,urldate=DAY)
refs['RAS2025']=dict(type='misc',author='Duque-Rosero, Juanita and Goodson, Heidi and Lorenzo Garcia, Elisa and Malmskog, Beth and Scheidler, Renate',title='On invariants of Artin-Schreier curves',year='2025',url='https://arxiv.org/html/2401.08843v2',eprint='2401.08843',version='2',note='verified',annote='Primary HTML opened; version2 dated18April2025. Section2.2 equations(2.2) and(2.3) give reduced-pole genus and p-rank formulas; used to independently verify coordinating claim C-SA04-647.',urldate=DAY)
stacks={
'Stacks03AJ':('21.4.3','Abelian torsors and extensions','Torsors under an abelian sheaf and the extension of the constant integer sheaf.'),
'Stacks08J7':('21.35','Internal hom in the derived category','Derived tensor--Hom adjunction and resolution requirements.'),
'Stacks01UP':('17.28.11','Modules of differentials','Difference of sections of a square-zero extension is a derivation.'),
'Stacks0620':('15.63.3','Tor spectral sequence','Base algebra and both inputs flat over A; two-input base-change spectral sequence.'),
'Stacks01ZR':('32.10.2','Descending relative objects','Finite-presentation module, map and equality descent on qcqs inverse limits.'),
'Stacks052A':('29.28.1','Generic flatness','Finite-type scheme over integral base and finite-type quasi-coherent module.'),
'Stacks03AZ':('21.10.6','Cech cohomology','Cover spectral sequence with cohomology presheaf.'),
'Stacks079Z':('21.13.2','Cohomology of a sheafified nerve','Surjective sheafification and nerve spectral sequence.'),
'Stacks0A1J':('36.30.7','Cohomology and base change VI','Finitely presented morphism, perfect first input, bounded finitely presented flat second input with proper support.'),
'Stacks0DPB':('108.6.2','Boundedness for Quot','Projective-space Quot fixed-polynomial statement.'),
'Stacks0DPC':('108.6.3','Boundedness for Quot','Proper finitely presented scheme with ample invertible sheaf.'),
'Stacks03NP':('59.12','Sheaves on a group','G-set site and the action from evaluation at the regular orbit.'),
'Stacks00VZ':('7.9','The example of G-sets','G-set/sheaf equivalence; basis refinement using G-sets with finitely many orbits is independently proved here.'),
'StacksTopology':('5','Topology','Chapter introduction and table of contents opened; basic product and gluing proofs are independent in analysis.md, not claimed as inspected numbered Stacks theorems.')}
for key,(loc,title,ann) in stacks.items():
    tag=key.removeprefix('Stacks') if key!='StacksTopology' else '004C'
    refs[key]=dict(type='misc',author='{The Stacks Project Authors}',title=f'The Stacks Project, {loc}: {title}',year='2026',url='https://stacks.math.columbia.edu/tag/'+tag,note='verified',annote='Opened exact primary page. '+ann,urldate=DAY)
with (OUT/'references.bib').open('w') as f:
    for key,d in refs.items():
        f.write('@'+d['type']+'{'+key+',\n')
        for field,v in d.items():
            if field!='type' and v:f.write('  '+field+' = {'+v+'},\n')
        f.write('}\n\n')

# Supplements discovered after primary follow-up, without changing source readings.
for a in c.claims:
    if a['id'] in ['C-SA04-456','C-SA04-457','C-SA04-458','C-SA04-459','C-SA04-460']:
        if 'Conrad2012' not in a['refs']:a['refs'].append('Conrad2012')
    if a['id'] in ['C-SA04-516','C-SA04-518','C-SA04-519']:a['refs'].append('Crainic2023')
    if a['id']=='C-SA04-448':
        a['fate']+=' The author erratum was also read: it corrects Lemma2.1(iii) and the semistable-reduction definition, and expressly says no other changes are necessary; the generic-Hom extension theorem is not retracted.'
    if a['id']=='C-SA04-517':
        a['statement']+=' The graph map x to (x,f(x)) is a homeomorphism onto its graph exactly when f is continuous, using the two projections.'
    dates=[]
    for key in a['refs']:
        if key.startswith('Stacks'):dates.append(key+': current primary page inspected 19 November 2026, not a first-publication date')
        elif key=='KatzOda1968':dates.append('Katz-Oda: communicated 19 April 1968, publication 1968; introduction records the 1966-1967 Mumford seminar')
        elif key=='Serre1967':dates.append('Serre: conference 1966, text December 1966, publication 1967')
        elif key=='Serre1979':dates.append('Serre: Rennes conference July 1978, publication 1979')
        elif key=='SGA4XVII':dates.append('SGA4: seminar 1963-1964, tome III publication 1973')
        elif key=='KatzSerreTate':dates.append('Serre-Tate theorem circulated at Woods Hole 1964; opened Katz exposition published 1981')
        elif key=='Grothendieck1961IV':dates.append('FGA IV: Bourbaki talk May 1961; companion erratum 1962')
        else:dates.append(key+': '+refs[key].get('year','undated'))
    a['fate_date']='Opened comparator dates: '+'; '.join(dates)+'. These dates are not an inferred first-discovery date or a date for the undated manuscript.'
for p in c.problems:
    if p['id']=='MP-SA04-119':
        p['refs'].append('Conrad2012')
        p['state_of_art']+=' Conrad2012 AppendixB.2 is an opened primary account of twisting; it does not supply the missing manuscript group definitions.'
c.save()

groupfiles={
'MC':[22,23,24,25],'GM':[1,3,4,5,6,9,12,15,27],'DIFF':[5,7,10,11,16,26],
'SQZERO':[2,5,16],'DERIVED':[2,5,16],'SERRE':[1,3,4,10,15,19,20,21,23,24,26],
'SEN':[1,10,11,12,13,14,15,20,21,25],'HTCAT':[1,6,8,11,22,23,24],
'BT':[5,6,7,8,9,13,25,26,27],'SERRETATE':[14,15,18,19,27],
'TORSOR':[2,14,16,20,26,27,28],'NABH1':[14,16,20,23,26,27,28],
'TORUS':[1,3,4,14,22,24],'NORM':[1,3,4,6,9,14,15,19,22,23],
'NORMAX':[1,3,4,9,22,23],'GSET':[16,17,18],'GCOH':[7,8,9,16,18],
'PICBRAUER':[7,8,9,28],'BOUNDED':[1,3,4,5,10,11,26,28],
'FIELDS':[1,2,4,5,26,28],'STRATA':[2,5,10,11,28],'TOR':[2,5,10,11,28],
'EXT':[2,5,10,11,28],'TOPOLOGY':[17,18,19,22,23,24,27],
'ABELIAN':[2,3,9,12,25,28]}
negative={
'MC':'No missing commutativity hypothesis can be recovered from the retained preceding-page fragment.',
'DIFF':'Exact formal-exactness phrase searches did not identify the finite-order all-P theorem; Spencer primary access failed. EGA principal-parts statements are narrower.',
'SQZERO':'No exact unrestricted crystalline-equivalence claim is present; located results concern the first-order derivation/torsor mechanism.',
'DERIVED':'No verbatim published theorem matching the mixed-notation draft was identified; additive roof is an explicit independent repair.',
'HTCAT':'No exact theorem on the unfinished all-two-weight Hodge-Tate target category was identified. Admissible/crystalline equivalences have smaller domains.',
'BT':'The erratum changes a kernel claim and semistable-reduction definition; it does not cancel the located generic-Hom extension theorem.',
'NABH1':'Literature does not determine the manuscript Gamma/pi/action. General restriction injectivity is not supplied by neutral-fibre triviality.',
'TORUS':'The unfinished integral model and point field remain undefined despite the restriction-of-scalars comparator.',
'NORMAX':'No literature theorem validates the inconsistent numerical degree on an empty target; the axiom convention needs repair.',
'TOPOLOGY':'No author or edition of the reused typescript was established; the negative gluing assertion is already in the source.',
'ABELIAN':'Modern projectivity does not certify the source full-rank homogeneous step or identify the pencil author.',
'PICBRAUER':'An unrestricted fixed-cover injection is not found; the nonzero Picard d2 is an explicit obstruction.',
'FIELDS':'No theorem permits arbitrary prescribed independent composita to replace a suitable common extension.',
'EXT':'No unrestricted relative Ext1 statement matching the final plan was identified.',
'STRATA':'Finite-range results do not give one finite stratification for every degree of an arbitrary unbounded complex.'}
logs=[];requests=[]
for num in range(1,29):
    p=c.ROOT/f'SA04_work/evidence/c_web_{num:02}.json'
    if not p.exists():continue
    q=json.loads(p.read_text())['query']
    for kind,queries in q.items():
        if kind in ['system1_search_query','system2_search_query']:
            for q0 in queries:requests.append(dict(request=f'c_web_{num:02}',date=DAY,engine=kind,query=q0['q'],purpose='Discovery followed by opened primary passages; see claim-level ledger.'))
for a in c.claims:
    group=c.claim_search[a['id']];fs=groupfiles[group]
    qs=[r['query'] for r in requests if int(r['request'].split('_')[-1]) in fs]
    logs.append(dict(claim_id=a['id'],date=DAY,group=group,searches=' || '.join(dict.fromkeys(qs)) or 'Opened-source section and bibliography search, using the listed exact primary locators.',primary_checks='; '.join(k+': '+refs[k]['url']+'; '+refs[k]['annote'] for k in a['refs']),result=a['fate'],negative_result=negative.get(group,'Broad topic matches were not treated as exact settlement; the row retains the matched hypotheses and does not infer manuscript priority.'),status='searched and primary passages compared; see event-specific proof scope'))
tsv('search_log.tsv',['claim_id','date','group','searches','primary_checks','result','negative_result','status'],logs)
tsv('search_requests.tsv',['request','date','engine','query','purpose'],requests)

links=[]
def link(kind,frm,to,what,evidence,notes):
    links.append(dict(kind=kind,**{'from':frm,'to':to},what=what,evidence=evidence,note_ids=notes))
link('folder','Cote93/231-233, '+c.P93+':224-315; SA04-420,423,424','Cote93/154-160, SA04_texts/codex/K93-02_transcription.tex:1-228; root C-SA04-618-620','Principal parts, stratified extension and differential-operator factorization; the Manin identity is checked at scan159 line215.','Both complete passages read; c_manin_check.py and analysis.md §11.1 verify nu Delta=mu D, not an identification of every formal-exactness hypothesis.',c.PK+'#20;'+c.PK+'#23;'+c.PK+'#24')
link('folder','Cote161-5/20, '+c.P93+':1047-1055; SA04-449','Cote161-5/29, '+c.P93+':1521-1552; SA04-490,492','Restriction-of-scalars torus is a same-object antecedent of the final group-of-points diagram.','Both endpoints read; T(Qp) versus T(K) independently computed. The entire integral-model diagram is not thereby completed.',c.PK+'#49;'+c.PK+'#90;'+c.PK+'#92')
link('folder','Cote93/234-236, '+c.P93+':318-461; SA04-427,435','Cote161-5/23-27, '+c.P93+':1114-1443; SA04-461,468,477','Square-zero comparison and the rational comparison-data question have distinct coefficients and domains.','Both endpoints read; this checked distinction prevents an unjustified general integral nil-invariance conclusion.',c.PK+'#27;'+c.PK+'#61;'+c.PK+'#68;'+c.PK+'#77')
link('folder','Cote98/3-14, '+c.P98+':9-363; SA04-510-524','Cote98/27-44, '+c.P98+':647-1058; SA04-538-569','Norms and bounded families supply separate ingredients for a later Hilbert-Chow comparison.','Both archive endpoints read; the archive does not construct that morphism. Published comparison checked in Rydh2008II §6.','MPL_98#4:N14;MPL_98#6')
for frm,key,loc,what,notes in [
('Cote93/222-230; C-SA04-402-411','KatzOda1968','section2 Theorem1 and section3','Same Gauss-Manin object; the exact theorem uses relative de Rham hypercohomology.',c.PK+'#8-18'),
('Cote93/223-229; C-SA04-463','Katz1970','Theorem10.0, pp209-210; Theorem14.1, p230','Conditional global-nilpotence and monodromy comparator; arithmetic properness hypotheses retained.',c.PK+'#95'),
('Cote93/231-233; C-SA04-416','EGAIV4','Proposition16.8.4; Theorem16.11.2','Principal-parts representation matches the quotient construction; it does not settle undefined formal exactness.',c.PK+'#20-25'),
('Cote93/235-236; C-SA04-421','Stacks03AJ','Lemma21.4.3','Additive torsor-to-extension mechanism; repaired roof is proved independently.',c.PK+'#27-34'),
('Cote161-5/19-21; C-SA04-443-444','Serre1979','section1.3 Theorem1; section1.4 Theorem2 and Corollary3','Sen theorem supplies the neutral-component and open-image correction.',c.PK+'#47-49'),
('Cote161-5/17; C-SA04-442','FontaineOuyang','AppendixA.4 TheoremA.85','Exact bounded-shift ramification/Lie comparison under its total-ramification and local-field hypotheses.',c.PK+'#46'),
('Cote161-5/21; C-SA04-448','deJongICM1998','section3 Theorem2, p261','Equal-characteristic generic-Hom extension hope is settled for normal noetherian integral bases.',c.PK+'#52'),
('Cote161-5/21-22; C-SA04-449','KatzSerreTate','section1; Theorem2.1; sections3.7,4.3','Published deformation theorem and precise ordinary Gauss-Manin comparison; source new-proof gaps are separate.',c.PK+'#53-54'),
('Cote161-5/23-27; C-SA04-451-454','Fontaine1979','sections3.4-3.6, Theorem3.6.5; section6.5','Filtered and tensor comparison on admissible categories, not all two-weight Hodge-Tate objects.',c.PK+'#61-80'),
('Cote98/3-14; C-SA04-465-476','SGA4XVII','6.3.1-6.3.7;6.3.13.1-6.3.15','Same determinant norm and trace formalism; exact symmetric-descent condition retained.','MPL_98#4'),
('Cote98/3-5; C-SA04-465','Ferrand1998','2.5.1;3.1.1-3.1.2','Polynomial-law representation and determinant norm under finite local freeness.','MPL_98#4:N02'),
('Cote98/27-28; C-SA04-488','Grothendieck1961IV','section1; Theorem2.1, with1962 erratum','Fixed-quotient and finite-Hilbert-polynomial boundedness; manuscript relative dating not inferred.','MPL_98#6:B01'),
('Cote98/35-43; C-SA04-501,508-510','EGAIII2','section7.7, especially7.7.5-7.7.7','Finite-complex/base-change and canonical gluing comparator.','MPL_98#6:B15-B25'),
('Cote98/39-41; C-SA04-503-507','Stacks0620','Example15.63.3','Two-input hyper-Tor sequence with flat base and flat inputs; wrong-ring manuscript proof repaired separately.','MPL_98#6:B18-B21'),
('Cote98/44; C-SA04-511','Stacks0A1J','Lemma36.30.7','Precise sufficient relative-RHom theorem with perfect/proper-support/flatness hypotheses.','MPL_98#6:B28'),
('Cote98/15,17,25; C-SA04-520-521,525','MilneAV','Theorem7.1; Propositions8.1,9.1,9.2; Remark9.3','Picard addition, finite-kernel isogeny, effective nondegeneracy and projectivity.','MPL_98#7:T04-T09')]:
    link('published work',frm,key+': '+loc+'; '+refs[key]['url'],what,'Both source passage and named primary result opened and compared; see search_log.tsv for hypotheses.',notes)

# Project endpoints were not attached. These rows audit the source-side report
# and explicitly do not enter the checked-link count.
for frm,to,what,notes in [
('Cote93/234-236; SA04-427','C30','First-order derived torsor comparison is a contextual lead, not proof of a C30 crystalline theorem.',c.PK+'#97'),
('Cote161-5/28-29; SA04-481-491','SECTIONS_OVER_Q; EXIT_TOWER; FINMON','Normalized-section cocycles and valuation obstruction may inform these projects; no arithmetic section theorem is checked.',c.PK+'#99'),
('Cote93/221-230; cote161-5/22; SA04-493,496','S20; ordinary-lift/Picard-Fuchs/Hasse-Witt comparison','Earlier-run proposed bridge; an integral model and reduction hypotheses remain to be specified.',c.PK+'#93;'+c.PK+'#96'),
('Cote98/16-24; SA04-525-537','LM7E23; FLAGGED149B9; LM1D11; LM4D12/F7','Finite-homotopy and section-project comparisons are contextual leads, not consequences of the ordinary cover spectral sequence.','MPL_98#5:G11'),
('Cote98/3-14; SA04-510-524','H98; Hua98; RS Orientation','Norm interpretation and alleged proof-status/Lean labels are originating-run reports, not certificates available here.','MPL_98#1;MPL_98#4'),
('Cote98/27-44; SA04-538-569','Hua98; BR; S19; MPL131','Bounded-family and chapter-plan links; precise remote endpoints were not supplied.','MPL_98#6:B01-B32'),
('Cote98/15,17,25; SA04-573-579','LM7 C.1; LM7 C.5; WG H9; WG2 Book II','Picard/Jacobian and projectivity background only; no Fermat extension order, splitting or Neron-Tate formula is verified.','MPL_98#7:T04-T05;MPL_98#7:T09'),
('Cote98 reading comparisons; SA04-584-596','Hua98; H98','Contextual normalized readings remain leads to compare on scans; current Pro source retains its alternatives.','MPL_98#8')]:
    link('our projects',frm,to,what,'LEAD ONLY: source-side note and transcription checked; project endpoint unavailable, so no two-endpoint theorem verification claimed.',notes)
def stable_note_ids(value):
    out=[]
    for token in value.split(';'):
        m=re.fullmatch(r'([^#]+)#(\d+)(?:-(\d+))?(?::.*)?',token)
        assert m,token
        pkg,lo,hi=m.groups()
        for n in range(int(lo),int(hi or lo)+1):
            eid=f'{pkg}#{n}'
            if eid not in out:out.append(eid)
    return ';'.join(out)
for row in links:row['note_ids']=stable_note_ids(row['note_ids'])
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)
tsv('project_leads.tsv',['kind','from','to','what','evidence','note_ids'],[l for l in links if l['kind']=='our projects'])
tsv('archive_leads.tsv',['kind','from','to','what','evidence','note_ids'],[dict(kind='archive lead',**{'from':'Cote93/221-236 and cote161-5/23-29; SA04-498','to':'Cote'+cote+'; endpoint scan not specified in the supplied note'},what='Possible Cartier, p-curvature or period-family comparison reported by the earlier context.',evidence='LEAD ONLY: the source-side indexed note was read, but no target passage from this cote was supplied; excluded from the checked folder-link count.',note_ids=c.PK+'#98') for cote in ['159','64']])

directions=r'''# Ranked directions from the part C consolidation

These are task definitions, not research carried out here. Interest and one-run reach are ranked separately; all claims of prior proof remain tied to the opened references.

1. **Recover the exact comparison-data category before testing the tensor-extension question.** Interest: very high; reach in a few hours: high for a definition audit, low for a general existence theorem. Sources: SA04-461,465,468,469,474,479,480; C-SA04-450–454; MP-SA04-116–118. Establish exactly which objects, morphisms, fields, Frobenius, filtration and normalization the edited draft retains. Crystalline admissible categories are understood, but the source generates from all two-weight Hodge-Tate objects and includes noncrystalline Tate-curve representations. First step: transcribe the five-data-list revisions and the unfinished qualification of j from scans23–27 into a typed diagram, keeping each cancelled stage separate.

2. **Write a companion proof for the Tor and Ext base-change sequence with every ring label fixed.** Interest: high; one-run reach: very high. Sources: SA04-555–563; C-SA04-503–510; MP-SA04-127–129. The conditional theorem is established, while the free-B_i resolution is genuinely the wrong proof object. The audit gives the polynomial-algebra repair and finite-complex argument. First step: produce a statement-by-statement commentary for scans39–43, distinguishing the original claim, the proof defect, and the corrected finite-range proof. Do not broaden it to unbounded all-degree claims.

3. **Recover the formal-exactness definition and its two variance conventions.** Interest: high; one-run reach: medium. Sources: SA04-406,420,421,423–425; C-SA04-412–418; MP-SA04-101–107. Principal-parts representation and the conditional injection are known; the retained fragment does not define the exact premise for the all-P finite-order sequences. First step: inspect preceding/parallel sheets and the scans for the order shifts, then compare the resulting definition with EGA IV4 and a fully accessible Spencer source. A result should be a precise identification or a demonstrable mismatch, not a broad subject citation.

4. **Prepare the additive torsor-roof companion and determine the degree/arrow readings.** Interest: high; one-run reach: very high. Sources: SA04-426,427,432,433,435; C-SA04-419–423; MP-SA04-108. The repaired roof already has an elementary proof; the source's mixed formulas, degree caption and boxed isomorphism are separate scan issues. First step: annotate scans234–236 against the explicitly typed data u,k and the complex in degrees minus1,0. The goal is faithful exposition of a first-order comparison, not a general crystalline-equivalence project.

5. **Explain the norm axioms through the finite-set/finite-locally-free bridge, including the empty base.** Interest: high; one-run reach: high. Sources: SA04-510–524; C-SA04-464–476; MP-SA04-121–123. SGA4 XVII and Ferrand settle the determinant-law mechanism; the literal global numerical degree is inconsistent. First step: extract the exact degree convention from scans11–13 and compare three repairs against all source diagrams. Use a ramified dual-number algebra and an empty pullback as diagnostic examples.

6. **Align the bounded-family draft with FGA IV and its erratum.** Interest: high historically; one-run reach: high. Sources: SA04-538–554,564–569; C-SA04-488–502,512–515; MP-SA04-125–126. The fixed quotient/Hilbert-polynomial theorem has a direct published match; faint cycle wording and generic embedding need scan decisions. First step: make a concordance of scans27–37/44 with FGA IV definition1.1, Propositions1.2–1.3, Theorem2.1 and the1962 erratum, preserving undated-manuscript chronology.

7. **Reconstruct the last section-extension problem from its actual groups and point fields.** Interest: medium to high; one-run reach: medium. Sources: SA04-481–491; C-SA04-456–462; MP-SA04-119–120. Abstract cocycle, twisting and valuation obstructions are settled, but Gamma, pi, action and the integral model remain incomplete. First step: inspect scans27–29 and identify every group arrow before invoking quotient H1 or Hilbert90. A few hours can determine whether there is a well-posed arithmetic question beyond the abstract countermodels.

8. **Compare the ordinary-lifting and period threads through an explicit published Gauss-Manin theorem.** Interest: medium to high; one-run reach: medium. Sources: SA04-408–419,454,493,495,496; C-SA04-402–411,449,463; MP-SA04-102–105,115. Katz's Serre-Tate local moduli §§3.7,4.3 supplies a concrete comparison, whereas the archive has no worked integral elliptic example. First step: choose one ordinary elliptic family with a specified model and good prime, then formulate which Picard-Fuchs/Hasse-Witt quantity is to be compared. This proposed experiment was not carried out in this audit.

9. **Produce a source-faithful commentary on the low-degree cover sequence and monodromy correction.** Interest: medium; one-run reach: high. Sources: SA04-525–537; C-SA04-477–487; MP-SA04-124. The ordinary topos statements are established. First step: define H3 prime and every E_r term on scan22, then place the field-cover case and the real-conic obstruction side by side; explain the deleted trivial-local-system phrase using the source's actual acting group.

10. **Separate the reused typescripts' attribution from their mathematical repairs.** Interest: medium historically; one-run reach: high if scans/editions are available. Sources: SA04-570–583; C-SA04-516–527; MP-SA04-131–132. Product, quotient, Picard and projectivity results are standard; the full-rank homogeneous step is false, while the gluing counterexample proves an exercise already stated. First step: inspect the printed numbers329/268 and the six mathematical ink alarms before comparing editions. Do not infer authorship from the physical folder alone.
'''
(OUT/'directions.md').write_text(directions)

events=[]
for key,d in refs.items():
    typ='carried as background without fault found' if d['note']=='unverified' or 'metadata only' in d['annote'].lower() or 'subscription full text' in d['annote'] else 'used and rechecked in this run'
    events.append([key,DAY,c.WHO,typ,d['annote']+' Verification label concerns the opened reference, not a complete independent proof.'])
proof_groups=[
('401,402,403,406,409,410,411,414,415,416,417','analysis.md sections2.1--2.4: explicit differential, path, boundary, quotient and strict-projective-system arguments; finite-order formal-exactness theorem not proved.'),
('419,420,421,422,423','analysis.md section3: square-zero derivation and additive torsor-roof proof, with the locally contractible tensor argument; rank counterexample separate.'),
('431,438,440,446','analysis.md section4: component counterexample, strict valuation inequality, and multiplicity-one reduction using opened Serre/Sen theorems as hypotheses.'),
('456,457,458,459,460,461,462','analysis.md section5: cocycle/section, normalization, twisting, stabilizer, valuation and restriction-of-scalars arguments.'),
('464,467,469,471,472,473','analysis.md section6: alternating image, determinant derivative/block formula, orbit basis, empty-degree contradiction and finite-fibre multiset proof.'),
('477,478,479,480,484,485,487','analysis.md section7: sheaf reconstruction on G-sets with finitely many orbits, resolution and edge-differential arguments; conditional monodromy reading isolated.'),
('489,491,492,493,494,496,497,498,499,500,501,502,515','analysis.md section8: boundedness counterexamples, field amalgamation/descent, relative positions, universal-field proof and finite-range flatness arguments.'),
('504,505,506,508,509,510','analysis.md section9: wrong-ring counterexample, polynomial-resolution repair and finite Hom-complex base-change/gluing proof.'),
('516,517,518,519,522,523,524','analysis.md section10: quotient/product/gluing and coefficient-flag proofs; original negative gluing exercise verified rather than refuted.')]
for ids,outcome in proof_groups:
    for n in ids.split(','):events.append(['C-SA04-'+n,DAY,c.WHO,'independent re-proof',outcome])
for bad,good,why in [('406','407,410','Open-arc dx example.'),('409','410','Intersecting-section velocities; moving-endpoint formula replaces arbitrary horizontality.'),('423','421','Rank-four RHom counterexample; repaired derived morphism.'),('431','444','Finite quadratic character excludes whole-inertia equality.'),('471','473','Empty-target numerical degree contradiction; finite-fibre prescribed-rank convention.'),('487','485','Conditional component-permutation interpretation fails for the reflected connected circle; retain the full local coefficient action.'),('489','488','O(n) fixed-cycle quotients require Hilbert-polynomial control.'),('505','506','B_i-free resolutions need not be B-flat.'),('515','488','Generic rank does not give global embedding.'),('523','522','Full-rank homogeneous equations have only zero.')]:
    events.append(['C-SA04-'+bad,DAY,c.WHO,"refuted, with the refined statement's id",'Refined: '+','.join('C-SA04-'+x for x in good.split(','))+'. '+why])
events.extend([
['C-SA04-526',DAY,c.WHO,'targeted proof check','The two sides of the literal equality have different types: a rational function and a divisor. Applying the principal-divisor operation is the candidate repair, awaiting ink inspection.'],
['C-SA04-527',DAY,c.WHO,'targeted proof check','The displayed sum omits the independent coefficient f0 although the preceding basis starts at0. Type/index check only; no palaeographic decision.'],
['C-SA04-620',DAY,c.WHO,'independent re-proof','Read K93-02 lines1--228; prove J(dE)lambda+=j(dP) and naturality identity. Full proof in analysis.md §11.1.'],
['C-SA04-620',DAY,c.WHO,'computation or formal certificate','c_manin_check.py; outputs/c_manin_check.json. Exact finite polynomial jet/cocycle/operator checks; not sampling proof of the universal statement.'],
['C-SA04-647',DAY,c.WHO,'computation or formal certificate','Independent c_review_genus2.py and outputs/c_review_genus2.json: counts3,7,9,31, P=1+T²+4T4, #J=6; source read K93-05 lines218--264.'],
['C-SA04-647',DAY,c.WHO,"refuted, with the refined statement's id",'Refined C-SA04-648. Genus2 Artin-Schreier model has rational2torsion dimension1, root1 algebraic multiplicity2; analysis.md §11.2 checks genus/smoothness and interpretation.']])
with (OUT/'CHECK_EVENTS.tsv').open('a') as f:csv.writer(f,delimiter='\t').writerows(events)
print('Supplement saved:',len(readings),'readings;',len(refs),'references;',len(links),'links of which',sum(l['kind']=='our projects' for l in links),'project leads;',len(logs),'claim searches;',len(requests),'actual search queries;',len(events),'additional check events.')
