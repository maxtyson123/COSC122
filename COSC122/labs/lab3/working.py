class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# your answer should be two lines
node1.next_node = node2
node2.next_node = node3

# Check
print('node1 ->', node1.data)
print('node2 ->', node2.data)
print('node3 ->', node3.data)
print()
print('Running through list:')
print('node1 ->', node1.data, '->', end=' ')
print(node1.next_node.data, '->', end=' ')
print(node1.next_node.next_node.data, '->', end=' ')
print(node1.next_node.next_node.next_node)