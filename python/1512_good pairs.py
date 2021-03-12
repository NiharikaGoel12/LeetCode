def numIdenticalPairs(nums):
    len_nums=len(nums)
    counter=0
    for i in range(0,len_nums):
        for j in range(i+1, len_nums):
            if (nums[i] == nums[j]) and (i<=j):
                counter+=1
    return counter


def main():
    nums=[1,2,3]
    print(numIdenticalPairs(nums))

main()