class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[:]=sorted(set(nums))
        # return len(nums)
        nums[:]=set(nums)
        nums.sort()
        return len(nums)
        