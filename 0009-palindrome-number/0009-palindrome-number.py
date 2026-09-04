class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num=x
        r=0
        while num>0:
            d=num%10
            num=num//10
            r=r*10+d
        if r==x:
            return True
        else:
            return False