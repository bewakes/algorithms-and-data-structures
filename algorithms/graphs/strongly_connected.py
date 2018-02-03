#Uses python3
#Author chitraketu pandey

import sys

sys.setrecursionlimit(200000)

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

def number_of_strongly_connected_components(adj, revAdj):
    result = 0
    visited = set()
    for i,v in enumerate(revAdj):
        if not i in visited:
            explore(revAdj,i,visited)

    #print(post)
    order = sorted(post, key=post.__getitem__, reverse=True)
    #print(order)
    visited.clear()
    for i in order:
        if not i in visited:
            result = result + 1
            explore(adj,i,visited)
            
    return result


'''
this program calculates a number of connected components of a given directed graph 

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
2
'''

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    revAdj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        revAdj[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj,revAdj))
