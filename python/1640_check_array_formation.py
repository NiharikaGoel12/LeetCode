class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """

        pieces_dict= {}
        index =0

        for i in pieces:
            if i[0] not in pieces_dict:
                pieces_dict[i[0]]=i

        while index < len(arr):
            if arr[index] in pieces_dict:
                list_value = pieces_dict[arr[index]]
                for each_value in list_value:
                    if index < len(arr) and (each_value == arr[index]):
                        index +=1
                    else:
                        return False
            else:
                return False

        return True

s= Solution()
print(s.canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))
