class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        number=[str(i) for i in range(1,n+1)]
        k-=1
        def find_perm(r,k):
            if r==0:
                return ""
            fact=math.factorial(r-1)
            idx=k//fact
            c=number.pop(idx)
            return c+find_perm(r-1,k%fact)
        return find_perm(n,k)