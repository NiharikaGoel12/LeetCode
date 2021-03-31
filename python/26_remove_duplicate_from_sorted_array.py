class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1=0
        p2=1

        while p2<len(nums):
            if nums[p1]==nums[p2]:
                p2 +=1
            else:
                nums[p1+1]= nums[p2]
                p1 +=1

        return p1+1


s=Solution()
print(s.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
