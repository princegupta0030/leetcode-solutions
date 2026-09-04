class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r=[]
        def para(open,close,s):
            if len(s)==2*n:
                r.append(s)
                return
            if open<n:
                para(open+1,close,s+"(")
            if close<open:
                para(open,close+1,s+")")
        para(0,0,"")
        return r