from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict=Counter(s)
        # return s_dict

        for i in range(0, len(s)):
            if s_dict[s[i]]==1:
                return i

        return -1

s=Solution()
print(s.firstUniqChar(s = "loveleetcode"))
