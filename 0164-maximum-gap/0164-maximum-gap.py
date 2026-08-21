class Solution(object):
    def maximumGap(self, nums):
        max_p = 0
        nums.sort()
        for i in range(len(nums)):
            max_p=max(max_p,nums[i]-nums[i-1])
        return max_p        