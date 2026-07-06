# A\* (A-Star) Search Explanation

## 1. Graph Representation

- The Romania road map is represented as a **graph**.
- Each city is a node, and each road is an edge with a travel distance.
- The graph stores neighboring cities and their distances.

---

## 2. Heuristic Function

- The heuristic stores the **estimated straight-line distance (SLD)** from each city to the goal city (Bucharest).
- It helps A\* choose the most promising path.

---

## 3. Priority Queue (`heapq`)

- A\* uses a **priority queue (min-heap)**.
- The city with the **lowest f-score** is explored first.
- Python's `heapq` module efficiently maintains this order.

---

## 4. A\* Search Function (`a_star_romanian()`)

- Solves the Romania Road Map problem using the **A\*** algorithm.
- Finds the shortest path from the start city to the goal city.

---

## 5. Queue Initialization

- The priority queue starts with the start city.
- It stores:
  - Current **f-score**
  - Current city
  - Path travelled
  - Current **g-score**

---

## 6. Visited Set

- Stores all explored cities.
- Prevents revisiting the same city.
- Improves search efficiency.

---

## 7. Priority Queue Loop

- Removes the city with the **smallest f-score**.
- Continues searching until the queue becomes empty or the goal is found.

---

## 8. Goal Checking

- Checks whether the current city is the goal city.
- If found, returns the shortest path and total distance.

---

## 9. Exploring Neighboring Cities

- Visits all neighboring cities of the current city.
- Calculates their travel costs.

---

## 10. Calculating the g-score

- **g-score** is the actual distance traveled from the start city.
- Formula:

```
g = Previous Cost + Road Distance
```

---

## 11. Calculating the f-score

- **f-score** estimates the total cost to reach the goal.
- Formula:

```
f = g + h
```

Where:

- **g** = Actual distance from the start.
- **h** = Heuristic (estimated distance to the goal).

---

## 12. Updating the Priority Queue

- Adds neighboring cities to the priority queue.
- The city with the lowest **f-score** will be explored next.

---

## 13. Printing the Solution

- Prints the shortest path from the start city to the goal.
- Displays the total travel distance.

---

## Why Use A\* Search?

- A\* finds the **shortest path efficiently**.
- It combines the actual travel cost and heuristic estimate.
- It usually explores fewer nodes than uninformed search algorithms.

---

## Why Use a Priority Queue?

- It always selects the city with the **lowest estimated total cost (f-score)**.
- This makes the search faster and more efficient.

---

## Why Use a Heuristic?

- The heuristic estimates how close a city is to the goal.
- It guides the search toward the destination.
- It reduces unnecessary exploration.

---

## Why Use a Visited Set?

- Prevents visiting the same city multiple times.
- Improves efficiency and avoids unnecessary processing.

---

## Program Flow

1. Start from the initial city.
2. Calculate the initial f-score.
3. Add the start city to the priority queue.
4. Remove the city with the lowest f-score.
5. Check if it is the goal city.
6. Explore all neighboring cities.
7. Calculate new g-score and f-score.
8. Add neighbors to the priority queue.
9. Repeat until the goal is found.
10. Print the shortest path and total distance.

---

## Formula Used

### Actual Cost (g)

```
g = Cost from Start to Current City
```

### Heuristic Cost (h)

```
h = Estimated Distance from Current City to Goal
```

### Total Cost (f)

```
f = g + h
```

---

## Very Simple Viva Explanation

> This program solves the **Romania Road Map Problem** using the **A\* Search Algorithm**. The road map is represented as a graph, where cities are nodes and roads are edges with travel distances. The algorithm uses a **priority queue** to always select the city with the lowest **f-score**, where **f = g + h**. Here, **g** is the actual distance traveled and **h** is the estimated distance to Bucharest (heuristic). A **visited** set prevents revisiting cities. When Bucharest is reached, the algorithm prints the shortest path and the total travel distance.
