# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 

# Constraints:

# 1 <= n <= 9


class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
      def initialize_board(n):
          board = {}
          for key in (['queen', 'row', 'col', 'nwtose', 'swtone']):
              board[key] = {}
          for i in range(n):
              board['row'][i] = 0
              board['col'][i] = 0
              board['queen'][i] = -1
          for i in range(-(n-1), n):
              board['nwtose'][i] = 0
          for i in range(2*n - 1):
              board['swtone'][i] = 0
          return (board)

      def place_queen(i, board):
          n = len(board['queen'].keys())
          for j in range(n):
              if isfree(i, j, board):
                  add_queen(i, j, board)
                  if i == n-1:
                      print_board(board)
                  else:
                      keepgoing = place_queen(i + 1, board)
                  remove_queen(i, j, board)

      def isfree(i, j, board):
          return(board['row'][i] == 0 and board['col'][j] == 0 and board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)                        
      def add_queen(i, j, board):
          board['queen'][i] = j
          board['row'][i] = 1
          board['col'][j] = 1
          board['nwtose'][j - i] = 1
          board['swtone'][i + j] = 1


      def remove_queen(i, j, board):
          board['queen'][i] = -1
          board['row'][i] = 0
          board['col'][j] = 0
          board['nwtose'][j - i] = 0
          board['swtone'][i + j] = 0

      def print_board(board):
          help_list = []
          for j in range(n):
              row_str = "."*n
              index = board['queen'][j]
              row_str = row_str[:index] +"Q" + row_str[index+1:]
              help_list.append(row_str)

          ans.append(help_list)
          for i in range(len(ans)):
              for j in range(i + 1, len(ans)):
                  if ans[i] == ans[j]:
                      ans.remove(ans[j])
          return (ans)

      ans = []
      get_board = initialize_board(n)
      if place_queen(0, get_board):
          print_board(board)

      return(ans)
