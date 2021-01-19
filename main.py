"""
1. 모든 문제에 대해 방심하지 않는다.
2. 제한 시간 내에 해결할 수 있는 방법을 생각한다.
3. 주어진 변수의 범위를 확인한다.
4. 범위의 최소값과 최대값에 대한 반례를 찾는다.
5. 문제를 풀기 전에 전략을 수립한다.
6. 예제에 모든 반례가 포함된 것은 아니다.
"""
from collections import deque

n, m = 6, 5

arr = [  # 6 * 5 배열
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1]
]

vis = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1, 0]

dy = [0, 0, 1, 0, -1]  # x, y축 좌표 이동

num, mx = 0, 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 or vis[i][j]: continue
        num += 1
        q = deque()
        vis[i][j]
        q.append([i, j])
        area = 0
        while not len(q) == 0:
            cur_x, cur_y = q.popleft()
            for d in range(5):
                nx, ny = cur_x + dx[d], cur_y + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                if vis[nx][ny] or arr[nx][ny] != 1: continue
                vis[nx][ny] = 1
                q.append([nx, ny])
                area += 1

        mx = max(mx, area)

print(num); print(mx)

# author : dolphin
