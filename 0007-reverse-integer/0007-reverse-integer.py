class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        is_n=x<0
        x=abs(x)
        d=0
        while x>0:
            l=x%10
            x=x//10
            d=d*10+l
        if is_n:
            d=-d
        if d<-2**31 or d>2**31-1:
            return 0
        return d