class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0 #4
        high=len(nums)-1 #2

        while low<=high:
            mid = int((low + high) / 2)  # 7
            if nums[mid]== target:
                return mid
            if nums[mid]>nums[high]: # left part is sorted
                if nums[low] <= target < nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid] < target <= nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1


s=Solution()
print(s.search(nums = [4,5,6,0,1,2,3], target = 1))
print(s.search(nums = [4,5,6,0,1,2,3], target = 7))


