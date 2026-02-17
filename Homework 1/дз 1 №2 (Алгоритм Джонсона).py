import heapq
from math import inf

N, M = map(int, input().split())
graph = {i: {} for i in range(N)}

for i in range(M):
    v1, v2, weight = input().split()
    v1, v2, weight = int(v1), int(v2), float(weight)
    graph[v1][v2] = weight


def bellman_ford(G, start):

    n = len(G)
    d = {i: float("inf") for i in G}
    d[start] = 0

    for i in range(n - 1):
        for u in G:
            for v, w in G[u].items():
                if d[u] != float("inf") and d[v] > d[u] + w:
                    d[v] = d[u] + w

    for u in G:
        for v, w in G[u].items():
            if d[u] != float("inf") and d[v] > d[u] + w:
                return None

    return d


def dijkstra(G, start):
    n = len(G)
    dist = [inf] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in G[u].items():
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))

    return dist


def johnson(G):

    n = len(G)
    vertices = list(range(n))

    s = n
    G_with_s = {i: G[i].copy() for i in range(n)}
    G_with_s[s] = {v: 0 for v in vertices}

    h_dict = bellman_ford(G_with_s, s)
    if h_dict is None:
        return None

    h = [h_dict[i] for i in range(n)]

    G_new = {i: {} for i in range(n)}
    for u in range(n):
        for v, w in G[u].items():
            G_new[u][v] = w + h[u] - h[v]

    dist_dijkstra = [[inf] * n for i in range(n)]

    for u in range(n):
        dist_u = dijkstra(G_new, u)
        for v in range(n):
            if dist_u[v] < inf:
                dist_dijkstra[u][v] = dist_u[v] - h[u] + h[v]

    return dist_dijkstra


result = johnson(graph)

print(result)
