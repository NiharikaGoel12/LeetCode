# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version<5:
        return False
    else:
        return True

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low <= high:
            mid = int((low + high)/2)

            if isBadVersion(mid) == True and (mid == 1 or isBadVersion(mid - 1) == False):
                return mid
            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                high = mid - 1
        return -1

s=Solution()
print(s.firstBadVersion(n=10))
print(s.firstBadVersion(n=5))
