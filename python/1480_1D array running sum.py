
def runningSum(nums):
    len_nums = len(nums)
    run_sum = []
    counter = 0
    for i in range(0,len_nums):
        counter = counter + nums[i]
        run_sum.append(counter)
    return run_sum

def main():
    nums=[1,2,3,4]
    print(runningSum(nums))

main()

