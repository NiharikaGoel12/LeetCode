class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in range(0, len(s)):
            if len(stack)!=0 and s[i]==')' and stack[-1] == '(':
                stack.pop()
            elif len(stack)!=0 and s[i]=='}' and stack[-1] == '{':
                stack.pop()
            elif len(stack)!=0 and s[i]==']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(s[i])

        if len(stack) ==0:
            return True
        else:
            return False

s=Solution()
print(s.isValid(s = "()"))
