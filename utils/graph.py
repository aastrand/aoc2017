def bfs(start, graph):
    visited = set()
    q = []

    q.append(start)
    visited.add(start)

    while len(q) > 0:
        cur = q.pop(0)
        for n in graph.get(cur, []):
            if not n in visited:
                q.append(n)
                visited.add(n)

    return visited
