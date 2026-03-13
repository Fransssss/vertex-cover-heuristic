"""Entry point that demonstrates the vertex cover heuristic on a toy graph."""
from __future__ import annotations

import time
from typing import Iterable

from vertex_cover import (
    GreedyStep,
    build_graph,
    greedy_vertex_cover_steps,
    list_edges,
)


def main() -> None:
    """Build the sample graph, run the heuristic, and print the results."""

    vertices = ["A", "B", "C", "D", "E"]
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
    ]

    graph = build_graph(vertices, edges)
    steps = greedy_vertex_cover_steps(graph)
    cover = list(steps[-1].cover_so_far) if steps else []

    print("Input edges:")
    for u, v in list_edges(graph):
        print(f"  ({u}, {v})")

    animate_process(steps, delay=1.2)

    print("\nGreedy vertex cover:")
    print(f"  Vertices: {cover}")
    print(f"  Size: {len(cover)}")


def animate_process(steps: Iterable[GreedyStep], *, delay: float) -> None:
    """Render a simple text animation of the greedy steps."""

    steps = list(steps)
    if not steps:
        print("\nNo edges to cover. Graph is already satisfied.")
        return

    print("\nAnimating greedy heuristic:")
    for idx, step in enumerate(steps, start=1):
        edge_text = f"({step.chosen_edge[0]}, {step.chosen_edge[1]})"
        added = ", ".join(step.added_vertices) or "(vertices already chosen)"
        remaining = _format_edges(step.remaining_edges)
        print(f"\nStep {idx}: pick edge {edge_text}")
        print(f"  Add to cover: {added}")
        print(f"  Cover so far: {list(step.cover_so_far)}")
        print(f"  Remaining edges: {remaining}")
        time.sleep(delay)


def _format_edges(edges: Iterable[tuple[str, str]]) -> str:
    formatted = [f"({u}, {v})" for u, v in edges]
    return ", ".join(formatted) if formatted else "none"


if __name__ == "__main__":
    main()
