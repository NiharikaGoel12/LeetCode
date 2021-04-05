class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        revised_s=[]
        for i in s.lower():
            if i.isalnum():
                revised_s.append(i)

        pal_1 = int(len(revised_s)/2) - 1

        if len(revised_s)%2 !=0:
            pal_2 = int(len(revised_s)/2)+1
        else:
            pal_2 = int(len(revised_s)/2)

        while pal_1>=0 and pal_2<=len(revised_s):
            if revised_s[pal_1]!= revised_s[pal_2]:
                return False
            else:
                pal_1 -=1
                pal_2 +=1

        return True

s=Solution()
print(s.isPalindrome(s = "0P"))
