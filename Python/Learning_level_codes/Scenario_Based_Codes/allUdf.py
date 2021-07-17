#Return list of all possible sublist from a list as input
from multipledispatch import dispatch
@dispatch(list)
def getAllSublist(inpL):
    outL=[]
    for i in range(len(inpL)):
        for j in range(len(inpL)+1):
            outSubL=inpL[i:j]
            if outSubL:
                outL.append(outSubL)
    return outL

@dispatch(list,int)
def getAllSublist(inpL,k):
    outL=[]
    for i in range(len(inpL)):
        oddNumCounter=0
        for j in range(len(inpL)+1):
            outSubL=inpL[i:j]
            if outSubL:
                if outSubL[-1]%2!=0:
                    oddNumCounter+=1
                if oddNumCounter<=k:
                    outL.append(outSubL)
                else:
                    break
    return outL


class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class linkedList:
    def __init__(self, data=None):
        if data:
            self.head = node(data)
        else:
            self.head = None

    def append(self, data):
        newNode = node(data)
        if self.head:
            currentNode = self.head
            while (currentNode.next):
                currentNode = currentNode.next
            currentNode.next = newNode
        else:
            self.head = newNode

    def __repr__(self):
        currentNode = self.head
        out = ''
        while (currentNode):
            out = out + str(currentNode)
            currentNode = currentNode.next
            if currentNode:
                out = out + ","
        return f"{self.__class__.__name__}({out})"
