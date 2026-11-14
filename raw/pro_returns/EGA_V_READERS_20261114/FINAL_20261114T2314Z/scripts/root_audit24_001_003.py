"""Save the completed visual review of cote24 sites1--3."""
from pathlib import Path
import csv
from audit_record import source_path, save, aggregate
from root_review_support import ReviewedPage

ROOT = Path(__file__).resolve().parents[1]
notes = {r['key']:r for r in csv.DictReader((ROOT.parent/'source/transcription/ega_v_cote24_blass/NOTES.tsv').open(), delimiter='\t')}

for n in (1, 2, 3):
    key=f'ega24_24_{n:03}'
    p=ReviewedPage(source_path(key).read_text())
    if n==1:
        observations=[
            'The upper numeral1 has a regular serif printed appearance; no pen stroke is visible in it. Its production by stamp versus a separate type element cannot be settled from this image.',
            'The numeral V has two short straight horizontal rules, above and below, of regular typed appearance. The original overline/underline encoding is retained; no handwritten correction is visible.',
            'Both halves were viewed, including the otherwise blank lower half. The upper-left dark/rust-colored mark has irregular paper-stain contours and contains no recoverable character.',
            'No long handwritten passage occurs.'
        ]
        p.note('7--15','Title, stage and translator lines','All words, the zero, hyphen, V rules and names agree with the supplied scan.','confirmed','Every title line and both blank-margin regions were read against the images.','full-text')
    elif n==2:
        observations=[
            'The upper numeral2 has the same regular serif appearance as site1, distinct from the monospaced body. No handwritten layer is discernible in it.',
            'The upper-left streak and small black spot contain no legible writing; they are not inserted into the text.',
            'The body asterisk after the bracketed translator query and the bottom-left Ask AG. are penned. The enlarged note confirms a final point after G.',
            'The handwritten matter consists of the asterisk and short note, not a long passage.'
        ]
        p.note('9--43','Complete Summary text','The typing, punctuation, reorganize???, grassmonians, No/No. forms, bracketed query and handwritten note agree with the scan.','confirmed','Every line in both halves was compared, including the overlapped middle lines and the note crop.','full-text')
        p.note('11','reorganize???','The three question marks are typed translator matter. French counterpart: cote25/site2, Commentaires, réorganisation de fond en comble.','cross-reference','The query is preserved; the checked French passage identifies its source without correcting Blass.','cote24-crossreference')
        p.note('31','[Ask AG if No16 has ever been written.]','The bracketed query is typed. Its source context is cote25/site2, Je n’ai pas encore rédi- le nº16, and cote25/site3, ainsi que le nº16 des présentes notes.','cross-reference','This is an added translator query, and the references identify the French statements it queries.','cote24-crossreference')
        p.note('43','* Ask AG.','Handwritten query linked by the body asterisk to the No16 bracket; French context cote25/sites2--3.','cross-reference','The handwritten query is retained verbatim and is not answered editorially.','cote24-crossreference')
        p.note('Summary order','Summary precedes contents','Cote24/site2 places the translated Commentaires before the contents at site3; the French Commentaires follow the contents on cote25/site2 and continue on site3.','comparison-recorded','Order compared with the checked French pages; neither source order is altered.','cote24-comparison')
    else:
        observations=[
            'The numeral3 is a regular serif printed form, with no visible pen addition.',
            'The upper-left rust-colored and dark spots contain no letter or readable notation.',
            'The title underline is straight and typed; all sixteen entries are typed. No handwritten addition is visible.',
            'No long handwritten passage occurs.'
        ]
        p.note('7--47','Contents, entries1--16','Every entry, number and line continuation agrees with the image; Grassmanians and forementioned are the actual typing.','confirmed','Both full scan halves, including the blank lower region, were read; no standard spelling is substituted.','full-text')
        p.note('Contents correspondence','Hyperplane Sections and Conic Projections','The sixteen headings correspond to the contents at cote25/site2; this page supplies Blass’s English wording.','comparison-recorded','Checked French contents used only to record coverage, not to replace any English reading.','cote24-comparison')
    entries=notes[key]['notes'].split(' | ')
    assert len(entries)==len(observations),(key,len(entries),len(observations))
    for i,(before,image) in enumerate(zip(entries,observations),1):
        p.note(f'NOTES item{i}',before,image,'checked','This listed concern was independently considered during the complete scan comparison.','NOTES')
    text,decisions=p.finish()
    save(key,text,decisions,0,'Both full scan halves were viewed and every line, numeral, punctuation mark and relevant margin compared; site2 handwritten note also inspected in an enlarged crop.')

print(aggregate())
