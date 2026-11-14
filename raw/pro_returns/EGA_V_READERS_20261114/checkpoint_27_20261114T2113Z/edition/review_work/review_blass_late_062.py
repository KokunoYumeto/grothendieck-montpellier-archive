import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
N=['The upper-right62 is in the separate regular serif face and has no pen addition.','The second image is a blank lower page region; every edge and the faint surface marks were inspected, with no readable ink or handwritten addition.','There is no handwritten passage anywhere on this page.']
E=[
dict(line=13,before='provided x is not conical',image='Lowercase x is typed after provided',decision='comparison-recorded',reason='Checked cote25 site54, closing discussion of8.18(a), says “pourvu que X ne soit pas conique en x”. Blass’s lowercase x and wider quotation span remain.',category='cote24-comparison'),
dict(line=15,before='Bertinisque',image='Bertinisque with a straight typed underline',decision='confirmed',reason='Every letter and the underline are clear. The source spelling is retained; French54 has Bertiniesques.',category='underline'),
dict(line=16,before='section... change of projective immersion.',image='Three typed periods after section',decision='retained_ellipsis_with_french_crossreference',reason='Checked cote25 site54 ends with “au nº suivant du changement d’immersion projective”. The Blass ellipsis is preserved without assigning missing words.',category='cote24-query'),
dict(line='7–16',before='All prose and formulas',image='Every line matches the image, including lowercaseu, raisedrings/1 and all inequalities.',decision='confirmed',reason='The displayed inequalities in French54 are run into ordinary prose here; their literal signs and terms remain. Both scan parts and every margin read. No text correction was needed.',category='full-text')]
rec=complete('ega24_24_062',[],{},N,E,visual_notes='Both full scan parts inspected. All ten body lines and their formulas, the numeral62, underline, three-dot ellipsis, and every margin read; the entire second image is blank apart from nontextual surface specks. Closing§8 comparisons and the ellipsis link to checked French54.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
