class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # c=0
        # for i in nums:
        #     if nums[i]==nums[i+1]:
        #         c+=1
        #     c=1
        #     if c
        d={}
        for i in nums:
            if  i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in d.values():
            if j%2!=0:
                return False
        return True

        