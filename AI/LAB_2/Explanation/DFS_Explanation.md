# DFS (Depth-First Search) Explanation

## 1. Stack

- DFS uses a **stack** to store puzzle states.
- It follows the **LIFO (Last In, First Out)** principle.
- The most recently added state is explored first.

---

## 2. Goal Checking Function (`is_goal()`)

- Checks whether the current puzzle state matches the goal state.
- Returns **True** if the goal is reached; otherwise returns **False**.

---

## 3. Blank Tile Finding Function (`find_blank()`)

- Finds the position (row and column) of the blank tile (`0`).
- Returns the coordinates of the blank tile.

---

## 4. Successor Generation Function (`get_successors()`)

- Generates all valid next puzzle states.
- Moves the blank tile **Up, Down, Left,** or **Right**.

---

## 5. Trying Each Move

- Calculates the new blank tile position.
- Creates a new puzzle state for every valid move.

---

## 6. Valid Move Checking

- Ensures the new position is inside the 3×3 puzzle.
- Prevents invalid moves outside the board.

---

## 7. Creating a New State

- Converts tuples into lists to allow tile swapping.
- Makes the puzzle state editable.

---

## 8. Swapping the Blank Tile

- Swaps the blank tile with a neighboring tile.
- Produces the next valid puzzle state.

---

## 9. Storing Successor States

- Converts the modified puzzle back to a tuple.
- Stores it for future exploration.

---

## 10. DFS Function (`dfs()`)

- Solves the puzzle using **Depth-First Search (DFS)**.
- Explores one path completely before backtracking.

---

## 11. DFS Loop

- Removes the last state from the stack.
- Continues until the stack becomes empty or the goal is found.

---

## 12. Goal Checking in DFS

- Compares the current state with the goal state.
- Returns the solution path if the goal is reached.

---

## 13. Generating Next States

- Generates all valid successor states.
- Uses a **visited** set to avoid revisiting states.
- Pushes new states onto the stack.

---

## 14. Printing the Solution

- Displays the total number of moves.
- Prints every puzzle state from start to goal.

---

## Why Use DFS?

- DFS explores one branch as deeply as possible before backtracking.
- It may find a solution faster but does **not guarantee the shortest path**.

---

## Why Use a Stack?

- DFS follows the **LIFO (Last In, First Out)** principle.
- The last inserted state is explored first.

---

## Why Use a Visited Set?

- Prevents revisiting the same state.
- Avoids infinite loops and unnecessary exploration.

---

## Why Use Tuple Instead of List?

- Tuples are immutable and can be stored in a **set**.
- Lists are mutable and cannot be stored in a set.

---

## Program Flow

1. Start from the initial puzzle state.
2. Find the blank tile.
3. Generate valid successor states.
4. Explore states using DFS.
5. Avoid duplicate states using the visited set.
6. Stop when the goal state is found.
7. Print the solution path.

---

## Very Simple Viva Explanation

> This program solves the **8-Puzzle Problem** using the **Depth-First Search (DFS)** algorithm. It represents the puzzle as a tuple of tuples, where **0** is the blank tile. The program finds the blank tile, generates valid next states, and uses a **stack** to explore one path deeply before backtracking. A **visited** set prevents repeated states. When the goal state is reached, the solution path is printed.
