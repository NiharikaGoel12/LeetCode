class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        folder_list=[]

        for i in logs:
            if i == "../" and len(folder_list)!=0:
                folder_list.pop(-1)
            elif i=="./" or (i == "../" and len(folder_list)==0):
                continue
            else:
                folder_list.append(i)

        return len(folder_list)


s=Solution()
print(s.minOperations(logs = ["d1/","../","../","../"]))
