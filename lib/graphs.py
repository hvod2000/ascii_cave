def graph_inverse(graph):
    G_inv = {u: set() for u in graph}
    for u, vs in graph.items():
        for v in vs:
            G_inv[v].add(u)
    return G_inv


def topological_sort(graph):
    visited, ordered = set(), []

    def dfs(u):
        if u in visited:
            return
        visited.add(u)
        for v in graph[u]:
            dfs(v)
        ordered.append(u)

    for u in graph:
        dfs(u)
    return list(reversed(ordered))


def graph_components(graph):
    ordered = topological_sort(graph)
    G_inv = graph_inverse(graph)
    visited, components = set(), []

    def dfs(u):
        if u in visited:
            return
        components[-1].add(u)
        visited.add(u)
        for v in G_inv[u]:
            dfs(v)

    for u in ordered:
        if u not in visited:
            components.append(set())
            dfs(u)
    return components


def contract_graph(graph, groups):
    v2g = {}
    for i, group in enumerate(groups):
        for u in group:
            v2g[u] = i
    for u in graph:
        if u not in v2g:
            v2g[u] = len(groups)
            groups.append({u})
    result = {u: set() for u in range(len(groups))}
    for i, group in enumerate(groups):
        result[i] = {v2g[v] for u in group for v in graph[u]} - {i}
    return result


if __name__ == "__main__":
    print("Non! Vous n'utilisez pas le module graphique correctement.")
    graph = {0: {1, 2}, 1: {0, 2}, 2: {3}, 3: {4}, 4: {3}}
    print(components := graph_components(graph))
    print(contracted := contract_graph(graph, components))
