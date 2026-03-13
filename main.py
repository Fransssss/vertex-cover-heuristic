"""
main.py
-------
Demonstrates the greedy Vertex Cover heuristic on a small example graph.

Example graph:
    Vertices : A, B, C, D, E
    Edges    : (A,B), (A,C), (B,D), (C,D), (D,E)

Expected output (exact cover may vary due to iteration order, but the
result will always be a valid cover of size ≤ 2 × OPT):
    Edges in the graph:
      (A, B)
      (A, C)
      (B, D)
      (C, D)
      (D, E)

    Vertex cover found: {'A', 'B', 'C', 'D'}   ← example; actual output may differ
    Size of cover     : 4
"""

from vertex_cover import Graph, greedy_vertex_cover


def build_example_graph():
    """Build and return the example graph described in the problem statement."""
    g = Graph()

    # Define edges; vertices are added automatically.
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
    ]

    for u, v in edges:
        g.add_edge(u, v)

    return g


def print_edges(graph):
    """Print all edges of the graph in a readable format."""
    print("Edges in the graph:")
    # Sort for a deterministic, readable output.
    for u, v in sorted(graph.get_edges()):
        print(f"  ({u}, {v})")


def main():
    # --- Build the graph ---
    graph = build_example_graph()

    # --- Display the edges ---
    print_edges(graph)
    print()

    # --- Run the heuristic ---
    cover = greedy_vertex_cover(graph)

    # --- Display results ---
    # Sort for reproducible output.
    sorted_cover = sorted(cover)
    print(f"Vertex cover found: {set(sorted_cover)}")
    print(f"Size of cover     : {len(cover)}")


if __name__ == "__main__":
    main()
