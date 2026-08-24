class Solution(object):
    def wiggleSort(self, nums):
        result=[]
        nums.sort()
        n = len(nums)
        left = (n-1)//2
        right = n-1
        for i in range(n):
            if i % 2 == 0:
                result.append(nums[left])
                left -= 1
            else:
                result.append(nums[right])
                right -= 1
        for i in range (n):
            nums[i] = result [i]
        