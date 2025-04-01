class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def rec(st,path):
            res.append(path[:])
            for i in range(st,len(nums)):
                path.append(nums[i])
                rec(i+1,path)
                path.pop()
        rec(0,[])
        return res