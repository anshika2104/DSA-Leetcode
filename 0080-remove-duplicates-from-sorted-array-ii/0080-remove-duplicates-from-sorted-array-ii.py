class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for key in list(f.keys()):  # Iterate over keys instead of values
            if f[key] > 2:  # Check frequency using correct reference
                while nums.count(key) > 2:  # Remove extra occurrences
                    nums.remove(key)  # Remove one occurrence at a time
        
        return len(nums)
        # for key,val in f.items():
        #     nums[:] = [key for key in nums if f[key] <= 2]
        # return len(nums)
        