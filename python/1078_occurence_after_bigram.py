class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """

        third_word=[]
        list_text= text.split()
        for i in range(0, len(list_text)):

            if ((i+2)<= len(list_text)-1) and (list_text[i] == first) and (list_text[i+1] == second):
                third_word.append(list_text[i+2])

        return third_word


s= Solution()
print(s.findOcurrences(text = "ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk",
                       first = "lnlqhmaohv", second = "ypkk"))
