# 101 - Leet code
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# My idea: Tree is divided in two parts - Left Subtree and Right Subtree. Compare both the left subtree with opposite of right subtree
# then return if it is true else false


root = [1,2,2,3,4,4,3]          #output: true

def isSymmetric(self, root) -> bool:
    def Mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and Mirror(t1.right, t2.left) and Mirror(t1.left, t2.right)
    
    return Mirror(root, root)
        