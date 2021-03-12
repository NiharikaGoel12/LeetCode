def maximumWealth(accounts):
    counter =0
    result_array=[]
    len_accounts = len(accounts)
    for list in accounts:
        for i in list:
            counter +=i
        result_array.append(counter)
        counter =0
    return(max(result_array))


def main():
    accounts=[[2,8,7],[7,1,3],[1,9,5]]
    print(maximumWealth(accounts))

main()