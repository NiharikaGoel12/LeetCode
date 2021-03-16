class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        char_dict= self.dict_creator(chars)

        valid_words=[]
        for each_word in words:
            word_dict = self.dict_creator(each_word)
            counter=0
            for key,value in word_dict.items():
                if key not in char_dict:
                    break
                elif char_dict[key] >= value:
                    counter +=1

            if counter == len(set(each_word)):
                valid_words.append(each_word)

        total =0
        for each_word in valid_words:
            total += len(each_word)

        return total

    def dict_creator(self, word):
        chars_dict = {}
        for i in word:
            if i in chars_dict:
                chars_dict[i] +=1
            else:
                chars_dict[i] = 1
        return chars_dict


s=Solution()
print(s.countCharacters(words= ["hello","world","leetcode"],
                        chars = "welldonehoneyr"))
