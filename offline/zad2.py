"""
Zuzanna Olszówka
Podaną tablicę przedziałów sortuję najpierw po początkach przedziałów i zapisuję indeksy, na których występują w posortowanej kolejności.
Następnie robię to samo z końcami przedziałów. Jeśli kilka przedziałów ma tę samą wartość początkową lub końcową, to zapisują dla nich
najmniejszy indeks występowania dla początków, a największy dla końców.
Maksimum z poziomów wyznaczam obliczając różnicę w indeksach kolejności występowania posortowanych przedziałów.
Złożoność obliczeniowa: O(nlogn)
"""

from zad2testy import runtests


def partition(A, p, r, indx):
    A[r], A[(p + r) // 2] = A[(p + r) // 2], A[r]     #program działa znacznie szybciej dla pivota na innej pozycji niż na pozycji r, wybrałam (p + r) // 2
    x = A[r][indx]
    i = p - 1
    for j in range(p, r):
        if A[j][indx] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r, indx):               # O(nlogn)
    while p < r:
        q = partition(A, p, r, indx)
        if (q - p) > (r - q):
            quicksort(A, q + 1, r, indx)
            r = q - 1
        else:
            quicksort(A, p, q - 1, indx)
            p = q + 1


def depth(T):
    for i in range(len(T)):                 # O(n)
        T[i] = [T[i][0], T[i][1], -1, -1]

    quicksort(T, 0, len(T) - 1, 0)          # O(nlogn)
    T[0][2] = 0
    for i in range(0, len(T)):              # O(n)
        if T[i - 1][0] == T[i][0]:
            T[i][2] = T[i - 1][2]
        else:
            T[i][2] = i

    quicksort(T, 0, len(T) - 1, 1)          # O(nlogn)
    T[len(T) - 1][3] = len(T) - 1
    for i in range(len(T) - 2, -1, -1):     # O(n)
        if T[i + 1][1] == T[i][1]:
            T[i][3] = T[i + 1][3]
        else:
            T[i][3] = i

    max_diff = -1
    for i in range(len(T)):                 # O(n)
        if T[i][3] - T[i][2] > max_diff:
            max_diff = T[i][3] - T[i][2]

    return max_diff


runtests(depth)

