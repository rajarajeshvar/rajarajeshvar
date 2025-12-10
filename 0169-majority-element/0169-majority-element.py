class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=set(nums)
        l=list(l)
        print(nums)
        for i in range(len(l)):
            if nums.count(l[i])>(len(nums)/2):
                s=l[i]
                return l[i]
                break
                


            
        

        
        