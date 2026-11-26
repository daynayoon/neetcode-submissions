class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs: 최단 거리
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()

        # put all 0 to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # for each new direction, if it's INF, update the distance and enque
        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    # update the distance from the nearest -> become not INF
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
                    