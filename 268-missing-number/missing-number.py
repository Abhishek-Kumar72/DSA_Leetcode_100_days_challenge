class Solution(object):
    def missingNumber(self, nums):
        
        n=len(nums)
        expec_sum=(n*(n+1))//2
        actual_sum=0

        for i in range(n):
            actual_sum+=nums[i]

        return expec_sum-actual_sum
        