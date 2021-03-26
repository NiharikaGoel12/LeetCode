class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        remove_backspace_S= self.remove_backspace(S)
        remove_backspace_T=self.remove_backspace(T)

        if ''.join(remove_backspace_S)==''.join(remove_backspace_T):
            return True
        else:
            return False

    def remove_backspace(self, word):
        output_list = []

        for each_word in word:
            if each_word == '#' and len(output_list)!=0:
               output_list.pop(-1)
            elif each_word == '#' and len(output_list) ==0:
                continue
            else:
                output_list.append(each_word)

        return output_list

s=Solution()
print(s.backspaceCompare(S = "a#c", T = "#"))
