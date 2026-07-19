class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>=len(s):
            return s
        r=['']*numRows
        c_row=0
        step=1
        for i in s:
            r[c_row]+=i
            c_row+=step
            if c_row==0 or c_row==numRows-1:
                step *= -1
        return ''.join(r)