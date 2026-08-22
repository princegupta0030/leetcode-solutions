class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=n
        s=0
        product=1
        while num>0:
            digit=num%10
            s=s+digit
            product=product*digit
            num=num//10
        t_s=s+product
        if n%t_s==0:
            return True
        else:
            return False