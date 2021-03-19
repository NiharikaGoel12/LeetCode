class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        perimeter = 0
        x_axis = [1, -1, 0, 0]
        y_axis = [0, 0, 1, -1]

        for row in range(0, n):
            for col in range(0, m):
                for k in range(0, len(y_axis)):
                    # To check left,right, top & bottom of each cell
                    newX = row + x_axis[k]
                    newY = col + y_axis[k]
                    # Coordinates are within the grid
                    if newX >= 0 and newY >= 0 and newX < n and newY < m:
                        if grid[row][col] == 0 and grid[newX][newY] == 1:
                            perimeter += 1
                    else:
                        # neighbour is outside the grid
                        if grid[row][col] == 1:
                            perimeter += 1
        return perimeter


s=Solution()
print(s.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))