class Node: 
  def __init__(self , val): 
      self.value = val  
      self.left = None
      self.right = None

def maxDepth(root):
  # Null node has 0 depth.
  if root == None:
    return 0

  # Get the depth of the left and right subtree 
  # using recursion.
  leftDepth = maxDepth(root.left)
  rightDepth = maxDepth(root.right)

  # Choose the larger one and add the root to it.
  if leftDepth > rightDepth:
    return leftDepth + 1
  else:
    return rightDepth + 1
        
# Driver code
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print("The max depth is:", maxDepth(root))
        