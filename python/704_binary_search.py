class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            # mid=int((low+high)/2)
            mid = int((high - low) / 2) + low

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

s=Solution()
print(s.search(nums = [-1,0,3,5,9,12], target = 9))
