def sorted_insert(head, data):
    node = Node(data)
    if head is None:
        node.next = head
        head = node
        return head
    if head.next is None:
        if data > head.data:
            node.next = head.next
            head.next = node
        else:
            node.next = head
            head.next = node
        return head
    if head.data > data:
        node.next = head
        head = node
        return head
    pivot = head
    while True:
        if head.next is None:
            node.next = head.next
            head.next = node
            return pivot
        elif head.next.data > data:
            node.next = head.next
            head.next = node
            return pivot
        else:
            head = head.next
