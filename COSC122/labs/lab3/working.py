class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class UnsortedLinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        """ Makes a new node containing item as the data and
            adds it to the start of the list, ie, before the
            current head
        """
        # your answer should be three lines
        node = Node(item)
        node.next_node = self.head
        self.head = node


my_list = UnsortedLinkedList()
my_list.add(10)
print(my_list.head.data)
print(my_list.head.next_node)
