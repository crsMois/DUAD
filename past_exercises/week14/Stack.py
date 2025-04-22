class Node:
    
    next : None
    data : str

    def __init__(self , data):
        self.data = data
        self.next = None
        

class Stack:

    head : Node
    def __init__(self, node):
        self.head = node

    def print_Queue(self):

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next


    def push(self, new_node):
        
        new_node.next = self.head
        self.head = new_node



    def pop(self):
        if self.head is not None:
            self.head = self.head.next


def main():

    node1 = Node("Node1 data")
    node2 = Node("Node2 data")  
    node3 = Node("Node3 data")  


    queue1 = Stack(node1)
    queue1.push(node2)
    queue1.push(node3)
    queue1.print_Queue()


    print("Pop Stack----")
    queue1.pop()
    queue1.print_Queue()


main()

