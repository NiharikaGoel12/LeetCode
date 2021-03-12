def countSmaller(nums):
    len_nums = len(nums)
    counter=0
    smaller_count =[]

    for i in range(0, len_nums):
        for j in range(i+1, len_nums):
            if nums[i] > nums[j]:
                counter +=1
        smaller_count.append(counter)
        counter = 0

    if len_nums == 1:
        smaller_count = [0]

    return smaller_count


def main():
    nums=[-1,-1]
    print(countSmaller(nums))

main()