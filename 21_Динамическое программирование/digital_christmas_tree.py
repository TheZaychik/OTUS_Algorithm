def dct(tree: list[list[int]]) -> None:
    i = len(tree) - 2
    while i >= 0:
        for j in range(i + 1):
            tree[i][j] += max(tree[i + 1][j], tree[i + 1][j + 1])
        i -= 1


if __name__ == '__main__':
    chris_tree = [
        [1],
        [2, 3],
        [4, 5, 6],
        [9, 8, 0, 3]
    ]
    dct(chris_tree)
    print(chris_tree[0][0])
