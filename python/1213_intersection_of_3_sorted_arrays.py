class Solution(object):
    def nextGreaterElement(self, arr1, arr2, arr3):

        common_arr1_arr2 = self.commonNumbers(arr1, arr2)
        common_arr_arr3 = self.commonNumbers(common_arr1_arr2, arr3)

        return common_arr_arr3


    def commonNumbers(self, array1, array2):
        common_numbers=[]
        pointer1=0
        pointer2=0
        while pointer1<len(array1) and pointer2<len(array2):
            if array1[pointer1] == array2[pointer2]:
                common_numbers.append(array1[pointer1])
                pointer1+=1
                pointer2+=1
            elif array1[pointer1]> array2[pointer2]:
                pointer2+=1
            elif array1[pointer1]< array2[pointer2]:
                pointer1+=1

        return common_numbers

s=Solution()
print(s.nextGreaterElement(arr1=[1,2,9], arr2=[1,9], arr3=[1,3,4,5,9]))
