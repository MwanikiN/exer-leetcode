class Node:
    def __init__(self, node, next_node=None) -> None:
        self.node = node
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def insert(self, node):
        if self.head is None:
            self.head = Node(node)
            return
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = Node(node)
            return
        
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.node, end=" --> ")
            current = current.next_node
        print("None")

ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.insert(20)
ll.print_list()