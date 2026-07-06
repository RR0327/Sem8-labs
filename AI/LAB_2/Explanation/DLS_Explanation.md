# DLS (Depth-Limited Search) Explanation

## 1. Stack

- DLS uses a **stack** like DFS.
- It also stores the current search depth.

---

## 2. Depth Limit

- DLS searches only up to a predefined depth limit.
- States beyond the limit are not explored.

---

## 3. Goal Checking Function (`is_goal()`)

- Checks whether the current state is the goal state.
- Returns **True** if found; otherwise returns **False**.

---

## 4. Blank Tile Finding Function (`find_blank()`)

- Finds the position of the blank tile (`0`).
- Returns its row and column.

---

## 5. Successor Generation Function (`get_successors()`)

- Generates all valid next puzzle states.
- Moves the blank tile in four possible directions.

---

## 6. Valid Move Checking

- Ensures every move stays inside the puzzle boundary.

---

## 7. Creating a New State

- Converts tuples into lists for swapping.
- Creates a new puzzle configuration.

---

## 8. Swapping the Blank Tile

- Swaps the blank tile with an adjacent tile.
- Produces a valid successor state.

---

## 9. Storing Successor States

- Converts the puzzle back into tuples.
- Stores the state for further exploration.

---

## 10. DLS Function (`dls()`)

- Solves the puzzle using **Depth-Limited Search**.
- Explores states only up to the specified depth limit.

---

## 11. DLS Loop

- Removes the latest state from the stack.
- Stops exploring when the depth limit is reached.

---

## 12. Goal Checking in DLS

- Checks whether the current state is the goal.
- Returns the solution path if found.

---

## 13. Generating Next States

- Generates valid successor states.
- Adds only states within the depth limit.

---

## 14. Printing the Solution

- Displays the number of moves.
- Prints each state from start to goal.

---

## Why Use DLS?

- Prevents searching too deeply.
- Reduces unnecessary exploration.

---

## Why Use a Depth Limit?

- Controls the maximum search depth.
- Prevents excessive memory and time usage.

---

## Why Use a Visited Set?

- Avoids revisiting the same states.
- Improves search efficiency.

---

## Why Use Tuple Instead of List?

- Tuples can be stored in a set.
- Lists cannot.

---

## Program Flow

1. Start from the initial state.
2. Find the blank tile.
3. Generate successor states.
4. Explore using DLS.
5. Stop when the depth limit is reached.
6. Return the solution if found.
7. Print the solution path.

---

## Very Simple Viva Explanation

> This program solves the **8-Puzzle Problem** using **Depth-Limited Search (DLS)**. It works like DFS but searches only up to a fixed depth limit. The program finds the blank tile, generates valid moves, and uses a **stack** with a **depth limit** to control the search. A **visited** set avoids repeated states. If the goal is found within the limit, the solution path is printed.
