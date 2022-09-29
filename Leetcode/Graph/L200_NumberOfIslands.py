"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1


Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


from typing import List

class Solution:
  def __init__(self):
    self.grid = []

  def numIslands(self, grid: List[List[str]]) -> int:
    self.grid = grid
    ans = 0
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if self.grid[i][j]=='1':
          self.dfs(i,j)
          ans+=1
    return ans
    
  def dfs(self,i,j):
    self.grid[i][j]='0'
    if i-1>=0 and self.grid[i-1][j]=='1': self.dfs(i-1,j)
    if i+1<len(self.grid) and self.grid[i+1][j]=='1': self.dfs(i+1,j)
    if j-1>=0 and self.grid[i][j-1]=='1': self.dfs(i,j-1)
    if j+1<len(self.grid[0]) and self.grid[i][j+1]=='1': self.dfs(i,j+1)