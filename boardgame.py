class player :
     "the player class has the player's operations"
     def __init__(self, startX, startY, endX, endY):
          self.startX = 0
          self.startY = 0
          self.endX = 0
          self.endY = 0
class chessboard :
     def __init__(self, board):
          self.board = [['#','#','#','.','.','#','#','#'],
                        ['#','#','.','.','.','.','#','#'],
                        ['#','.','.','.','.','.','.','#'],
                        ['.','.','.','.','.','.','.','.'],
                        ['.','.','O','O','O','O','.','.'],
                        ['.','.','.','O','O','.','.','.'],
                        ['.','.','.','.','.','.','.','.'],
                        ['.','.','.','.','.','.','.','.'],
                        ['.','.','.','X','X','.','.','.'],
                        ['.','.','X','X','X','X','.','.'],
                        ['.','.','.','.','.','.','.','.'],
                        ['#','.','.','.','.','.','.','#'],
                        ['#','#','.','.','.','.','#','#'],
                        ['#','#','#','.','.','#','#','#']]
     def win(self,board):
          if(self.board[0][0] == 'X' and self.board[0][1] == 'X') : return true
          if(self.board[11][3] == 'O' and self.board[11][4] == 'O') : return true
          countO = 0, countX = 0
          for(v : board):
               for(i : v) :
                    if(i == 'O') : countO++
                    else if(i == 'X') : countX++
          if(countO == O and countX >= 2) : return true
          if(countX == O and countO >= 2) : return true
          return false
     def plainMove(self, player) :
          startX = player.startX
          startY = player.startY
          endX = player.endX
          endY = payer.endY
          if(board[startY][startX] == '.') :
               print("Invaid move")
               return false
          if(board[endY][endX] == 'O' or board[endY][endX] == 'X') :
               print("Invaid move")
               return false
          if(board[player.startX][player.startY] == 'O') :
               if(abs(endX - startX) > 1) :
                    print("Invaid move")
                    return false
               if(abs(endY - startY) > 1) :
                    print("Invaid move")
                    return falae
               board[endY][endX] = 'O'
               board[startY][startX] = '.'
               if(win(board)):
                    return "Win the game"
               return true
          else if(board[player.startY][player.startX] == 'X') :
               if(abs(endX - startX) > 1) :
                    print("Invaid move")
                    return false
               if(abs(endY - startY) > 1) :
                    print("Invaid move")
                    return false
                board[endY][endX] = 'X'
                board[startX][startY] = '.'
                if(win(board)):
                        return "Win the game"
               return false
     def canteringMove(self, player) :
          startX = player.startX
          startY = player.startY
          endX = player.endX
          endY = payer.endY
          if(board[startY][tartX] == '.') :
               print("Invaid move")
               return false
          if(board[endY][endX] == 'O' or board[endY][endX] == 'X') :
               print("Invaid move")
               return false
          value = board[startY][startX]
          if(endY - startY == 0) :
               v = range(startX, endX)
               for(x in v) :
                    if(board[startY][x] != board[startY][startX]) :
                         return false
               board[endY][endX] = board[startY][startX]
               board[startY][startX] = '.'
                if(win(board)):
                    return "Win the game"
               return true
          else if(endX - startX == 0) :
               v = range(startY, endY)
               for(y in v) :
                    if(board[y][startX] != board[startY][startX]) :
                         return false
               board[endY][endX] = board[startY][startX]
               board[startY][startX] = '.'
                   if(win(board)) :
                        return "Win the game"
               return true
          else if(abs(startX - endX) == as(startY - endY)) :
               v = range(abs(endX - startX))
               for(i in v) :
                    if(board[startY+i][startX+i] != board[startY][startX]) :
                         return false
                    board[endX][endX] = board[startY][startX]
                    board[startY][startX] = '.'
                    if(win(board)):
                         return "Win the game"
                    return true
     def capturingMove(self, player) :
          startX = player.startX
          startY = player.startY
          endX = player.endX
          endY = payer.endY
          if(board[startY][startX] == '.') :
               print("Invaid move")
               return false
          if(board[endY][endX] != '.') :
               print("Invaid move")
               return false
          if(abs(endY - startY) == 2 and endX == startX) :
               mid = (endY + startY)/2
               if(board[startY][startX] == 'O' and board[mid][endX] == 'X') :
                    board[endY]endY] = 'O'
                    board[startY][startX] == '.'
                    return true
               if(board[startY][startX] == 'X' and board[mid][endX] == 'O') :
                    board[endY]endY] = 'X'
                    board[startY][startX] == '.'
                    return true
          if(abs(endX - startX) == 2 and endY == startY) :
               mid = (endX + startX)/2
               if(board[startY][startX] == 'O' and board[endY][mid] == 'X') :
                    board[endY]endY] = 'O'
                    board[startY][startX] == '.'
                    if(win(board)):
                         return "Win the game"
                    return true
               if(board[startY][startX] == 'X' and board[mid][endX] == 'O') :
                    board[endY]endY] = 'X'
                    board[startY][startX] == '.'
                    if(win(board)):
                         return "Win the game"
                    return true
          if(abs(endY - startY) == 2 and abs(endX - startX) == 2) :
               midY = (endY + startY)/2
               midX = (endX + startX)/2
               if(board[startY][startX] == 'O' and board[midY][midX] == 'X') :
                    board[endY]endY] = 'O'
                    board[startY][startX] == '.'
                    if(win(board)):
                         return "Win the game"
                    return true
               if(board[startY][startX] == 'X' and board[midY][midX] == 'O') :
                    board[endY]endY] = 'X'
                    board[startY][startX] == '.'
                    if(win(board)):
                         return "Win the game"
                    return true
          return false
          
