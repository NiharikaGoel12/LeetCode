class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # output_list=[]
        decreasing_list=[]
        key_value_nums2={}

        for i in range(0, len(nums2)):
            if i+1 <len(nums2) and nums2[i] > nums2[i+1]:
                decreasing_list.append(nums2[i])
            elif i+1 <len(nums2) and nums2[i] < nums2[i+1]:
                key_value_nums2[nums2[i]] = nums2[i+1]

        next_greater_element=[]
        for i in nums1:
            if i in key_value_nums2.keys():
                next_greater_element.append(key_value_nums2[i])
            else:
                next_greater_element.append(-1)

        return next_greater_element



#############Second brut force approach ############

        # for each_nums1 in nums1:
        #     for i in range(0, len(nums2)):
        #         if nums2[i] == each_nums1:
        #             for j in range(i, len(nums2)):
        #                 if j+1<len(nums2) and nums2[j+1] > each_nums1:
        #                     output_list.append(nums2[j+1])
        #                     break
        #                 if j+1 >= len(nums2):
        #                     output_list.append(-1)
        #                     break
        #             break
        #
        # return output_list

s=Solution()
print(s.nextGreaterElement(nums1 = [1,3,5,2,4], nums2 = [6,5,4,3,2,1,7]))

