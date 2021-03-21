from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        word = "balloon"
        balloon_dict = Counter(word)
        text_dict = Counter(text)
        mult_factor =[]


        for key,value in balloon_dict.items():
            if key in text_dict and text_dict[key] >= value:
                mult_factor.append(int(text_dict[key]/value))
            else:
                return 0

        return min(mult_factor)

s = Solution()
print(s.maxNumberOfBalloons(text = "leetcode"))