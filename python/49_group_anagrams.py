from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # key type str
        # value type list

        dict_str=defaultdict(list)

        for word in strs:
            keyW=''.join(sorted(word))
            dict_str[keyW].append(word)
        return list(dict_str.values())

s=Solution()
print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
