class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        for i in range(len(s)):
            if i%2==0:
                d='0'
            else:
                d='1'
            
            if s[i]!=d:
                c+=1
        c1=len(s)-c
        return min(c,c1)