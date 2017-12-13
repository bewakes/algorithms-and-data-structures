import sys
sys.path.insert(0, '/home/bibek/projects/DSA')

from data_structures.disjoint_sets import DisjointSet

INF = 999999999


## first get graph here
with open('network.txt', 'r') as f:
    func = lambda x: int(x.strip()) if x.strip()!='-' else INF
    filterf = lambda x: x!=''
    lines = f.read().split('\n')[:-1] # last one is empty
    adjacency = [list(map(func, list(filter(filterf, x.split(','))))) for x in lines]


# adjacency = [[INF,7,2,5],
# [7,INF,4,1],
# [2,4,INF,4],
# [5,1,4,INF]]

# number of vertices
v = len(adjacency)

# now get the edges
# an edge is a tuple (vertex 1, vertex 2, weight)
edges = [(i, j, adjacency[i][j]) for i in range(v) for j in range(i, v) if adjacency[i][j]!=INF]

# total weight of the graph
totalwt = sum([x[2] for x in edges])

# sort edges
# because we need to take out smallest edges first.
edges.sort(key=lambda x: x[2])

# CREATE a disjoint set datastructure
disset = DisjointSet(v) # v is number of vertices

c = 0
wts = 0
final_edges = []
while c < len(edges):
    edge = edges[c]
    i,j, w = edge[0], edge[1], edge[2]
    #print(i, j)
    #print(disset.find(i), disset.find(j))
    if disset.find(i) != disset.find(j):
        wts+=w
        disset.union(i, j)
        final_edges.append(edge)
    #print(','.join(list(map(lambda x: str(x).zfill(2), disset.parents_array))))
    #print(','.join(list(map(lambda x: str(x).zfill(2), disset.ranks_array))))
    c+=1

print(final_edges)
print(totalwt-wts)
