# Time O(n)
# Space O(1)
class Solution:
    def __init__(self):
        self.result = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #using DFS preorder traversal
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, root: Optional[TreeNode], level: int) -> None:
        if root == None:
            return
        
        if len(self.result) < level + 1:
            self.result.append([root.val])
        else:
            self.result[level].append(root.val)
        
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)


# Time O(n)
# Space O(n/2)
from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #using BFS
        result = []
        if root is None: return result
        q = Queue()
        q.put(root)
        while not q.empty():
            size = q.qsize()
            level_ele = []
            for i in range(0, size):
                node = q.get()
                level_ele.append(node.val)
                if node.left != None: q.put(node.left) 
                if node.right != None: q.put(node.right) 
            result.append(level_ele)
        return result
        