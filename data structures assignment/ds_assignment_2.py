#PROBLEM 2
print("\n solution of problem 2")
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 
def printInorder(root): 
	if root: 
		printInorder(root.left) 
		print(root.val), 
		printInorder(root.right) 
def printPostorder(root): 
	if root: 
		printPostorder(root.left) 
		printPostorder(root.right) 
		print(root.val), 
def printPreorder(root): 

	if root: 
		print(root.val), 
		printPreorder(root.left) 
		printPreorder(root.right) 
root = Node('A') 
root.left	 = Node('B') 
root.right	 = Node('C') 
root.left.left = Node('D') 
root.right.right = Node('G')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.left.left = Node('N')
root.left.right.left = Node('M')
print ("Preorder traversal of binary tree is")
printPreorder(root) 
print ("\nInorder traversal of binary tree is")
printInorder(root) 
print ("\nPostorder traversal of binary tree is")
printPostorder(root) 



#PROBLEM 3
print("\n solution of problem 3")
def maxDepth(node): 
	if node is None: 
		return 0 ; 
	else : 
		lDepth = maxDepth(node.left) 
		rDepth = maxDepth(node.right) 
		if (lDepth > rDepth): 
			return lDepth+1
		else: 
			return rDepth+1

root = Node('A') 
root.left	 = Node('B') 
root.right	 = Node('U') 
root.left.left = Node('S') 
root.right.right = Node('P')
root.left.right = Node('R')
root.right.left = Node('E')
root.left.left.left = Node('W')
root.left.right.left = Node('Y')
root.left.right.right = Node('A')
root.right.right.left = Node('G')
root.right.right.right = Node('J')
root.left.left.left.left = Node('Z')
print ("\nPostorder traversal of binary tree is")
printPostorder(root) 
print ("Height of tree is %d" %(maxDepth(root))) 



#PROBLEM 1
print("\nn the solution of problem 1")
root = Node('A') 
root.left	 = Node('B') 
root.right	 = Node('C') 
root.left.left = Node('D') 
root.left.right = Node('E')
root.right.left = Node('F')
root.left.right.left = Node('P')
root.left.right.left.right = Node('E')
print("\n the traversal nodes are")
printInorder(root)
