def shuffle(nums, n):
    shuffle_array=[]
    for i in range (0, n):
        shuffle_array.append(nums[i])
        shuffle_array.append(nums[i+n])
    return shuffle_array


def main():
    nums =[2,5,1,3,4,7]
    n=3
    print(shuffle(nums, n))


main()