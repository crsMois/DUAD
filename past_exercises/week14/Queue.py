class Node:
    
    next : None
    data : str

    def __init__(self , data):
        self.data = data
        self.next = None
        


class Queue:

    head : Node
    def __init__(self, node):
        self.head = node

    def print_Queue(self):

        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next


    def enqueue(self, new_node):
        current_node = self.head

        while current_node.next is not None:
            current_node=current_node.next
        
        current_node.next= new_node

    def dequeue(self):
        if self.head is not None:
            self.head = self.head.next


def main():

    node1 = Node("Node1 data")
    node2 = Node("Node2 data")  
    node3 = Node("Node3 data")  


    queue1 = Queue(node1)
    queue1.enqueue(node2)
    queue1.enqueue(node3)
    queue1.print_Queue()

    queue1.dequeue()
    queue1.dequeue()
    queue1.dequeue()

    
    print("Dequeue")
    queue1.print_Queue()


main()

