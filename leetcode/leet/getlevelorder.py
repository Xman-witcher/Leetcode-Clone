def get(root):
    if not root:
        return []
    queue=[root]
    result=[]
    while queue!=[]:
        node=queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result