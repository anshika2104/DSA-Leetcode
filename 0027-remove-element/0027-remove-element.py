class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # using remove fxn ------------------------------
        # c=nums.count(val)
        # for i in range(c):
        #     nums.remove(val)
        # return len(nums)
        # using list comprehension--------------
        # nums[:]=[i for i in nums if i !=val]
        # return len(nums)
        # ----------two pointer----
        i,j=0,0
        while i<len(nums): 
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
            i+=1
        return j
        
        