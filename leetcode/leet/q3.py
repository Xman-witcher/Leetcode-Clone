def getinorder(root,result=None):
    if result==None:
        result=[]
    if not root:
        return
    getinorder(root.left,result)
    result.append(root.val)
    getinorder(root.right,result)
    return result