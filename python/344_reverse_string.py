class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        len_s=len(s)

        for i in range (0, int(len(s)/2)):
            temp_str=s[i]
            s[i] = s[len_s-1]
            s[len_s-1] = temp_str
            len_s -=1

        return s



s=Solution()
print(s.reverseString(s = ["H","a","n","n","a","h"]))