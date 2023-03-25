from pprint import pprint

from graph import Graph

if __name__ == "__main__":
    graph = Graph(directed=False)

    for person in [
        "David",
        "Ron",
        "James",
        "Julia",
        "Mor",
        "Nathan",
        "Jim",
        "Dor",
    ]:
        graph.add_node(person)

    graph.add_edge("David", "James", 1)
    graph.add_edge("Ron", "Julia", 1)
    graph.add_edge("Julia", "Mor", 1)
    graph.add_edge("James", "Jim", 1)
    graph.add_edge("Mor", "Jim", 1)
    graph.add_edge("Mor", "Nathan", 1)
    graph.add_edge("Jim", "Dor", 1)

    pprint(graph.get_nodes())

    print(
        f"Are David and Jim 2nd degree related? {graph.is_second_degree_related('David', 'Jim')}"
    )

    data = graph.cheapest_path("David", "Nathan")
    if data:
        distance = data[0]
        path = data[1]
        print(f"Distance from David to Nathan: {distance}, path: {path}")
