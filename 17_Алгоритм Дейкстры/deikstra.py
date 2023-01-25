def dijkstra(current, nodes, distances):
    unvisited = {node: None for node in nodes}
    visited = {}
    current_distance = 0
    unvisited[current] = current_distance
    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            new_distance = current_distance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        print(sorted(candidates, key=lambda x: x[1]))
        current, current_distance = sorted(candidates, key=lambda x: x[1])[0]
    return visited


nodes = ('A', 'B', 'C', 'D', 'E')
distances = {
    'A': {'B': 5, 'C': 2},
    'B': {'C': 2, 'D': 3},
    'C': {'B': 3, 'D': 7},
    'D': {'E': 7},
    'E': {'D': 9}}
current = 'A'

print(dijkstra(current, nodes, distances))
