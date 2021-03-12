def kidsWithCandies(candies, extraCandies):
    max_candy = max(candies)
    kids_count = len(candies)
    final_status=[]

    for i in range(0, kids_count):
        if (candies[i] + extraCandies) >= max_candy:
            final_status.append(True)
        else:
            final_status.append(False)
    return final_status

def main():
    candies=[2,3,5,1,3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))

main()
