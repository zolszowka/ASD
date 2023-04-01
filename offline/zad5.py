"""
Zuzanna Olszówka
Algorytm zachłanny
Do kolejki priorytetowej wkładam ilość paliwa, gdy nie jest równa 0, ze znakiem ujemnym oraz indeks tej stacji.
Ujemny znak przy ilości paliwa powoduje, że na przodzie kolejki znajdzie się stacja z największą ilością paliwa.
Gdy paliwo w baku będzie <=0 to zdejmuję z kolejki pierwszy element, jest to stacja, na której musimy zatankować,
więc do tablicy ze stacjami wynikowymi wrzucamy indeks, a do naszego baku dodajemy całe paliwo, które mogliśmy zatankować na tej stacji.
Tablicę wynikową sortuję w kolejności postojów.

Dowód:
Algorytm wyznacza najmniejszą liczbę stacji na których musimy zatankować, ponieważ tankuje paliwo tylko na stacjach gdy wynosi <= 0
i tankuje na stacji z największą możliwą ilością paliwa.


Złożoność pamięciowa: O(nlogn)

"""

from zad5testy import runtests
from queue import PriorityQueue


def plan(T):
    n = len(T)
    result = []
    queue = PriorityQueue()
    petrol = 0
    for i in range(n - 1):
        if T[i] != 0:
            queue.put((-T[i], i))
        if petrol <= 0 and not queue.empty():
            f, indx = queue.get()
            result.append(indx)
            petrol -= f
        petrol -= 1

    result.sort()
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
