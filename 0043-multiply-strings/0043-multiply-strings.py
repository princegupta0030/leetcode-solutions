class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        m=len(num1)
        n=len(num2)
        r=[0]*(m+n)
        for i in range (m-1,-1,-1):
            for j in range (n-1,-1,-1):
                mul=(ord(num1[i])-ord('0')) * (ord(num2[j])-ord('0'))
                p=i+j
                q=i+j+1
                total=mul+r[q]
                r[q]=total%10
                r[p]+=total//10
        ans =""
        for num in r:
            if not (ans=="" and num==0):
                ans +=str(num)
        return ans