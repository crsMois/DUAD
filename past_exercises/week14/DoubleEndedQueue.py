class Node:
    def __init__(self, data:None):
        self.next = None
        self.prev = None
        self.data = data


class DoubleEndedQueue:
    def __init__(self):
        self.head = None
        self.tail = None


### INSERT AT HEAD == push_left

    def push_left(self , node):        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node


### INSERT AT TAIL == push_right
        
    def push_right(self, node):
        if self.head is None:
            self.head = node
            self.tail = node 
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node


### REMOVE AT HEAD == pop_left

    def pop_left(self):
        if self.head is None:
            print("There is not more nodes to remove, the Queue is empty")
            return
        elif self.head == self.tail:
            self.head= None
            self.tail= None
        else:
            self.head = self.head.next
            self.head.prev = None


### REMOVE AT TAIL == pop_right

    def pop_right(self):       
        if self.tail is None:
            print("There is not more nodes to remove, the Queue is empty")
            return
        elif self.tail == self.head:
            self.tail = None
            self.head =None
        else:    
            self.tail = self.tail.prev
            self.tail.next = None


#PRINT DOUBLE ENDED QUEUE

    def print_Double_Ended_Queue (self):
        current_node = self.head
        concatenated_ouput_string = ""

        while current_node is not None:
            concatenated_ouput_string= concatenated_ouput_string + f"{current_node.data} <-> "
            current_node = current_node.next

        concatenated_ouput_string= concatenated_ouput_string + " None "
        print(concatenated_ouput_string)

def main():
    node1 = Node("Node1")
    node2 = Node("Node2")
    node3 = Node("Node3")
    node4 = Node("Node4")
    node5 = Node("Node5")
    node6 = Node("Node6")
    node7 = Node("Node7")                

    doubleEnded1 = DoubleEndedQueue()
    doubleEnded1.push_left(node1)
    doubleEnded1.push_left(node2)
    doubleEnded1.push_left(node3)
    doubleEnded1.push_left(node4)

    doubleEnded1.push_right(node5)
    doubleEnded1.push_right(node6)
    doubleEnded1.push_right(node7)        
    doubleEnded1.print_Double_Ended_Queue()


    print("\nREMOVING NODES\n")

    doubleEnded1.pop_left()
    doubleEnded1.pop_right()
    doubleEnded1.print_Double_Ended_Queue()

main()