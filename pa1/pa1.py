#!/usr/bin/env python3
"""Student starter for PA1."""

from __future__ import annotations

from typing import Any, Dict, List
import re
import sys


def solve_horn(formula: Dict[str, Any]) -> Dict[str, Any]:
    """Implement Horn resolution with unit propagation."""
    rules = formula['rules']
    true_vars = set(formula['facts'])
    queue = list(formula['facts'])

    # unmet body literals per rule
    unmet = [len(r['body']) for r in rules]

    rules_using = {}
    for i, r in enumerate(rules):
        for v in r['body']:
            rules_using.setdefault(v, []).append(i)

    for i, r in enumerate(rules):
        if unmet[i] == 0:
            # contradiction
            if r['head'] is None:
                return {'satisfiable': False, 'true_vars': []}
            if r['head'] not in true_vars:
                true_vars.add(r['head'])
                queue.append(r['head'])

    # propagate
    while queue:
        v = queue.pop()
        for i in rules_using.get(v, []):
            unmet[i] -= 1
            if unmet[i] == 0:
                head = rules[i]['head']
                if head is None:
                    return {'satisfiable': False, 'true_vars': []}
                if head not in true_vars:
                    true_vars.add(head)
                    queue.append(head)

    return {'satisfiable': True, 'true_vars': sorted(true_vars)}


def parse_horn_clause_string(text: str) -> Dict[str, Any]:
    """
    Parse text like: [[-a,-b,c], [-c,-d,e], [a]]
    Each clause must be Horn (at most one positive literal).
    """
    src = ''.join(text.strip().split())
    clause_texts = re.findall(r'\[([^\[\]]*)\]', src)

    clauses: List[List[str]] = []
    for raw in clause_texts:
        if raw == '':
            clauses.append([])
            continue
        tokens = [tok for tok in raw.split(',') if tok]
        clauses.append(tokens)

    variables = set()
    facts: List[str] = []
    rules: List[Dict[str, Any]] = []

    for clause in clauses:
        neg_body: List[str] = []
        positives: List[str] = []

        for lit in clause:
            if lit.startswith('-'):
                v = lit[1:]
                if v:
                    neg_body.append(v)
                    variables.add(v)
            else:
                positives.append(lit)
                if lit:
                    variables.add(lit)

        if len(positives) > 1:
            head = positives[0]
        elif len(positives) == 1:
            head = positives[0]
        else:
            head = None

        if not neg_body and head is not None:
            facts.append(head)
        else:
            rules.append({'body': neg_body, 'head': head})

    return {
        'variables': sorted(variables),
        'facts': sorted(set(facts)),
        'rules': rules,
    }


def format_result(result: Dict[str, Any]) -> str:
    sat = 'true' if result['satisfiable'] else 'false'
    if result['satisfiable']:
        tv = ' '.join(sorted(set(result['true_vars'])))
        return f'satisfiable: {sat}\ntrue_vars: {tv}'.rstrip()
    return f'satisfiable: {sat}'


def main() -> None:
    raw = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    formula = parse_horn_clause_string(raw)
    result = solve_horn(formula)
    print(format_result(result))


if __name__ == '__main__':
    main()
