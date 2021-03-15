class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        overall_dict = {}
        common_char=[]

        len_A= len(A)
        for i in range(0, len_A):
            overall_dict[i+1] = self.word_count(A[i])


        for each_key,each_value in overall_dict[1].items():
            temp_min = []
            for v in overall_dict.keys():
                if each_key in overall_dict[v]:
                    min_counter=min(each_value,overall_dict[v][each_key])
                else:
                    min_counter=0
                    temp_min.append(min_counter)
                    break
                temp_min.append(min_counter)
            common_char.extend(each_key * min(temp_min))

        return common_char

    def word_count(self, word):
        dict_words ={}
        for i in range(0, len(word)):
            if word[i] in dict_words:
                dict_words[word[i]] +=1
            else:
                dict_words[word[i]] = 1
        return dict_words



s=Solution()
print(s.commonChars(A=["cool","lock","cook"]))