from lib import graphs


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
