class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output_list=[]
        for each_nums1 in nums1:
            for i in range(0, len(nums2)):
                if nums2[i] == each_nums1:
                    for j in range(i, len(nums2)):
                        if j+1<len(nums2) and nums2[j+1] > each_nums1:
                            output_list.append(nums2[j+1])
                            break
                        if j+1 >= len(nums2):
                            output_list.append(-1)
                            break
                    break

        return output_list

s=Solution()
print(s.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))

