class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # c=nums.count(val)
        # for i in range(c):
        #     nums.remove(val)
        # return len(nums)
        nums[:]=[i for i in nums if i !=val]
        return len(nums)
        
        