
"""8-Puzzle using IDS"""

# =====================================================
# 8-Puzzle Problem using IDS
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


# --- DLS Function for IDS ---
def dls(start, goal, limit):
    return recursive_dls(start, goal, limit, [start])


def recursive_dls(state, goal, limit, path):
    if is_goal(state, goal):
        return path

    if limit == 0:
        return None

    for successor in get_successors(state):
        # Avoid repeated state in the current path
        if successor not in path:
            result = recursive_dls(successor, goal, limit - 1, path + [successor])

            if result is not None:
                return result

    return None


# --- IDS Search ---
def ids(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Checking depth limit: {depth}")

        result = dls(start, goal, depth)

        if result is not None:
            return result

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


# --- Run IDS ---
max_depth = 30
solution = ids(initial_state, goal_state, max_depth)
print_solution(solution)