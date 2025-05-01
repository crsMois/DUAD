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

        concatenated_string = ""
        current_node = self.head

        while current_node is not None:
            concatenated_string=  concatenated_string + f"{current_node.data} -> "
            current_node=current_node.next
        concatenated_string = concatenated_string+ f"None" 
        
        return concatenated_string


    def enqueue(self, new_node):
        current_node = self.head

        while current_node.next is not None:
            current_node=current_node.next
        
        current_node.next= new_node

    def dequeue(self):
        if self.head is not None:
            self.head = self.head.next
            if self.head is None:
                print("The Queue is empty now")
        else:
            print("The Queue is empty, there is nothing to remove")


def main():

    node1 = Node("Node1 ")
    node2 = Node("Node2 ")  
    node3 = Node("Node3 ")  

    queue1 = Queue(node1)
    queue1.enqueue(node2)
    queue1.enqueue(node3)

    print(queue1.print_Queue())

    queue1.dequeue()
    queue1.dequeue()
    queue1.dequeue()
    queue1.dequeue()

    print(queue1.print_Queue())



main()

