class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)

        k=k%n
        def reversed(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        reversed(0,n-1)
        reversed(0,k-1)
        reversed(k,n-1)
           