#!/usr/bin/env python3
"""Stage a complete family and publish only explicitly selected standalone forms.

This supports a localized repair while another form remains frozen for review.
Unselected standalone TEX bytes and all PDF bytes remain untouched.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, os, shutil, tempfile

from build_readers import EDITION, PAGE_MAP, PAGES, certified_keys, validate_translation
from edition_core import read_tsv, write_tsv, sha256
from edition_render import build_family


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--family', choices=['en', 'fr', 'blass'], required=True)
    parser.add_argument('readers', nargs='+')
    args = parser.parse_args()
    keys = [r['key'] for r in PAGES if r['cote'] == ('24' if args.family == 'blass' else '25')]
    certified = certified_keys()
    if any(k not in certified for k in keys):
        raise SystemExit('A requested source page lacks its review record.')
    for key in keys:
        if not (EDITION/'checked_pages'/(key+'.tex')).is_file():
            raise SystemExit('Missing checked source '+key)
        if not (EDITION/'master_pages'/args.family/(key+'.tex')).is_file():
            raise SystemExit('Missing annotated master '+key)
    if args.family == 'en':
        ledger = {r['key']: r for r in read_tsv(EDITION/'records/EN_TRANSLATION_STATUS.tsv')}
        for key in keys:
            fr = (EDITION/'master_pages/fr'/(key+'.tex')).read_text()
            en = (EDITION/'master_pages/en'/(key+'.tex')).read_text()
            checked = (EDITION/'checked_pages'/(key+'.tex')).read_text()
            validate_translation(key, fr, en)
            current = dict(french_master_sha256=sha256(fr), english_master_sha256=sha256(en), checked_page_sha256=sha256(checked))
            if any(ledger.get(key, {}).get(k) != v for k,v in current.items()):
                raise SystemExit('Stale English provenance '+key)
    selected = set(args.readers)
    untouched = {p: sha256(p.read_text()) for p in (EDITION/'readers').glob('*.tex') if p.stem not in selected}
    runtime = EDITION.parent/'tex_runtime/reader_staging'
    runtime.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=args.family+'_', dir=runtime))
    try:
        for sub in ['master_pages', 'checked_pages', 'variant_records', 'scripts']:
            (stage/sub).symlink_to(EDITION/sub, target_is_directory=True)
        (stage/'records').mkdir()
        for name in ['TYPESETTING_PATCHES.json', 'MECHANICAL_SYNTAX_PATCHES.json', 'EN_VARIANT_NOTES.tsv', 'EN_VARIANT_OMISSIONS.tsv']:
            if (EDITION/'records'/name).is_file():
                (stage/'records'/name).symlink_to(EDITION/'records'/name)
        outputs = build_family(stage, args.family, keys, PAGE_MAP)
        available = {p.stem for p in outputs}
        if not selected <= available:
            raise SystemExit('Selected forms are outside the requested family: '+str(sorted(selected-available)))
        for name in sorted(selected):
            for rel in [Path('readers')/(name+'.tex'), Path('records')/('LINK_EXPECTATIONS_'+name+'.json')]:
                target = EDITION/rel
                temporary = target.with_suffix(target.suffix+'.selected-tmp')
                temporary.write_bytes((stage/rel).read_bytes())
                os.replace(temporary, target)
        fixfile = 'TYPESETTING_FIXES_'+args.family+'.tsv'
        fixes = [r for r in read_tsv(EDITION/'records'/fixfile) if r['reader'] not in selected]
        fixes += [r for r in read_tsv(stage/'records'/fixfile) if r['reader'] in selected]
        write_tsv(EDITION/'records'/fixfile, fixes)
        assert all(sha256(p.read_text()) == h for p,h in untouched.items()), 'An unselected standalone changed'
        stamp = datetime.now(timezone.utc).isoformat()
        log = EDITION/'records/SELECTIVE_BUILD_LOG.tsv'
        rows = read_tsv(log) if log.is_file() else []
        added = [dict(utc=stamp, reader=n, standalone_sha256=sha256((EDITION/'readers'/(n+'.tex')).read_text()), source_pages=len(keys), unselected_standalones_unchanged='true', purpose='Publish only selected complete forms from a private family staging build; no PDF is modified by this step.') for n in sorted(selected)]
        write_tsv(log, rows+added)
        print(json.dumps(added))
    finally:
        shutil.rmtree(stage)


if __name__ == '__main__':
    main()
