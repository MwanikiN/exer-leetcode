class Node:
    def __init__(self, node, next=None):
        self.node = node
        self.next = next

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def insert(self, node):
        if self.head is None:
            self.head = Node(node)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(node)

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.node, end=" --> ")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.insert(20)
ll.print_list()