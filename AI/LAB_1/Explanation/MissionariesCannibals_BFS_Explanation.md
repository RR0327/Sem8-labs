# Missionaries and Cannibals Problem using BFS

## 1. Import Library

- Imports **deque** from the `collections` module.
- Used to implement the BFS queue efficiently.

---

## 2. User Input

- Takes the number of missionaries and cannibals as input.
- Makes the program flexible for different problem sizes.

---

## 3. State Representation

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

## 4. Possible Boat Moves

- The boat can carry at most **two people**.
- Possible moves are:
  - 1 Missionary
  - 2 Missionaries
  - 1 Cannibal
  - 2 Cannibals
  - 1 Missionary and 1 Cannibal

---

## 5. State Validation (`is_valid()`)

- Checks whether a state is valid.
- Ensures:
  - Numbers are not negative.
  - Total missionaries and cannibals remain constant.
  - Boat position is valid.
  - Missionaries are never outnumbered by cannibals on either river bank.

---

## 6. Successor Generation (`get_successors()`)

- Generates all valid next states.
- Moves passengers according to the boat position.
- Returns only valid successor states.

---

## 7. BFS Function (`bfs()`)

- Solves the problem using **Breadth-First Search (BFS)**.
- Explores states level by level.
- Guarantees the shortest solution.

---

## 8. Queue

- Uses a **queue** to store unexplored states.
- Follows the **FIFO (First In, First Out)** principle.

---

## 9. Visited Set

- Stores explored states.
- Prevents revisiting the same state.
- Avoids infinite loops.

---

## 10. Goal Checking

- Checks whether all missionaries and cannibals have crossed the river.
- Stops when the goal state is reached.

---

## 11. Printing the Solution

- Displays the total number of steps.
- Prints every state from the initial state to the goal state.

---

## Why Use BFS?

- Explores states level by level.
- Guarantees the shortest sequence of crossings.

---

## Why Use a Queue?

- BFS follows **FIFO**.
- The first generated state is explored first.

---

## Why Use a Visited Set?

- Prevents repeated states.
- Improves efficiency and avoids infinite loops.

---

## Why Validate States?

- Ensures only legal puzzle states are explored.
- Prevents missionaries from being outnumbered by cannibals.

---

## Program Flow

1. Read the number of missionaries and cannibals.
2. Create the initial state.
3. Validate the state.
4. Generate valid successor states.
5. Explore states using BFS.
6. Avoid duplicate states using the visited set.
7. Stop when the goal state is reached.
8. Print the complete solution.

---

## Very Simple Viva Explanation

> This program solves the **Missionaries and Cannibals Problem** using the **Breadth-First Search (BFS)** algorithm. A state represents the number of missionaries, cannibals, and the boat position on both river banks. The program first checks whether each state is valid, then generates all valid next states. A **queue** is used to explore states level by level, while a **visited** set prevents repeated states. When all missionaries and cannibals safely reach the opposite bank, the program prints the shortest solution path.
