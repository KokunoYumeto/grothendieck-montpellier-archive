from review_root import review, macro_occurrences, TEXT

def ds(key,name,reasons,resolved=None):
    s=(TEXT/'transcription/ps_pages'/(key+'.tex')).read_text();o=macro_occurrences(s,name);resolved=resolved or {}
    assert len(o)==len(reasons),(key,name,len(o),len(reasons))
    return [(resolved.get(i,x['source']),'doubt resolved' if i in resolved else 'doubt retained',reason) for i,(x,reason) in enumerate(zip(o,reasons),1)]

k='ps_134-2_012'
review(k,changes=[],doubts={'unsure':ds(k,'unsure',['The overtyped fourth character of Proof remains a blot, so the proposed o stays doubtful.']),'illegible':ds(k,'illegible',['The roughly three overwritten characters before onically remain unreadable; the likely intended word does not recover the struck letters.'])},notes=[
    'The final digit is visibly 4, with another digit overtyped beneath it. The former digit cannot be settled.',
    'The fourth character is overtyped too heavily to separate o from another letter; the doubt remains.',
    'The overtyped prefix is unreadable. The live suffix onically is preserved without supplying a conjectural c.',
    'The lowered exclamation mark has the same typewriter form and ink as the adjacent formula; it remains typed.',
    'The final s is visible despite a faint overtyped underletter; ponderings is retained.',
    'The old parenthesized III is overtyped; the following (2) is plain typing.',
    'The completion note and lower-left folio are handwritten; the remainder of the lower half is blank.'
],summary='Both halves viewed. Typed/handwritten layers, cancelled heading, overtyped letters and formula subscript checked. One uncertain letter and one illegible cancelled prefix remain; no reading change is warranted.')

k='ps_134-2_013'
review(k,changes=[
    (r'\unsure{À}',r'À','The accented capital A is legible; the long cancellation stroke terminates on the preceding et.'),
    (r'\unsure{notre}',r'notre','The letters of notre remain legible through the horizontal cancellation.'),
    (r'\unsure{commun}',r'commun','The cancelled word commun is legible above the hatched extension towards père.')
],doubts={'unsure':ds(k,'unsure',[
    'The capital A and its accent are legible; et bears the cancellation stroke.',
    'The beginning of rencontrer is overwritten; the proposed reading remains marked.',
    'The short cancelled word after Sibérie is densely hatched and cannot be settled.',
    'The cancelled word notre is legible.',
    'The letters commun are legible through the cancellation.',
    'The mark after père is merged with the hatching; s remains only a possible reading.'
],{1:'À',4:'notre',5:'commun'}),'illegible':ds(k,'illegible',[
    'The cancelled word after demi-siècle is hidden by dense pen strokes.',
    'The cancelled word after Sascha remains obscured by its horizontal retracing.'
])},notes=[
    'Both halves are wholly handwritten French, with pencil cancellation across the upper dedication.',
    'The four upper lines are crossed by broad diagonal pencil strokes; all their wording remains in deletion macros.',
    'The longest diagonal stroke ends on et. The accented A remains legible and is retained as live text.',
    'Rencontrer has overworked initial letters and remains doubtful.',
    'Alors que is underlined; the circled que j’aie is inserted between tangibles and de.',
    'Notre and commun can be read through their strokes and are resolved. The short word after Sibérie, the possible s after père and both densely cancelled words remain doubtful or illegible.',
    'The lower-left folio 13 is handwritten.'
],summary='Both halves of the French dedication closely read. Resolved the live À and the cancelled notre and commun; preserved the upper deletion and all unresolved overwritten or hatched wording. Five doubts remain.')
