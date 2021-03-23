class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter=0
        s_list=[]
        result=""

        for i in range(0, len(S)):
            if S[i] == '(':
                counter +=1
                s_list.append(S[i])
            elif S[i] == ')' and counter !=0:
                counter -=1
                s_list.append(S[i])
            if counter ==0:
                s_list.pop(0)
                s_list.pop(-1)
                output_list = ''.join(s_list)
                result +=output_list
                s_list = []

        return result

s=Solution()
print(s.removeOuterParentheses(S= "(()())(())(()(()))"))



