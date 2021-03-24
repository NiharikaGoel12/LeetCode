class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        output_list=[]
        min_loop = min(target[-1], n)
        for i in range(1, min_loop+1):
            if i in target:
                output_list.append("Push")
            else:
                output_list.append("Push")
                output_list.append("Pop")

        return output_list


s=Solution()
print(s.buildArray(target = [2,3,4], n = 4))
