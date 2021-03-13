def hasGroupsSizeX(deck):
    len_deck = len(deck)
    deck_dict={}

    for i in range(0, len_deck):
        if deck[i] in deck_dict:
            deck_dict[deck[i]] +=1
        else:
            deck_dict[deck[i]] = 1

    if len(deck_dict) == 1:
        return len(deck) > 1

    lowest_count = min(deck_dict.values())
    divisible_list=[]

    for i in range(2, lowest_count+1):
        if lowest_count %i==0:
            divisible_list.append(i)

    for div in divisible_list:
        all_divisble = True
        for count in deck_dict.values():
            if count % div != 0:
                all_divisble = False
                break
        if all_divisble:
            return True

    return False

def main():
    deck=[1,1,1,1,1,1,2,2,2,2,2,2,2,2,2]
    print(hasGroupsSizeX(deck))

main()