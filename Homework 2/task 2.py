def dfs(G, visited, matching, start):
    if start in visited:
        return False
    visited.add(start)
    for i in G[start]:
        if matching[i] is None or dfs(G, visited, matching, matching[i]):
            matching[i] = start
            matching[start] = i
            return True
    return False


def Kuhn2(G, half):
    matching = {i: None for i in G}
    for i in half:
        visited = set()
        if matching[i] is None:
            dfs(G, visited, matching, i)
    return matching


def edge_min(G, half):
    matching = Kuhn2(G, half)
    used_v = set()
    for u, v in matching.items():
        if v is not None:
            used_v.add(u)
            used_v.add(v)
    result = set()
    for u, v in matching.items():
        if (u, v) not in result and (v, u) not in result:
            result.add((u, v))
    for vertex in G:
        if vertex not in used_v:
            if G[vertex]:
                for neighbor in G[vertex]:
                    result.add((vertex, neighbor))
                    break
    return result
