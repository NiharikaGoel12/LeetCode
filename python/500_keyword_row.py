class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = "qwertyuiop"
        second ="asdfghjkl"
        third="zxcvbnm"

        output_words=[]
        unique_first=set(first)
        unique_second = set(second)
        unique_third = set(third)

        for each_word in words:
            unique_word= set(each_word.lower())
            if unique_word.issubset(unique_first):
                output_words.append(each_word)
            if unique_word.issubset(unique_second):
                output_words.append(each_word)
            if unique_word.issubset(unique_third):
                output_words.append(each_word)

        return output_words

s=Solution()
print(s.findWords(words = ["adsdf","sfd"]))
