class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size==0 or size<3:
            return 0
        leftMax=[0] * size
        rightMax=[0] * size

        leftMax_height=height[0]

        for i in range(0, size):
            leftMax_height=max(leftMax_height,height[i])
            leftMax[i]=max(leftMax_height,height[i])

        rightMax_height=height[-1]

        for i in reversed(range(size-1)):
            rightMax_height=max(rightMax_height,height[i])
            rightMax[i]=max(rightMax_height,height[i])

        water_sum=0
        for i in range(1,size-1):
            water_sum +=min(leftMax[i],rightMax[i])-height[i]

        return water_sum

s=Solution()
print(s.trap(height = [4,2,0,3,2,5]))
