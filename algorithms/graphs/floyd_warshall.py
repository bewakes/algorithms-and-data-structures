#uses python2
#authon: chitraketu

'''
this is the implementation of floyd warshall's algorithm to calculate the all pair shortest path 
and construct the path based on it.
'''

'''
this method takes an adjacency matrix as an input and
returns D showing the shortest path if exists and construction path matrix P
'''
def fw(matrix):
    #first define D(0)
    D = []
    #number of vertices
    n = len(matrix)
    #initializing the base matrix
    for i in range(n+1):
        D.append([])

    print len(D)
    D[0] = matrix
    for k in range(1,n+1):
        #initializing an nxn array here
        D[k] = [[0 for x in range(n)] for y in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                print k,i,j
                D[k][i][j] = min( D[k-1][i][j],D[k-1][i][k-1] + D[k-1][k-1][j] )
    Pi = []
    Pi = constructPath(D)
    return D[n],Pi


def constructPath(D):
    #definition of Parents
    Pi = []

    #number of vertices
    n = len(D) - 1

    #initializing the base matrix
    for i in range(n+1):
        Pi.append([])

    print len(Pi)

    #initializing the first element of Pi
    Pi[0] = [[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                Pi[0][i][j] = None
            else:
                Pi[0][i][j] = i

    #building the other matrices
    for k in range(1,n+1):
        #initialzing an nxn array here
        Pi[k] = [[0 for x in range(n)] for y in range(n)]
        for i in range(0,n):
            for j in range(0,n):
                if D[k-1][i][j] <= D[k-1][i][k-1] + D[k-1][k-1][j]:
                    Pi[k][i][j] = Pi[k-1][i][j]
                else:
                    Pi[k][i][j] = Pi[k-1][k-1][j]
    return Pi[n]


def add_path(i, j, Pi):
    path = []
    while(j != i):
        print i,j
        path.append(j)
        j = Pi[i][j]
    path.append(i)
    path.reverse()
    return path

def prettyPrinting(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

