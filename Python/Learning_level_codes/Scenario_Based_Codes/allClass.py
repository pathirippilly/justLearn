class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __eq__(self, other):
        return (self.data == other.data)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class linkedList:
    def __init__(self, data=None):
        if data:
            self.length = 1
            self.head = node(data)
            self.tail = self.head
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def traverse(self, index):
        if index < self.length:
            currentNode = self.head
            runIndx = 0
            while runIndx < index:
                currentNode = currentNode.next
                runIndx += 1
            return currentNode
        else:
            raise IndexError(f"index out of range for {self.__class__.__name__}")

    def insert(self, data, index):
        if self.head:
            newNode = node(data)
            if index == 0:
                print("at head")
                swapNode = self.head
                newNode.next = swapNode
                self.head = newNode
            elif index == self.length:
                swapNode = self.tail
                if self.tail is self.head:
                    self.head = node(swapNode.data, next=newNode)
                swapNode.next = newNode
                self.tail = newNode

            else:
                print("middle insert")
                prevNode = self.traverse(index - 1)
                #                 print(prevNode)
                swapNode = prevNode.next
                #                 print(prevNode)
                prevNode.next = newNode
                newNode.next = swapNode
            self.length += 1
        elif index == 0:
            self.__init__(data)
        else:
            raise IndexError(f"index out of range for {self.__class__.__name__}")

    def remove(self, index):
        if index == 0:
            delNode = self.head
            swapNode = delNode.next
            delNode.next = None
            self.head = swapNode
            self.length -= 1
            return delNode
        elif index < self.length:
            prevNode = self.traverse(index - 1)
            delNode = prevNode.next
            prevNode.next = delNode.next
            if self.tail == delNode:
                self.tail = prevNode
            delNode.next = None
            self.length -= 1
            return delNode
        else:
            raise IndexError(f"index out of range for {self.__class__.__name__}")

    def append(self, data):
        self.insert(data, self.length)

    def popItem(self):
        return self.remove(self.length - 1)

    def __iter__(self):
        self._iterPointer = self.head
        return self

    def __next__(self):
        if self._iterPointer:
            currentNode = self._iterPointer
            self._iterPointer = self._iterPointer.next
            return currentNode.data
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.traverse(index)

    def __repr__(self):
        currentNode = self.head
        out = ''
        while (currentNode):
            if isinstance(currentNode.data, str):
                out = f"{out}'{currentNode}'"
            else:
                out = f"{out}{currentNode}"
            currentNode = currentNode.next

            if currentNode:
                out = out + ","
        return f"{self.__class__.__name__}({out})"

    def __len__(self):
        return self.length