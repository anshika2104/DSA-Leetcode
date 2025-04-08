class Solution:
    def rob(self, nums: List[int]) -> int:
        s1,s2=0,0
        for i in range(len(nums)):
            temp=max(s1,s2+nums[i])
            s2,s1=s1,temp
        return temp
        