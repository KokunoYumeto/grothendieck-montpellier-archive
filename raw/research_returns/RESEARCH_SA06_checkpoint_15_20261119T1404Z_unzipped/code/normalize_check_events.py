#!/usr/bin/env python3
"""Conservative aggregate metadata normalization; original owner logs are untouched."""
from pathlib import Path
import collections
import csv
import datetime
import json
import re

ALLOWED = {
    'targeted proof check', 'independent re-proof',
    'computation or formal certificate', 'used and rechecked in this run',
    'carried as background without fault found',
}

class EventNormalizer:
    def __init__(self, root):
        self.root = Path(root)
        self.overrides = {}
        for source in [self.root / 'agents/real_weil/output/event_metadata_recommendations.tsv',
                       self.root / 'notes/ROOT_EVENT_METADATA_OVERRIDES.tsv']:
            with source.open(newline='') as f:
                for row in csv.DictReader(f, delimiter='\t'):
                    key = (row['path'], row['statement_id'], row['date'],
                           row['who_original'], row['type_original'], row['outcome_original'])
                    self.overrides[key] = row
        self.applied = set()
        self.records = []
        self.auxiliary = []

    @staticmethod
    def identity(who):
        aliases = {
            'root': '/root', '/root': '/root',
            'frobenius': '/root/frobenius', '/root/frobenius': '/root/frobenius',
            'cycles': '/root/cycles', '/root/cycles': '/root/cycles',
            'real_weil': '/root/real_weil', '/root/real_weil': '/root/real_weil',
        }
        if who.strip() in aliases:
            return ('GPT-6 Astra (OpenAI, ChatGPT Pro mode); run RESEARCH_SA06 '
                    + aliases[who.strip()]
                    + '; inherited effort, setting not separately exposed')
        result = who
        if 'ChatGPT Pro' not in result:
            result += '; ChatGPT Pro mode'
        if 'effort' not in result.lower():
            result += '; inherited effort, setting not separately exposed'
        if '/root' not in result and 'RESEARCH_SA06' not in result:
            result += '; run RESEARCH_SA06'
        return result

    def normalize(self, source, line, row):
        statement, date, who, kind, outcome = row
        path = str(Path(source).relative_to(self.root))
        key = (path, statement, date, who, kind, outcome)
        override = self.overrides.get(key)
        if override:
            self.applied.add(key)
            reason = override['rationale']
            category = override['recommended_category']
            if override['recommended_action'] == 'retain in auxiliary administrative/access log':
                self.auxiliary.append({
                    'source': path, 'line': line, 'statement_id': statement,
                    'date': date, 'who_original': who, 'type_original': kind,
                    'outcome_original': outcome, 'classification_reason': reason,
                })
                return None
        elif kind in ALLOWED or kind.startswith('refuted, with the refined statement'):
            category, reason = kind, 'Existing requested category preserved; no new verification inferred.'
        elif re.search(r'request|received|source[- ]access|source access|reconstruction|restoration|recovery|typograph|retrieval', kind, re.I):
            raise ValueError('Administrative/access/recovery label needs an explicit row-level '
                             'scope audit before classification: ' + repr((path, line, kind)))
        elif re.search(r'computation|certificate|code/experiment|program execution|compile|typeset|document validation|compilation|exact finite arithmetic', kind, re.I):
            category = 'computation or formal certificate'
            reason = 'Computation or document check only in the scope stated by the original outcome.'
        else:
            category = 'targeted proof check'
            reason = ('Conservative classification of an actual proof/source/scope audit; '
                      'a descriptive independent-audit label is not promoted to independent re-proof.')
        normalized_who = self.identity(who)
        detail = outcome
        if category != kind:
            detail = '[Original check label: ' + kind + '.] ' + detail
        if override:
            detail += ' [Metadata scope: ' + reason + ']'
        self.records.append({
            'source': path, 'line': line, 'statement_id': statement, 'date': date,
            'who_original': who, 'who_normalized': normalized_who,
            'type_original': kind, 'type_normalized': category,
            'classification_reason': reason,
        })
        return [statement, date, normalized_who, category, detail]

    def save(self):
        missing = set(self.overrides) - self.applied
        if missing:
            raise ValueError('Audited metadata overrides no longer match their source rows: '
                             + repr([(k[0], k[1], k[4]) for k in missing]))
        logs = self.root / 'logs'
        for filename, rows, fields in [
            ('check_event_normalization.tsv', self.records,
             ['source','line','statement_id','date','who_original','who_normalized',
              'type_original','type_normalized','classification_reason']),
            ('check_event_auxiliary_provenance.tsv', self.auxiliary,
             ['source','line','statement_id','date','who_original','type_original',
              'outcome_original','classification_reason']),
        ]:
            with (logs / filename).open('w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
                writer.writeheader()
                writer.writerows(rows)
        result = {
            'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_rows': len(self.records) + len(self.auxiliary),
            'canonical_check_rows': len(self.records),
            'auxiliary_records_not_counted_as_checks': len(self.auxiliary),
            'explicit_row_overrides_applied': len(self.applied),
            'categories': dict(collections.Counter(r['type_normalized'] for r in self.records)),
            'scope': ('Aggregate metadata only. Owner files and historical checkpoint archives '
                      'remain unchanged. No independent re-proof is inferred from an audit label; '
                      'no mathematical movement is counted.'),
        }
        (logs / 'check_event_normalization.json').write_text(json.dumps(result, indent=2) + '\n')
        return result
