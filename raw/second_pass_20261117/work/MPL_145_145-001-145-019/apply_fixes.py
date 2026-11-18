# Apply the second-pass corrections of block MPL_145_145-001-145-019 (this checker's own script).
# Usage: python -I -B apply_fixes.py FIXFILE [--init]
#   --init copies the 19 first-pass page files into the output folder first (only if absent there).
# FIXFILE holds blocks: a line "@@ scanNNN", then the old text, a line "==>", the new text, a line "@@end".
# Each old text must occur exactly once in the current output file, or the script stops without writing.
import sys, os, shutil

BASE = 'C:/Users/user/Documents/grothendieck_archive_transcription_20261110'
SRC = BASE + '/returns/MPL_145_unzipped/pages'
OUT = BASE + '/second_pass/out/MPL_145'
NAME = 'MPL_145_145_scan{:03d}.tex'

def parse(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    fixes, i = [], 0
    while i < len(lines):
        if lines[i].startswith('@@ scan'):
            scan = int(lines[i][7:].strip())
            j = i + 1
            old = []
            while lines[j] != '==>':
                old.append(lines[j]); j += 1
            j += 1
            new = []
            while lines[j] != '@@end':
                new.append(lines[j]); j += 1
            fixes.append((scan, '\n'.join(old), '\n'.join(new)))
            i = j + 1
        else:
            i += 1
    return fixes

def main():
    fixfile = sys.argv[1]
    if '--init' in sys.argv:
        os.makedirs(OUT, exist_ok=True)
        for n in range(1, 20):
            dst = os.path.join(OUT, NAME.format(n))
            if not os.path.exists(dst):
                shutil.copyfile(os.path.join(SRC, NAME.format(n)), dst)
    fixes = parse(fixfile)
    texts = {}
    for scan, old, new in fixes:
        p = os.path.join(OUT, NAME.format(scan))
        if scan not in texts:
            texts[scan] = open(p, encoding='utf-8').read()
        c = texts[scan].count(old)
        if c != 1:
            print('STOP: scan %03d: old text found %d times:\n%s' % (scan, c, old))
            sys.exit(1)
        texts[scan] = texts[scan].replace(old, new)
    for scan, t in texts.items():
        open(os.path.join(OUT, NAME.format(scan)), 'w', encoding='utf-8', newline='\n').write(t)
        print('written scan %03d' % scan)
    print('%d fixes applied' % len(fixes))

if __name__ == '__main__':
    main()
