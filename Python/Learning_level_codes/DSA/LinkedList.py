class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
NodeA = Node(5)
NodeB = Node(6)
NodeC = Node(7)
NodeD = Node(8)

NodeA.next=NodeB
NodeB.next=NodeC

def count_all_nodes(node):
    current_node=node
    count=1
    while(current_node.next != None):
        current_node=current_node.next
        count=count+1
    return count
n=count_all_nodes(NodeA)
print(n)
