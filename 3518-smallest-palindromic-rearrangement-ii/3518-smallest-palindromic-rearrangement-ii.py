from math import comb
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq=[s.count(c) for c in "abcdefghijklmnopqrstuvwxyz"]
        mid = ""
        for i in range(26):
            if freq[i]%2:
                mid=chr(97 + i)

        half=[x//2 for x in freq]

        def ways(a):
            total=sum(a)
            ans=1

            for x in a:
                if x:
                    ans*=comb(total, x)

                    if ans >= k:
                        return k
                    total-=x
            return ans

        if ways(half)<k:
            return ""

        left=[]
        for _ in range(sum(half)):
            for i in range(26):
                if half[i]==0:
                    continue

                half[i]-=1
                count=ways(half)

                if count>=k:
                    left.append(chr(97+i))
                    break

                k-=count
                half[i]+=1

        left=''.join(left)

        return left+mid+left[::-1]