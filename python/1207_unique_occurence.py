class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_dict= {}
        for i in arr:
            if i in arr_dict:
                arr_dict[i] +=1
            else:
                arr_dict[i] = 1

        len_dict= len(arr_dict)
        if len_dict != len(set(list(arr_dict.values()))):
            return False
        return True


s=Solution()
print(s.uniqueOccurrences(arr=[1,2]))

