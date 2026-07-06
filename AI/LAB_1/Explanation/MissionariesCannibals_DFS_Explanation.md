# Missionaries and Cannibals Problem using DFS

## 1. User Input

- Takes the number of missionaries and cannibals as input.
- Allows the program to solve different problem sizes.

---

## 2. State Representation

- A state is represented as:

```
(m_left, c_left, boat, m_right, c_right)
```

Where:

- **m_left** = Missionaries on the left bank.
- **c_left** = Cannibals on the left bank.
- **boat** = Boat position (`L` or `R`).
- **m_right** = Missionaries on the right bank.
- **c_right** = Cannibals on the right bank.

---

## 3. Possible Boat Moves

- The boat can carry a maximum of **two people**.
- Valid moves include:
  - 1 Missionary
  - 2 Missionaries
  - 1 Cannibal
  - 2 Cannibals
  - 1 Missionary and 1 Cannibal

---

## 4. State Validation (`is_valid()`)

- Checks whether a state satisfies all problem constraints.
- Ensures:
  - No negative values.
  - Total missionaries and cannibals remain unchanged.
  - Boat position is valid.
  - Missionaries are never outnumbered by cannibals.

---

## 5. Successor Generation (`get_successors()`)

- Generates all valid next states.
- Returns only legal moves.

---

## 6. DFS Function (`dfs()`)

- Solves the problem using **Depth-First Search (DFS)**.
- Explores one path completely before backtracking.

---

## 7. Stack

- Uses a **stack** to store unexplored states.
- Follows the **LIFO (Last In, First Out)** principle.

---

## 8. Visited Set

- Stores explored states.
- Prevents revisiting the same state.
- Avoids infinite loops.

---

## 9. Goal Checking

- Checks whether all missionaries and cannibals have crossed the river.
- Returns the solution path when the goal is reached.

---

## 10. Printing the Solution

- Displays the total number of steps.
- Prints every state from the initial state to the goal state.

---

## Why Use DFS?

- Explores one path deeply before trying another.
- Can find a solution quickly but does not always guarantee the shortest path.

---

## Why Use a Stack?

- DFS follows the **LIFO** principle.
- The most recently generated state is explored first.

---

## Why Use a Visited Set?

- Prevents revisiting the same states.
- Improves efficiency.

---

## Why Validate States?

- Ensures every explored state follows the puzzle rules.
- Prevents invalid situations where missionaries are outnumbered.

---

## Program Flow

1. Read the number of missionaries and cannibals.
2. Create the initial state.
3. Validate the state.
4. Generate valid successor states.
5. Explore states using DFS.
6. Avoid duplicate states using the visited set.
7. Stop when the goal state is reached.
8. Print the complete solution.

---

## Very Simple Viva Explanation

> This program solves the **Missionaries and Cannibals Problem** using the **Depth-First Search (DFS)** algorithm. Each state stores the number of missionaries, cannibals, and the boat position on both river banks. The program validates every state and generates only valid successor states. A **stack** is used to explore one path deeply before backtracking, while a **visited** set prevents repeated states. When all missionaries and cannibals safely cross the river, the solution path is printed.
