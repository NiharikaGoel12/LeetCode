class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
#         C: Remove previous record from stack
#         D: Record new score by doubling previous record from stack

        ops_list=[]
        for i in range(0, len(ops)):
            if ops[i] == 'C':
                ops_list.remove(ops_list[-1])
            elif ops[i] == 'D':
                ops_list.append(2 * int(ops_list[-1]))
            elif ops[i] == '+':
                ops_list.append(ops_list[-1] + ops_list[-2])
            elif int(ops[i]) >= 0 or int(ops[i]) <= 0:
                ops_list.append(int(ops[i]))

        return sum(ops_list)

s= Solution()
print(s.calPoints(ops = ["1"]))
