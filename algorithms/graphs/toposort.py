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


def toposort(adj):
    global post
    order = []
    visited = set()
    for i,v in enumerate(adj):
        if not i in visited:
            explore(adj,i,visited)

    #print(post)
    order = sorted(post, key=post.__getitem__, reverse=True)
    return order
    

'''
this program provides a topological sorting of a given directed graph (must be a DAG)
the input for the following graph should be in the following format
first line contains n (number of vertices) m (number of edges) followed by m lines 
each line containing a(starting node of the edge) b(ending node of the edge)
For ex:
4 3
1 2
4 1
3 1

4 nodes, 3 edges with edges described as in the last four lines

Output:
4 3 1 2

The output is list of nodes topologically sorted.
Ref: Please look at cormen's Introduction to Algorithm
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
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

