class Graph:
    def __init__(self, row: int, col: int, g: list[list[int]]):
        self.row = row
        self.col = col
        self.graph = g

    def is_safe(self, i: int, j: int, visited: list[list[bool]]):
        return (0 <= i < self.row and 0 <= j < self.col and
                not visited[i][j] and self.graph[i][j])

    def dfs(self, i: int, j: int, visited: list[list[bool]]):
        row_num = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_num = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        for k in range(8):
            if self.is_safe(i + row_num[k], j + col_num[k], visited):
                self.dfs(i + row_num[k], j + col_num[k], visited)

    def count_islands(self) -> int:
        visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j] is False and self.graph[i][j] == 1:
                    self.dfs(i, j, visited)
                    count += 1

        return count


if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 1, 1, 0, 1]]
    row = len(graph)
    col = len(graph[0])
    g = Graph(row, col, graph)
    print(g.count_islands())
