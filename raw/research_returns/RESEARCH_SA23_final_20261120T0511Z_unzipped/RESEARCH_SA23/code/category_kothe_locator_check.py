from pathlib import Path
import unicodedata
ROOT=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
text=(ROOT/'notes/category_date_Schneps_chapter4.txt').read_text()
for page_no,page in enumerate(text.split('\f'),1):
    normal=unicodedata.normalize('NFC',page)
    if 'Köthe' in normal:
        print('PHYSICAL_PAGE',page_no,'FOOTER',repr(page.strip().splitlines()[-1]))
        for line_no,line in enumerate(normal.splitlines()):
            if 'Köthe' in line:
                print('CONTEXT','\n'.join(normal.splitlines()[max(0,line_no-1):line_no+6]))
print('PRIMARY_A201_LOCAL_HTML',(ROOT/'notes/category_date_Kothe_A201.html').exists())
print('PRIMARY_I6_LOCAL_HTML',(ROOT/'notes/category_date_Kothe_I6.html').exists())
print('PRIMARY_I6_ENCLOSURE_LOCAL_HTML',(ROOT/'notes/category_date_Kothe_I6_enclosure.html').exists())
