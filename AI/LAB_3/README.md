# A\* Search Algorithm for the Romania Road Map Problem

## Overview

This project implements the **A\* (A-Star) Search Algorithm** to solve the classic **Romania Road Map Problem**, a well-known example in Artificial Intelligence.

The objective is to determine the shortest path from **Arad** to **Bucharest** by combining the actual travel cost with a heuristic estimate of the remaining distance.

---

## Problem Statement

Given a map of Romanian cities connected by roads with known distances, implement the A\* Search algorithm to find the optimal route from a starting city to a destination city.

In this project:

- **Start City:** Arad
- **Goal City:** Bucharest

---

## A\* Search Algorithm

A\* Search is an informed search algorithm that selects the next node based on the evaluation function:

```
f(n) = g(n) + h(n)
```

where:

- **g(n)** = Actual cost from the start node to the current node.
- **h(n)** = Estimated cost from the current node to the goal (heuristic).
- **f(n)** = Estimated total cost of the solution through the current node.

The algorithm always expands the node with the smallest **f(n)** value.

---

## Project Components

The implementation consists of the following parts:

- Romania road map represented as a graph
- **Straight-Line Distance (SLD)** heuristic values
- Priority queue using Python's `heapq`
- A\* Search implementation
- Path reconstruction
- Total distance calculation

---

## Data Structure

### Graph

The road map is represented as a dictionary where:

- Keys represent cities.
- Values represent neighboring cities and road distances.

Example:

```python
'Arad': {
    'Zerind': 75,
    'Sibiu': 140,
    'Timisoara': 118
}
```

---

### Heuristic Function

The heuristic values represent the **Straight-Line Distance (SLD)** from each city to Bucharest.

Example:

```python
'Arad': 366
'Sibiu': 253
'Pitesti': 100
'Bucharest': 0
```

These heuristic values guide the search toward the destination efficiently.

---

## Algorithm Workflow

1. Initialize the priority queue with the starting city.
2. Calculate the evaluation function:

```
f(n) = g(n) + h(n)
```

3. Select the node with the smallest evaluation value.
4. Expand neighboring cities.
5. Update path cost and estimated cost.
6. Repeat until the destination city is reached.
7. Return the shortest path and total distance.

---

## Expected Output

```
Path found:
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest

Total distance:
418 km
```

---

## Project Structure

```text
Romania_AStar_Search/
│
├── a_star_search.py
├── outputs/
│   └── A_Search.txt
│
└── README.md
```

---

## Requirements

Install **Python 3.x**.

No external libraries are required.

The project uses only the following built-in Python module:

```
heapq
```

---

## How to Run

Execute the Python file:

```bash
python a_star_search.py
```

The program will:

- Load the Romania road map.
- Apply the A\* Search algorithm.
- Find the shortest path.
- Display the optimal route.
- Display the total travel distance.

---

## Sample Output

```
Path found:
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest

Total distance:
418 km
```

---

## Time Complexity

| Case       | Complexity |
| ---------- | ---------- |
| Worst Case | O(b^d)     |

where:

- **b** = Branching factor
- **d** = Depth of the optimal solution

The heuristic significantly reduces the number of explored nodes compared to uninformed search algorithms.

---

## Space Complexity

```
O(b^d)
```

The algorithm stores generated nodes in the priority queue and maintains a visited set.

---

## Advantages

- Finds the optimal path when the heuristic is admissible.
- More efficient than uninformed search algorithms.
- Uses heuristic knowledge to reduce unnecessary exploration.
- Guarantees the shortest path with a consistent heuristic.

---

## Limitations

- Performance depends on the quality of the heuristic.
- Can consume significant memory for large search spaces.
- Requires heuristic values for every node.

---

## Conclusion

This project demonstrates the implementation of the A\* Search algorithm for solving the Romania Road Map Problem. By combining actual travel costs with heuristic estimates, the algorithm efficiently finds the shortest route from Arad to Bucharest with a total distance of **418 km**.

---
