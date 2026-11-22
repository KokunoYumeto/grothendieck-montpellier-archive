from pathlib import Path
ROOT=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
for name in ['category_mss1_date_audit.md','category_correspondence_date_audit.md','category_CHECK_EVENTS.tsv']:
    p=ROOT/'notes'/name
    s=p.read_text()
    s=s.replace('printed archive footer','printed public PDF footer')
    s=s.replace('archive footers','public PDF footers').replace('archivefooters','public PDF footers')
    s=s.replace('carry archive\nfooters','carry public PDF\nfooters')
    s=s.replace('pencil numbers80–81','archival pencil numbers80–81')
    s=s.replace('pencil numbers 80–81','archival pencil numbers 80–81')
    s=s.replace('and pencil80–81','and archival pencil80–81')
    s=s.replace('The small pencilled sheet numbers','The small archival pencilled sheet numbers')
    p.write_text(s)
    print('CORRECTED_NUMBERING_TERMS',name)
p=ROOT/'notes/category_mss1_date_audit.md'
s=p.read_text()
paragraph='\nThe archive\'s official method identifies the lower-left pencil numbering as archival; the public PDF footer is a separate continuous sequence. Root/algebra directly checked the early jump in pencil numbering: physical2/3/4 correspond to archival pencil1/2/5 and public PDF footers1/2/3. This discrepancy does not identify the skipped pencil numbers3/4 as the1953 letter, and no such identification is made here.\n'
if 'official method identifies the lower-left pencil' not in s:
    p.write_text(s+paragraph)
