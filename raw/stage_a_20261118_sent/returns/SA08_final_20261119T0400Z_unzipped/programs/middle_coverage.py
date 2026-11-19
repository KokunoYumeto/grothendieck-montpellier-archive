"""Emit a human-authored disposition for every embedded N/R/O/L note.
The source extraction is only a locator aid. All mappings and judgments below
were written after reading each note and the actual referenced passages.
"""
from pathlib import Path
import json,csv
root=Path(__file__).resolve().parents[1];out=root/'work/middle'
source={r['embedded_id']:r for r in json.loads((out/'embedded_source.json').read_text())}
items={r['id']:r for r in json.loads((out/'items.json').read_text())}
data='''
N01|203,206|101||kept|Free special algebra is distinct from the unproved comparison strength.
N02|206|102||kept|The canonical square alone does not prove localization equivalence; inverted arrows must be specified.
N03|206|102||kept|Point-like groupoid does not establish all higher homotopy of its nerve.
N04|207|103|30|kept|Positive divided-power preservation remains conditional; the proposed proof is retracted on100.
N05|207|104|30|kept|Read the explicit faux tel quel and projectivity insertion; no corrected general theorem is supplied.
N06|207|104|30|corrected|Our flat acyclic counterexample tests a chain-complex inference, not every historical flasque notion.
N07|203,206|105||kept|Evaluation adjunction is independently checked; its localization consequences are separate.
N08|304|106||kept|Economical has no formal minimality criterion and produces no new minimal-object theorem.
N09|208|107|31|corrected|Primed completed category allows extra morphisms; isotropy must be retained.
N10|208|107|31|corrected|Ambiguous pointed/point-like wording is read together with106 asking for two groups.
N11|208|107|31|kept|The two groups are explicitly to be determined, not proved trivial.
N12|209|108|31|flagged for scan check|Scalar/pair alternatives on106 do not define a coherent coefficient condition without an ink check.
N13|209|108|31|flagged for scan check|Endpoint and sum constants on108 are explicitly unsure; no theorem silently repairs them.
N14|221|194|136|corrected|English donor is unattributed; rational nilpotent quotient language requires the corresponding group interpretation.
N15|221|195|136|corrected|A generalized nilpotent tower is not automatically an unrestricted homotopy classification.
N16|221|196|136|kept|The leaf openly limits its nonsimply-connected interpretation; broad later analogues do not close that exact wording.
N17|210|109||corrected|Contravariant representability sends colimits to limits; cancelled/modal text cannot impose extra axioms.
N18|201,210|110||kept|Earlier finite-weight and proposed τ∞ definitions were read; their unresolved quotient issue is retained.
N19|201|110||kept|Ordinary cohomology is extracted from weighted data; no direct unweighted PD ring equivalence is stated.
N20|202|110||kept|The actual two-arrow derived comparison on113–115 is the relevant sheaf statement.
N21|210|110||kept|The writer weakens demand to desire; comparison is not a theorem merely by its diagram.
N22|210|110||kept|Kernel/cokernel negligible language is not silently replaced by an already established exact quotient.
N23|211|111,112|32|kept|The weight threshold depends on exterior degree; independence of simplex dimension is a separate question.
N24|211|111|32|kept|The standard model later realizes the bound; no universal all-theories optimum is proved.
N25|211|112|33|kept|A sufficiently long resolution supplies the horizontal comparison in the stated range.
N26|211|112|33|kept|Growth of the first nonflasque degree is a sufficient hypothesis, not automatically necessary.
N27|211|113|33|kept|Sans doute equivalence remains tentative; no exact converse theorem located.
N28|211|113|33|flagged for scan check|The marginal weakening is illegible; mathematical convenience cannot supply its missing words.
N29|201,211|111,173|32|corrected|Existence has support in the earlier standard model and231–233; it is not a proof for every coefficient datum.
N30|212|114|34|kept|Uniqueness groupoid is conjectural; Mandell2002 is an enhanced analogue with different axioms.
N31|212|114|34|kept|Forgetting PD may help a weaker comparison; restoring PD compatibility is an additional step.
N32|212|188||kept|Admissible morphisms become isomorphisms formally once the comparison axioms and τ∞ category are valid.
N33|212|114|34|corrected|Connected simply connected groupoid is weaker than contractible nerve.
N34|212|115|35|kept|A common admissible refinement is an explicit conjectural construction.
N35|212|115|35|kept|Precomposition equalization is a separate Ore-type requirement, not implied by objectwise quasi-isomorphism.
N36|212|115|35|kept|Right-versus-left fraction doubt is explicit and preserved.
N37|213|189|137|kept|PD scalar homogeneity forces degree i in the representing symmetric algebra; direct proof supplied.
N38|213,214|116,117|137|kept|Affine polynomial operations and representing modules are kept distinct from unrestricted module duality.
N39|214|117||kept|Eliminating one barycentric coordinate gives the stated polynomial/exterior representing module.
N40|214|118|36|corrected|Hom of the subcoalgebra inclusion need not be surjective without splitting or an exactness condition.
N41|214|117,122||kept|Completed coefficient products are dual to ordinary polynomial direct sums degree by degree.
N42|213|190|137|kept|Yoneda transports structures only after algebra-side identities are established.
N43|215|191|137|kept|Cosimplicial variance is corrected on the page; naturality and identities are not omitted from the statement.
N44|215|119||kept|The Hom of the ordinary colimit is the required limit; no derived assertion is inferred.
N45|215|119||kept|Empty X gives zero and disproves automatic injectivity of the fixed coaugmentation.
N46|215|120|37|corrected|Colimit preservation in X is formal; structured coefficient colimits require separate hypotheses.
N47|215|120|37|kept|Base change of the free integral construction is distinct from arbitrary derived base change.
N48|216|123||kept|Naturality in coefficient algebras transports total grading to the representing object.
N49|216|121||flagged for scan check|The weight of X^(i) is iδ; the written alternative δ needs an ink check.
N50|216|122||kept|Primitive polynomial coalgebra duals have binomial PD multiplication; infinite duals are completed products.
N51|216|192|137|kept|All-structures Hom reconstruction is checked through representing operations, not merely groups.
N52|216|123||kept|The displayed integral tensor base-change formula is a statement about this constructed chain object.
N53|216|123||flagged for scan check|A Hom target is absent; the following arbitrary coefficient M does not justify silently filling the ink.
N54|215,216|123||corrected|Arbitrary abelian coefficients support external pairings, not a canonical internal ring product.
N55|217|124|38|kept|The κ maps must satisfy a chain equation before defining comparison.
N56|217|124|38|kept|Existence of a chain map does not supply a quasi-isomorphism.
N57|217|124|38|flagged for scan check|Cancelled dual signs on137 require a fixed orientation and source collation.
N58|217|124|38|kept|Cartan integration theorem is a source match under axioms, not a complete independent proof of every scratch line.
N59|218|125||kept|All positive Hasse operators give the invariant subring; ordinary first derivative is insufficient in characteristic p.
N60|219|126||kept|The exterior quotient dual is the zero-sum kernel with explicit unimodular basis.
N61|219|126||flagged for scan check|Kernel rank n forces top exterior degree n, with ambient top degree n+1.
N62|219|126||kept|Determinant identification requires orientation; no sign chosen by convenience changes transcription.
N63|220|127|39|kept|Beta integration proves all normalized coefficients equal1; actual integrals are recomputed.
N64|220|127|39|kept|The coefficient result uses the stated positive orientation and PD normalization.
N65|220|128|39|flagged for scan check|The inserted binomial factor is mathematically necessary in the final recurrence; its ink placement remains open.
N66|220|128|39|kept|Generating-function proof and84 finite tests settle the final recurrence under the explicit reading.
N67|210|110||kept|The cancelled augmentation demand is not restored as a live axiom.
N68|210|109,110||kept|Peuvent/voudrait and implique preserve the weakened logical force.
N69|221|193||kept|Sullivan§5 matches the add-and-kill construction, including potentially infinite steps; donor authorship remains unknown.
R01|223|132||corrected|The formal-homomorphism lemma is proved across95→105→101, not wholly left unproved.
R02|224|134||kept|Cycle-lattice positivity and orientation invariance require nodal edges and positive thicknesses.
R03|223|130|135|kept|Relative analytic exponential is explicitly admitted as donor background.
R04|223|132||flagged for scan check|The corollary self-reference should be compared with lemma13.2.1; frozen numbering retained.
R05|223|133||kept|The corollary uses the completed lemma and its spanning-period hypotheses.
R06|224|135||kept|The one-node reduction separates graph rank0 and1 cases.
R07|224|135||kept|Weighted thickness formula is a separate extension of the regular total-space formula.
R08|223|131||kept|Relative analytic Lie/lattice correspondence has smooth connected-fibre hypotheses.
R09|223|131||kept|Proper abeloid case imposes locally constant lattice of twice the complex rank.
R10|225|136|130|kept|Transport and functoriality are donor assertions with omitted routine verifications.
R11|225|136|130|kept|Transpose symmetry uses fixed Cartier/Poincaré conventions; it is not arbitrary sign-free duality.
R12|225|136|130|corrected|Néron–Severi symmetry does not require ampleness, but positivity does; equivalence uses nondegeneracy.
R13|225|136|130|kept|The tedious formal checks are explicitly deferred to the reader and recorded as such.
R14|225|501|131|kept|Deeper integral positivity is published in10.4 and reduced to Jacobians; source collation is not a new proof.
R15|225|136||flagged for scan check|The dual-of-A wording conflicts with the bidual formula; keep diplomatic text unchanged.
R16|227|139|41|kept|Potentially semistable normalization is rational and ramification-independent; integral descent is queried.
R17|227|139|41|kept|No exact general later settlement verified; this bounded result does not establish current openness.
R18|227|140|41|kept|The elliptic rank-one case is a distinct assertion from the general integrality question.
R19|227|140||flagged for scan check|v(j) also occurs in print; valuation/sign conventions must precede any proposed minus sign.
R20|226|138||kept|The mixed extension and orthogonality data define the all-primes pairing under inherited assumptions.
R21|226|138||flagged for scan check|F_eta versus E_eta changes the partial extension and needs source/ink comparison.
R22|226|199|134|kept|Finite extension/inertia identity is explicitly left to the reader and is separate from the p-primary definition.
R23|226|137|40|kept|de Jong Cor1.2 settles the equal-characteristic DVR full-faithfulness input without the F-crystal p-basis hypothesis.
R24|226|502|56|kept|Alternative good-reduction route uses9.5.6 and11.6.2(a); it is not the same omitted proof as general Tate faithfulness.
R25|226|197|132|kept|Global regular dimension-one extension is separately left to the reader in9.5.6.3.
R26|226|198|133|kept|Transition compatibility is an actual finite-level check required before taking the ℓ-adic system.
R27|226|137|40|kept|Characteristic-zero proviso and equal-characteristic expectation are preserved chronologically.
R28|226|137|40|kept|Full faithfulness and extension as a mixed object use different parts of the argument.
R29|228|141|42|corrected|11.5.2(a) gives rational nondegeneracy including p without10.4; the integral refinement uses10.4.
R30|228|141|42|kept|The component cokernel is a semistable henselian-trait theorem, not a general nonsemistable pairing theorem.
R31|228|142|42|kept|Finite prime-to-p pairing and the p-primary conclusion are distinguished.
R32|228|142||flagged for scan check|The apparent D_l target for Q_l-vector pairing also needs published-source interpretation.
R33|228|142||kept|A target notation doubt does not refute rational nondegeneracy.
R34|226|197||flagged for scan check|An extending group over S must be distinguished from its generic fibre X_eta.
R35|205|137,140||flagged for scan check|Bracket numbers19/33 versus20/36 signal bibliography/version collation, not permission to edit the transcription.
O01|230|||kept|Conditional CP² square-divisibility obstruction is reproved and does not refute the weighted theory.
O02|314|||kept|Represented-point H0 diagnostic depends on coefficients and chain grading; no missing τ∞ definition is invented.
O03|232|||kept|Bézout recovery uses several admissible weights; exact coefficients and the general gcd argument are retained.
O04|201|||kept|Weight-additive multiplication does not make each fixed positive weight a subalgebra.
O05|220|127|39|kept|Beta integral is independently derived; the mathematical value does not determine pale ink.
O06|220|128|39|kept|The final recurrence is proved under the explicitly reconstructed binomial convention.
O07|218|125||kept|Translation proof works over arbitrary coefficient rings when all Hasse operators are used.
O08|234|||kept|A tetrahedral-sphere nerve gives terminal groupoid completion without higher contractibility.
O09|284|||corrected|S² versus point tests only the quoted truncated hunch; the unseen project theorem is not refuted.
O10|280,229|||kept|Numerical/binomial operations differ from PD; no literal theorem transfer is allowed.
O11|216|117,122||kept|Infinite linear dual gives a product; degreewise finite duality does not imply global reflexivity.
O12|233|||kept|Ordinary simplex colimit does not by itself prove derived invariance or descent.
L01|237,276|172,173||kept|Cartan§7 is an exact attributed publication; Miller preprint circulation and1978 publication are distinguished.
L02|277,306|||corrected|Cenkl–Porter1982 adds DASH and higher products; theorem pages were opened with strict p<q.
L03|305|||corrected|Garvín Th4.2 explicitly gives p<q for every simplicial set; vague up-to wording is not strengthened.
L04|307|||corrected|Cubical theorem uses Qq coefficients, weight-sum products and a finite-type hypothesis in§4.
L05|278,313|||corrected|Dwyer comparison is checked through Scheerer–Tanré1991; original1979 full proof not obtained.
L06|279|||kept|Mandell2006 integral E∞ theorem classifies finite-type nilpotent spaces, faithful but not full.
L07|308|||corrected|Mandell2001 full embedding uses Fp-bar and finite p-type; finite-field version has extra maps.
L08|280|||kept|Ekedahl numerical models are unique up to numerical homotopy; numerical maps are not group homomorphisms.
L09|281|||kept|Toën simply-connected finite-type affinization is faithful/object-injective with retraction, not full.
L10|282|||kept|Horel cosimplicial binomial rings recover nilpotent finite-type spaces; general connected finite-type result is completion.
L11|310|||corrected|Richter–Sagave strict multiplication is in a diagram category and its homotopy colimit is E∞.
L12|275,236|||corrected|Quoted PS withdrawal and local scan100 retraction concern different statements; external target remains unverified.
L13|216,275|||corrected|Constructed integral-chain base change differs from forgetting an arbitrary module structure in unavailable PS context.
L14|311|||kept|Cenkl1989 obstruction requires all its functorial/cochain/unit hypotheses; weighted modules are not excluded.
L15|221|129,193,194,195,196||kept|Sullivan comparison is rational and qualified; it neither proves an integral theorem nor attributes donor N27.
'''
rows=[]
for line in data.strip().splitlines():
 eid,ins,cns,pns,verdict,reason=line.split('|',5)
 its=[f'SA08-{i}' for i in ins.split(',') if i]
 rows.append({'embedded_id':eid,'parent_entry_id':'MPL_136_095-141#'+{'N':'6','R':'7','O':'8','L':'9'}[eid[0]],'notes_lines':source[eid]['notes_lines'],'item_ids':';'.join(its),'claim_ids':';'.join('SA08-C'+c for c in cns.split(',') if c),'problem_ids':';'.join('MP-SA08-'+p for p in pns.split(',') if p),'verdict':verdict,'reason':reason,'actual_manuscript_locators':'; '.join(dict.fromkeys(items[i]['lines'] for i in its)),'evidence_type':'direct reading of embedded note and actual passage; scope-specific proofs/source matches in linked records'})
assert len(rows)==131 and {r['embedded_id'] for r in rows}==set(source)
with (out/'embedded_coverage.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'embedded_entries':len(rows),'manual_dispositions':True,'all_source_ids_covered':True}))
