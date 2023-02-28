def get(root):
    if not root:
        return []
    result=[]
    while root:
        result.append(root.value)
        root=root.next
    return result