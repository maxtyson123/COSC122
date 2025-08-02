from PythonTools.debug import capture_and_assert_file


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

def print_linked_list(start):

    node = start
    while node:
        print(node.data)
        node = node.next_node


# TESTING
def t1():
    head = Node(10)
    head.next_node = Node(20)
    head.next_node.next_node = Node(30)
    head.next_node.next_node.next_node = Node(40)
    print_linked_list(head)


def t2():
    start = Node('y')
    start.next_node = Node('a')
    start.next_node.next_node = Node('y')
    start.next_node.next_node.next_node = Node('a')
    start.next_node.next_node.next_node.next_node = Node('y')
    print_linked_list(start)

capture_and_assert_file(t1, "tests/t1.txt")
capture_and_assert_file(t2, "tests/t2.txt")
