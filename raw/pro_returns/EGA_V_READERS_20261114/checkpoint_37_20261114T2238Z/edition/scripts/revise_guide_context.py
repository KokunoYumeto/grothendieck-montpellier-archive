"""Document editorial prose repairs and add verified published-EGA context.

This script never edits a checked transcription or an annotated text master.
"""
from pathlib import Path
import csv
import datetime
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
records = ROOT / 'records' / 'GUIDE_REVISIONS.tsv'
fields = ['utc', 'file', 'kind', 'before_sha256', 'after_sha256', 'reason']

def save(path, before, after, kind, reason):
    if before == after:
        return
    path.write_text(after, encoding='utf-8')
    row = dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
               file=str(path.relative_to(ROOT)), kind=kind,
               before_sha256=hashlib.sha256(before.encode()).hexdigest(),
               after_sha256=hashlib.sha256(after.encode()).hexdigest(), reason=reason)
    exists = records.exists()
    with records.open('a', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t')
        if not exists:
            writer.writeheader()
        writer.writerow(row)

# Root-authored guide prose has several word/number boundary typing slips.
# Restrict this repair to an explicit set of editorial nouns, outside URLs.
for path in sorted((ROOT / 'guide_parts').glob('IV20_*.tex')):
    before = path.read_text(encoding='utf-8')
    after = re.sub(r'\b(Site|site|sites|section|sections|paragraph|paragraphs|number|numbers|reference|references|Proposition|proposition|Corollary|corollary|remarks|formulations|using|as|to|of|including|between|new|and|is|on|at|read|legibly|IV|III)(?=\d)', r'\1 ', before)
    after = re.sub(r'(?<=\d)and(?=\d)', ' and ', after)
    save(path, before, after, 'editorial-spacing',
         'Insert omitted word/number spaces in guide prose only; no source reading or mathematical expression is changed.')

path = ROOT / 'guide_parts' / 'IV20_05.tex'
before = path.read_text(encoding='utf-8')
old = 'published EGA IV references explicitly written here include 11.3, 12.1.1, 12.1.4 and 15.2.2.'
new = ('the manuscript explicitly cites 11.3, 12.1.1, 12.1.4 and 15.2.2. '
       'The published numbering needs care: EGA IV 12.1.4 is a remark about fibre dimension, '
       'whereas the published list of geometric fibre properties occurs in 12.1.6. '
       'The manuscript number is preserved. See '
       r'\href{https://www.numdam.org/articles/10.1007/BF02684343/}{EGA IV, third part, 12.1.4 and 12.1.6, pp.\ 177--178}.')
if old in before:
    save(path, before, before.replace(old, new), 'published-reference-context',
         'Checked published EGA IV 12.1.4 and 12.1.6; distinguish their printed numbering from the reference actually written in the prenotes without altering it.')

path = ROOT / 'guide_parts' / 'IV20_06.tex'
before = path.read_text(encoding='utf-8')
old = 'the explicit published EGA IV reference is 15.6.3.'
new = 'the manuscript cites EGA IV 15.6.3. The precise concordance of that citation with the published numbering remains unestablished here.'
if old in before:
    save(path, before, before.replace(old, new), 'reference-status',
         'Avoid claiming a verified published-number concordance that the available primary-source retrieval has not established.')

path = ROOT / 'guide_parts' / 'iv16_singular_supersingular.tex'
before = path.read_text(encoding='utf-8')
old = 'The construction proceeds through the sections $d^i\\phi$ of the sheaves of principal parts.'
new = (old + ' The published reference for principal parts is '
       r'\href{https://www.numdam.org/articles/10.1007/BF02732123/}{EGA IV 16.3.1--16.3.2}; '
       'the use of the diagonal there gives the context for these differential constructions.')
if old in before and new not in before:
    save(path, before, before.replace(old, new), 'published-reference-context',
         'Verified the definition of principal parts and the two structure homomorphisms in published EGA IV 16.3.1--16.3.2.')
before = path.read_text(encoding='utf-8')
old = 'It then defines an augmentation of ordinary quadratic type through a nondegenerate invertible relation Module in degree two.'
new = (r'The terminology can be compared with \href{https://www.numdam.org/articles/10.1007/BF02732123/}{published EGA IV 16.9.1--16.9.3}, '
       'which defines regular and quasi-regular ideals and immersions and uses the symmetric-algebra comparison in 16.9.3. '
       + old)
if old in before and new not in before:
    save(path, before, before.replace(old, new), 'published-reference-context',
         'Verified the published definitions and their displayed symmetric-algebra map; retain the author\'s question about his terminology.')

# The supplied English terminology standard applies to editorial guide prose.
# Preserve every quoted source fragment while adjusting the reviewed English words.
spellings = {'fibre':'fiber', 'fibres':'fibers', 'fibrewise':'fiberwise',
             'neighbourhood':'neighborhood', 'neighbourhoods':'neighborhoods',
             'cancelled':'canceled', 'cancelling':'canceling', 'Artinian':'artinian'}
for path in sorted((ROOT / 'guide_parts').glob('*.tex')):
    before = path.read_text(encoding='utf-8')
    parts = re.split(r"(``.*?'')", before, flags=re.S)
    for i in range(0, len(parts), 2):
        for oldword, newword in spellings.items():
            parts[i] = re.sub(r'\b' + oldword + r'\b', newword, parts[i])
        parts[i] = re.sub(r'\b(Remark|remark|Theorem|theorem|Corollary|corollary|Proposition|proposition|Lemma|lemma|Site|site|sites|Section|section|sections|paragraph|paragraphs|number|numbers|reference|references|IV|III)(?=\d)', r'\1 ', parts[i])
    after = ''.join(parts)
    save(path, before, after, 'editorial-terminology',
         'Apply the supplied English spelling and lower-case terminology to guide prose and repair word/number spacing; quoted source fragments remain unchanged.')

path = ROOT / 'guide_parts' / 'iv21_4_linear_systems.tex'
before = path.read_text(encoding='utf-8')
old = 'Grothendieck says that this part should refer to the calculations'
addition = (r'On site 130, the written definition \(F_o=F\otimes_A k\) is followed by the phrase ``fibre réduite''; '
            r'the argument also says \(h_o\) is surjective immediately after naming the preceding homomorphism \(h_o^*\). '
            r'Site 131 gives the Hom expression the subscript \(\underline O_{X_o}\) and the target \(\underline O_{P_o}\). '
            'These literal choices remain in the text. ')
if old in before and addition not in before:
    save(path, before, before.replace(old, addition + old), 'checked-notation-observations',
         'Add the literal notation juxtapositions noted during translation; the scan reviewer independently confirmed the two site130 readings. No text correction or replacement mathematical argument is introduced.')
