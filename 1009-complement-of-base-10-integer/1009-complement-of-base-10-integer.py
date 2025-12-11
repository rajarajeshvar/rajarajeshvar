class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=""
        s1=""
        l=[0,1]
        while n not in l:
            s=str(n%2)+s
            n=n//2
        s=str(n)+s
        for i in range(len(s)):
            if s[i]=="0":
                s1=s1+"1"
            else:
                s1=s1+"0"
        
        b=int(s1,2)
        return b

        