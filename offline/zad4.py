"""
Zuzanna Olszówka
F(i,p) - max liczba studentów, którzy zamieszkają w budynkach od 0 do i, które na siebie nie nachodzą i ich koszt jest <= p
h,a,b,w=T[i]
v=h*(b-a)
F[i][p]=max(F[i-1][p],F[prev[i]][p-w]+v)
Na początku dla każdego budynku szukam pierwszego budynku przed nim, który na niego nie nachodzi i wpisuję indeksy do tablicy prev.
Następnie podobnie jak w problemie plecakowym sprawdzam czy opłaca się wybudować budynek, ale porównuję z budynkiem, który mogłam użyć, czyli o indeksie w prev[i].
Na koniec odtwarzam wynik.

złożoność czasowa: O(n^2+np)
"""

from zad4testy import runtests


def previous(T):  # O(n^2)
    n = len(T)
    prev = [-1 for _ in range(n)]
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if T[j][2] < T[i][1]:
                prev[i] = j
                break
    return prev


def get_buildings(F, T, Indx, prev, p):  # O(n)
    n = len(T)
    max_v, min_price = 0, p + 1
    for i in range(p + 1):
        if F[n - 1][i] > max_v:
            max_v = F[n - 1][i]
            min_price = i

    res = []
    i = n - 1
    while max_v != 0:
        h, a, b, w = T[i]
        v = h * (b - a)
        if max_v == v and min_price == w:
            res.append(Indx[i][0])
            break
        elif min_price - w >= 0:
            if F[i][min_price] == F[prev[i]][min_price - w] + v:
                res.append(Indx[i][0])
                max_v -= v
                min_price -= w
                i = prev[i]
            else:
                i -= 1
        else:
            i -= 1

    return res


def select_buildings(T, p):  # O(n^2+np)
    n = len(T)
    Indx = []
    for i in range(n):
        Indx.append((i, T[i][2]))
    Indx.sort(key=lambda x: x[1])  # O(nlogn)
    T.sort(key=lambda x: x[2])  # O(nlogn)
    prev = previous(T)  # O(n^2)

    F = [[-1 for _ in range(p + 1)] for _ in range(n)]

    h, a, b, w = T[0]
    v = h * (b - a)
    for i in range(w, p + 1):
        F[0][i] = v

    for i in range(1, n):  # O(np)
        h, a, b, w = T[i]
        v = h * (b - a)
        for price in range(p + 1):
            F[i][price] = F[i - 1][price]
            if price >= w:
                F[i][price] = max(F[i][price], v)
                if prev[i] != -1:
                    F[i][price] = max(F[i][price], F[prev[i]][price - w] + v)

    res = get_buildings(F, T, Indx, prev, p)
    res.sort()
    return res


runtests(select_buildings)
