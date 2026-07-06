# Breadth-First Search (BFS) Explanation

## 1. `deque`

- `deque` is used to implement the BFS queue.
- It follows the **FIFO (First In, First Out)** principle.
- It is faster than a normal list for adding and removing elements from the front.

---

## 2. Goal Checking Function (`is_goal()`)

- Checks whether the current puzzle state matches the goal state.
- Returns **True** if the goal is reached; otherwise returns **False**.

---

## 3. Blank Tile Finding Function (`find_blank()`)

- Finds the position (row and column) of the blank tile (`0`) in the puzzle.
- Returns the coordinates of the blank tile.

---

## 4. Successor Generation Function (`get_successors()`)

- Generates all valid next puzzle states by moving the blank tile.
- Considers four possible moves: **Up, Down, Left,** and **Right**.

---

## 5. Trying Each Move

- Calculates the new position of the blank tile for each possible move.
- Creates a new state for every valid movement.

---

## 6. Valid Move Checking

- Ensures the new position is within the puzzle boundaries.
- Prevents invalid moves outside the 3×3 grid.

---

## 7. Creating a New State

- Converts the puzzle from **tuple** to **list** so the tiles can be modified.
- Allows swapping of puzzle tiles.

---

## 8. Swapping the Blank Tile

- Swaps the blank tile (`0`) with a neighboring tile.
- Represents one valid move in the puzzle.

---

## 9. Storing Successor States

- Converts the updated puzzle back to a **tuple**.
- Stores the new state in the successor list for further exploration.

---

## 10. BFS Function (`bfs()`)

- Solves the puzzle using the **Breadth-First Search (BFS)** algorithm.
- Explores states level by level to find the shortest solution path.

---

## 11. BFS Loop

- Removes the first state from the queue.
- Continues exploring until the queue becomes empty or the goal is found.

---

## 12. Goal Checking in BFS

- Compares the current state with the goal state.
- Returns the solution path when the goal is reached.

---

## 13. Generating Next States

- Generates all valid successor states.
- Uses a **visited** set to avoid revisiting the same state.
- Adds new states to the queue for further exploration.

---

## 14. Printing the Solution

- Displays the total number of moves.
- Prints each puzzle state from the initial state to the goal state.

---

## Why Use BFS?

- BFS explores the puzzle **level by level**.
- It guarantees the **shortest path** in terms of the number of moves.

---

## Why Use a Queue?

- BFS follows the **FIFO (First In, First Out)** principle.
- The state inserted first is explored first.

---

## Why Use a Visited Set?

- Prevents exploring the same puzzle state multiple times.
- Avoids infinite loops and improves efficiency.

---

## Why Use Tuple Instead of List?

- Puzzle states are stored as **tuples** because tuples are immutable.
- Tuples can be stored in a **set**, while lists cannot.

---

## Program Flow

1. Start from the initial puzzle state.
2. Find the blank tile.
3. Generate all valid successor states.
4. Explore states using BFS.
5. Avoid duplicate states using the **visited** set.
6. Stop when the goal state is found.
7. Display the complete solution path.

---

## Very Simple Viva Explanation

> This program solves the **8-Puzzle Problem** using the **Breadth-First Search (BFS)** algorithm. The puzzle is represented as a tuple of tuples, where **0** represents the blank tile. The **find_blank()** function locates the blank tile, and the **get_successors()** function generates all valid next states by moving it in four possible directions. The **bfs()** function uses a **queue** to explore states level by level and a **visited** set to avoid revisiting the same states. When the current state matches the goal state, the algorithm returns and prints the shortest solution path.
