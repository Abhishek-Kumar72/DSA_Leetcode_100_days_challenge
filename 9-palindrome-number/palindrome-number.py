class Solution(object):
    def isPalindrome(self, x):

        if x<0:
            return False

        num=x
        reverse=0

        while num!=0:
            
            rem=num%10
            reverse=reverse*10+rem
            num=num//10

        rev=reverse

        if x==rev:
            return True
        
        if num==rev:
            return True
        
        else:
            return False





        