from collections import deque

N, M = map(int, input().split())
G = {i: {} for i in range(N + 2)}
for i in range(N):
    a, b = map(int, input().split())
    G[0][i] = a
    G[i][N + 1] = b
for k in range(M):
    i, j, c = map(int, input().split())
    G[i][j] = c


def bfs(G, start, finish):
    parent = {}
    visited = set()

    q = deque()
    q.append(start)
    visited.add(start)
    parent[start] = start

    while len(q) > 0:
        current = q.popleft()

        if current == finish:
            break

        for neighbor in G[current]:
            if G[current][neighbor] > 0 and neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                q.append(neighbor)

    if finish not in parent:
        return 0, None

    flow = float("inf")
    v = finish
    while v != start:
        u = parent[v]
        flow = min(flow, G[u][v])
        v = u

    return flow, parent


def edmonds_karp(G, start, finish):
    res = 0

    while True:
        flow, parent = bfs(G, start, finish)
        if flow == 0:
            break
        v = finish
        while v != start:
            u = parent[v]
            G[u][v] -= flow
            if v not in G:
                G[v] = {}
            G[v][u] = G[v].get(u, 0) + flow
            v = u

        res += flow

    return res


print(edmonds_karp(G, 0, N + 1))
