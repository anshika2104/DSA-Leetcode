class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # f={}
        # for i in nums:
        #     if i in f:
        #         f[i]+=1
        #     else:
        #         f[i]=1
        # for key in list(f.keys()):  
        #     if f[key] > 2:
        #         while nums.count(key) > 2:  
        #             nums.remove(key)  
        # return len(nums)
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k
       
        