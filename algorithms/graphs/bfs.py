#Uses python3
#Author chitraketu

import sys
import queue

dist = {}
def distance(adj, s, t):
    global dist
    q = queue.Queue()
    q.put(s)
    dist[s] = 0
    
    visited = set()
    visited.add(s)
    while not q.empty():
        v = q.get()
        for n in adj[v]:
            if n in visited:
                continue
            q.put(n)
            dist[n] = dist[v] + 1
            visited.add(n)
            if(n == t):
                return dist[n]

    return -1

'''
this program calculates a shortest path of a given undireced not weighted graph using BFS algorithm

the input for the following graph should be in the following format
first line contains n (number of vertices) m (number of edges) followed by m lines 
each line containing a(starting node of the edge) b(ending node of the edge)
For ex:
4 4
1 2
4 1
2 3
3 1
2 4

Output:
2
'''

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
