"""
Zuzanna Olszówka
Podaną listę sortuję za pomocą kolejki priorytetowej opartej na kopcu binarnym typu min o wielkości k+1 (zakładam, że k<n, n-długość listy).
Wkładając elementy do kopca, naprawiam go od dołu do góry za pomocą funkcji parent.
Najmniejszy element, który znajduje się w korzeniu zamieniam z elementem na pozycji k-tej i przenoszę go do posortowanej listy.
Następnie do kopca wkładam kolejny element z podanej na wejściu listy.
Używam funkcji heapify, żeby najmniejszy element z kopca zawsze był w korzeniu.
Złożoność czasowa algorytmu: O(nlogk)
Zlożoność pamięciowa algorytmu: O(k)
Złożoność czasowa dla:
k = O(1) - O(n)
k = O(logn) - O(nlog(logn))
k = O(n) - O(nlogn)
"""

from zad1testy import Node, runtests


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def insert_1(A, x):  # insert z appendem
    A.append(x)
    i = len(A) - 1
    while i > 0 and x.val < A[parent(i)].val:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def insert_2(A, x):  # insert bez appenda
    A[len(A) - 1] = x
    i = len(A) - 1
    while i > 0 and x.val < A[parent(i)].val:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    min_ind = i
    if l < n and A[l].val < A[min_ind].val:
        min_ind = l
    if r < n and A[r].val < A[min_ind].val:
        min_ind = r
    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]
        heapify(A, n, min_ind)


def SortH(p, k):
    n=0
    q=p
    while q is not None:
        n+=1
        q=q.next
    if k>=n:
        k=n-1

    H = []
    for i in range(k + 1):
        curr = p
        p = p.next
        curr.next = None
        insert_1(H, curr)

    sorted_list = Node()
    l = sorted_list
    while p is not None:
        H[0], H[k] = H[k], H[0]
        l.next = H[k]
        l = l.next
        heapify(H, len(H) - 1, 0)
        curr = p
        p = p.next
        curr.next = None
        insert_2(H, curr)
        heapify(H, len(H), 0)

    for i in range(k, -1, -1):
        H[0], H[i] = H[i], H[0]
        heapify(H, i, 0)
        l.next = H[i]
        l = l.next

    return sorted_list.next


runtests(SortH)
