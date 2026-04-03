from collections import deque


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


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total_a = sum(a)
total_b = sum(b)

if total_a > total_b:
    print("NO")
else:
    source = 2 * n
    sink = 2 * n + 1

    G = {i: {} for i in range(2 * n + 2)}

    for i in range(n):
        G[source][i] = a[i]

    INF = 10**15
    for i in range(n):
        for j in range(n):
            G[i][n + j] = INF

    for j in range(n):
        G[n + j][sink] = b[j]

    max_flow_value = edmonds_karp(G, source, sink)

    if max_flow_value == total_a:
        print("YES")
    else:
        print("NO")
