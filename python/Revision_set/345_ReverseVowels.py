class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vow=['a','e','i','o', 'u', 'A', 'E', 'I', 'O', 'U']
        front_vow=0
        end_vow=len(s)-1
        list_s=list(s)

        while front_vow<end_vow:
            if list_s[front_vow] not in vow:
                front_vow +=1
            if list_s[end_vow] not in vow:
                end_vow -=1
            if list_s[front_vow] in vow and list_s[end_vow] in vow:
                temp=list_s[front_vow]
                list_s[front_vow] = list_s[end_vow]
                list_s[end_vow] = temp
                front_vow +=1
                end_vow -=1

        return ''.join(list_s)

s=Solution()
print(s.reverseVowels(s = "leetcode"))
