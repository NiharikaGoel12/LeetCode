from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """

        A_list=A.split()
        B_list=B.split()
        uncommon_words=[]

        A_dict= Counter(A_list)
        B_dict = Counter(B_list)

        for key,value in A_dict.items():
            if key not in B_dict and value ==1:
                uncommon_words.append(key)

        for key,value in B_dict.items():
            if key not in A_dict and value == 1:
                uncommon_words.append(key)

        return uncommon_words


s=Solution()
print(s.uncommonFromSentences(A = "apple apple", B = "banana"))
