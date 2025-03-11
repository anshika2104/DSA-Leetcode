class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # for i in range(0,len(nums)-1):
        #     if nums[i-1]<nums[i]>nums[i+1]:
        #         return i
        # return len(nums)-1
        l=0
        r=len(nums)-1
        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>nums[mid+1]:
                r=mid
            else:
                l=mid+1
        return l
        