#!/usr/bin/env python3
"""One authorized, bounded source-cache normalization; no network or mathematics.

Changes only fifteen selected MCP retrieval blocks and thirty-three OpenAIRE
description values.  Exact original file bytes stay outside the deliverable.
The unselected-value proof restores the selected values from the original and
compares the entire parsed document, both before and after the actual writes.
"""

from __future__ import annotations

import copy
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import time


ROOT = Path('/workspace/scratch/9c53b536a97f')
PROJECT = ROOT / 'RESEARCH_SA22'
CACHE = ROOT / 'source_reading' / 'named_source_cache_20261119'
MANIFEST = PROJECT / 'checks' / 'part_c_named_source_cache_normalization_manifest.json'
OUTPUT = PROJECT / 'code' / 'part_c_normalize_named_source_cache_output.json'
PREVIOUS = PROJECT / 'checks' / 'part_c_remaining_web_normalization_manifest.json'
PREVIOUS_HASH = 'e207ed61066cc5751c0fd8a854ba28b6611ebc88be856add53855549337ca9ef'
PFLUGER = 'part_a567_pfluger_offprint_variant_queries.json'
PAGE1 = 'part_a567_fujiwara1992_openaire_raw.json'
PAGE2 = 'part_a567_fujiwara1992_openaire_page2_raw.json'
EXPECTED = {
    PFLUGER: ('132efc985d2eaf7d8f5cfcec378bfafb178a1a96826a6fab5200f8e9a1564faa', 28420),
    PAGE1: ('c6cf049fa26dd4d337c8787ea36674ef1625149e0e143cd693be52aebd70bace', 602011),
    PAGE2: ('e2e67e6a410f5e3527fbffb4c4ce086107b4bc74a4c7eefb6a2fb8b1d0479997', 8852),
}
BLOCK_HASHES = [
    'f3fbcb7dd0de7ed4bd0b68ce551d69ba58c7beb35e6e216e54b1a6e8771465e3',
    '0520880140d637f6472e2a573e4f8d1cfff1547f4b0d41da5e83a2d99c7e761b',
    'd7e50fc63b2e86d3339e9d9cfebcd4982b6792f4847144f0fc6806a29ce3716e',
    '44f56ab09cc6ad0b992c7472d712402fd419ba3231f4eb6ae8b5b5e023617367',
    '7edc5655296c7928dfae68cb7aff9eb839eac8b2905ea26af5cb42304ee57530',
    '793c1ec274d6776c658d20c05bf4fe5168ae77e7d08c9f5a7fb403ca5d0ecd65',
    'a34509d518dc43c552bafc6a62bd76b2bfcaf78f242c5ccc0a4f294d3bc4a814',
    'cf0a4fd31fb6c8e3a83a264925bc5c6869b9a4cd8b6d8592b3b926357c1d7a90',
    '350ef826a229002d6597b0ccbdeaaafd5c7d88705089ff80067d6bb160d7c076',
    '141b15245fd3e1664a0ac1f327190da15afd4cbf6a04fca387bbbdbd08fd550e',
    '46d6d5a93a0dddc4bbc166177e6c16c52bbbd1d4a7d720f3c945891cc8d51089',
    'e5fedf8f9e778915a18fbb27bb71d3e4d8b9f2eb3df9f9a094d20ab3e92c01ee',
    '43da11aea1ee78dc6ea671b43206ac586050164eb2abb1d8b63ac698bc936000',
    '5704f44b8ee501874c2b176cbab48774fd2a5afb20cbb5e8bdcec404b362e304',
    'debb62550f209a5135870af80d32b86bf9086f94baf095f1c3383b904a3c9211',
    '9e1f8175fea74eb9815f943c67e4a57a23d823ebd230150833f6b5bec4c86130',
    'ca1c9a6f4778d399353bee2a18eea1eeebd52844115d7a4fbcd26a679d25357c',
]
KEEP_BLOCKS = {9, 13}
SELECT_BLOCKS = [i for i in range(17) if i not in KEEP_BLOCKS]
TEXT_POINTER = '/result/content/0/text'
URL_RE = re.compile(r'https?://[^\s<>\[\]{}\"]+')
DOI_RE = re.compile(r'10\.[0-9]{4,9}/[^\s<>\[\]{}\"]+', re.I)
ISBN_RE = re.compile(r'(?<!\d)(?:97[89][\d -]{10,17}\d)(?!\d)')
ACCESS_NOTICE = 'zbMATH Open Web Interface contents unavailable due to conflicting licenses.'


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical(x) -> bytes:
    return json.dumps(x, ensure_ascii=False, separators=(',', ':'), sort_keys=True).encode('utf-8')


def encoded(x) -> bytes:
    return (json.dumps(x, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def tokens(text: str) -> dict:
    # Exact matched tokens are retained without decoding, following, or guessing URLs.
    return {
        'url_tokens_exact': sorted(set(URL_RE.findall(text))),
        'doi_tokens_exact': sorted(set(DOI_RE.findall(text))),
        'isbn_tokens_exact': sorted(set(ISBN_RE.findall(text))),
    }


def pointer_escape(s: str) -> str:
    return s.replace('~', '~0').replace('/', '~1')


def desc_fields(x, pointer=''):
    if isinstance(x, dict):
        for key, value in x.items():
            p = pointer + '/' + pointer_escape(key)
            if 'description' in key.lower() or 'abstract' in key.lower():
                yield p, value
            yield from desc_fields(value, p)
    elif isinstance(x, list):
        for i, value in enumerate(x):
            yield from desc_fields(value, pointer + '/' + str(i))


def pointer_set(doc, pointer, value):
    segments = [s.replace('~1', '/').replace('~0', '~') for s in pointer.split('/')[1:]]
    cur = doc
    for s in segments[:-1]:
        cur = cur[int(s)] if isinstance(cur, list) else cur[s]
    final = segments[-1]
    if isinstance(cur, list):
        cur[int(final)] = value
    else:
        cur[final] = value


def verify_unselected_pfluger(old, new, original_parts):
    candidate = copy.deepcopy(new)
    new_text = candidate['result']['content'][0]['text']
    pieces = re.split(r'(\n-{8,}\n)', new_text)
    assert len(pieces) == len(original_parts) == 33
    assert pieces[1::2] == original_parts[1::2], 'Retrieval separators changed'
    for i in KEEP_BLOCKS:
        assert pieces[2*i].encode() == original_parts[2*i].encode(), 'Historical stub changed'
    for i in SELECT_BLOCKS:
        assert pieces[2*i] != original_parts[2*i], 'A selected block was not replaced'
        pieces[2*i] = original_parts[2*i]
    assert ''.join(pieces) == old['result']['content'][0]['text']
    candidate['result']['content'][0]['text'] = ''.join(pieces)
    assert candidate == old, 'An unselected Pfluger JSON value changed'


def verify_unselected_page1(old, new, selected):
    candidate = copy.deepcopy(new)
    for p, value in selected:
        pointer_set(candidate, p, copy.deepcopy(value))
    assert candidate == old, 'An unselected OpenAIRE JSON value changed'
    assert new['response']['header'] == old['response']['header']
    assert len(new['response']['results']['result']) == 25


def atomic_write(path: Path, data: bytes):
    temporary = path.with_name(path.name + '.normalization-tmp')
    assert not temporary.exists(), f'Unexpected existing temporary file: {temporary}'
    with temporary.open('xb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temporary, path)


def main():
    t0 = time.perf_counter()
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    # Refuse to repeat any completed mutation or overwrite its immutable evidence.
    assert not MANIFEST.exists() and not OUTPUT.exists(), 'Evidence already exists; inspect it rather than rerun'
    assert sha(PREVIOUS.read_bytes()) == PREVIOUS_HASH
    originals = {}
    docs = {}
    for name, (expected_hash, expected_size) in EXPECTED.items():
        raw = (PROJECT / 'code' / name).read_bytes()
        assert sha(raw) == expected_hash and len(raw) == expected_size, f'Preflight mismatch: {name}'
        originals[name] = raw
        docs[name] = json.loads(raw)

    selected = list(desc_fields(docs[PAGE1]))
    assert len(selected) == 33
    assert all(isinstance(v, dict) and list(v) == ['$'] and isinstance(v['$'], str) for _, v in selected)
    assert not list(desc_fields(docs[PAGE2]))
    old_text = docs[PFLUGER]['result']['content'][0]['text']
    parts = re.split(r'(\n-{8,}\n)', old_text)
    assert len(parts) == 33
    assert [sha(parts[2*i].encode()) for i in range(17)] == BLOCK_HASHES

    # Back up complete, exact current bytes, including the two already-normalized stubs.
    CACHE.mkdir(parents=True, exist_ok=True)
    for name in (PFLUGER, PAGE1):
        cache_path = CACHE / name
        if cache_path.exists():
            assert cache_path.read_bytes() == originals[name], 'Conflicting external backup'
        else:
            with cache_path.open('xb') as f:
                f.write(originals[name])
                f.flush()
                os.fsync(f.fileno())
        assert sha(cache_path.read_bytes()) == EXPECTED[name][0]

    new_pfluger = copy.deepcopy(docs[PFLUGER])
    new_parts = list(parts)
    block_records = []
    offsets = []
    pos = 0
    for piece in parts:
        offsets.append(pos)
        pos += len(piece)
    for index in SELECT_BLOCKS:
        block = parts[2*index]
        metadata = {
            'kind': 'retrieval_source_body_cache_pointer',
            'retrieval_block_index_zero_based': index,
            'title_line': block.splitlines()[0] if block.splitlines() else '',
            'source_reference_ids': sorted(set(re.findall(r'【([^】]+)】', block))),
            'retrieval_metadata_lines': [line for line in block.splitlines()[1:] if re.match(r'^【[^】]+】\s*\[wordlim:', line)],
            **tokens(block),
            'external_raw_file': str(CACHE / PFLUGER),
            'external_raw_file_sha256': EXPECTED[PFLUGER][0],
            'json_pointer': TEXT_POINTER,
            'original_character_range': [offsets[2*index], offsets[2*index] + len(block)],
            'original_characters': len(block),
            'original_utf8_bytes': len(block.encode()),
            'original_text_sha256': sha(block.encode()),
        }
        new_block = '[Retrieval body retained in the external source cache; provenance metadata follows.]\n' + json.dumps(metadata, ensure_ascii=False, sort_keys=True)
        new_parts[2*index] = new_block
        block_records.append({**metadata, 'replacement_text_sha256': sha(new_block.encode()), 'replacement_utf8_bytes': len(new_block.encode())})
    new_pfluger['result']['content'][0]['text'] = ''.join(new_parts)
    verify_unselected_pfluger(docs[PFLUGER], new_pfluger, parts)

    new_page1 = copy.deepcopy(docs[PAGE1])
    field_records = []
    for p, value in selected:
        text = value['$']
        metadata = {
            'kind': 'openaire_description_cache_pointer',
            'external_raw_file': str(CACHE / PAGE1),
            'external_raw_file_sha256': EXPECTED[PAGE1][0],
            'json_pointer': p,
            'original_value_canonical_json_sha256': sha(canonical(value)),
            'original_value_canonical_json_bytes': len(canonical(value)),
            'original_text_sha256': sha(text.encode()),
            'original_characters': len(text),
            'original_utf8_bytes': len(text.encode()),
            **tokens(text),
        }
        # This factual access notice is not a scientific abstract; retain it explicitly.
        if text == ACCESS_NOTICE:
            metadata['factual_access_notice'] = text
        compact = {
            'file': metadata['external_raw_file'],
            'json_pointer': p,
            'text_sha256': metadata['original_text_sha256'],
            'characters': metadata['original_characters'],
            'utf8_bytes': metadata['original_utf8_bytes'],
        }
        for key, values in tokens(text).items():
            if values:
                compact[key] = values
        if text == ACCESS_NOTICE:
            compact['factual_access_notice'] = text
        replacement = {'_source_cache': compact}
        pointer_set(new_page1, p, replacement)
        field_records.append({**metadata, 'replacement_value_canonical_json_sha256': sha(canonical(replacement))})
    verify_unselected_page1(docs[PAGE1], new_page1, selected)

    candidates = {PFLUGER: encoded(new_pfluger), PAGE1: encoded(new_page1)}
    # Verify all candidate bytes before writing either target.
    verify_unselected_pfluger(docs[PFLUGER], json.loads(candidates[PFLUGER]), parts)
    verify_unselected_page1(docs[PAGE1], json.loads(candidates[PAGE1]), selected)
    for name, candidate in candidates.items():
        path = PROJECT / 'code' / name
        assert path.read_bytes() == originals[name], 'Input changed during preparation'
        atomic_write(path, candidate)

    # Read back each actual file and prove the same equality, not merely an in-memory result.
    actual_pfluger = (PROJECT / 'code' / PFLUGER).read_bytes()
    actual_page1 = (PROJECT / 'code' / PAGE1).read_bytes()
    assert actual_pfluger == candidates[PFLUGER]
    assert actual_page1 == candidates[PAGE1]
    verify_unselected_pfluger(docs[PFLUGER], json.loads(actual_pfluger), parts)
    verify_unselected_page1(docs[PAGE1], json.loads(actual_page1), selected)
    assert (PROJECT / 'code' / PAGE2).read_bytes() == originals[PAGE2]
    assert sha(PREVIOUS.read_bytes()) == PREVIOUS_HASH

    duration = time.perf_counter() - t0
    completed = dt.datetime.now(dt.timezone.utc).isoformat()
    records = []
    for name in (PFLUGER, PAGE1):
        records.append({
            'file': 'code/' + name,
            'original_bytes': len(originals[name]),
            'original_sha256': sha(originals[name]),
            'normalized_bytes': len(candidates[name]),
            'normalized_sha256': sha(candidates[name]),
            'external_raw_file': str(CACHE / name),
            'external_raw_sha256': sha((CACHE / name).read_bytes()),
            'selected_blocks' if name == PFLUGER else 'selected_fields': block_records if name == PFLUGER else field_records,
        })
    manifest = {
        'operation': 'authorized minimal source-cache hygiene; no research or source-status movement',
        'started_utc': started,
        'normalization_verified_utc': completed,
        'normalization_and_verification_seconds': duration,
        'runtime_scope': 'preflight, exact external backups, transformations, atomic target writes, and actual-file readback/equality checks; excludes writing this manifest and compact output',
        'canonical_json_convention': 'UTF-8, ensure_ascii=False, separators=(comma,colon), sort_keys=True',
        'previous_manifest': {'file': str(PREVIOUS.relative_to(PROJECT)), 'sha256': PREVIOUS_HASH, 'link': 'Pfluger current original hash is the previous pass normalized hash; blocks 9 and 13 are preserved'},
        'files': records,
        'unchanged_page2': {'file': 'code/' + PAGE2, 'bytes': len(originals[PAGE2]), 'sha256': sha(originals[PAGE2]), 'byte_identical_verified': True},
        'proof_checks': {
            'selected_retrieval_blocks': 15,
            'existing_stub_indices_preserved': sorted(KEEP_BLOCKS),
            'existing_stub_sha256s': {str(i): BLOCK_HASHES[i] for i in sorted(KEEP_BLOCKS)},
            'retrieval_separators_identical': True,
            'all_unselected_pfluger_json_values_identical_by_full_restoration': True,
            'selected_openaire_description_fields': len(selected),
            'all_unselected_openaire_json_values_identical_by_full_restoration': True,
            'openaire_record_count_retained': 25,
            'openaire_header_query_count_page_values_identical': True,
            'all_unselected_urls_identifiers_and_other_factual_values_identical': True,
            'selected_text_exact_url_doi_isbn_tokens_retained_in_metadata': True,
            'factual_access_notices_retained': sum(v['$'] == ACCESS_NOTICE for _, v in selected),
            'previous_manifest_unchanged': True,
        },
        'network_requests': 0,
        'mathematical_checks_or_reruns': 0,
        'existing_input_files_changed': ['code/' + PFLUGER, 'code/' + PAGE1],
        'other_existing_files_or_archives_changed': 0,
        'historical_request_timings_changed': 0,
    }
    manifest_bytes = encoded(manifest)
    with MANIFEST.open('xb') as f:
        f.write(manifest_bytes)
    output = {
        'status': 'completed and verified',
        'started_utc': started,
        'normalization_verified_utc': completed,
        'normalization_and_verification_seconds': duration,
        'manifest': str(MANIFEST.relative_to(PROJECT)),
        'manifest_sha256': sha(manifest_bytes),
        'files': [{k: r[k] for k in ('file', 'original_bytes', 'original_sha256', 'normalized_bytes', 'normalized_sha256')} for r in records],
        'selected_blocks': 15,
        'selected_description_fields': 33,
        'historical_stubs_preserved': 2,
        'page2_byte_identical': True,
        'all_unselected_values_proved_equal': True,
        'research_status_change': False,
        'network_requests': 0,
        'mathematical_checks_or_reruns': 0,
    }
    with OUTPUT.open('xb') as f:
        f.write(encoded(output))
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
