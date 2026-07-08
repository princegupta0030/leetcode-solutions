class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        s=min(len(str1),len(str2))
        for i in range(s,0,-1):
            if len(str1)%i==0 and len(str2)%i==0:
                p=str1[:i]
                if p*(len(str1)//i)==str1 and p*(len(str2)//i)==str2:
                    return p
        return ""