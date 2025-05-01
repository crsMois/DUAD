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

    def print_Stack(self):

        current_node = self.head

        if current_node is None:
            print("You can not print any element of the Stack , The Stack is empty")


        while current_node is not None:
            print(current_node.data)
            current_node=current_node.next


    def push(self, new_node):
        
        new_node.next = self.head
        self.head = new_node



    def pop(self):

        if self.head is not None:
            self.head = self.head.next
        else:
            print("You can not pop the Stack, The Stack is empty")


def main():

    node1 = Node("Node1 data")
    node2 = Node("Node2 data")  
    node3 = Node("Node3 data")  


    stack1 = Stack(node1)
    stack1.push(node2)
    stack1.push(node3)
    stack1.print_Stack()


    print("Pop Stack----")
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.print_Stack()
    stack1.pop()
    


main()

