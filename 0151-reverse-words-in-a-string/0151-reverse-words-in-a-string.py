class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        w=s.split()
        w=w[::-1]
        return " ".join(w)