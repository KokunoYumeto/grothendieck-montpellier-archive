"""Generate a Lean proof of the exact size of a small forest's edge function.

python generate.py --edges "[[0,1],[1,2]]" --output Path3.lean
Use --vertices to include trailing isolated vertices, and --expression to match
the body of a posted Boolean function, for example "x 1 && (x 0 || x 2)".
"""

import argparse
import ast
import itertools
import json
import re
from collections import deque
from pathlib import Path


def component_data(n, edges):
    neighbors = [[] for _ in range(n)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    parents = {}
    roots = []
    for root in range(n):
        if root in parents:
            continue
        roots.append(root)
        parents[root] = None
        queue = deque([root])
        while queue:
            a = queue.popleft()
            for b in neighbors[a]:
                if b not in parents:
                    parents[b] = a
                    queue.append(b)
    return roots, parents


def parse_graph(raw_edges, n):
    if not isinstance(raw_edges, list) or any(
        not isinstance(edge, list) or len(edge) != 2
        or any(type(v) is not int or v < 0 for v in edge) for edge in raw_edges
    ):
        raise ValueError("edges must be JSON pairs of nonnegative integers")
    edges = sorted(tuple(sorted(edge)) for edge in raw_edges)
    if n is None:
        n = max((b + 1 for _, b in edges), default=1)
    if not 1 <= n <= 9 or any(a == b or b >= n for a, b in edges):
        raise ValueError("use distinct endpoints from 0 through n-1, with 1 <= n <= 9")
    if len(set(edges)) != len(edges):
        raise ValueError("repeated edge")
    roots, _ = component_data(n, edges)
    if len(edges) != n - len(roots):
        raise ValueError("graph contains a cycle")
    return n, edges, roots


def certificates(n, edges):
    for size in range(n + 1):
        for cover in itertools.combinations(range(n), size):
            if all(a in cover or b in cover for a, b in edges):
                for matching in itertools.combinations(edges, size):
                    if len({v for edge in matching for v in edge}) == 2 * size:
                        return cover, matching
                raise AssertionError("minimum forest cover has no matching certificate")


def graph_decl(name, n, edges):
    predicate = " ||\n    ".join(f"(i == {a} && j == {b})" for a, b in edges)
    return f"""private def {name}Arc (i j : Fin {n}) : Bool :=
  {predicate}

private abbrev {name} : SimpleGraph (Fin {n}) where
  Adj i j := ({name}Arc i j || {name}Arc j i) = true
  symm := ⟨fun _ _ => by simp [Bool.or_comm]⟩
  loopless := ⟨by decide⟩
"""


def forest_proof(n, edges, roots):
    disconnected = len(roots) > 1
    tree = "spanning" if disconnected else "graph"
    tree_edges = edges + [(0, root) for root in roots[1:]]
    text = graph_decl(tree, n, tree_edges) + "\n" if disconnected else ""
    _, parents = component_data(n, tree_edges)
    for v in sorted(range(1, n), key=lambda x: distance(parents, x)):
        par = parents[v]
        step = f"(show {tree}.Adj {par} {v} by decide).reachable"
        proof = step if par == 0 else f"reach{par}.trans {step}"
        text += f"private theorem reach{v} : {tree}.Reachable 0 {v} :=\n  {proof}\n\n"
    cases = "\n".join(f"    · exact reach{v}" for v in range(1, n))
    text += f"""private theorem tree_acyclic : {tree}.IsAcyclic := by
  apply SimpleGraph.IsTree.isAcyclic
  apply SimpleGraph.isTree_iff_connected_and_card.mpr
  constructor
  · apply {tree}.connected_iff_exists_forall_reachable.mpr
    refine ⟨0, ?_⟩
    intro w
    fin_cases w
    · exact SimpleGraph.Reachable.rfl
{cases}
  · rw [Nat.card_eq_fintype_card, ← {tree}.edgeFinset_card, Nat.card_eq_fintype_card]
    decide
"""
    if disconnected:
        text += f"""
private theorem forest : graph.IsAcyclic := by
  have h : graph ≤ spanning := by
    change ∀ ⦃i j : Fin {n}⦄, graph.Adj i j → spanning.Adj i j
    decide
  exact tree_acyclic.comap (SimpleGraph.Hom.ofLE h) (fun _ _ he => he)
"""
    return text


def distance(parents, v):
    depth = 0
    while parents[v] is not None:
        depth += 1
        v = parents[v]
    return depth


def check_expression(expression, n, edges):
    token = r"(?:x\s+[0-9]+|true|false|&&|\|\||[()!])"
    if not re.fullmatch(r"\s*(?:" + token + r"\s*)+", expression):
        raise ValueError("use x i, true, false, &&, ||, ! and parentheses")
    inputs = [sum(1 << word for word in range(1 << n) if word >> i & 1)
              for i in range(n)]
    mask = (1 << (1 << n)) - 1
    values = {"true": mask, "false": 0, **{f"x{i}": bits for i, bits in enumerate(inputs)}}
    source = re.sub(r"x\s+(\d+)", r"x\1", expression)
    source = source.replace("&&", "&").replace("||", "|").replace("!", "~")

    def table(node):
        if isinstance(node, ast.Name) and node.id in values:
            return values[node.id]
        if isinstance(node, ast.BinOp):
            left, right = table(node.left), table(node.right)
            if isinstance(node.op, ast.BitAnd):
                return left & right
            if isinstance(node.op, ast.BitOr):
                return left | right
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Invert):
            return mask ^ table(node.operand)
        raise ValueError("invalid Boolean function or out-of-range input")

    expected = 0
    for u, v in edges:
        expected |= inputs[u] & inputs[v]
    try:
        observed = table(ast.parse(source.strip(), mode="eval").body)
    except SyntaxError as error:
        raise ValueError("malformed Boolean expression") from error
    if observed != expected:
        word = ((observed ^ expected) & -(observed ^ expected)).bit_length() - 1
        raise ValueError(f"expression differs from the edge function on input bits {word:0{n}b} (x0 at right)")


def empty_case(n, expression):
    binder = "x" if re.search(r"\bx\s", expression) else "_x"
    local_depth = "set_option maxRecDepth 4096 in\n" if n >= 7 else ""
    return f"""{local_depth}private theorem classified (s : ℕ) :
    PEqualNP.MetaComplexity.HasCircuitSize {n} (fun {binder} : Fin {n} → Bool => {expression}) s ↔ 0 ≤ s := by
  refine ⟨fun _ => Nat.zero_le _, fun _ => ?_⟩
  refine ⟨⟨[], {n}⟩, ?_, Nat.zero_le _, ?_⟩
  · simp [PEqualNP.MetaComplexity.FanInTwo]
  · intro x
    have h : ({expression}) = false := by decide +revert
    rw [h]
    simp [PEqualNP.CircuitLowerBounds.Circuit.eval, PEqualNP.CircuitLowerBounds.Circuit.wires,
      List.getD_eq_getElem?_getD]
"""


def nonempty_case(n, edges, roots, expression, cover, matching):
    k, m = len(cover), len(edges)
    first, second = edges[0]
    acyclic = "forest" if len(roots) > 1 else "tree_acyclic"
    disjoint = " → ".join(f"({a} ∈ T ∨ {b} ∈ T)" for a, b in matching)
    endpoints = " ".join(f"(h {a} {b} (by decide))" for a, b in matching)
    cover_set = "{" + ", ".join(map(str, cover)) + "}"
    local_depth = "set_option maxRecDepth 4096 in\n" if n >= 7 else ""
    return graph_decl("graph", n, edges) + "\n" + forest_proof(n, edges, roots) + f"""
private def cover : Finset (Fin {n}) := {cover_set}

{local_depth}private theorem cover_lower (T : Finset (Fin {n}))
    (h : ∀ i j : Fin {n}, graph.Adj i j → i ∈ T ∨ j ∈ T) : {k} ≤ T.card := by
  have bound : ∀ T : Finset (Fin {n}), {disjoint} → {k} ≤ T.card := by decide
  exact bound T {endpoints}

{local_depth}private theorem edge_fn :
    (fun x : Fin {n} → Bool => decide (∃ i j : Fin {n},
      graph.Adj i j ∧ x i = true ∧ x j = true)) =
    (fun x : Fin {n} → Bool => {expression}) := by
  funext x
  decide +revert

private theorem classified (s : ℕ) :
    PEqualNP.MetaComplexity.HasCircuitSize {n} (fun x : Fin {n} → Bool => {expression}) s ↔ {m+k-1} ≤ s := by
  have he : ∃ i j : Fin {n}, graph.Adj i j := ⟨{first}, {second}, by decide⟩
  have ec : graph.edgeFinset.card = {m} := by decide
  constructor
  · intro h
    rw [← edge_fn] at h
    have lower := PEqualNP.MetaComplexity.L104 {n} {k} s graph {acyclic} he cover_lower h
    rw [ec] at lower
    omega
  · intro hs
    have hc : ∀ i j : Fin {n}, graph.Adj i j → i ∈ cover ∨ j ∈ cover := by decide
    have cc : cover.card = {k} := by decide
    have upper := PEqualNP.MetaComplexity.L105 {n} graph cover he hc
    rw [edge_fn, ec, cc] at upper
    obtain ⟨c, legal, size, computes⟩ := upper
    exact ⟨c, legal, size.trans hs, computes⟩
"""


def generate(raw_edges, vertices, expression, name):
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name):
        raise ValueError("the filename stem must be a Lean identifier")
    n, edges, roots = parse_graph(raw_edges, vertices)
    if expression is None:
        expression = " || ".join(f"(x {a} && x {b})" for a, b in edges) or "false"
    check_expression(expression, n, edges)
    cover, matching = certificates(n, edges)
    body = nonempty_case(n, edges, roots, expression, cover, matching) if edges else empty_case(n, expression)
    size = max(0, len(edges) + len(cover) - 1)
    namespace = f"PEqualNP.Outside.{name}"
    binder = "x" if re.search(r"\bx\s", expression) else "_x"
    return f"""import PEqualNP.MetaComplexity.L104
import PEqualNP.MetaComplexity.L105

namespace {namespace}_aux

{body}
end {namespace}_aux

theorem {namespace} : ∀ s : ℕ,
    PEqualNP.MetaComplexity.HasCircuitSize {n} (fun {binder} : Fin {n} → Bool => {expression}) s ↔ {size} ≤ s :=
  {namespace}_aux.classified
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edges", required=True, type=json.loads)
    parser.add_argument("--vertices", type=int)
    parser.add_argument("--expression")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        proof = generate(args.edges, args.vertices, args.expression, args.output.stem)
    except ValueError as error:
        parser.error(str(error))
    args.output.write_text(proof, encoding="utf-8")
