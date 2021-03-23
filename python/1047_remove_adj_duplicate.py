class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        unique_list=[]
        for each_letter in S:
            if len(unique_list) and each_letter== unique_list[-1]:
                unique_list.pop(-1)
            else:
                unique_list.append(each_letter)

        return ''.join(unique_list)

s=Solution()
print(s.removeDuplicates(S= "abbaca"))

