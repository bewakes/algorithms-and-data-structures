#Uses python3
#Author: chitraketu


import sys
import queue

def relax(adj, i, j, dist, cost, prev):
    if dist[i] == float('inf'):
        return False
    if dist[j] > dist[i] + cost:
        dist[j] = dist[i] + cost
        prev[j] = i
        return True
    else:
        return False


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance[s] = 0
    reachable[s] = 1
    prev = {}
    for (i, v) in enumerate(adj):
        prev[i] = -1
    for i in range(len(adj)-1):
        for i,v in enumerate(adj):
            for ind,j in enumerate(v):
                if relax(adj,i,j,distance,cost[i][ind],prev):
                    #print("relaxing ",i,"distance",distance[i],j,"distance",distance[j])
                    reachable[j] = 1
    for x in range(2):
        for i,v in enumerate(adj):
            for ind,j in enumerate(v):
                #print("trying to relax:",i,j)
                if relax(adj,i,j,distance,cost[i][ind],prev):
                    distance[j] = -float('inf')
                    #print("relaxing at vth iteration",i,"distance",distance[i],j,"distance",distance[j])
                    shortest[j] = 0


    for i,v in enumerate(distance):
        if v == float('inf'):
            reachable[i] = 0

    pass


'''
this program calculates the shortest path with or without negative weight cycle exists in a given directed graph.
this algorithm works on any case has bad time complexity as compared to Dijkstras algorithm but can calculate the shortest
path if exists even in a graph with negative cycle

the input for the following graph should be in the following format
first line contains n (number of vertices) m (number of edges) followed by m lines 
each line containing a(starting node of the edge), b(ending node of the edge) and w(weight of the edge)
For ex:
6 7
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1
1

Output:
0
10
-
- 
-
*

This program calculates shortest path for every vertex from the vertex '1' (note the vertex name always start from 1) and 
for each vertex from 1 to n provides prints:
   a.) the cost of the shortest path if exist, 
   b.) '-' if it consists of a negative weight cycle,
   c.) '*' if there is no path to that vertex

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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

