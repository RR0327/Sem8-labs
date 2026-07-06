# Hill Climbing Search Explanation

## 1. Graph Representation

- The Romania road map is represented as a **graph**.
- Each city is a node, and each road is an edge with a travel distance.
- The graph stores neighboring cities and their distances.

---

## 2. Heuristic Function

- The heuristic stores the **estimated straight-line distance (SLD)** from each city to Bucharest.
- It helps the algorithm choose the neighbor that appears closest to the goal.

---

## 3. Hill Climbing Function (`hill_climbing()`)

- Solves the Romania Road Map problem using the **Hill Climbing** algorithm.
- Starts from the initial city and repeatedly moves to the best neighboring city.

---

## 4. Current City

- The algorithm begins with the **start city**.
- This city becomes the current position for the search.

---

## 5. Path Initialization

- A path list is created to store the cities visited.
- The start city is added as the first city in the path.

---

## 6. Search Loop

- The algorithm continues searching until the goal city is reached.
- In each step, it examines the neighboring cities.

---

## 7. Getting Neighboring Cities

- Retrieves all cities directly connected to the current city.
- These cities are considered as possible next moves.

---

## 8. Choosing the Best Neighbor

- Selects the neighboring city with the **lowest heuristic value**.
- This city is considered the most promising move.

---

## 9. Improvement Checking

- Compares the heuristic value of the best neighbor with the current city.
- If there is no improvement, the search stops.

---

## 10. Moving to the Next City

- Updates the current city to the selected neighbor.
- Adds the new city to the path.

---

## 11. Returning the Solution

- Returns the path followed by the algorithm.
- Displays the sequence of cities from the start to the final city reached.

---

## Why Use Hill Climbing?

- Hill Climbing is simple and fast.
- It always chooses the best immediate move.
- It is suitable when a quick solution is needed.

---

## Why Use a Heuristic?

- The heuristic estimates how close each city is to the goal.
- It helps the algorithm make better decisions at each step.

---

## Why Compare Heuristic Values?

- The algorithm moves only if the next city has a lower heuristic value.
- This ensures progress toward the goal.

---

## Limitation of Hill Climbing

- Hill Climbing does **not always find the optimal solution**.
- It may stop at a **local maximum**, **local minimum**, or **plateau** even if the goal has not been reached.

---

## Program Flow

1. Start from the initial city.
2. Add the start city to the path.
3. Find all neighboring cities.
4. Choose the neighbor with the lowest heuristic value.
5. If the heuristic improves, move to that city.
6. Otherwise, stop the search.
7. Repeat until the goal is reached or no better neighbor exists.
8. Print the final path.

---

## Formula Used

### Heuristic Value (h)

```
h(n) = Estimated Distance from Current City to Goal
```

### Neighbor Selection

```
Choose the neighbor with the minimum heuristic value.
```

---

## Very Simple Viva Explanation

> This program solves the **Romania Road Map Problem** using the **Hill Climbing Search** algorithm. The map is represented as a graph, and each city has a heuristic value that estimates its distance to Bucharest. Starting from the initial city, the algorithm always moves to the neighboring city with the **lowest heuristic value**. If no better neighboring city exists, the search stops. Finally, the program prints the path followed by the algorithm.
