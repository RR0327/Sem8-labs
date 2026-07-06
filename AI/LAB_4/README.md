# Hill Climbing Search Algorithm for the Romania Road Map Problem

## Overview

This project implements the **Hill Climbing Search Algorithm** to solve the classic **Romania Road Map Problem**, a well-known problem in Artificial Intelligence.

The objective is to find a path from **Arad** to **Bucharest** by repeatedly moving to the neighboring city with the lowest heuristic value (Straight-Line Distance to Bucharest).

Unlike informed search algorithms such as A\*, Hill Climbing makes decisions based only on the current state and its immediate neighbors without considering the total path cost.

---

## Problem Statement

Given a map of Romanian cities connected by roads, implement the Hill Climbing Search algorithm to navigate from a starting city to the destination city using heuristic information.

In this project:

- **Start City:** Arad
- **Goal City:** Bucharest

---

## Hill Climbing Search

Hill Climbing is a **local search algorithm** that iteratively moves to the neighboring state with the best heuristic value.

The algorithm follows these steps:

1. Start from the initial city.
2. Examine all neighboring cities.
3. Select the neighbor with the lowest heuristic value.
4. Move to the selected neighbor if it improves the heuristic.
5. Repeat until the goal is reached or no better neighbor exists.

---

## Project Components

The implementation consists of the following components:

- Romania road map represented as a graph
- Straight-Line Distance (SLD) heuristic values
- Hill Climbing Search algorithm
- Path generation from start to goal
- Output of the selected path

---

## Data Structure

### Graph Representation

The Romania road map is represented as a dictionary where:

- Keys represent cities.
- Values represent neighboring cities and their road distances.

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

The heuristic represents the Straight-Line Distance (SLD) from each city to Bucharest.

Example:

```python
'Arad': 366
'Sibiu': 253
'Pitesti': 100
'Bucharest': 0
```

The algorithm always selects the neighboring city with the smallest heuristic value.

---

## Algorithm Workflow

1. Initialize the search from Arad.
2. Retrieve all neighboring cities.
3. Compare their heuristic values.
4. Select the neighbor with the minimum heuristic.
5. Move to the selected city.
6. Continue until Bucharest is reached or no better neighbor exists.

---

## Expected Output

```text
Path taken by Hill Climbing Search:

Arad → Sibiu → Fagaras → Bucharest
```

---

## Project Structure

```text
Romania_Hill_Climbing/
│
├── hill_climbing.py
├── outputs/
│   └── Hill_Climbing_Search.txt
│
└── README.md
```

---

## Requirements

Install **Python 3.x**.

No external libraries are required.

The project uses only Python's built-in language features.

---

## How to Run

Execute the Python file:

```bash
python hill_climbing.py
```

The program will:

1. Load the Romania road map.
2. Apply the Hill Climbing Search algorithm.
3. Display the path from Arad to Bucharest.

---

## Sample Output

```text
Path taken by Hill Climbing Search:

Arad → Sibiu → Fagaras → Bucharest
```

---

## Time Complexity

| Case       | Complexity |
| ---------- | ---------- |
| Worst Case | O(b × d)   |

where:

- **b** = Branching factor
- **d** = Depth of the search

The algorithm evaluates only the neighboring nodes at each step.

---

## Space Complexity

```text
O(d)
```

Only the current path and neighboring nodes are maintained during execution.

---

## Advantages

- Simple and easy to implement.
- Requires very little memory.
- Fast for small search problems.
- Uses heuristic information to guide the search.

---

## Limitations

- Does not always find the optimal solution.
- Can become trapped in local maxima or local minima.
- Cannot escape plateaus without additional strategies.
- Does not perform backtracking.

---

## Comparison with A\* Search

| Feature                     | Hill Climbing | A\* Search                         |
| --------------------------- | ------------- | ---------------------------------- |
| Search Type                 | Local Search  | Informed Search                    |
| Uses Path Cost              | No            | Yes                                |
| Uses Heuristic              | Yes           | Yes                                |
| Guarantees Optimal Solution | No            | Yes (with an admissible heuristic) |
| Memory Usage                | Low           | Higher                             |
| Risk of Local Optimum       | High          | Very Low                           |

---

## Conclusion

This project demonstrates the implementation of the Hill Climbing Search algorithm for the Romania Road Map Problem. Using the Straight-Line Distance heuristic, the algorithm moves toward neighboring cities with lower heuristic values until it reaches Bucharest.

Although Hill Climbing is computationally efficient and easy to implement, it does not guarantee the shortest or optimal path because it considers only local improvements.

---
