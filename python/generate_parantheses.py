class Solution:

    def generate(self,n):
        result=[]
        current=""

        self.generateRecurs(current, result, 0,0,n)
        return result


    def generateRecurs(self, current_str, result, leftOpen, rightOpen, numberOfBracket):
        if leftOpen==numberOfBracket and rightOpen==numberOfBracket:
            result.append(current_str)
            return
        if leftOpen > numberOfBracket or rightOpen > numberOfBracket:
            return
        if leftOpen>rightOpen:
            self.generateRecurs(current_str+")", result, leftOpen, rightOpen+1, numberOfBracket)
            self.generateRecurs(current_str+"(", result, leftOpen+1, rightOpen, numberOfBracket)

        if leftOpen==rightOpen:
            self.generateRecurs(current_str + "(", result, leftOpen + 1, rightOpen, numberOfBracket)

s=Solution()
print(s.generate(n=3))