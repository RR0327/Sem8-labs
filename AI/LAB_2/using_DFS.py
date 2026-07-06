
# =====================================================
# 8-Puzzle Problem using DFS
# =====================================================

# --- Check if state is goal ---
def is_goal(state, goal):
    return state == goal


# --- Find blank position ---
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# --- Generate successors ---
def get_successors(state):
    successors = []
    x, y = find_blank(state)

    # Possible moves: Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]

            # Swap blank tile with neighbor tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            # Convert list back to tuple
            successors.append(tuple(tuple(row) for row in new_state))

    return successors


# --- DFS Search ---
def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if is_goal(state, goal):
            return path

        if state not in visited:
            visited.add(state)

            for successor in get_successors(state):
                if successor not in visited:
                    stack.append((successor, path + [successor]))

    return None


# --- Print Solution ---
def print_solution(solution):
    if solution:
        print(f"Solution found in {len(solution)-1} moves:")

        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")


# --- Initial State ---
initial_state = (
    (1, 2, 3),
    (4, 0, 5),
    (6, 7, 8)
)

# --- Goal State ---
goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)


# --- Run DFS ---
solution = dfs(initial_state, goal_state)
print_solution(solution)

# --- Final Line ---
if solution:
    print(f"Solution found in {len(solution)-1} moves.")
else:
    print("No solution found.")