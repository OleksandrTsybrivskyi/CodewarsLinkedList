def linked_list_from_string(s):
    if s == 'None':
        return None
    mas = s.split(' -> ')
    head = None
    for i in range(len(mas) - 2, -1, -1):
        node = Node(int(mas[i]), head)
        head = node
    return head
