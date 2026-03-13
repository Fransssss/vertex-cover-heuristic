# Vertex Cover Heuristic

This small Python demo builds a sample graph, explains the NP-complete vertex
cover problem, and showcases a greedy 2-approximation whose step-by-step
execution is animated in the terminal for easy visualization.

## Problem Overview
A vertex cover of a graph $G = (V, E)$ is a subset $C \subseteq V$ such that every edge in $E$ touches at least one vertex in $C$. Determining the smallest possible cover is a classic combinatorial optimization problem that quickly becomes challenging even for modestly sized graphs.

## Why Vertex Cover Is NP-Complete
The decision version ("does there exist a vertex cover of size $k$?") is in NP because a proposed cover can be verified in polynomial time, and it is NP-hard via a reduction from 3-SAT or CLIQUE. Because the problem is both in NP and NP-hard, it is NP-complete, implying we should not expect a polynomial-time exact algorithm unless P = NP.

## Heuristic Strategy Implemented Here
Exact solutions often rely on exponential-time search or mixed integer programming, but many practical scenarios only need a feasible (not necessarily optimal) cover. The simple greedy heuristic implemented in `vertex_cover.py` works as follows:

1. Represent the graph with adjacency lists for efficient edge lookups.
2. While uncovered edges remain, pick one arbitrarily.
3. Add both endpoints of that edge to the cover.
4. Remove all edges incident to the newly selected vertices.

The heuristic runs quickly, but it can overshoot the optimal solution, especially on graphs where a small set of vertices touches many edges.

## Running the Demo

```
python main.py
```

The script prints the input edges, animates the greedy heuristic (with a built-in
1.2s delay so each step is readable), and then summarizes the final cover.
Tweak the delay constant in `main.py` if you want a different pace.

## Sample Output

```
Input edges:
	(A, B)
	(A, C)
	(B, D)
	(C, D)
	(D, E)

Animating greedy heuristic:

Step 1: pick edge (A, B)
	Add to cover: A, B
	Cover so far: ['A', 'B']
	Remaining edges: (C, D), (D, E)

Step 2: pick edge (C, D)
	Add to cover: C, D
	Cover so far: ['A', 'B', 'C', 'D']
	Remaining edges: none

Greedy vertex cover:
	Vertices: ['A', 'B', 'C', 'D']
	Size: 4
```

The sample graph has an optimal cover of size 2 (vertices {A, D}), so the heuristic cover of size 4 is feasible but not optimal—exactly the trade-off this project is meant to showcase.

## Video Demo
If video not show, open the video directly from the repo (.mp4 file)

## Approximation vs. Exact Solutions
- **Exact algorithms** (branch-and-bound, ILP formulations, kernelization plus search) can find optimal covers but typically require exponential time in the worst case.
- **Approximation algorithms** deliver guarantees at a fraction of the runtime. The simple edge-picking heuristic here is a 2-approximation: it never returns a cover more than twice the optimal size, though in practice it may perform much better—or slightly worse than the theoretical bound when the selection order is unlucky.

Use this project as a starting point for experimenting with tighter heuristics, local search, or exact solvers to see how solution quality and runtime trade off for your graphs.
