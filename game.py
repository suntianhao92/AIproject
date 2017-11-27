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

if __name__ == '__main__':
    g = Game()
    board = g.m_chessBoard
    playerChess= board.m_player1.m_chesses
    oppoChess = board.m_player2.m_chesses
    steps = 0
    win = GraphWin('Game', 400, 700)
    while not g.end():
        win.autoflush = False
        g.m_chessBoard.displayBoard(win)
        g.m_chessBoard.displayChess(win)
        win.flush()
        win.autoflush = True
        if  steps % 2 == 0:
            g.printChessTable()
            g.printPlayerChess()
            [i, j] = g.m_chessBoard.position2Index(win.getMouse())
            preChess = Chess(j, i)
            g.m_chessBoard.highlightChess(win, preChess) 
            [i, j] = g.m_chessBoard.position2Index(win.getMouse())
            aftChess = Chess(j, i)
            #x = input("Enter x pos of your chess: ")
            #y = input("Enter x pos of your chess: ")
            #delta_x = input("Enter delta_x direction of your chess: ")
            #delta_y = input("Enter delta_y direction of your chess: ")
            [delta_x, delta_y] = g.m_chessBoard.chessDirection(preChess, aftChess)
            if not board.move(preChess, [delta_x, delta_y], playerChess, oppoChess) == board.Status.INVALID:
                g.movePlayerChess(preChess, aftChess)
            else:
                print ("Invalid move")
        else:
            g.moveAIChess()
        steps += 1
