"""Bounded primary-source byline audit of the fourteen class-A records.

This changes no mathematical statement. Class A identifies a counterpart in a
publication authored or coauthored by Grothendieck; it does not assign sole
discovery or chronological priority to him.
"""
import datetime,hashlib

locators={
 14:'Exposé IV, 1.2',
 15:'Exposé IV, 1.2 and 9.1.2–9.1.7',
 26:'Exposé IV, 1.2 and 9.1.2–9.1.7, especially 9.1.6(d)',
 29:'Exposé IV, 9.1.4 and 9.1.6(b,c,d), printed pp.433–435',
 31:'Exposé IV, 9.1, 9.2.1–9.2.6 and 9.3.4–9.3.5',
 34:'Exposé IV, 1.2; the other matched source remains separately attributed to Lack–Power',
 37:'Exposé IV, 1.2 and the sheaf presentation',
 38:'Exposé IV, 1.2; the exact local-ring comparisons remain separately attributed to Gabber–Kelly',
 45:'Exposé IV, 1.2 and 9.2–9.3',
 52:'Exposé IV, 9.2.1–9.2.6, especially Remark 9.2.3, printed pp.451–452',
 55:'Exposé IV, 9.2 and the site/flat-functor mechanism',
 57:'Exposé IV, 1.2 and the classifying topos B_G',
 86:'Exposé IV, Exercise 7.6(a–g), printed pp.414–417; 7.6(d), p.415, explicitly credits J.-E. Roos',
 107:'Exposé IV, Exercise 9.1.6(d), printed p.435; the other matched source remains separately attributed to Vickers',
}
assert {int(c['id'].rsplit('-',1)[1]) for c in claims if c['class']=='A'}==set(locators)
common=dict(
    publication='SGA 4, Tome I, Exposé IV, Topos (1972)',
    bibliography_key='SGA4I1972',
    exact_byline='par A. Grothendieck et J. L. Verdier',
    byline_locator='Original printed p.299; one-based PDF p.313',
    authors=['Alexander Grothendieck','Jean-Louis Verdier'],
    authorship_type='jointly authored exposé, not attribution from volume editorship',
    source_url='https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-1.pdf',
    primary_pdf='SA23_work/external/spaces/sga4-1.pdf',
    primary_images=['SA23_work/parts/groupes/external/authorship-IV-313.png',
                    'SA23_work/parts/groupes/external/authorship-IV-314.png',
                    'SA23_work/parts/groupes/external/authorship-IV76-429.png'],
    verification='The original title page, introductory credit paragraph, and Roos credit were rendered and visually read in this bounded authorship audit.',
    interpretation='Class A records an exact or explicitly limited published counterpart in a work coauthored by Grothendieck. It does not assign all matched results to his sole discovery, turn a secondary comparison into his work, or establish the date of an undated manuscript.')
rows=[]
for c in claims:
    n=int(c['id'].rsplit('-',1)[1])
    if n not in locators:continue
    credit=('Exercise 7.6(d), printed p.415, explicitly attributes the conservative-essential-points/presheaf criterion to J.-E. Roos, reference [12 c], Proposition 11. That discovery attribution is retained.'
        if n==86 else
        'The exposé introduction, §0.2 printed p.300, credits Giraud for the exactness characterization and says the gluing treatment follows Artin. Joint publication authorship is not sole discovery credit.')
    c['class_a_authorship_support']={**common,'matched_loci':locators[n],
                                    'additional_credit_boundary':credit,'audit_decision':'retain A'}
    if n==29:
        c['fate']=c['fate'].replace('Exact own later published result:','Exact counterpart in a jointly authored publication:')
    rows.append(dict(claim_id=c['id'],class_before='A',class_after='A',decision='retain A',
                     matched_loci=locators[n],byline=common['exact_byline'],
                     byline_locator=common['byline_locator'],additional_credit_boundary=credit))

# Retain the volume's correct editor metadata; identify the exact chapter
# authors in the annotation instead of treating volume editors as authors.
for i,b in enumerate(bibliography):
    if '@book{SGA4I1972,' in b:
        b=b.replace('annotation={SGA4, seminar1963--1964, publication1972.',
          'annote={SGA4, seminar1963--1964, publication1972. Expose IV, Topos, is jointly authored by A. Grothendieck and J. L. Verdier: the exact byline was visually checked on original printed p.299 / PDF p.313. The introductory p.300 separately credits Giraud and Artin; Exercise7.6(d), original p.415, credits J.-E. Roos. Publication authorship is not sole discovery or manuscript priority.')
        bibliography[i]=b
        break
else:raise AssertionError('SGA4I1972 bibliography record absent')

checked_ref('SGA4I1972',
    'Authorship audit only: original Exposé IV title page, printed299/PDF313, reads par A. Grothendieck et J. L. Verdier. Original printed300 credits Giraud and Artin; printed415/Exercise7.6(d) credits Roos. All fourteen A records cite this jointly authored exposé; no class was inferred from volume editorship and no sole-discovery or priority claim is made.',
    kind='used and rechecked in this run')
audit=dict(date=datetime.datetime.now(datetime.timezone.utc).isoformat(),
           scope='Only the authorship boundary for the fourteen existing Groupes class-A rows; no new mathematical or literature-fate investigation.',
           primary_evidence=common,
           primary_pdf_sha256=hashlib.sha256((BASE.parents[2]/common['primary_pdf']).read_bytes()).hexdigest(),
           findings=rows,retained_A=len(rows),changed_to_B=[],mathematical_statements_changed=False,
           chronology_wording_change='C029 now says jointly authored publication rather than own later published result; undated manuscript priority remains unknown.')
(BASE/'authorship_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
