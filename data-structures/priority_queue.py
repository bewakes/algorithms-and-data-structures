class NaivePriorityQueue:
    """
    Implements the priority queue naively using unsorted array: dequeue has O(n)
    enqueue has O(1)
    Dynamic array is not implemented though(List is dynamic array)
    NOTE: using sorted array has O(n) for insertion and O(1) for dequeue
    """
    elements = []

    def __init__(self):
        pass

    def insert(self, element):
        """
        Insert an element to the queue
        """
        self.elements.append(element)
        #print(self.elements)

    def dequeue(self):
        """
        Pop the element with highest priority
        """
        print(self.elements)
        if not self.elements:
            print("Empty Queue!!")
            return None

        mx = self.elements[0]
        for i in range(1, len(self.elements)):
            if self.elements[i] > mx:
                self.elements[i], mx = mx, self.elements[i]
            self.elements[i-1] = self.elements[i]
            print('..', self.elements)
        # now pop, as all elements are shifted towards beginning
        self.elements.pop()
        print(self.elements)
        return mx

    def getMax(self):
        """
        Returns element of highest priority
        """
        return max(self.elements)


if __name__=="__main__":
    import random
    pq = NaivePriorityQueue()
    [pq.insert(random.randrange(0,100)) for _ in range(10)]
    print('now dequeuing')
    print(pq.dequeue())
    print(pq.dequeue())
