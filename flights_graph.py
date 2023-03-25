from graph import Graph

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