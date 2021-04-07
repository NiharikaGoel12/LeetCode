class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """

        name_p1=0
        typed_p2=0

        while name_p1< len(name) and typed_p2< len(typed):
            if name[name_p1]!= typed[typed_p2]:
                if typed_p2>0 and typed[typed_p2]==typed[typed_p2-1]:
                    typed_p2+=1
                else:
                    return False
            elif name[name_p1]==typed[typed_p2]:
                name_p1+=1
                typed_p2+=1

        if name_p1<len(name):
            return False
        if typed_p2<len(typed):
            if len(set(typed[typed_p2:]))==1:
                if typed[typed_p2] == typed[typed_p2-1]:
                    return True
                else:
                    return False
            else:
                return False

        return True


s=Solution()
print(s.isLongPressedName(name = "zlexya", typed = "aazlllllllllllllleexxxxxxxxxxxxxxxya"))
