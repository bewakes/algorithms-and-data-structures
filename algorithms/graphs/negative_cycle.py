#Uses python3

import sys
inf = 2 ** 128 - 1

def relax(adj, i, j, dist, cost, prev):
    if dist[j] > dist[i] + cost:
        dist[j] = dist[i] + cost
        prev[j] = i
        return True
    else:
        return False

def negative_cycle(adj, cost):
    #write your code here
    dist = {}
    prev = {}
    for (i, v) in enumerate(adj):
        dist[i] = inf
        prev[i] = -1
    dist[0] = 0
    for i in range(len(adj)-1):
        for i,v in enumerate(adj):
            for ind,j in enumerate(v):
                relax(adj,i,j,dist,cost[i][ind],prev)

    for i,v in enumerate(adj):
        for ind,j in enumerate(v):
            if(relax(adj,i,j,dist,cost[i][ind],prev)):
                return 1
    return 0


'''
this program calculates if a path with negative weight cycle exists in a given directed graph.
To check negative weight cycle in graph is important because if such path exists then Dijkstra's algorithm fails
to calculate the shortest path

the input for the following graph should be in the following format
first line contains n (number of vertices) m (number of edges) followed by m lines 
each line containing a(starting node of the edge), b(ending node of the edge) and w(weight of the edge)
For ex:
4 4
1 2 -5
4 1 2
2 3 2
3 1 1

Output:
1

This program outputs 1 if such negative weight cycle exists in a graph 0 otherwise
'''


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
