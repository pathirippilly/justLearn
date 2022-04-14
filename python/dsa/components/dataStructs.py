class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __add__(self, other):
        if isinstance(other, node):
            return self.data + other.data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        if isinstance(other, node):
            if other.data == self.data:
                return True
        return False


class LinkedList:
    def __init__(self, *args):
        self.head = None
        self.length = 0
        if len(args) > 0:
            for item in args:
                self.append(item)

    def __str__(self):
        nextNode = self.head
        out = nextNode
        while isinstance(nextNode, node):
            nextNode = nextNode.next
            out = (str(out) + "," + str(nextNode)) if nextNode else out
        return f"LinkedList({out})" if out else f"LinkedList()"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            out = self.current
            self.current = self.current.next
            return out
        else:
            raise StopIteration

    def __reversed__(self):
        PrevNode = None
        currNode = self.head
        while currNode:
            currNextNode = currNode.next
            currNode.next = PrevNode
            PrevNode = currNode
            currNode = currNextNode
            if not currNode:
                self.head = PrevNode
        return self

    def insertAtBeginning(self, data):
        temp = self.head
        self.head = node(data)
        self.head.next = temp
        self.length += 1

    def append(self, data):
        nextNode = self.head
        currNode = self.head
        while nextNode:
            currNode = nextNode
            nextNode = nextNode.next
        if currNode:
            currNode.next = node(data)
        else:
            self.head = node(data)
        self.length += 1

    def insert(self, data, index):
        if index <= self.length:
            currIndex = 0
            nextNode = self.head
            currNode = self.head
            while currIndex < index:
                currNode = nextNode
                nextNode = nextNode.next
                currIndex += 1
            temp = currNode.next
            currNode.next = node(data)
            currNode.next.next = temp
            self.length += 1
        else:
            raise IndexError(f"index to be inserted can not be greater than length of linkedList!   ")

    def clear(self):
        self.head = None
        self.length = 0

    def pop(self, index=None):
        index = index if index else self.length - 1
        if not self.length:
            raise Exception(f"pop operation is not permitted on an Empty LinkedList")
        elif self.length > index >= 0:
            currIndex = 0
            nextNode = self.head
            currNode = self.head
            while currIndex < index:
                currNode = nextNode
                nextNode = nextNode.next
                currIndex += 1
            if nextNode == self.head:
                self.head = currNode.next
                self.length -= 1
                return currNode.data
            elif nextNode == self.head.next:
                self.head.next = nextNode.next
                self.length -= 1
                return nextNode.data
            else:
                currNode.next = nextNode.next
                self.length -= 1
                return nextNode.data
        else:
            raise IndexError(f"index to be deleted should be less than the length of linkedList!")

    def popItem(self, data):
        currentNode = self.head
        prevNode = None
        found = False
        while currentNode:
            if data == currentNode.data:
                found = True
                if prevNode:
                    prevNode.next = currentNode.next
                else:
                    self.head = currentNode.next
                break
            prevNode = currentNode
            currentNode = currentNode.next
        self.length -= 1
        if not found:
            raise ValueError("Provided Value not found!")
