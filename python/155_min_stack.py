class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.output_list=[]


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.output_list.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.output_list.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.output_list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.output_list)

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(val=-2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
