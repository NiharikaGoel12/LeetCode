def numJewelsInStones(jewels, stones):
    counter={}

    for each_jewel in jewels:
        counter[each_jewel] = 0

    for each_stone in stones:
        if each_stone in counter:
            counter[each_stone] +=1
    return (sum(counter.values()))

def main():
    jewels="aA"
    stones="aAAbbbb"
    print(numJewelsInStones(jewels, stones))

main()