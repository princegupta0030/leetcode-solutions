class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v=set("aeiouAEIOU")
        s_list=list(s)
        l=0
        r=len(s)-1
        while l<r:
            while l<r and s_list[l] not in v:
                l+=1
            while l<r and s_list[r] not in v:
                r-=1
            if l<r:
                s_list[l],s_list[r]=s_list[r],s_list[l]
                l+=1
                r-=1
        return "".join(s_list)
