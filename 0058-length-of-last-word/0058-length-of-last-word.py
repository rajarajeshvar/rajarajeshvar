class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        h=s.split(" ")
        for i in range(len(h)):
            if h[i]!='':
                h.append(h[i])
        print(h)
        return len(h[-1])
        