class Vertex:
    def __init__(self, value: str) -> None:
        self.value = value
        self.d = None
        self.f = None


class Graph:

    def __init__(self) -> None:
        self.adj = {}

    def has_vertex(self, v: Vertex) -> bool:
        try:
            self.adj[v]
            return True
        except KeyError:
            return False

    def add_vertex(self, v: Vertex) -> bool:
        if self.has_vertex(v):
            return False
        else:
            self.adj[v] = {}
            return True

    def add_vertices(self, arr: list) -> bool:
        for v in arr:
            self.add_vertex(v)
        return True

    def has_edge(self, start: Vertex, end: Vertex) -> bool:
        if self.has_vertex(start) and self.has_vertex(end):
            try:
                if self.adj[start][end] is True:
                    return True
                return False
            except KeyError:
                return False
        return False

    def add_edge(self, start: Vertex, end: Vertex) -> bool:
        if self.has_vertex(start) and self.has_vertex(end):
            self.adj[start][end] = True
            return True
        return False

    def remove_edge(self, start: Vertex, end: Vertex) -> bool:
        if self.has_edge(start, end):
            del self.adj[start][end]
            return True
        return False

    def remove_vertex(self, v: Vertex) -> bool:
        if self.has_vertex(v):
            for vertex in self.adj.keys():
                self.remove_edge(vertex, v)
            del self.adj[v]
            return True
        return False


time = 0


def dfs_visit(G: Graph, s: Vertex, parent: Vertex, stack: list) -> None:
    global time
    time += 1
    s.d = time

    for v in G.adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(G, v, parent, stack)

    time += 1
    s.f = time
    stack.append(s)


def dfs(G: Graph, stack: list) -> list:
    parent = {}
    stack = []

    for vertex in list(G.adj.keys()):
        if vertex not in parent:
            parent[vertex] = None
            dfs_visit(G, vertex, parent, stack)

    return stack


def dfs_single_visit(adj_list: dict, v: dict, visited: dict, stack: list) -> None:
    for u in adj_list[v]:
        if u not in visited:
            visited[u] = v
            dfs_single_visit(adj_list, u, visited, stack)
    stack.append(v)


def kosaraju(G: Graph) -> list:
    stack = dfs(G, [])

    rev_adj = {}

    for vertex in G.adj.keys():
        rev_adj[vertex] = {}

    for vertex in G.adj.keys():
        for u in G.adj[vertex]:
            rev_adj[u][vertex] = True

    visited = {}
    components = []
    i = 0

    while stack:
        v = stack.pop()
        if v in visited:
            continue
        else:
            components.append([])
            if v not in visited:
                visited[v] = True
                dfs_single_visit(rev_adj, v, visited, components[i])

            components.append([])
            i += 1

    return components


if __name__ == '__main__':
    G = Graph()

    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')

    G.add_vertices([a, b, c, d])
    G.add_edge(a, b)
    G.add_edge(b, c)
    G.add_edge(c, a)
    G.add_edge(b, d)

    y = kosaraju(G)

    for j in range(len(y)):
        if y[j]:
            print("Компонент:", j + 1, "(", end=" ")
            for v in y[j]:
                print(v.value, end=" ")
            print(")")
