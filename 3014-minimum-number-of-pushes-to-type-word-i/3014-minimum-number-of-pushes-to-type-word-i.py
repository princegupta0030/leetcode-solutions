class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        l=len(word)
        a=l//8
        b=l%8
        c=4*a*(a+1)+b*(a+1)
        return c