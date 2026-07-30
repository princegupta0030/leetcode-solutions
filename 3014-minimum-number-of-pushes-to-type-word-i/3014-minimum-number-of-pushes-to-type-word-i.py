class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        s=0
        for i in range(len(word)):
            s+=(i//8)+1
        return s