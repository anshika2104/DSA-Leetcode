class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f={}
        n=len(nums)
        for i in nums:
            f[i]=f.get(i,0)+1
            if f[i]>n//2:
                return i
        return None
        