class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        w=[]
        r=len(s)-1
        while r>=0:
            while r>=0 and s[r]==' ':
                r-=1
            if r<0:
                break
            l=r
            while l>=0 and s[l]!=' ':
                l-=1
            w.append(s[l+1:r+1])
            r=l
        return " ".join(w)