class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        new_S= self.removebackspace(S)
        new_T = self.removebackspace(T)

        if new_S == new_T:
            return True
        else:
            return False

    def removebackspace(self, word):
        new_word=[]

        for i in range(0, len(word)):
            if word[i] == '#' and len(new_word)!=0:
                new_word.pop()
            elif word[i] == '#' and len(new_word)==0:
                continue
            else:
                new_word.extend(word[i])
        return ''.join(new_word)


s=Solution()
print(s.backspaceCompare(S = "y#fo##f", T = "y#f#o##f"))


