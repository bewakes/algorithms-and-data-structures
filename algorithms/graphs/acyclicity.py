#Uses python3
#Author chitraketu pandey

import sys

clock = 1
post = {}
def explore(adj,x,visited):
    global clock
    global post
    visited.add(x)
    clock = clock + 1
    for v in adj[x]:
        if not v in visited:
            visited.add(v)
            explore(adj,v,visited)
    clock =  clock + 1
    post[x] = clock

def acyclic(adj):
    global post
    visited = set()
    for i,v in enumerate(adj):
        if not i in visited:
            explore(adj,i,visited)
    
    for i,v in enumerate(adj):
        for n in adj[i]:
            if(post[i] < post[n]):
                return 1 # cycle exists
    return 0 # cycle doesn't exist

'''
this program checks if a given directed graph is acyclic or not
the input for the following graph should be in the following format
first line contains n (number of vertices) m (number of edges) followed by m lines 
each line containing a(starting node of the edge) b(ending node of the edge)
For ex:
4 4
1 2
4 1
2 3
3 1

4 nodes, 4 edges with edges described as in the last four lines

The output is 1 if a graph contains cycle 0 if a graph is a DAG.
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
    print(acyclic(adj))
