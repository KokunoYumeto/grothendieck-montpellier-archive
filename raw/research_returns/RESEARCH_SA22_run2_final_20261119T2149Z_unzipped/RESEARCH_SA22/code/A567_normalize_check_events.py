"""Apply the root-approved event metadata proposal without inventing checks.

Imported by consolidate_registers.py; not a standalone research program.
Only exact reviewed noncanonical events are transformed. New events already
using a prompt category pass unchanged; other new events require review.
"""
from collections import Counter
import csv
import hashlib
import io
import json
from time import perf_counter


EVENT_FIELDS = ('statement_id', 'date', 'who', 'type', 'outcome')
APPROVED_PROPOSAL = 'notes/A567_event_type_normalization_proposal.json'
APPROVED_PROPOSAL_SHA256 = (
    '5694e26b1348eb4e7cb03a3d47450c32005fe079dfa2124306330ce3ba5e31cb'
)
APPROVED_SNAPSHOT = 'notes/CHECK_EVENTS_pre_normalization_c30d395564a7f175.tsv'
APPROVED_SNAPSHOT_SHA256 = (
    'c30d395564a7f1756651e516f800b4518f9ea421710aa3054b9ad30460a3f656'
)
ALLOWED_TYPES = frozenset((
    'targeted proof check',
    'independent re-proof',
    'computation or formal certificate',
    'used and rechecked in this run',
    'carried as background without fault found',
    "refuted, with the refined statement's id",
))


class EventReviewRequired(ValueError):
    """Stop before output publication when metadata needs a fresh review."""


def event_fingerprint(event):
    encoded = json.dumps(event, ensure_ascii=False, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()


def _checked_bytes(root, relative_path, expected_hash):
    data = (root / relative_path).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != expected_hash:
        raise EventReviewRequired(
            f'Approved provenance changed: {relative_path}: {digest}'
        )
    return data


def normalize_events(root, events, statement_ids):
    """Return canonical events, verbatim access events, and reconciliation.

    This function reads immutable reviewed inputs and makes no file changes.
    The caller publishes outputs only after all checks below have passed.
    """
    started = perf_counter()
    proposal_bytes = _checked_bytes(
        root, APPROVED_PROPOSAL, APPROVED_PROPOSAL_SHA256
    )
    proposal = json.loads(proposal_bytes)
    snapshot_bytes = _checked_bytes(
        root, APPROVED_SNAPSHOT, APPROVED_SNAPSHOT_SHA256
    )
    if proposal['source_sha256'] != APPROVED_SNAPSHOT_SHA256:
        raise EventReviewRequired('Proposal and preserved input disagree.')
    if set(proposal['allowed_canonical_types']) != ALLOWED_TYPES:
        raise EventReviewRequired('Proposal categories disagree with the prompt.')
    snapshot = list(csv.DictReader(
        io.StringIO(snapshot_bytes.decode()), delimiter='\t'
    ))
    original_counts = Counter(event_fingerprint(e) for e in snapshot)
    input_counts = Counter(event_fingerprint(e) for e in events)
    missing_originals = original_counts - input_counts
    if missing_originals:
        raise EventReviewRequired(
            'Rebuilding components lost or changed an approved original event: '
            + repr(dict(missing_originals))
        )

    reviewed = {}
    for change in proposal['event_changes']:
        fingerprint = event_fingerprint(change['original_event'])
        if fingerprint != change['event_sha256'] or fingerprint in reviewed:
            raise EventReviewRequired('Invalid or duplicate approved event rule.')
        reviewed[fingerprint] = change

    canonical = []
    source_access = []
    origins = []
    normalized_count = 0
    for input_row, event in enumerate(events, 2):
        if set(event) != set(EVENT_FIELDS):
            raise EventReviewRequired(f'Unexpected event schema at row {input_row}.')
        original = dict(event)
        fingerprint = event_fingerprint(original)
        change = reviewed.get(fingerprint)
        if original['type'] in ALLOWED_TYPES:
            if change is not None:
                raise EventReviewRequired('Reviewed rule unexpectedly changes a canonical type.')
            destination = 'CHECK_EVENTS.tsv'
            output = original.copy()
        else:
            if change is None or change['original_event'] != original:
                raise EventReviewRequired(
                    'Unreviewed noncanonical event; no automatic upgrade: '
                    + repr((input_row, original['statement_id'], original['type']))
                )
            destination = change['destination']
            output = dict(change['proposed_event'])
            if destination == 'SOURCE_ACCESS_EVENTS.tsv':
                if output != original:
                    raise EventReviewRequired('A retrieval-only event must remain verbatim.')
            elif destination == 'CHECK_EVENTS.tsv':
                if output['type'] not in ALLOWED_TYPES:
                    raise EventReviewRequired('Proposed type is outside the prompt categories.')
                for field in ('statement_id', 'date', 'who'):
                    if output[field] != original[field]:
                        raise EventReviewRequired('Normalization changed event identity or attribution.')
                prefix = '[Original event type: ' + original['type'] + '] '
                if not output['outcome'].startswith(prefix):
                    raise EventReviewRequired('Original event type was not preserved verbatim.')
                if not output['outcome'].endswith(original['outcome']):
                    raise EventReviewRequired('Original event outcome was not preserved verbatim.')
                normalized_count += 1
            else:
                raise EventReviewRequired('Unapproved destination register.')
        if destination == 'CHECK_EVENTS.tsv':
            canonical.append(output)
        else:
            source_access.append(output)
        origins.append({
            'rebuilt_input_row': input_row,
            'original_event_sha256': fingerprint,
            'destination': destination,
            'output_event_sha256': event_fingerprint(output),
            'reviewed_snapshot_line': change['source_line'] if change else None,
        })

    if Counter(o['original_event_sha256'] for o in origins) != input_counts:
        raise EventReviewRequired('Original-event accounting failed.')
    before_reproofs = sum(e['type'] == 'independent re-proof' for e in events)
    after_reproofs = sum(e['type'] == 'independent re-proof' for e in canonical)
    if before_reproofs != after_reproofs:
        raise EventReviewRequired('Normalization changed the independent re-proof count.')
    missing_statements = sorted(set(statement_ids) - {
        e['statement_id'] for e in canonical
    })
    if missing_statements:
        raise EventReviewRequired('Missing statement coverage: ' + repr(missing_statements))
    if len(canonical) + len(source_access) != len(events):
        raise EventReviewRequired('An original event was dropped or duplicated.')
    if normalized_count != proposal['proposed_counts']['normalized_canonical_events']:
        raise EventReviewRequired('An approved event transformation was not applied exactly once.')
    if len(source_access) != proposal['proposed_counts']['supplemental_source_access_events']:
        raise EventReviewRequired('Approved source-access event count changed.')

    reconciliation = {
        'scope': 'Administrative normalization of exact root-approved event metadata; no proof, source reading, or mathematical certificate executed',
        'execution_mode': 'Imported helper invoked by code/consolidate_registers.py',
        'helper_source': 'code/A567_normalize_check_events.py',
        'approved_proposal': APPROVED_PROPOSAL,
        'approved_proposal_sha256': APPROVED_PROPOSAL_SHA256,
        'immutable_input_snapshot': APPROVED_SNAPSHOT,
        'immutable_input_snapshot_sha256': APPROVED_SNAPSHOT_SHA256,
        'rebuilt_event_rows': len(events),
        'original_snapshot_event_rows': len(snapshot),
        'canonical_event_rows': len(canonical),
        'source_access_event_rows': len(source_access),
        'normalized_canonical_event_rows': normalized_count,
        'unchanged_canonical_event_rows': len(canonical) - normalized_count,
        'canonical_type_counts': dict(Counter(e['type'] for e in canonical)),
        'independent_reproof_count_before': before_reproofs,
        'independent_reproof_count_after': after_reproofs,
        'missing_statement_ids': missing_statements,
        'all_original_events_accounted_for': True,
        'all_snapshot_events_retained': True,
        'retrieval_events_preserved_verbatim': True,
        'component_files_mutated_by_helper': False,
        'future_noncanonical_policy': 'Exact reviewed original-event fingerprint required; otherwise EventReviewRequired before any output write',
        'event_origins': origins,
        'helper_elapsed_seconds': perf_counter() - started,
    }
    return canonical, source_access, reconciliation
