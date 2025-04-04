class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    head_1 = None
    while head is not None:
        node = head
        head = node.next
        node.next = head_1
        head_1 = node
    return head_1
