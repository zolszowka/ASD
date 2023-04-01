"""
Zuzanna Olszówka
Do posortowania tablicy używam bucket sorta, w którym tworzę jednostkowe kubełki w zakresie od 0 do n
(gdzie n jest największym końcem w tablicy P - wyznacza nam największy element, który może się pojawić w tablicy T).
Przy sortowaniu pomijam przedziały z tablicy P, ponieważ liczby są losowane zgodnie z rozkładem jednostajnym.
Kubełki sortuję za pomocą quick sorta O((buckets[i])log(buckets[i]))
Złożoność czasowa: O(n)
Złożoność pamięciowa: O(n+len(T))

"""
from zad3testy import runtests


def partition(T, p, k):
    l = p - 1
    for i in range(p, k):
        if T[i] < T[k]:
            l += 1
            T[i], T[l] = T[l], T[i]
    T[l + 1], T[k] = T[k], T[l + 1]
    return l + 1


def quicksort(T, p, k):
    while p < k:
        q = partition(T, p, k)
        if (q - p) > (k - q):
            quicksort(T, q + 1, k)
            k = q - 1
        else:
            quicksort(T, p, q - 1)
            p = q + 1
    return T


def bucket_sort(T, n):
    norm = n
    buckets = [[] for _ in range(n)]
    for num in T:
        norm_num = num / norm
        bucket_indx = int(n * norm_num)
        buckets[bucket_indx].append(num)
    k = 0
    for i in range(n):
        if buckets[i]:
            buckets[i] = quicksort(buckets[i], 0, len(buckets[i]) - 1)
            for j in range(len(buckets[i])):
                T[k] = buckets[i][j]
                k += 1
    return T


def SortTab(T, P):
    n = -1
    for i in range(len(P)):  # O(k) k=len(P)
        if P[i][1] > n:
            n = P[i][1]

    T = bucket_sort(T, n)

    return T


runtests(SortTab)
