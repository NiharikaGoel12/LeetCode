def repeatedNTimes(A):
    unique_A={}

    for key in A:
        if key not in unique_A:
            unique_A[key] =1
        else:
            unique_A[key] +=1
    return (max(unique_A, key=unique_A.get))


def main():
    A= [5,1,5,2,5,3,5,4]
    print(repeatedNTimes(A))

main()