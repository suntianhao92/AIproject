from boardgame import chessboard
from boardgame import player
def nextmove(chessboard) :
     board = chessboard.board
     for(y1 in len(board)):
          for(x1 in len(board[y]) :
              if(board[y1][x1] == 'O') :
                    for(y2 : len(board)) :
                         for(x2 : len(board[y2]) :
                              player1 = player(y1,x1,y2,x2)
                              if(chessboard.capturingmove(player) == "Win the game" or
                                   chessboard.canteringmove(player) == "Win the game" or
                                   chessboard.plainmove(player) == "Win the game"):
                                   return
                              else if(chessboard.capturingmove(player)) :
                                      
                         
                                                                  
                                   
                                 

def avgO(chessboard) :
     board = chessboard.board
     dis = 0, count = 0
     for(y in len(board)) :
         for(x in len(board[y])) :
               if(board[y][x] == 'O') :
                    count++
                    dis += abs(11 - y) + abs(3-x)
     return float(dis/count)
def avgX(chessboard) :
     board = chessboard.board
     dis = 0, count = 0
     for(y in len(board)) :
         for(x in len(board[y])) :
               if(board[y][x] == 'X') :
                    count++
                    dis += abs(11 - y) + abs(3-x)
     return float(dis/count)

                    
