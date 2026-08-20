class Solution(object):
    def missingNumber(self, nums):
        abu = nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)        

        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]<nums[j]:
        #             nums[i],nums[j]=nums[j],nums[ ]