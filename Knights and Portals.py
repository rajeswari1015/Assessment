from collections import deque

def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    q = deque([start])
    dist[start[0]][start[1]] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and dist[nr][nc] == float('inf'):
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist

def shortest_path_with_portal(grid):
    rows, cols = len(grid), len(grid[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    dist_from_start = bfs(grid, start)
    dist_from_end = bfs(grid, end)

    min_path = dist_from_start[end[0]][end[1]]  # path without teleport

    empty_cells = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] != '#']

    for (r1, c1) in empty_cells:
        for (r2, c2) in empty_cells:
            if (r1, c1) != (r2, c2):
                # Disallow teleporting directly from start to end
                if (r1, c1) == start and (r2, c2) == end:
                    continue
                d1 = dist_from_start[r1][c1]
                d2 = dist_from_end[r2][c2]
                if d1 != float('inf') and d2 != float('inf'):
                    min_path = min(min_path, d1 + 1 + d2)

    return min_path if min_path != float('inf') else -1

# === Hardcoded Grid Input ===
grid = [
    ['.', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '#'],
    ['.', '.', '.', '#', '.', '.', '.']
]

# === Run the Function and Print Output ===
result = shortest_path_with_portal(grid)
print("Shortest path with one portal:", result)
