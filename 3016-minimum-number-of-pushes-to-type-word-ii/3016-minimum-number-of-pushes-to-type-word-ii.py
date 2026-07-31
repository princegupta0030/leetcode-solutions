class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        f=[0]*26
        for c in word:
            f[ord(c)-ord('a')]+=1
        f.sort(reverse=True)
        a=0
        for i in range(26):
            a+=f[i]*(i//8+1)
        return a