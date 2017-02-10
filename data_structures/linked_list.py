class Node:
    """
    Node for linked list
    """
    def __init__(self, item):
        self.previous = None
        self.next = None
        self.value = item


class LinkedList:
    """
    Simple implementation of linked list
    """

    def __init__(self):
        self.head = [None]
        self.length = 0

    def append(self, node):
        if not type(node) == Node:
            node = Node(node)

        if self.length==0:
            self.head = [node]
        else:
            headelem = self.head[0]
            node.next = headelem
            self.head[0] = node
            headelem.previous = node
        self.length += 1

    def show(self):
        curr = self.head[0]
        while curr.next:
            print(curr.value,)
            curr = curr.next

if __name__=='__main__':
    ll = LinkedList()
    ll.append(3)
    ll.append(2)
    print(ll.length)
    ll.show()
