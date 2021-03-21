class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        counter =0
        for i in arr:
            for j in pieces:
                if i in j:
                    counter +=1

        if counter == len(arr):
            return True
        else:
            return False


s= Solution()
print(s.canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))