class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def isSymmertric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return  True
        return self.isSymm(root.left, root.right)

    def isSymm(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False

        if r1.val != r2.val:
            return False

        return self.isSymm(r1.left, r2.right) and self.isSym(r1.right, r2.left)

def start():
    print("start")
    root = TreeNode(2)
    print(Solution().isSymmertric(root))


if __name__ == "__main__":
    start()
