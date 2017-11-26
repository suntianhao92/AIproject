from boardgame import *
class Game:
    def __init__(self):
        self.m_chessBoard = ChessBoard()
        self.m_playerChess = self.m_chessBoard.m_player1.m_chesses
        self.m_aiChess = self.m_chessBoard.m_player2.m_chesses
    def end(self):
        return self.m_chessBoard.win()
    def printChessTable(self):
        print (self.m_chessBoard)
    def printPlayerChess(self):
        print (self.m_chessBoard.m_player1)
    def movePlayerChess(self, chessPrev, chessAft):
        self.m_chessBoard.moveChess(self.m_chessBoard.m_player1, self.m_aiChess, chessPrev, chessAft)
    def setMaxSteps(self, s):
        self.m_chessBoard.setMaxSteps(s)
    def moveAIChess(self):
        print ("AI moving")
        [_, chess, chessAft] = self.m_chessBoard.oneStep(self.m_aiChess, self.m_playerChess, 1)
        print "moving " + str(chess) + ", to" + str(chessAft)
        self.m_chessBoard.moveChess(self.m_chessBoard.m_player2, self.m_playerChess, chess, chessAft)
#
#def avgO(chessboard) :
#     board = chessboard.board
#     dis = 0, count = 0
#     for(y in len(board)) :
#         for(x in len(board[y])) :
#               if(board[y][x] == 'O') :
#                    count++
#                    dis += abs(11 - y) + abs(3-x)
#     return float(dis/count)
#
#def avgX(chessboard) :
#     board = chessboard.board
#     dis = 0, count = 0
#     for(y in len(board)) :
#         for(x in len(board[y])) :
#               if(board[y][x] == 'X') :
#                    count++
#                    dis += abs(11 - y) + abs(3-x)
#     return float(dis/count)
#
if __name__ == '__main__':
    g = Game()
    board = g.m_chessBoard
    playerChess= board.m_player1.m_chesses
    oppoChess = board.m_player2.m_chesses
    steps = 0
    while not g.end():
        if  steps % 2 == 0:
            g.printChessTable()
            g.printPlayerChess()
            x = input("Enter x pos of your chess: ")
            y = input("Enter x pos of your chess: ")
            delta_x = input("Enter delta_x direction of your chess: ")
            delta_y = input("Enter delta_y direction of your chess: ")
            if not board.move(Chess(x,y), [delta_x, delta_y], playerChess, oppoChess) == board.Status.INVALID:
                g.movePlayerChess(Chess(x,y), Chess(x+delta_x, y+delta_y))
            else:
                print ("Invalid move")
        else:
            g.moveAIChess()
        steps += 1
