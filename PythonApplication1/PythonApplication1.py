
class Node: 
    # Node Constructor
    def __init__(self, key): 
        self.key =  key 
        self.left = None
        self.right = None
  
# Finds the path from root node to given node of the tree. 
def findPath(root, path, val): 
   
    if root is None: 
        return False

    path.append(root.key) 
  
    if root.key == val : 
        return True
  
    if ((root.left != None and findPath(root.left, path, val)) or
            (root.right!= None and findPath(root.right, path, val))): 
        return True 
  
    path.pop() 
    return False
  
# Returns LCA if given descendants are in the tree, returns -1 otherwise
def findLCA(root, descendant1, descendant2): 
   
    path1 = [] 
    path2 = [] 
  
    if (not findPath(root, path1, descendant1) or not findPath(root, path2, descendant2)): 
        return -1 
  
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.left.left.right = Node(8); 
root.left.left.left = Node(9); 
root.left.right.right = Node(10);
root.left.right.left = Node(11);
root.right.left.right = Node(12);
root.right.left.left = Node(13);
root.right.right.right = Node(14);
root.right.right.left = Node(15);
  
print ("LCA(10, 15) = %d" %(findLCA(root, 10, 15,))) 
print ("LCA(8, 11) = %d" %(findLCA(root, 8, 11))) 
print ("LCA(3, 8) = %d" %(findLCA(root, 3, 8))) 
print ("LCA(11, 14) = %d" %(findLCA(root, 11, 14))) 
