from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if not isinstance(index, int) or index < 0:
        raise IndexError
    for i in range(index):
        if node is None:
            raise IndexError
        node = node.next
    if node is None:
        raise IndexError
    return node
    # Your code goes here.
