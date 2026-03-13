# vertex-cover-heuristic

A Python project that demonstrates the **Vertex Cover** NP-hard problem and
implements a simple greedy heuristic algorithm.

---

## Table of Contents

1. [What is the Vertex Cover Problem?](#what-is-the-vertex-cover-problem)
2. [Why is it NP-Complete?](#why-is-it-np-complete)
3. [Heuristic Algorithm](#heuristic-algorithm)
4. [Project Structure](#project-structure)
5. [Example Run](#example-run)
6. [Approximation vs. Exact Solutions](#approximation-vs-exact-solutions)

---

## What is the Vertex Cover Problem?

Given an **undirected graph** G = (V, E), a **vertex cover** is a subset C ⊆ V
such that for every edge (u, v) ∈ E, at least one of u or v is in C.

The **Vertex Cover decision problem** asks: does a vertex cover of size ≤ k
exist?  
The **optimization variant** asks: what is the smallest such cover?

### Example

```
    A --- B
    |     |
    C --- D --- E
```

Edges: (A,B), (A,C), (B,D), (C,D), (D,E)  
One optimal cover: {A, D} – every edge touches A or D.

---

## Why is it NP-Complete?

1. **In NP** – given a candidate cover C, it is easy (polynomial time) to
   verify that every edge has at least one endpoint in C.

2. **NP-hard** – the problem can be shown to be at least as hard as every
   other problem in NP by a polynomial-time reduction from the **Independent
   Set** problem (itself NP-complete):  
   A set I is an independent set of G if and only if V \ I is a vertex cover
   of G.  Since Independent Set is NP-complete, Vertex Cover is NP-hard.

Because it is both in NP and NP-hard, Vertex Cover is **NP-complete**.

No polynomial-time exact algorithm is known (unless P = NP), which makes
heuristic and approximation algorithms practically important.

---

## Heuristic Algorithm

This project implements the classic **greedy 2-approximation** heuristic:

```
cover = {}
while there exists an uncovered edge (u, v):
    add u and v to cover
    remove all edges incident to u or v
return cover
```

### Properties

| Property | Value |
|---|---|
| Time complexity | O(V + E) |
| Approximation ratio | ≤ 2 × OPT |
| Guaranteed valid cover | Yes |

The approximation guarantee follows because every picked edge (u, v) must
have at least one endpoint in any valid cover; by adding *both* endpoints we
add at most twice the minimum necessary.

---

## Project Structure

```
vertex-cover-heuristic/
├── main.py           # Entry point – builds the example graph and prints results
├── vertex_cover.py   # Graph class and greedy_vertex_cover() function
└── README.md         # This file
```

### Running the program

```bash
python main.py
```

No external dependencies are required – the project uses only the Python
standard library.

---

## Example Run

```
Edges in the graph:
  (A, B)
  (A, C)
  (B, D)
  (C, D)
  (D, E)

Vertex cover found: {'A', 'B', 'C', 'D'}
Size of cover     : 4
```

The cover `{A, B, C, D}` is valid: every edge touches at least one vertex in
the set.  The optimal cover for this graph is `{A, D}` (size 2), so this run
produces a cover 2× the optimal – exactly the theoretical worst case.

---

## Approximation vs. Exact Solutions

| Approach | Time complexity | Cover quality |
|---|---|---|
| Greedy heuristic (this project) | O(V + E) | ≤ 2 × OPT |
| Brute-force exact | O(2^V · (V + E)) | Optimal |
| Integer Linear Programming | exponential worst-case | Optimal |
| Fixed-parameter tractable (FPT) | O(2^k · (V + E)) | Optimal for small k |

### When to use the heuristic

* The graph is large and an exact solution would be too slow.
* A near-optimal solution is acceptable in practice.
* Speed and simplicity are priorities over optimality.

### Limitations

* The heuristic can return a cover up to twice the optimal size.
* It does not guarantee the *minimum* vertex cover.
* The output may vary depending on the order in which edges are processed.
