class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.output_list=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.output_list.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.output_list.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.output_list[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.output_list)==0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x=1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
