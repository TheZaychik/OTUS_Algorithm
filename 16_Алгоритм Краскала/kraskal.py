graph = [(13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
         (26, 2, 3), (22, 2, 5), (3, 3, 4), (19, 4, 6)]

graph_sorted = sorted(graph, key=lambda x: x[0])
U = set()
D = {}
T = []

for gs in graph_sorted:
    if gs[1] not in U or gs[2] not in U:
        if gs[1] not in U and gs[2] not in U:
            D[gs[1]] = [gs[1], gs[2]]
            D[gs[2]] = D[gs[1]]
        else:
            if not D.get(gs[1]):
                D[gs[2]].append(gs[1])
                D[gs[1]] = D[gs[2]]
            else:
                D[gs[1]].append(gs[2])
                D[gs[2]] = D[gs[1]]

        T.append(gs)
        U.add(gs[1])
        U.add(gs[2])

for gs in graph_sorted:
    if gs[2] not in D[gs[1]]:
        T.append(gs)
        gr1 = D[gs[1]]
        D[gs[1]] += D[gs[2]]
        D[gs[2]] += gr1

print(T)
