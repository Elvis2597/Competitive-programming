class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def PathSum(root,s):
    if root==None:
        return False
    else:
        ans=False
        sub=s-root.data
        print(sub)
        if sub==0 and root.left==None and root.right==None:
            return True
        if root.left:
            ans=ans or PathSum(root.left,sub)
        if root.right:
            ans=ans or PathSum(root.right,sub)
        return ans
s = 14
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)
ans=PathSum(root, s)
print(ans)
