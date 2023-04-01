from zad6testy import runtests
from collections import deque

def bfs(G, s, t):
    queue=deque()
    visited=[False]*len(G)
    d=[-1]*len(G)

    queue.append(s)
    visited[s]=True
    d[s]=0

    while queue:
        u=queue.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                d[v]=d[u]+1
                queue.append(v)
    return d[t]


def longer( G, s, t ):
    smallest_path=bfs(G,s,t)
    print(smallest_path)
    
    # tu prosze wpisac wlasna implementacje
    return (0,0)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = False )