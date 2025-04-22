class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def pre_order_print(node):
        if node is not None:
            print(node.value)
            pre_order_print(node.left)
            pre_order_print(node.right)


def main ():
    root = Node("I am the root")
    root.left = Node("Root Left")
    root.right = Node("Root Right")
    root.left.left = Node("Left Left")
    root.left.right = Node("Left Right")
    root.right.left = Node("Right Left")    
    root.right.right = Node("Right Right")


    pre_order_print(root)

main()