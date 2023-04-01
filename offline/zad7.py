"""
Zuzanna Olszówka

Program używa DFS'a do utworzenia wszyskich ścieżek zawierających wszystkie wierzchołki.
Gdy przegląda nieodwiedzonych sąsiadów do których możemy dojść od danej bramy sprawdza którą bramą wejdziemy do sąsiada.
Dalej do funkcji rekurencyjnej przekazuję, numer bramy którą nie weszliśmy do miasta.
Gdy ścieżka ma długość n (zawiera już wszystkie wierzchołki) i z ostatniego sprawdzanego miasta
da się dość podaną bramą do miasta 0 to funkcja zwraca wartość True, że ścieżka została znaleziona.
"""

from zad7testy import runtests


def droga(G):
    def ispath(G, u, path, n, visited, gate, find):
        if len(path) == n and 0 in G[u][gate]:
            return True

        for v in G[u][gate]:
            if not visited[v] and not find:
                if u not in G[v][0]:
                    visited[v] = True
                    path.append(v)
                    find = ispath(G, v, path, n, visited, 0, find)
                    if find:
                        return find
                    visited[v] = False
                    path.pop()
                elif u not in G[v][1]:
                    visited[v] = True
                    path.append(v)
                    find = ispath(G, v, path, n, visited, 1, find)
                    if find:
                        return find
                    visited[v] = False
                    path.pop()

    n = len(G)
    find = False
    visited1 = [False] * n
    path1 = [0]
    visited1[0] = True
    res1 = ispath(G, 0, path1, n, visited1, 0, find)

    if res1:
        return path1
    else:
        return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
