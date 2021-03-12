def smallerNumbersThanCurrent(nums):
    len_nums = len(nums)
    counter=0
    smaller_count =[]

    for i in range(0, len_nums):
        for j in range(0, len_nums):
            if nums[i] > nums[j]:
                counter +=1
        smaller_count.append(counter)
        counter = 0

    return smaller_count


def main():
    nums=[6,5,4,8]
    print(smallerNumbersThanCurrent(nums))

main()