class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

def sum_check(root:TreeNode, t):
	if root == None:
		return 
	if root.left is None and root.right is None:
		return t == root.val
	return sum_check(root.left,t-root.val) or sum_check(root.right,t-root.val)
	

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

print(sum_check(root,23))
