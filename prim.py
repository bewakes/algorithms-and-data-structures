INF = 99999999

def getminind(l, used):
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
    l = len(g)
    frm = [-1] * l 
    wts = [INF]*l
    wts[0] = 0 
    used = []
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
    graph = [[INF]*numnodes for x in range(numnodes)]
    for i, edge in enumerate(edges):
        graph[edge[0]-1][edge[1]-1] = weights[i]
        graph[edge[1]-1][edge[0]-1] = weights[i]
    return graph
    
def main():
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
        graph = get_graph(edges, weights, n)
        newwts, frm = prim(graph)
        print(sum(newwts))
main()
