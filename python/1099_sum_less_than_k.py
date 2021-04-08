class Solution(object):
    def twoSumlessthanK (self, A, K):

        pointer1=0
        pointer2=len(A)-1
        max_sum=0

        A.sort()

        while pointer1<len(A) and pointer2>=0:
            if A[pointer1]+A[pointer2]<K:
                max_sum=max(max_sum, A[pointer1]+A[pointer2])
                pointer1+=1
            else:
                pointer2-=1

        return max_sum

s=Solution()
print(s.twoSumlessthanK(A = [34,23,1,24,75,33,54,8], K = 60))



