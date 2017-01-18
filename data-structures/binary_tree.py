class Node(object):
    """
        Represents node for binary tree
    """
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def is_leaf(self):
        return not self.left_child and not self.right_child

    def __lt__(self, node):
        return self.value<node.value

    def __gt__(self, node):
        return self.value>node.value

    def __eq__(self, node):
        return self.value==node.value

    def __le__(self, node):
        return self.value<=node.value

    def __ge__(self, node):
        return self.value>=node.value


class BinaryTree(object):
    """
        Represents the binary tree datastructure
    """

    def __init__(self, root=None):
        if root != None and not type(root)==Node:
            root = Node(root)
        self.root = root

    def insert(self, node):
        """
        Insert a node to the binary tree
        """
        if not type(node)==Node:
            node = Node(node)

        if not self.root:
            self.root = node

        else:
            self._insert_recursive(self.root, node)

    def _insert_recursive(self, ref_node, insertnode):
        """
        Inserts node recursively
        Parameters:
            insert node: node to be inserted
            ref_node: node which is the root of the current subtree
        """
        if not type(insertnode) == Node:
            insertnode = Node(insertnode)

        if insertnode<=ref_node:
            if not ref_node.left_child:
                ref_node.left_child = insertnode
            else:
                self._insert_recursive(ref_node.left_child, insertnode)
        else:
            if not ref_node.right_child:
                ref_node.right_child = insertnode
            else:
                self._insert_recursive(ref_node.right_child, insertnode)

    def DF_traverse(self):
        return self._DF_traverse(self.root)

    def _DF_traverse(self, root):
        """
        Recursive Depth first traversal of the root
        Returns the traversed list
        """
        lst = []

        if not root:
            return []
        elif root.is_leaf():
            return [root]
        else:
            lst.extend(self._DF_traverse(root.left_child))
            lst.append(root)
            lst.extend(self._DF_traverse(root.right_child))
            return lst

if __name__=="__main__":
    import random
    lst = [random.randrange(12, 100) for x in range(6)]
    print(lst)

    bintree = BinaryTree()

    [bintree.insert(x) for x in lst]

    print([x.value for x in bintree.DF_traverse()])
