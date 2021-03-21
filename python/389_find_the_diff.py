from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_dict = Counter(s)
        t_dict = Counter(t)

        for key,value in t_dict.items():
            if key not in s_dict or value != s_dict[key]:
                return key


s= Solution()
print(s.findTheDifference(s = "abcd", t = "abcde"))
