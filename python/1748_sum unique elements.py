def sumOfUnique(nums):
    unique_nums = {}
    counter =0

    for key in nums:
        if key not in unique_nums:
            unique_nums[key] =1
        else:
            unique_nums[key] =0

    for k,v in unique_nums.items():
        if v!=0:
            counter += k
    return counter

def main():
    nums=[1,2,3,4,5]
    print(sumOfUnique(nums))

main()