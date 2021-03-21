from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict=Counter(s)
        t_dict = Counter(t)

        for key,value in t_dict.items():
            if key in s_dict and value == s_dict[key]:
                continue
            else:
                return False

        for key,value in s_dict.items():
            if key in t_dict and value == t_dict[key]:
                continue
            else:
                return False

        return True


s=Solution()
print(s.isAnagram(s = "rat", t = "car"))