"""A bookkeeping check, not a mathematical proof or a cycle computation."""
from pathlib import Path
import csv
import re

root = Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work')
labels = set()
for path in root.joinpath('sections').glob('b3_*.tex'):
    labels.update(re.findall(r'\\label\{((?:lem|prop|thm|cor):B-[^}]+)\}', path.read_text()))
with root.joinpath('part_b/part_b_LABEL_CHECKS.tsv').open() as stream:
    checked = {row['statement_label'] for row in csv.DictReader(stream, delimiter='\t')}
print('B3 fragment labels missing a Part B check crosswalk:', sorted(labels-checked))
for path in [root/'sections/b3_unit_cup_generation.tex', root/'sections/b3_all_bases_brauer_units.tex']:
    contents = path.read_text()
    print(path.name, 'braces', contents.count('{')-contents.count('}'),
          'display openings', contents.count('\\['), 'closings', contents.count('\\]'))
