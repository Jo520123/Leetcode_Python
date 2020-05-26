"""
class Node:
    #Utility  function to create new  node
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

"""
def IsMirror(r1, r2):

    if r1 is None and r2 is None:
        return True

    if (r1 is not None and r2 is not None):
        if r1.key == r2.key:
            return(IsMirror(r1.left, r2.right) and IsMirror(r1.right, r2.left))
    return False

def isSymmetric(root):
    return IsMirror(root,root)





















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        











