N, M = map(int, input().split())
graph = {i: {} for i in range(N)}

for i in range(M):
    v1, v2, rate = map(float, input().split())
    v1, v2 = int(v1), int(v2)
    graph[v1][v2] = rate
# print(graph)


def rich(n, graph, start=0):
    dist = [0.0] * n
    dist[start] = 1.0

    for _ in range(n - 1):
        updated = False
        for v1 in range(n):
            for v2, rate in graph[v1].items():
                if dist[v1] > 0 and dist[v2] < dist[v1] * rate:
                    dist[v2] = dist[v1] * rate
                    updated = True
        if not updated:
            break

    for v1 in range(n):
        for v2, rate in graph[v1].items():
            if dist[v1] > 0 and dist[v2] < dist[v1] * rate:
                return True

    return False


result = rich(N, graph)
print(result)
