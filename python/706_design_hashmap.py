class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.new_hash_map = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.new_hash_map[key] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if key in self.new_hash_map:
            return self.new_hash_map[key]
        else:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.new_hash_map:
            del self.new_hash_map[key]


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj.put(key = 1,value = 1))
param_2 = obj.get(key= 1)
print(obj.remove(key = 1))