#Uses python3

import sys
import queue


dist = {}
def bipartite(adj):
    global dist
    q = queue.Queue()
    visited = set()
    for i,v in enumerate(adj):
        if not i in visited:
            #print("visiting vertex:",i+1)
            q.put(i)
            visited.add(i)
            dist[i] = 0
            while not q.empty():
                ver = q.get()
                for n in adj[ver]:
                    #print("neigbhour of:",ver+1,"->",n+1)
                    if n in dist.keys() and dist[n] == dist[ver]:
                        return 0
                    if not n in visited:
                        q.put(n)
                        visited.add(n)
                        dist[n] = dist[ver] + 1

    return 1

'''
this program checks if the given graph is a bipartite or not

the input for the following graph should be in the following format
first line contains n (number of vertices) m (number of edges) followed by m lines 
each line containing a(starting node of the edge) b(ending node of the edge)
For ex:
4 4
1 2
4 1
2 3
3 1

Output:
0

outputs 0 or 1 based on the bipartiteness of the graph

Logic of this program:
The main intuition behind this solution is that while constructing the tree for the path of every vertex from some single vertex the
the edge should not occur between the vertex at same height. This can be confirmed by comparing the distance metrics while iterating 
through the neighbour of any vertex.

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
    print(bipartite(adj))
