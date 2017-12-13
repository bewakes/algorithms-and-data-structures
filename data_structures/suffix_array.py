from binary_tree import BinaryTree, Node

def suffix_array(string):
    # TODO:
    suffixes = [string[x:len(string)] for x in range(len(string))][::-1]
    return suffixes

def list_to_binary_tree(lst):
    bintree = BinaryTree()
    [bintree.insert(x) for x in list]
    return bintree

def suffix_tree(string):
    bintree = BinaryTree()
    for x in range(len(string)):
        bintree.insert(string[x:len(string)])
    return bintree

if __name__=="__main__":
    tree = suffix_tree("banana")
    print([x.value for x in tree.DF_traverse()])
    print(suffix_array("banana"))
