def findMaxConsecutiveOnes(nums):
    counter = 0
    max_count = 0

    for i in nums:
        if i == 1:
            counter +=1
        else:
            counter =0
        max_count = max(counter, max_count)

    return max_count


def main():
    nums=[1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(nums))

main()