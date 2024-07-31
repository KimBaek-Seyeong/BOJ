from collections import deque

m, n, h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()
dx, dy, dz = [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, -1]
res = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if matrix[k][i][j] == 1:
                queue.append((k, i, j))

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and matrix[nz][nx][ny] == 0:
                matrix[nz][nx][ny] = matrix[z][x][y] + 1
                queue.append((nz, nx, ny))

bfs()
for k in range(h):
    for i in range(n):
        for j in range(m):
            if matrix[k][i][j] == 0:
                print(-1)
                exit(0)
            res = max(res, matrix[k][i][j])
print(res - 1)
