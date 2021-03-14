class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = list(s)
        len_s = len(list_s)
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        front=0
        end= len_s-1
        front_vow=''
        end_vow=''

        while front <= end:
            if list_s[front] in vow and front_vow is '':
                front_vow= list_s[front]
            if list_s[end] in vow and end_vow is '':
                end_vow = list_s[end]
            if front_vow is not '' and end_vow is not '':
                list_s[front] = end_vow
                list_s[end] = front_vow
                front_vow = ''
                end_vow = ''

            if front_vow is '' or list_s[front] not in vow:
                front +=1
            if end_vow is '' or list_s[end] not in vow:
                end -=1

        return ''.join(list_s)

s = Solution()
# print(s.reverseVowels(s= "hello"))
print(s.reverseVowels(s= "ai"))