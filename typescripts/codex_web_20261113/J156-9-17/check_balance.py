#!/usr/bin/env python3
"""Structural checks only; this script never invokes a TeX engine."""
from pathlib import Path
import re
import sys


def check(path):
    source = path.read_text(encoding='utf-8')
    group_stack, environment_stack = [], []
    math_mode = None
    counts = {'groups': 0, 'dollar_pairs': 0, 'display_pairs': 0, 'environments': 0}
    pos = 0
    while pos < len(source):
        char = source[pos]
        line = source.count('\n', 0, pos) + 1
        if char == '%':
            newline = source.find('\n', pos)
            pos = len(source) if newline < 0 else newline + 1
            continue
        if char == '\\':
            assert pos + 1 < len(source), f'{path.name}:{line}: terminal backslash'
            command_match = re.match(r'\\([A-Za-z]+|.)', source[pos:])
            command = command_match.group(1)
            if command in ('begin', 'end'):
                match = re.match(r'\\(?:begin|end)\s*\{([^{}]+)\}', source[pos:])
                assert match, f'{path.name}:{line}: malformed environment command'
                name = match.group(1)
                if command == 'begin':
                    environment_stack.append((name, line))
                    counts['environments'] += 1
                else:
                    assert environment_stack, f'{path.name}:{line}: unmatched end {name}'
                    opened, opened_line = environment_stack.pop()
                    assert opened == name, f'{path.name}:{line}: end {name}, expected {opened} from {opened_line}'
                pos += match.end()
                continue
            if command in ('[', '('):
                assert math_mode is None, f'{path.name}:{line}: nested math delimiter'
                math_mode = command
            elif command in (']', ')'):
                expected = '[' if command == ']' else '('
                assert math_mode == expected, f'{path.name}:{line}: unmatched math closer'
                math_mode = None
                counts['display_pairs'] += int(command == ']')
            pos += command_match.end()
            continue
        if char == '{':
            group_stack.append(line)
            counts['groups'] += 1
        elif char == '}':
            assert group_stack, f'{path.name}:{line}: unmatched closing brace'
            group_stack.pop()
        elif char == '$':
            assert math_mode in (None, '$'), f'{path.name}:{line}: dollar inside delimited display'
            if math_mode is None:
                math_mode = '$'
            else:
                math_mode = None
                counts['dollar_pairs'] += 1
        pos += 1
    assert not group_stack, f'{path.name}: unclosed groups from {group_stack}'
    assert not environment_stack, f'{path.name}: unclosed environments {environment_stack}'
    assert math_mode is None, f'{path.name}: unclosed math delimiter {math_mode}'
    return counts


def main():
    root = Path(__file__).resolve().parent
    pages = sorted((root/'pages').glob('J156-9-17_156-9_scan*.tex'))
    expected = [126, 127, 128, 130, 131, 132, 133]
    assert [int(re.search(r'scan(\d+)', p.name).group(1)) for p in pages] == expected
    assembled = root/'J156-9-17_transcription.tex'
    assert assembled.read_bytes() == b''.join(p.read_bytes() for p in pages), 'Fragment differs from concatenated pages'
    assert assembled.read_text().startswith(r'\cotefile{156-9}'), 'Missing initial cote'
    assert assembled.read_text().count(r'\cotefile{') == 1, 'Cote count is not one'
    for path in pages + [assembled, root/'J156-9-17_standalone.tex']:
        result = check(path)
        print('PASS', path.name, result)
    print('PASS: braces, dollar pairs, display delimiters, environment nesting, exact concatenation, scan order and one initial cote.')


if __name__ == '__main__':
    try:
        main()
    except AssertionError as error:
        print('FAIL:', error, file=sys.stderr)
        sys.exit(1)
