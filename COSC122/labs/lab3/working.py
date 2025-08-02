class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

node1 = Node(10)
node2 = Node(20)

# your answer should be only one line
node1.next_node = node2

# Check that node2 is indeed now linked in after node1
# check_answer()