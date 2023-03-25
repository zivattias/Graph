from typing import Union, List, Optional


class Graph:
    def __init__(self, directed=False):
        self._nodes: dict[str, set] = {}
        self._weights: dict[tuple, int] = {}
        self._directed = directed

    def add_node(self, node):
        self._nodes[node] = set()

    def add_edge(
        self,
        from_node: str,
        to_node: Union[str, List[str]],
        weight: Union[int, List[int]],
    ):
        if from_node not in self._nodes:
            self.add_node(from_node)

        if isinstance(to_node, list) and isinstance(weight, list):
            if len(to_node) != len(weight):
                raise NotImplemented("Weights and nodes length do not match")

            for node, w in zip(to_node, weight):
                if node not in self._nodes:
                    self.add_node(node)
                self._nodes[from_node].add(node)
                self._weights[(from_node, node)] = w
                if not self._directed:
                    self.add_edge(node, from_node, w)

        else:
            if to_node not in self._nodes:
                self.add_node(to_node)
            self._nodes[from_node].add(to_node)
            self._weights[(from_node, to_node)] = weight
            if not self._directed:
                self.add_edge(to_node, from_node, weight)

    def is_adjacent(self, node_1, node_2) -> int:
        if node_2 in self._nodes.get(node_1, set()):
            return -1
        elif node_1 in self._nodes.get(node_2, set()):
            return 1
        else:
            return 0

    def get_nodes(self) -> dict:
        return self._nodes

    def get_weights(self) -> dict:
        return self._weights

    def dfs(self, from_node, to_node) -> bool:
        return self._dfs_rec(from_node, to_node, set())

    def _dfs_rec(self, from_node, to_node, visited) -> bool:
        if from_node == to_node:
            return True

        visited.add(from_node)
        for node in self._nodes[from_node]:
            if node not in visited:
                if self._dfs_rec(node, to_node, visited):
                    return True
        return False

    def _cheapest_path_rec(
        self, to_node, unvisited: list, distance, previous
    ):
        if len(unvisited) > 0:
            min_vertex = min(unvisited, key=lambda v: distance[v])

            if not min_vertex:
                return None

            unvisited.pop(unvisited.index(min_vertex))

            for neighbor in self._nodes[min_vertex]:
                if neighbor in unvisited:
                    alt = distance[min_vertex] + self._weights[(min_vertex, neighbor)]
                    distance[neighbor] = alt
                    previous[neighbor] = min_vertex
                    
            self._cheapest_path_rec(to_node, unvisited, distance, previous)


        return distance[to_node], self.get_path(to_node, previous) if distance[to_node] != float("inf") else None

    def cheapest_path(self, from_node, to_node):
        distance: dict[str, float] = {}
        previous: dict[str, Optional[str]] = {}

        for node in self._nodes:
            distance[node] = float("inf")
            previous[node] = None
        distance[from_node] = 0

        unvisited = list(self._nodes)

        return self._cheapest_path_rec(
            to_node, unvisited, distance, previous
        )

    def _get_path_rec(self, to_node, previous: dict, current_node=None, path: Optional[list]=None):
        if not current_node:
            return " -> ".join(list(reversed(path))[1::])

        path.append(previous[to_node])

        return self._get_path_rec(to_node=path[-1], previous=previous, current_node=path[-1], path=path)

    def get_path(self, to_node, previous):
        current_node = to_node
        path = [to_node]

        return self._get_path_rec(to_node, previous, current_node, path)

        


if __name__ == "__main__":
    graph = Graph(directed=True)
    for city in (
        "Brussels",
        "Kyoto",
        "Tokyo",
        "Tel-Aviv",
        "Amsterdam",
        "Paris",
        "London",
        "Hong Kong",
    ):
        graph.add_node(city)

    graph.add_edge("Brussels", ["Tokyo", "Tel-Aviv"], [5, 1])
    graph.add_edge("Tokyo", ["Kyoto", "Hong Kong"], [1, 2])
    graph.add_edge("Hong Kong", "Tel-Aviv", 7)
    graph.add_edge("Tel-Aviv", "Paris", 2)
    graph.add_edge("Paris", ["Tel-Aviv", "Amsterdam", "London"], [2, 1, 1])
    # Mexico City is not initially added as a node, checking add_node within add_edge case
    graph.add_edge("Mexico City", "Tel-Aviv", 9)

    print(f"Path from Brussels to Amsterdam: {graph.dfs('Brussels', 'Amsterdam')}")
    print(f"Path from Tokyo to Tel-Aviv: {graph.dfs('Tokyo', 'Tel-Aviv')}")
    print(f"Path from London to Kyoto: {graph.dfs('London', 'Kyoto')}")
    print(f"Path from Mexico City to Tel-Aviv: {graph.dfs('Mexico City', 'Tel-Aviv')}")
    print(f"Path from Tel-Aviv to Mexico City: {graph.dfs('Tel-Aviv', 'Mexico City')} \n")

    cost, trail = graph.cheapest_path('Brussels', 'Paris')
    print(f"Cheapest path from Brussels to Paris: {cost}")
    print(f"Path from Brussels to Paris: {trail} \n")

    cost, trail = graph.cheapest_path('Brussels', 'Amsterdam')
    print(f"Cheapest path from Brussels to Amsterdam: {cost}")
    print(f"Path from Brussels to Amsterdam: {trail}")
