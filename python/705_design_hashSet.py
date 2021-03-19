class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.new_hashset = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.new_hashset:
            self.new_hashset.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.new_hashset:
            self.new_hashset.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.new_hashset:
            return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(key =1)
obj.remove(key = 1)
param_3 = obj.contains(key=1)