#!/usr/bin/env python3
"""Build the final archive only after the actual required stopping review.

Preparing or importing this program does not authorize a stop or create a ZIP.
Run without arguments after prepare_final_status, fresh compilation, actual
visual approval, canonical consolidation and the final report refresh.
"""
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path, PurePosixPath
import csv
import hashlib
import json
import os
import re
import tempfile
import time
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = 'RESEARCH_SA22'
PAPER = 'RESEARCH_SA22_paper.pdf'
LIMIT = 500_000_000
EVENT_TYPES = {
    'targeted proof check', 'independent re-proof',
    'computation or formal certificate', 'used and rechecked in this run',
    'carried as background without fault found',
    "refuted, with the refined statement's id",
}
REQUIRED = {
    'RESEARCH_SA22_paper.tex', PAPER, 'RESEARCH_SA22_results.csv',
    'RESEARCH_SA22_references.bib', 'RESEARCH_SA22_report.md',
    'PROGRESS_LEDGER.md', 'CHECK_EVENTS.tsv', 'SOURCE_ACCESS_EVENTS.tsv',
    'logs/final_status.json', 'logs/integrated_build_summary.json',
    'logs/paper_visual_qa.json', 'logs/report_inventory.json',
    'logs/register_consolidation.json',
}
README = 'RESEARCH_SA22_README.md'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def local(name):
    path = ROOT / name
    require(path.resolve().is_relative_to(ROOT), 'Path escapes the project: ' + name)
    require(path.is_file(), 'Required file is absent: ' + name)
    return path


def read_json(name):
    return json.loads(local(name).read_text())


def instant(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    require(result.tzinfo is not None, 'Evidence timestamp lacks a timezone.')
    return result


def checked_stop_and_publication(now):
    status = read_json('logs/final_status.json')
    require(status['status'] == 'INCOMPLETE', 'Only the recorded INCOMPLETE stopping route is implemented.')
    name = status['final_archive_name']
    require(re.fullmatch(r'RESEARCH_SA22_final(?:_INCOMPLETE)?\.zip', name), 'Unexpected final archive name.')
    review_path = local(status['stopping_review_path'])
    prior_path = local(status['preceding_review_path'])
    review = json.loads(review_path.read_text())
    prior = json.loads(prior_path.read_text())
    latest = sorted((ROOT / 'logs').glob('progress_review_[0-9][0-9].json'))
    require(latest and latest[-1] == review_path, 'Final status does not reference the latest actual review.')
    require(sha(review_path) == status['stopping_review_sha256'], 'Stopping review changed.')
    require(sha(prior_path) == status['preceding_review_sha256'], 'Preceding review changed.')
    require(review['review'] == prior['review'] + 1 == status['stopping_review'], 'Reviews are not consecutive.')
    require(review['movement'] is False and prior['movement'] is False, 'Two actual no-movement reviews are required.')
    require(review['consecutive_stagnant_reviews'] >= 2 and prior['consecutive_stagnant_reviews'] >= 1, 'Required stagnation count not reached.')
    require(review['stop_required'] is True and review['next_review_utc'] is None, 'Research stop has not actually been triggered.')
    require(review['baseline_review'] == prior['review'] and review['baseline_actual_utc'] == prior['actual_utc'], 'Review baseline mismatch.')
    require(instant(review['due_utc']) - instant(prior['due_utc']) == timedelta(hours=1), 'Reviews were not scheduled one hour apart.')
    require(review['due_utc'] == prior['next_review_utc'], 'The stopping review differs from the previously scheduled review.')
    require(review['consecutive_stagnant_reviews'] == prior['consecutive_stagnant_reviews'] + 1, 'The recorded stagnation increment is inconsistent.')
    ledger = local('PROGRESS_LEDGER.md').read_text()
    for record in (prior, review):
        require(instant(record['due_utc']) <= instant(record['actual_utc']) <= now, 'Premature or future-dated review.')
        require(record['actual_utc'] in ledger, 'Actual review is absent from the ledger.')
        require(sha(local(record['assessment_note'])) == record['assessment_sha256'], 'Review assessment changed.')
    require(instant(prior['actual_utc']) < instant(review['actual_utc']), 'Actual review order is invalid.')
    require(status['research_stopped_utc'] == review['actual_utc'], 'Research-stop time differs from the actual stopping review.')
    framed = instant(status['framing_applied_utc'])
    require(instant(review['actual_utc']) <= framed <= now, 'Final framing predates the required stop.')
    require(status['assessment_note'] == review['assessment_note'] and status['assessment_sha256'] == review['assessment_sha256'], 'Final assessment identity mismatch.')

    build = read_json('logs/integrated_build_summary.json')
    qa = read_json('logs/paper_visual_qa.json')
    require(build['outcome'] == 'compiled' and build['passes'], 'No successful final compilation.')
    require(all(p['returncode'] == 0 for p in build['passes']), 'A final compilation pass failed.')
    require(not build['overfull_above_2pt'] and build['overfull_max_pt'] <= 2, 'Unresolved overflow exceeds two points.')
    for field in ('undefined_warnings', 'missing_glyphs', 'rerun_warnings', 'source_changed_during_build'):
        require(not build[field], 'Unresolved build condition: ' + field)
    require(build['source_hashes_before'] == build['source_hashes_after'], 'Sources changed during the final build.')
    require({'RESEARCH_SA22_paper.tex', 'RESEARCH_SA22_references.bib'} <= set(build['source_hashes_after']), 'Final build lacks mandatory source hashes.')
    for source_name, digest in build['source_hashes_after'].items():
        require(sha(local(source_name)) == digest, 'Current source differs from the approved build: ' + source_name)
    pdf_hash = sha(local(PAPER))
    require(pdf_hash == build['pdf_sha256'] == qa['pdf_sha256'], 'Current PDF, build and actual QA disagree.')
    require(build['run_id'] == qa['run_id'], 'Build and actual QA run IDs differ.')
    # build_paper records start times to whole seconds; final framing records
    # microseconds. Also require a different PDF and exact current source hashes.
    require(framed.replace(microsecond=0) <= instant(build['started_utc']), 'A fresh post-framing build is required.')
    require(pdf_hash != status['pre_framing_pdf_sha256'], 'The final PDF is still the pre-framing PDF.')
    require(str(qa['inspection']).startswith('PASS') and qa.get('inspected_by'), 'No actual visual approval.')
    require(instant(build['started_utc']) <= instant(qa['inspected_utc']) <= now, 'Visual approval timing is invalid.')
    pages = qa['rendered_pages']
    require(pages and all(isinstance(p, int) and 1 <= p <= qa['pdf_pages'] for p in pages), 'Invalid rendered-page evidence.')
    require(set(qa.get('full_resolution_pages_viewed', [])) <= set(pages), 'Full-resolution approval references unrendered pages.')
    for image in qa.get('contact_parts', []):
        local(image)
    for supplement in qa.get('supplementary_renderings', []):
        require(supplement['pdf_sha256'] == pdf_hash, 'Supplementary QA refers to a different PDF.')
        require(str(supplement['inspection']).startswith('PASS'), 'Supplementary rendering still lacks actual approval.')
        for image in supplement.get('images', []):
            local(image)

    with local('RESEARCH_SA22_results.csv').open() as stream:
        results = list(csv.DictReader(stream))
    with local('CHECK_EVENTS.tsv').open() as stream:
        events = list(csv.DictReader(stream, delimiter='\t'))
    with local('SOURCE_ACCESS_EVENTS.tsv').open() as stream:
        access = list(csv.DictReader(stream, delimiter='\t'))
    require(len(results) == len({r['id'] for r in results}), 'Duplicate canonical statement ID.')
    require({r['id'] for r in results} <= {e['statement_id'] for e in events}, 'Canonical statement lacks a check event.')
    require({e['type'] for e in events} <= EVENT_TYPES, 'Noncanonical mathematical event type.')
    inventory = read_json('logs/report_inventory.json')
    require(inventory['final_mode'] is True and not inventory['missing_outcome_labels'], 'Final report has not been refreshed.')
    require(instant(qa['inspected_utc']) <= instant(inventory['updated_utc']) <= now, 'Final report predates the actual final visual approval.')
    for key, count in [('numbered_statements', len(results)), ('canonical_check_events', len(events)), ('source_access_events', len(access))]:
        require(inventory[key] == count, 'Final report register count is stale: ' + key)
    require(local('RESEARCH_SA22_report.md').read_text().splitlines()[0] == 'INCOMPLETE', 'Final report must start INCOMPLETE.')
    counts = status['counts_at_research_stop']
    require(counts['numbered_statements'] == len(results) and counts['statement_statuses'] == dict(Counter(r['status'] for r in results)), 'Statement outcomes changed after the recorded research stop.')
    return status, {
        'stopping_review_path': status['stopping_review_path'],
        'stopping_review_sha256': sha(review_path),
        'preceding_review_path': status['preceding_review_path'],
        'preceding_review_sha256': sha(prior_path),
        'actual_review_times': [prior['actual_utc'], review['actual_utc']],
        'final_status_sha256': sha(local('logs/final_status.json')),
        'build_run_id': build['run_id'], 'pdf_sha256': pdf_hash,
        'pdf_pages': qa['pdf_pages'], 'overfull_above_2pt': 0,
        'actual_visual_inspector': qa['inspected_by'],
        'actual_visual_inspected_utc': qa['inspected_utc'],
        'source_hashes': build['source_hashes_after'],
        'numbered_statements': len(results), 'canonical_events': len(events),
        'source_access_events': len(access),
    }


def included_files():
    files = []
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if relative.parts[0] in {'literature', 'build', 'sources', 'upload', '__pycache__'}:
            continue
        if '__pycache__' in relative.parts or path.suffix.lower() in {'.zip', '.pyc'}:
            continue
        # Deliver only the current approved paper PDF, never source or older PDFs.
        if path.suffix.lower() == '.pdf' and relative.as_posix() != PAPER:
            continue
        if relative.parts[0] == 'qa' and path.suffix.lower() not in {'.txt', '.json', '.md'} and not path.name.startswith('paper_'):
            continue
        require(path.resolve().is_relative_to(ROOT), 'Included symlink leaves the project: ' + str(relative))
        files.append(path)
    return files


def prior_archives(status, current_names):
    archives = sorted(ROOT.parent.glob('RESEARCH_SA22_checkpoint_[0-9][0-9].zip'))
    require(archives and archives[-1].name == status['latest_checkpoint'], 'Latest preserved checkpoint disagrees with final status.')
    numbers = [int(re.search(r'_(\d+)\.zip$', p.name).group(1)) for p in archives]
    require(numbers == list(range(1, numbers[-1] + 1)), 'An earlier checkpoint archive is missing locally.')
    union = set()
    records = []
    for path in archives:
        with zipfile.ZipFile(path) as archive:
            names = [info.filename for info in archive.infolist() if not info.is_dir()]
        require(len(names) == len(set(names)), 'Duplicate member in a prior archive: ' + path.name)
        for name in names:
            relative = PurePosixPath(name)
            require(not relative.is_absolute() and '..' not in relative.parts and relative.parts[0] == PACKAGE, 'Unsafe prior archive member: ' + name)
            require(not name.lower().endswith('.zip'), 'Nested archive in an earlier checkpoint: ' + name)
        missing = set(names) - current_names
        require(not missing, 'Earlier checkpoint paths would be lost: ' + repr(sorted(missing)))
        union.update(names)
        records.append({'name': path.name, 'bytes': path.stat().st_size, 'sha256': sha(path), 'member_count': len(names)})
    return archives, records, union


def write_json_new(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')


def write_readme(status):
    """Write the final navigation note only after the actual stop/publication gates."""
    path = ROOT / README
    text = f'''# RESEARCH_SA22 — final incomplete research record

**Status: INCOMPLETE.** The research phase stopped at the actual review
{status['stopping_review']:02d} on {status['research_stopped_utc']}, after the two
consecutive scheduled reviews without qualifying movement required by the
user's stopping rule. The exact remaining obligations, qualifications, actual
review records and assessment hashes are in `logs/final_status.json` and
`PROGRESS_LEDGER.md`. The status does not certify completion of those obligations.

## Reading the package

- `RESEARCH_SA22_paper.pdf` is the single delivered, actually visually approved
  paper PDF. `RESEARCH_SA22_paper.tex`, `sections/` and
  `RESEARCH_SA22_references.bib` contain its reproducible source.
- `RESEARCH_SA22_report.md` gives the outcomes, limits, source access scope and
  computation provenance; `RESEARCH_SA22_results.csv` is the canonical statement
  register.
- `CHECK_EVENTS.tsv` records mathematical checks with their actual scope.
  `SOURCE_ACCESS_EVENTS.tsv` preserves four relocated retrieval-only records;
  the full source-route history remains in the notes and logs.
- `PROGRESS_LEDGER.md`, `notes/` and `logs/` preserve the research, source,
  review, build and actual visual-inspection evidence.
- `code/` contains the research certificates and administrative programs. Their
  saved outputs distinguish actual executions, partial failures and unexecuted
  preparation. No computation should be inferred solely from program presence.

## Reproduction and source exclusions

From the extracted `RESEARCH_SA22` directory, use Python 3 and a standard TeX Live
installation providing LuaLaTeX and BibTeX to compile the paper:

```sh
python3 code/build_paper.py
```

Compilation creates build logs; it does not certify visual quality. Rendering
with `code/render_paper_qa.py` and `code/render_supplementary_qa.py` is followed by
actual viewing of the relevant pages. `code/record_visual_approval.py` records
only that completed inspection. Rendering utilities have their own dependencies
declared in their source. Mathematical programs likewise retain their exact
dependencies and saved execution scope.

Supplied scans, downloaded source PDFs and literature bodies are excluded from
the archive. Source URLs, access and reading limits, and available source hashes
remain in the bibliography, notes and logs. Earlier checkpoint member paths are
retained; earlier checkpoint ZIPs and historical paper PDFs are not nested in
this archive. The single paper-PDF path contains the current approved version.

## Archive verification

The timestamped internal `logs/final_archive_validation_*.json` records the
actual validation completed before ZIP creation; the associated
`notes/final_archive_inventory_*.json` hashes its payload, excluding the
inventory's own recursive self-hash. The postcreation receipt
`logs/final_archive_creation.json` is retained outside the archive with the
completed ZIP's hash, size, elapsed time and all-member verification outcome.
That receipt cannot be inside the ZIP whose final hash it records; no self-hash
or circular inclusion is claimed.
'''
    if path.exists():
        require(path.read_text() == text, 'Existing final README differs from the validated stop; preserve it for review instead of overwriting.')
        return False
    with path.open('x') as stream:
        stream.write(text)
    return True


def main():
    started = time.perf_counter()
    now = datetime.now(timezone.utc)
    run_id = now.strftime('%Y%m%dT%H%M%S%fZ')
    temporary = None
    published = False
    target = None
    validation_path = None
    inventory_path = None
    phase = 'stop and publication guards'
    try:
        status, gates = checked_stop_and_publication(now)
        target = ROOT.parent / status['final_archive_name']
        receipt_path = ROOT / 'logs/final_archive_creation.json'
        require(not target.exists() and not receipt_path.exists(), 'Final archive or receipt already exists; refusing overwrite.')
        phase = 'payload preparation'
        readme_created = write_readme(status)
        files = included_files()
        relative_names = {p.relative_to(ROOT).as_posix() for p in files}
        require((REQUIRED | {README}) <= relative_names, 'A mandatory deliverable is absent.')
        names = {PACKAGE + '/' + name for name in relative_names}
        archives, earlier, prior_union = prior_archives(status, names)
        manifest = [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size, 'sha256': sha(p)}
                    for p in sorted((ROOT/'literature').rglob('*')) if p.is_file()]
        # Preserve the existing manifest path from checkpoints, with current source hashes.
        (ROOT/'notes/source_file_manifest.json').write_text(json.dumps({
            'at': datetime.now(timezone.utc).isoformat(),
            'note': 'Downloaded literature and supplied scans are not redistributed. URLs, source hashes and retrieval/read logs are retained.',
            'files': manifest,
        }, indent=2) + '\n')
        validated_at = datetime.now(timezone.utc)
        validation_path = ROOT / f'logs/final_archive_validation_{run_id}.json'
        inventory_path = ROOT / f'notes/final_archive_inventory_{run_id}.json'
        validation = {
            'phase': 'Actual precreation validation; archive integrity/size/hash are checked afterwards and recorded externally',
            'started_utc': now.isoformat(), 'validated_utc': validated_at.isoformat(),
            'created_utc': datetime.now(timezone.utc).isoformat(), 'status': 'PASS',
            'research_status': 'INCOMPLETE', 'final_archive_name': target.name,
            'publication_and_stop_gates': gates,
            'readme_created_in_this_attempt': readme_created,
            'identical_readme_from_prior_attempt_preserved': not readme_created,
            'all_prior_checkpoint_member_paths_preserved': True,
            'prior_checkpoints': earlier, 'prior_union_member_count': len(prior_union),
            'only_delivered_pdf': PACKAGE + '/' + PAPER,
            'nested_zip_members': [],
            'source_exclusion_policy': 'Exclude supplied sources, downloaded literature, build products and source-page images; retain authored proofs, registries, code, logs and paper QA images.',
            'inventory_path': str(inventory_path.relative_to(ROOT)),
            'external_postcreation_receipt': str(receipt_path.relative_to(ROOT)),
            'receipt_limitation': 'A complete archive cannot contain its own final hash; postcreation receipt is external and is not represented as included.',
        }
        write_json_new(validation_path, validation)
        files = included_files()
        file_records = [{'path': p.relative_to(ROOT).as_posix(), 'bytes': p.stat().st_size, 'sha256': sha(p)} for p in files]
        write_json_new(inventory_path, {
            'started_utc': now.isoformat(),
            'created_utc': datetime.now(timezone.utc).isoformat(), 'archive_name': target.name,
            'file_count_before_inventory': len(file_records), 'files': file_records,
            'inventory_self_exclusion': 'This inventory lists and hashes every earlier payload file; its own path is an additional archive member, without a recursive self-hash.',
        })
        files.append(inventory_path)
        expected = {PACKAGE + '/' + r['path']: r['sha256'] for r in file_records}
        expected[PACKAGE + '/' + inventory_path.relative_to(ROOT).as_posix()] = sha(inventory_path)
        require(prior_union <= set(expected), 'A prior member disappeared during preparation.')
        require([n for n in expected if n.lower().endswith('.pdf')] == [PACKAGE + '/' + PAPER], 'Final package must deliver exactly the current paper PDF.')
        phase = 'temporary archive construction and verification'
        with tempfile.NamedTemporaryFile(prefix=target.stem + '_', suffix='.partial', dir=ROOT.parent, delete=False) as stream:
            temporary = Path(stream.name)
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
            for path in files:
                archive.write(path, PACKAGE + '/' + path.relative_to(ROOT).as_posix())
        require(temporary.stat().st_size < LIMIT, 'Final archive is not strictly below 500 MB.')
        with zipfile.ZipFile(temporary) as archive:
            require(len(archive.namelist()) == len(expected) and set(archive.namelist()) == set(expected), 'Final member list differs from the prepared inventory.')
            for name, digest in expected.items():
                hashed = hashlib.sha256()
                with archive.open(name) as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                        hashed.update(chunk)
                require(hashed.hexdigest() == digest, 'Archive member hash/CRC check failed: ' + name)
        current = {PACKAGE + '/' + p.relative_to(ROOT).as_posix(): sha(p) for p in included_files()}
        require(current == expected, 'Authored files changed while final packaging was running.')
        latest_status, latest_gates = checked_stop_and_publication(datetime.now(timezone.utc))
        require(latest_status == status and latest_gates == gates, 'Stop or publication evidence changed during packaging.')
        require(all(sha(path) == record['sha256'] for path, record in zip(archives, earlier)), 'An earlier immutable checkpoint changed during final packaging.')
        # Same-filesystem exclusive hard link publishes without overwriting a race-created target.
        phase = 'exclusive archive publication'
        os.link(temporary, target)
        published = True
        temporary.unlink()
        temporary = None
        phase = 'external postcreation receipt'
        receipt = {
            'outcome': 'PASS', 'created_utc': datetime.now(timezone.utc).isoformat(),
            'path': str(target), 'files': len(expected), 'bytes': target.stat().st_size,
            'sha256': sha(target), 'elapsed_seconds': time.perf_counter() - started,
            'scope': 'Final archive construction, all-member content/CRC verification and current-source/actual-QA/stopping-rule validation; no research or mathematical certificate execution',
            'prior_checkpoint_count': len(archives), 'prior_union_paths_preserved': len(prior_union),
            'only_delivered_pdf': PACKAGE + '/' + PAPER,
            'internal_validation': str(validation_path.relative_to(ROOT)),
            'internal_inventory': str(inventory_path.relative_to(ROOT)),
            'self_hash_limitation': 'This postcreation receipt is outside the ZIP; its final ZIP hash is not claimed as an archive member.',
            'receipt_is_external': True, 'library_save_status': 'Not performed by this program',
        }
        write_json_new(receipt_path, receipt)
        print(json.dumps(receipt, indent=2))
    except Exception as error:
        if temporary is not None and temporary.exists():
            temporary.unlink()
        write_json_new(ROOT / f'logs/final_archive_runs/{run_id}_failed.json', {
            'outcome': ('Failure after publication; the already published archive is preserved'
                        if published else 'FAILED before archive publication'),
            'started_utc': now.isoformat(),
            'failed_utc': datetime.now(timezone.utc).isoformat(), 'phase': phase,
            'archive_published': published,
            'published_path': str(target) if published else None,
            'error': repr(error), 'elapsed_seconds': time.perf_counter() - started,
            'validation_path': str(validation_path.relative_to(ROOT)) if validation_path else None,
            'inventory_path': str(inventory_path.relative_to(ROOT)) if inventory_path else None,
            'retry_policy': 'Preserve every preparation and failure record; an existing README may be reused only if exactly equal to the newly validated expected text. An existing final archive or postcreation receipt always blocks automatic retry.',
        })
        raise


if __name__ == '__main__':
    main()
