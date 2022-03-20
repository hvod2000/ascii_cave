from lib import graphs

wall = object()


class Cave:
    def __init__(self, cells, items):
        self.cells = cells
        self.items = items

    @staticmethod
    def from_levels_topology(top):
        order = list(reversed(graphs.topological_sort(top.graph)))
        levels = [top.levels[i] for i in order]
        order = {j: i for i, j in enumerate(order)}
        graph = {order[u]: {order[v] for v in V} for u, V in top.graph.items()}
        lvl_size = max(len(lvl) for lvl in levels)
        lvl_size = max(lvl_size, len(levels) * 2 - 1)
        cave, items = [], []
        for u, level_content in enumerate(levels):
            cave.append([[wall] * (lvl_size + 2) for _ in range(5)])
            layer = [[wall] * (lvl_size + 2) for _ in range(5)]
            for j in range(u):
                cave[-1][3][1 + j * 2] = None
                layer[3][1 + j * 2] = None
            for j in range(lvl_size):
                layer[1][1 + j] = None
            for v in graph[u]:
                layer[2][1 + v * 2] = None
            for i, item in enumerate(level_content):
                layer[1][1 + i] = len(items)
                items.append(item)
            layer[2][1 + 2 * u] = None
            layer[3][1 + 2 * u] = None
            cave.append(layer)
        return Cave(cave, items)


class LevelsTopology:
    def __init__(self, levels, available_moves):
        self.levels = levels
        self.graph = available_moves

    @staticmethod
    def from_available_moves(graph):
        levels = graphs.graph_components(graph)
        graph = graphs.contract_graph(graph, levels)
        return LevelsTopology(levels, graph)


if __name__ == "__main__":
    pass
