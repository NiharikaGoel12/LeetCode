class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        good_list=[]
        for char in range(0, len(s)):
            if len(good_list)!=0 and s[char].isupper() and good_list[-1]== s[char].lower():
                good_list.pop(-1)
            elif len(good_list)!=0 and good_list[-1] == s[char].upper() and s[char].islower():
                good_list.pop(-1)
            else:
                good_list.append(s[char])
        return ''.join(good_list)

s=Solution()
print(s.makeGood(s = "kkdsFuqUfSDKK"))
