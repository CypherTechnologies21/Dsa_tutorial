class Solution(object):
    def isPalindrome(self, x):
        reversed=0
        temp2=x
        while x>0:
            temp=x%10
            reversed=reversed*10+temp
            x//=10
        if temp2==reversed:
            return True 
        else:
            return False 
