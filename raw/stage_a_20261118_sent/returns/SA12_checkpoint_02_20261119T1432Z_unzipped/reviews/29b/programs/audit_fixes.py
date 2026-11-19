#!/usr/bin/env python3
"""Manually adjudicated corrections after exact primary-source comparisons."""
import json,pathlib,datetime
r=pathlib.Path(__file__).resolve().parents[1]
cs=json.loads((r/'claims.json').read_text()); by={x['id']:x for x in cs}
items=json.loads((r/'items.json').read_text()); ib={x['id']:x for x in items}
def fix(n,**kw):
 c=by[f'CL-SA12-{n}'];c.update(kw);c['present_status']='As of 2026-11-19: '+c['fate']
fix(203,
 statement='For the formal neighbourhood of a smooth curve, vanishing of pi_2 does not force the tame inertia extension to split. The written assertion of a trivial extension fails already for the zero section of a degree-one line bundle on a complex elliptic curve.',
 status_on_pages='false as stated if extension triviale means split extension; explicit assertion on scan96',
 computation='Finite Heisenberg commutators in exact_checks.json and review29a checks.py C14; a finite algebraic cover of degree n^3, retained after formal completion, is constructed in reviews/29a/formal_elliptic_nonsplitting.md.',
 fate='Let E/C be elliptic, L=O_E(0), M=L^n, n>1. The identity M^n=[n]^*L gives a connected finite tame cover M^×→L^× with central deck extension 1→mu_n→H→E[n]→1 and nondegenerate theta commutator. Completing along zero sections preserves this cover. A split extension with abelian base group and trivial cyclotomic action would have only abelian quotients, contradiction. Mumford1966 §1 Theorem1 and the symmetric pullback formula give the precise primary inputs. The later actual leaf, unlike the earlier note alone, explicitly asserts triviality after excluding P1; no scan reading is changed.',
 refs=['SA12_Mumford1966','SA12_MoonenTheta','SA12_Stacks03PK'],fate_date='Theta-group result published1966; this run checks its application to the manuscript on2026-11-19.')
ib['SA12-207']['check_reason']='N003 correctly isolates the Chern-class obstruction. Full cross-reading of K29-07 scan96 lines51–64 confirms the written curve assertion; a finite formal elliptic counterexample checks the stated setting. No ink reading is changed.'
ib['SA12-207']['reconstruction']='For an elliptic curve E/C and L=O_E(0), multiplication by n and M=L^n yield a connected tame cover M^×→L^× of degree n^3 with noncommutative theta deck group. Formal completion retains this cover, contradicting the split reading. This is this review’s reconstruction, using the opened Mumford theorem; see CL-SA12-203 and reviews/29a/formal_elliptic_nonsplitting.md.'
fix(210,
 statement='On the small category of finite abelian constant coefficients, H^1(X,C)=0 for every C implies that H^2(X,−) is left exact and hence prorepresentable; Artinianity gives strict prorepresentability. Identifying its representing proobject with a particular pi_2 of a universal procover requires a further homotopy comparison.',
 fate='The long exact sequence proves left exactness; the small-category category-of-elements argument proves prorepresentability, and Bourbaki Exposé195 A§3 Proposition3.1 and its corollary give strictness for Artinian objects. SGA4 I8.13.3 is a different accessible-category criterion, requiring filtered colimits and other hypotheses; it is not directly applicable to FinAb. SGA4 I8.3.3 is the relevant small-category criterion. Artin–Mazur provides an étale homotopy framework, but that does not identify every unrestricted site-level construction without hypotheses.',
 refs=['SA12_Bourbaki195','SA12_SGA4I','SA12_ArtinMazur1967','SA12_ArtinMazur1969'])
fix(233,
 statement='For g:Y→S and h:X→S locally of finite presentation, an S-morphism f:X→Y is unramified iff every fibre map f_s is unramified. For f locally of finite presentation, smoothness at x is equivalent to flatness at x plus smoothness of the fibre there, and to the displayed formal-smoothness condition.',
 fate='The smoothness equivalences match final EGA IV4 Theorem17.5.1 (1967). The preceding typescript proof matches final Proposition17.4.9. Crucially, the draft fibrewise proposition labelled17.4.10 was not retained at that number: final17.4.10 is a remark about formally unramified morphisms locally of finite type. The draft proposition follows from final17.4.1(d), since the f-fibre over y equals the f_s-fibre. These final passages were read in the downloaded primary PDF; the numbering difference is recorded rather than silently equated.',
 confidence='high')
fix(241,
 **{'class':'C'},
 fate='The opened EGA IV4 and SGA1 passages establish the local unramified/smooth machinery and the global irreducibility argument. Avoidance of a locus with image dimension<s is immediate for a generic codimension-s linear section. However, the exact combined unibranch/normal/smooth formulation has not been identified with one unchanged printed theorem; its local-property clauses and field-extension hypotheses remain separated. This is a partial precise match, not an assertion that every clause is still open.')
fix(250,fate_date='Classical Nullstellensatz predates these leaves; modern exact comparator Stacks10.34.1, accessed2026-11-19.')
fix(251,fate_date='Bourbaki Topologie générale ChaptersI–II first published1940; opened English reprint describes1971 translation. Exact date/edition of the reused sheet remains unidentified.')
fix(273,refs=by['CL-SA12-273']['refs']+['SA12_Stacks02LR'],fate=by['CL-SA12-273']['fate']+' Stacks37.43.2 (02LR) supplies the quasi-finite separated normalization factorization; apply it to quasi-compact local pieces before invoking the global finite-component argument, so quasi-compactness is not assumed at the step being proved.')
# Dates below are explicit comparator publication dates, not invented manuscript dates.
sgathree=[214,221,222,228,229,231,232,249,261,267,269]
sgaone=[202,204,207,208,211,212,236,242,243,246,247,252,253,254,255,256,257,258,259]
for n in sgathree:
 c=by[f'CL-SA12-{n}'];c['fate_date']='SGA3 seminar1962–1964; first publication1970; corrected edition2009. Individual undated leaves are not thereby dated.'
for n in sgaone:
 c=by[f'CL-SA12-{n}'];c['fate_date']='SGA1 seminar1960–1961; first publication1971; SGA7 publication1972–1973 where cited. No manuscript date inferred.'
for n in [223,224]:by[f'CL-SA12-{n}']['fate_date']='Relative-group obstruction compared with Antei preprint2015; independent counterexample checked2026-11-19, with no novelty claim.'
for n in [225,226,234,235]:by[f'CL-SA12-{n}']['fate_date']='Standard algebra predating these leaves; modern comparator accessed2026-11-19. Exact typescript attribution not established.'
for n in [263,264,268,270,271,272]:by[f'CL-SA12-{n}']['fate_date']='Bourbaki Exposé195 February1960/publication1960; SGA3 first publication1970; Bhatt–Scholze preprint2013-09-04/revision2014-12-17/publication2015 where applicable.'
by['CL-SA12-213']['fate_date']='Exact structure theorem checked in Milne2017 Proposition11.3; this comparator does not establish its first historical proof.'
by['CL-SA12-220']['fate_date']='No exact historical identification from the open-ended Witt-module fragment; related Nori papers1976,1982,1983.'
by['CL-SA12-237']['fate_date']='Modern root constructions; exact Stacks04V8 description accessed2026-11-19. No priority date inferred.'
by['CL-SA12-238']['fate_date']='Classical Kummer construction; étale/fppf distinction checked in Stacks03PK on2026-11-19.'
by['CL-SA12-260']['fate_date']='Gabber result in Déglise2007 exposition; proper/separable SGA1 cases published1971.'
by['CL-SA12-265']['fate_date']='Artin–Mazur conference1966/publication1967, monograph1969; SGA4I1972.'
by['CL-SA12-266']['fate_date']='SGA1 publication1971; SGA3 publication1970.'
by['CL-SA12-203']['statement']='The page asserts that the tame inertia extension in the formal curve setting is trivial when the indicated pi_2 vanishes, excluding the projective-line/empty-boundary case. Under the split-extension reading this is false, even for a degree-one line bundle on a complex elliptic curve.'
by['CL-SA12-223']['status_on_pages']='unjustified unrestricted equalizer step; later category-closure hypothesis must be retained'
by['CL-SA12-223']['statement']='The minimality proof needs the equalizer of the two structural-group maps to remain in the finite-flat admissible category, so that its coincidence reduction is a torsor in that category. Arbitrary finite-flat S-groups do not have this closure; the restarted source explicitly adds it.'
by['CL-SA12-224']['statement']='The asserted minimality criterion would make Hom_S-grp(G,G′)→Z(G′) injective for every minimal pointed admissible finite-flat torsor on a reduced connected S. It is false for all variable-base S-group maps; a category restricted as on scan143 is a different claim.'
by['CL-SA12-225']['status_on_pages']='proof sketched; source asserts the forward Chinese-remainder implication'
by['CL-SA12-236']['statement']='The diagram writes pi_1(Z)=Zhat^2 beside a spectrum of a complete local ring. On the literal interpretation Z=Spec C[[x,y]] this is false; the complement of the two coordinate divisors gives the plausible intended two-inertia object.'
by['CL-SA12-255']['statement']='The page proposes that a finite group action on an étale Y-scheme has an open free locus and an étale quotient, with an uncertain finite-case restriction. The finite étale version is valid; the arbitrary nonseparated version is false.'
by['CL-SA12-259']['statement']='The page compares a rational nodal curve with its normalization and writes a procyclic fundamental group deprived of its p-component. This is false for ordinary étale pi_1 in characteristicp: cyclic graph covers also exist in degreep.'
by['CL-SA12-270']['statement']='The page claims that a left-exact F:Set→Set preserving filtered intersections and strictly prorepresented by (K_i), with all lim K_i→K_i surjective, equals the functor I↦C(lim K_i,I_discrete) for the ordinary inverse-limit topology. All three assumptions can hold while this equality fails.'
fix(243,
 fate='SGA1 X2.10–2.11 proves the hyperplane version by generic Bertini and Zariski connectedness. For higher codimension, the reconstruction uses the universal Grassmannian incidence family, whose total space and geometric generic fibre are irreducible. Properness and Stein connectedness over the normal Grassmannian give geometrically connected special fibres. Applying this to connected finite étale covers requires the stated geometric-unibranch/local hypotheses. Merely iterating a special-hyperplane theorem would be insufficient because an intermediate special section need not be irreducible; no such iteration is used here.',
 computation='Incidence/Stein reconstruction checked with review29a; final published locator directly covers the hyperplane case, not a verbatim copy of every draft quantifier.')
fix(240,
 **{'class':'B'},
 fate='The general geometric-irreducibility assertion is established. Poonen–Slavov Theorem1.8 and §7 prove that the bad hyperplanes are a finite exceptional-image union plus a constructible set of dimension≤codim(image)+1; when image dimension≥2 this is a proper subset of the dual projective space. This covers arbitrary morphisms of geometrically irreducible finite-type varieties, without properness or normality. Generic successive sections give the stated higher-codimension range. SGA1X2.10 invokes Bertini under its proper/normal hypotheses; the exact broader development is classified B rather than silently assigned to that narrower printed invocation. The paper traces the earlier theorem to Jouanolou1983 Theorem6.3(4), whose text was not opened here.',
 refs=['SA12_SGA1','SA12_PoonenSlavov2020'],
 fate_date='Modern proof first arXiv2020-01-23, revised2020-08-04; online2020-08-04, print issue2022. Earlier SGA1 invocation1971; backward reference Jouanolou1983 is not a first-discovery claim.')
(r/'claims.json').write_text(json.dumps(cs,ensure_ascii=False,indent=2)+'\n')
(r/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
sm=json.loads((r/'claim_search_map.json').read_text())
for s in sm:
 c=by[s['claim_id']];s['opened_reference_keys']=c['refs'];s['scope_note']=c['fate']
 if s['claim_id'] in ['CL-SA12-250','CL-SA12-251','CL-SA12-273','CL-SA12-239']:s['search_batches'] += [f'web_root_{n:03}.json' for n in range(39,45)]
 if s['claim_id']=='CL-SA12-233':s['primary_file_check']='reference_cache/EGAIV4.txt lines2809–2840,3015–3055; read against manuscript106 lines319–356'
 if s['claim_id']=='CL-SA12-210':s['search_batches']+=['web_root_040.json'];s['primary_file_check']='reviews/29a/SGA4_8133_check.md'
 if s['claim_id']=='CL-SA12-203':s['primary_file_check']='reviews/29a/formal_elliptic_nonsplitting.md and its primary-source log'
 if s['claim_id'] in ['CL-SA12-203','CL-SA12-240']:s['search_batches']+=[f'web_root_{n:03}.json' for n in [45,46,47]]
 s['search_batches']=list(dict.fromkeys(s['search_batches']))
(r/'claim_search_map.json').write_text(json.dumps(sm,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'claims':len(cs),'items':len(items),'manual_primary_comparison_fixes':True,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
