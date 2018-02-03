INF = 99999999

def getminind(l, used):
    '''
    inputs:
        l       => list of the costs of reaching the nodes: 
                    l[i] has the cost of reaching node i
        used    => list containing information about used nodes in 
                   prim's algorigthm. used[i]==1 means node i is used
    output:
        returns the index of the unused node whose cost is the minimum
    '''
    for i, x in enumerate(l):
        if i not in used:
            mini = i
            minv = x
    for i, x in enumerate(l):
        if x<minv and i not in used:
            minv = x
            mini = i
    return mini

def prim(g):
    '''
    inputs:
        g       => graph represented as adjacency matrix
    output:
        weights => a list: weights[i] is the weight of connection to node i from parent
        frm     => a list: frm[i]= j means, node i is reached from node j, -1 represents its starting
    '''
    l = len(g)
    frm = [-1] * l # frm[i]=j means, in the spanning tree, node i is reached from node j
    wts = [INF]*l # wts[i] is the weight of reaching node i from its parent/adjacent node
    wts[0] = 0 
    used = [] # nodes used from the initial graph
    weights = []
    while len(used)!=l:
        curr = getminind(wts,used)
        used.append(curr)
        weights.append(wts[curr])

        for i, x in enumerate(g[curr]):
            if i!=curr and x< wts[i]:
                wts[i] =x
                frm[i] = curr   
    return (weights, frm)   

def get_graph(edges, weights, numnodes):
    '''
    -the inputs are the lists of edges and weghts: len(edges)==len(weights)
    -and numnodes: total number of nodes
    -outputs the graph in matrix form with unconnected vertices having weights
     INF(=99999999)
    NOTE: edges numbering start from 1(actually this code I used for solving hacker rank)
    '''
    graph = [[INF]*numnodes for x in range(numnodes)]
    for i, edge in enumerate(edges):
        graph[edge[0]-1][edge[1]-1] = weights[i]
        graph[edge[1]-1][edge[0]-1] = weights[i]
    return graph
    
def main():
        # preprocessing starts
        n,m = [int(x) for x in input().strip().split(' ')]
        edges = []
        weights = []
        start = 0
        while m>0:
            a,b,w = [int(x) for x in input().strip().split(' ')]
            edges.append((a,b))
            weights.append(w)
            m-=1
        input()
        # preprocessing ends
        # now we have total num of nodes and edges and weights
        graph = get_graph(edges, weights, n)
        # now graph is in adjacency matrix form
        newwts, frm = prim(graph)
        print(sum(newwts))

if __name__=='__main__':
    main()
