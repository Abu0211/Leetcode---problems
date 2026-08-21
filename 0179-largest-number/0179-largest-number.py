class Solution(object):
    def largestNumber(self, nums):
        s=[]
        for i in range (len(nums)):
           s.append (str(nums[i]))
        for i in range (len(s)):
           for j in range (len(s) -1):
              if s[j] + s[j + 1] < s[j + 1] + s[j]:
                 s[j] , s[j + 1] = s[j + 1] , s[j]
        result = ""
        for num in s:
            result +=num
        if result [0]=="0":
           return "0"
        return result
        