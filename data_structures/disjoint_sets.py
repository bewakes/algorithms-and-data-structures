class DisjointSet:
    """
    Implementation of disjoint sets
    """

    def __init__(self, n):
        """
        n is the number of elements
        """
        # create different sets where each is a unique set
        self.parents_array = [x for x in range(n)]
        self.ranks_array = [0 for x in range(n)] # initial rank is zero for all


    def find(self, p):
        """
        find the parent of the element (0 indexed)
        """
        while self.parents_array[p] != p:
            p = self.parents_array[p]
        return p

    def make_set(self, i):
        """
        assign element i to its own set
        """
        self.parents_array[i] = i
        self.ranks_array[i] = 0

    def union(self, i, j):
        """
        i and j are 0 indexed elements which are to be unioned
        """
        i_root = self.find(i)
        j_root = self.find(j)

        if i_root == j_root:
            # nothing to be done already in same set
            return

        if self.ranks_array[i_root] < self.ranks_array[j_root]:
            self.parents_array[i_root] = j_root
        else:
            self.parents_array[j_root] = i_root
            if self.ranks_array[i_root] == self.ranks_array[j_root]:
                self.ranks_array[i_root]+=1

