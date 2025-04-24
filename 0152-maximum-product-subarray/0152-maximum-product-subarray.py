class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxres=nums[0]
        maxpos=nums[0]
        minneg=nums[0]
        c1=0
        c2=0
        for i in range(1,len(nums)):
            c1=maxpos*nums[i]
            c2=minneg*nums[i]
            maxpos=max(nums[i],c1,c2)
            minneg=min(nums[i],c1,c2)
            maxres=max(maxres,maxpos,minneg)
        return maxres
        