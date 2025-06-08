from collections import deque

def count_islands_8dir(grid):
    if not grid:
        return 0

    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]

    # 8-direction deltas
    DIRS = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)]

    def bfs(sr, sc):
        """Mark the entire island containing (sr, sc)."""
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C \
                   and not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))

    islands = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1 and not visited[r][c]:
                islands += 1
                bfs(r, c)

    return islands

# === Hardcoded input grid ===
grid = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

# === Run the function and print output ===
print("Number of islands (8-direction):", count_islands_8dir(grid))
