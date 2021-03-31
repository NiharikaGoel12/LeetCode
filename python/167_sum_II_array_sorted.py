class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1=0
        p2=len(numbers)-1
        output_list=[]

        while len(output_list)==0:
            if numbers[p1] + numbers[p2] == target:
                output_list.append(p1+1)
                output_list.append(p2+1)
            elif numbers[p1] + numbers[p2] < target:
                p1 +=1
            elif numbers[p1] + numbers[p2] > target:
                p2 -=1

        return output_list


s=Solution()
print(s.twoSum(numbers = [-1,0], target = -1))