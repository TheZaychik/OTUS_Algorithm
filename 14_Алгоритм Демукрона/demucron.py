def demukron(adj_graph: dict) -> list:
    stack = []
    color = dict()
    for i in adj_graph.keys():
        color[i] = 0

    def topological_sort() -> list:
        def dfs(v: str) -> bool:
            if color[v] == 1:
                return True
            if color[v] == 2:
                return False
            color[v] = 1
            for i in range(len(adj_graph[v]) - 1):
                if dfs(adj_graph[v][i]):
                    return True
            stack.append(v)
            color[v] = 2
            return False

        for key in adj_graph.keys():
            if dfs(key):
                print("Имеется цикл")
                return []
        stack.reverse()
        
        return stack

    return topological_sort()


if __name__ == '__main__':
    # граф смежности
    graph = {'a': ['c'], 'c': ['b'], 'd': ['c', 'b', 't'], 'b': [], 't': []}
    print(demukron(graph))
