class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # O cell이 가장자리 하고 연결되어있는 구역은 전부 살아남고 아닌건 전부 죽음
        
        rows, cols = len(board), len(board[0])
        q = deque()

        # 가장자리 O 전부 큐에 넣기
        for r in range(rows):
            for c in range(cols):
                if (r in (0, rows-1) or c in (0, cols-1)) and board[r][c] == 'O':
                    q.append((r, c))
                    board[r][c] = 'T'

        # set all connected O to T
        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'T'
                    q.append((nr, nc))

        # set all left O to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # set all T to O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        