def stringify(node):
    head = node
    ans = ''
    while head != None:
        ans += f'{head.data} -> '
        head = head.next
    ans += 'None'
    return ans
