import collections
from collections import defaultdict

def frequencySort(nums):
    unique_nums = {}
    result_nums=[]
    inv_map=defaultdict(list)

    for key in nums:
        if key not in unique_nums:
            unique_nums[key]=1
        else:
            unique_nums[key] +=1

    for key,value in unique_nums.items():
        inv_map[value].append(key)

    for key,value in inv_map.items():
        if len(value) > 1:
            inv_map[key] = sorted(inv_map[key], reverse=True)

    ordered_dict = collections.OrderedDict(sorted(inv_map.items()))

    for key,value in ordered_dict.items():
        for each_value in value:
            result_nums.extend([each_value] * key)

    return result_nums



def main():
    nums=[-1,1,-6,4,5,-6,1,4,1]
    print(frequencySort(nums))

main()