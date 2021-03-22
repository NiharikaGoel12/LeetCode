from collections import Counter
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licence_clean = ''.join([i for i in licensePlate.lower() if not i.isdigit()]).replace(" ", "")
        licence_dict= Counter(licence_clean)
        shortest_word=[]

        for each_word in words:
            counter = 0
            word_dict=Counter(each_word)

            for key,value in licence_dict.items():
                if key in word_dict and word_dict[key] >= value:
                    counter +=1
                else:
                    break

            if counter == len(licence_dict):
                shortest_word.append(each_word)

        if len(shortest_word) == 0:
            return None
        else:
            return min(shortest_word, key=len)


s=Solution()
print(s.shortestCompletingWord(licensePlate = "GrC8950",
                               words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]))
