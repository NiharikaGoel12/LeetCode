class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.output_list=[]

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.output_list.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.output_list.pop(-1)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.output_list[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.output_list)==0:
            return True
        else:
            return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
