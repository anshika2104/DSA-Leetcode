class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def rec(st,path):
            res.append(path[:])
            for i in range(st,len(nums)):
                if i > st and nums[i] == nums[i - 1]: 
                    continue
                path.append(nums[i])
                rec(i+1,path)
                path.pop()
        rec(0,[])
        return res
        