from collections import Counter
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """

        candy_dict= Counter(candyType)
        distinct_candy= len(candy_dict.keys())
        revise_candy = int(len(candyType)/2)
        return min(distinct_candy, revise_candy)


s =Solution()
print(s.distributeCandies(candyType = [6,6,6,6]))
