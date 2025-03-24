# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # res=[]
        # queue=deque([root])
        # while queue:
        #     sum1=0
        #     c=len(queue)
        #     for  i in range(len(queue)):
        #         node=queue.popleft()
        #         sum1+=node.val
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(sum1/c)
        # return res

        
   #dfs soln------------
        s=[]
        c=[]
        # node=root(1)
        # depth=0
        def dfs(root,depth) :
            if not root:
                return 
            if depth<len(s):
                s[depth]+=root.val
                c[depth]+=1
            else:
                s.append(root.val)
                c.append(1)
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        dfs(root,0)
        res=[]
        for i in range(len(s)):
            avg=s[i]/c[i]
            res.append(avg)
        return res
