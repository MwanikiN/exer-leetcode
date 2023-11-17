class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, value):
        new_node = LinkedListNode(value)
        new_node.next_node = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node

    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" --> ")
            current_node = current_node.next_node
        print("None")

# Create a linked list and perform operations
head_node = LinkedListNode(5)  # Example head node
ll = LinkedList(head_node)
ll.insert_at_end(10)
ll.insert_at_end(15)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.print_linked_list()
