class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        count=0
        new_count=0

        for i in nums:
            if i==1:
                count+=1
                new_count=max(new_count,count)

            else:
                    count=0
            
            
            
        return new_count
            
            
        