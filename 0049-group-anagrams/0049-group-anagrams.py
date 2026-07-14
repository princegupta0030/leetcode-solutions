class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        a={}
        for w in strs:
            b="".join(sorted(w))
            if b not in a:
                a[b]=[]
            a[b].append(w)
        return list(a.values())

