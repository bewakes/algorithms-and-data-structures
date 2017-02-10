class MaxHeap:
    """
    Implementation of Max Heap where root element is the largest.
    Each node has children no greater than itself
    NOTE: complete binary tree is used
    """
    # elements is the array containing the heap, size will increase as required
    elements = [None]

    def __init__(self):
        pass

    def insert(self, elem):
        if not self.elements[0]:
            self.elements[0] = elem
        else:
            # get a leaf
            leaf = self._get_leaf_index()
            leaf_child = leaf * 2 + 1

            if len(self.elements) <= leaf_child:
                print('adding layer')
                # expand the array
                self.elements.extend([None] * (len(self.elements)*2 + 1))

            self.elements[leaf_child] = elem
        print(self.elements)

    def _get_leaf_index(self):
        """
        Get leaf element from last level so that new element may be added as its child
        """
        size = len(self.elements)
        for i in range(size/2, size):
            if self.elements[i] is not None:
                return i
        print('Last level is empty')

if __name__=="__main__":
    hp = MaxHeap()
    hp.insert(1)
    hp.insert(4)
