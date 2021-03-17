class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_grid=len(grid)
        total_perimeter=0
        for xaxis in range(0, len_grid):
            for yaxis in range(0, len_grid):
                if grid[xaxis][yaxis] ==0 and ((xaxis+1 <= len_grid) and (xaxis-1 >= 0) and (yaxis+1 <= len_grid) and (yaxis-1 >= 0)):
                    total_perimeter +=1
                    count_perimeter = self.one_presence(grid, xaxis,yaxis)
                    total_perimeter +=count_perimeter

        return total_perimeter

    def one_presence(self, grid, xaxis,yaxis):
        counter =0
        if grid[xaxis][yaxis-1] ==1:
            counter+=1
        if grid[xaxis-1][yaxis]==1:
            counter +=1
        if grid[xaxis][yaxis+1] ==1:
            counter +=1
        if grid[xaxis+1][yaxis] ==1:
            counter +=1

        return counter



s=Solution()
print(s.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))