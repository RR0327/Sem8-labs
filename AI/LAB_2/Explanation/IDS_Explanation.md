# IDS (Iterative Deepening Search) Explanation

## 1. Depth-Limited Search

- IDS repeatedly performs **Depth-Limited Search (DLS)**.
- The depth limit increases one level at a time.

---

## 2. Goal Checking Function (`is_goal()`)

- Checks whether the current puzzle state matches the goal state.
- Returns **True** if the goal is found.

---

## 3. Blank Tile Finding Function (`find_blank()`)

- Finds the position of the blank tile (`0`).
- Returns its row and column.

---

## 4. Successor Generation Function (`get_successors()`)

- Generates all valid next puzzle states.
- Moves the blank tile in four directions.

---

## 5. Valid Move Checking

- Ensures every move stays inside the puzzle boundary.

---

## 6. Creating a New State

- Converts tuples into lists for swapping.
- Creates a new puzzle configuration.

---

## 7. Swapping the Blank Tile

- Swaps the blank tile with a neighboring tile.
- Produces the next valid state.

---

## 8. Storing Successor States

- Converts the puzzle back into tuples.
- Stores the state for future exploration.

---

## 9. IDS Function (`ids()`)

- Solves the puzzle using **Iterative Deepening Search**.
- Repeats DLS with increasing depth limits until the goal is found.

---

## 10. Iterative Deepening

- Starts with depth limit **0**.
- Increases the limit step by step until a solution is found.

---

## 11. Goal Checking in IDS

- Checks whether the current state matches the goal.
- Returns the solution path if found.

---

## 12. Generating Next States

- Generates valid successor states.
- Explores them within the current depth limit.

---

## 13. Printing the Solution

- Displays the number of moves.
- Prints every state from start to goal.

---

## Why Use IDS?

- Combines the advantages of **DFS** and **BFS**.
- Uses less memory than BFS while still finding the shortest solution.

---

## Why Increase the Depth Limit?

- Ensures shallow solutions are found first.
- Gradually explores deeper levels.

---

## Why Use a Visited Set?

- Prevents revisiting the same states.
- Improves search efficiency.

---

## Why Use Tuple Instead of List?

- Tuples are immutable and can be stored in a set.
- Lists cannot be stored in a set.

---

## Program Flow

1. Start from the initial puzzle state.
2. Begin with depth limit 0.
3. Run DLS.
4. Increase the depth limit if the goal is not found.
5. Repeat until the goal is reached.
6. Print the solution path.

---

## Very Simple Viva Explanation

> This program solves the **8-Puzzle Problem** using **Iterative Deepening Search (IDS)**. It repeatedly performs **Depth-Limited Search (DLS)** with increasing depth limits until the goal is found. The program finds the blank tile, generates valid moves, and gradually searches deeper while using less memory than BFS. Once the goal state is reached, the complete solution path is printed.
