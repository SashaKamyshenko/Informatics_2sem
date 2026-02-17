from collections import deque

N, M = map(int, input().split())
graph = {i: set() for i in range(N)}
for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
# print(graph)


def deg(G, start):
    res = len(G[start])
    return res


visited = set()
order = []

queue = deque()


def bfs(G, start, queue, order, visited):
    queue.append(start)
    visited.add(start)
    while queue:
        current = queue.popleft()
        order.append(current)
        for i in G[current]:
            if i not in visited:
                queue.append(i)
                visited.add(i)


def connected_components(graph):
    N = 0
    visited = set()
    for i in graph:
        if i not in visited and deg(graph, i) != 0:
            N += 1
            bfs(graph, i, queue, order, visited)
    return N


odd_vertex = []


def exist(G):
    odd = 0
    for i in G:
        if int(deg(G, i)) % 2 != 0:
            odd += 1
            odd_vertex.append(i)
    if odd == 2 or odd == 0 and connected_components(G) == 1:
        return True
    else:
        return False


# print(exist(graph))
# print(odd_vertex)

result = []


def euler(G):
    if exist(G) is False:
        return None
    if len(odd_vertex) != 0:
        start = odd_vertex[0]
    else:
        start = None
        for v in G:
            if len(G[v]) > 0:
                start = v
                break

    def dfs(v):
        while G[v]:
            u = list(G[v])[0]
            G[v].remove(u)
            G[u].remove(v)
            dfs(u)
        result.append(v)

    dfs(start)
    return result[::-1]


print(euler(graph))
