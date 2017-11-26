from enum import Enum
from copy import copy, deepcopy
import unittest
import sys

class Chess:
    """initial for chess"""
    def __init__(self, x = 0, y = 0):
        self.m_x = x
        self.m_y = y
    def __str__(self):
        ss = "pos_x:" + str(self.m_x) + ", pos_y:" + str(self.m_y)
        return ss
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.m_x == self.m_x and other.m_y == self.m_y
        return False
    def set(self, x, y):
        self.m_x = x
        self.m_y = y

class Player :
    """the player class has the player's operations"""
    def __init__(self, name, startPositions):
        self.m_chesses = []
        self.m_name = name
        for pos in startPositions:
            self.m_chesses.append(Chess(pos[0], pos[1]))

    def __str__(self):
        ss = "Player:" + self.m_name + ", Chesses:"
        for chess in self.m_chesses:
            ss += str(chess)
        return ss

    def size(self):
        return len(self.m_chesses)

    def setChess(self, positions):
        self.m_chesses = []
        for pos in positions:
            self.m_chesses.append(Chess(pos[0], pos[1]))

    def moveChess(self, chessPrev, chessAfter):
        self.m_chesses.remove(chessPrev)
        self.m_chesses.append(chessAfter)

class ChessBoard :
    class Status(Enum):
        INVALID = 0
        PLAIN = 1
        CANTER = 2
        CAPTURE = 3
        WIN = 4

    def __init__(self):
        self.m_rows = 14
        self.m_cols = 8
        self.MAX_STEPS = 3
        self.m_initBoard = [['#','#','#','.','.','#','#','#'],
                ['#','#','.','*','*','.','#','#'],
                ['#','.','.','.','.','.','.','#'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['#','.','.','.','.','.','.','#'],
                ['#','#','.','*','*','.','#','#'],
                ['#','#','#','.','.','#','#','#']]
        self.m_player1 = Player("player", [[4,2],[4,3],[4,4],[4,5],[5,3],[5,4]])
        self.m_player2 = Player("computer", [[9,2],[9,3],[9,4],[9,5],[8,3],[8,4]])
        self.m_curBoard = [] 

    """set max steps, eq to set level of AI"""
    def setMaxSteps(self, l):
        self.MAX_STEPS = l

    """apply player chesses on board"""
    def applyPlayer(self):
        self.m_curBoard = deepcopy(self.m_initBoard)
        for chess in self.m_player1.m_chesses:
            self.m_curBoard[chess.m_x][chess.m_y] = 'O'
        for chess in self.m_player2.m_chesses:
            self.m_curBoard[chess.m_x][chess.m_y] = 'X'

    """print chessboard"""
    def __str__(self):
        self.applyPlayer()
        str = ""
        for row in self.m_curBoard:
            str += ", ".join(row)
            str += "\n"
        return str

    """return true when there is a winner"""
    def win(self):
        self.applyPlayer()
        if(self.m_curBoard[0][0] == 'X' and self.m_curBoard[0][1] == 'X') : 
            return true
        if(self.m_curBoard[11][3] == 'O' and self.m_curBoard[11][4] == 'O') : 
            return true
        return self.m_player1.size() <= 2 or self.m_player2.size() <= 2

    """return score of current step"""
    def getScore(self, chess, d, status):
        return 0

    """iterate all possible next move, return max score of current step"""
    def oneStep(self, myChess, oppoChess, curStep):
        maxScore = - (sys.maxint - 1)
        maxChessPrev = Chess()
        maxChessAft = Chess() 
        if curStep == self.MAX_STEPS:
            return 0, maxChessPrev, maxChessAft 
        directions = [[-1,-1], [-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]
        # iterate all chess
        for chess in myChess:
            # iterate all directions
            for d in directions:
                nx_status = self.move(chess, d, myChess, oppoChess)
                # move chess
                nx_chess = Chess(chess.m_x + d[0]*1, chess.m_y + d[1]*1)
                nx_score = 0
                remove_oppo = False
                if (nx_status == self.Status.INVALID):
                    continue
                elif (nx_status == self.Status.CAPTURE):
                    remove_oppo = True
                    nx_chess = Chess(chess.m_x + d[0]*2, chess.m_y + d[1]*2)
                    nx_score = 200
                elif (nx_status == self.Status.CANTER):
                    nx_chess = Chess(chess.m_x + d[0]*2, chess.m_y + d[1]*2)

                myChess.remove(chess)
                myChess.append(nx_chess)
                if remove_oppo:
                    oppoChess.remove(Chess(chess.m_x + d[0], chess.m_y + d[1]))
                # get score
                if self.win():
                    nx_score += 300
                [mx_nx_score, _, _] = self.oneStep(oppoChess, myChess, curStep + 1)
                nx_score -= mx_nx_score 
                if nx_score > maxScore:
                    maxScore = nx_score
                    maxChessPrev = chess
                    maxChessAft = nx_chess

                # reverse move
                myChess.remove(nx_chess)
                myChess.append(chess)
                if remove_oppo:
                    oppoChess.append(Chess(chess.m_x + d[0], chess.m_y + d[1]))
        return maxScore, maxChessPrev, maxChessAft
            
    """return status of current move"""
    def move(self, chess, nxD, myChess, oppoChess):
        # as long as two steps 
        status = self.Status.PLAIN
        nx_x = chess.m_x + nxD[0]
        nx_y = chess.m_y + nxD[1]
        nx_chess = Chess(nx_x, nx_y)
        if (nx_chess in myChess):
            nx_x += nxD[0]
            nx_y += nxD[1]
            status = self.Status.CANTER
        elif (nx_chess in oppoChess):
            nx_x += nxD[0]
            nx_y += nxD[1]
            status = self.Status.CAPTURE
        if not self.isValid(nx_x, nx_y):
            status = self.Status.INVALID
        return status

    """move chess"""
    def moveChess(self, player, oppoChess, chessPrev, chessAft):
        if abs(chessAft.m_x - chessPrev.m_x) >= 2 or abs(chessAft.m_y - chessPrev.m_y) >= 2:
            # if oppo chess should be removed
            chess = Chess((chessPrev.m_x+chessAft.m_x)/2, (chessPrev.m_y+chessAft.m_y)/2)
            if chess in oppoChess:
                oppoChess.remove(chess)
        player.moveChess(chessPrev, chessAft)

    """return true if is at valid position"""
    def isValid(self, pos_x, pos_y):
        if (pos_x< 0 or pos_x >= self.m_rows) or (pos_y < 0 or pos_y >= self.m_cols):
            return False
        return self.m_initBoard[pos_x][pos_y] in ['.', '*'] 


class TestPlayerMethods(unittest.TestCase):
    def test_print(self):
        p = Player("test_player", [[0,1]])
        self.assertEqual(0, p.m_chesses[0].m_x)
        self.assertEqual(1, p.m_chesses[0].m_y)
        self.assertEqual(1, p.size())

class TestChessBoardMethods(unittest.TestCase):
    def test_print(self):
        b = ChessBoard()

    def test_win(self):
        b = ChessBoard()
        self.assertFalse(b.win())
        b.m_player1.setChess([[8,3], [8,4], [9,1]])
        self.assertFalse(b.win())
        b.m_player1.setChess([[8,3], [8,4]])
        self.assertTrue(b.win())
        b.m_player1.setChess([[8,3]])
        self.assertTrue(b.win())

    def test_ai(self):
        b = ChessBoard()
        playerChess = b.m_player1.m_chesses
        oppoChess = b.m_player2.m_chesses
        b.oneStep(playerChess, oppoChess, 1)

    def test_move(self):
        b = ChessBoard()
        playerChess = b.m_player1.m_chesses
        oppoChess = b.m_player2.m_chesses
        chess = b.m_player1.m_chesses[0]
        # plain move
        self.assertEqual(b.Status.PLAIN, b.move(chess, [0,-1], playerChess, oppoChess))
        # invalid move
        chess.set(4,0)
        self.assertEqual(b.Status.INVALID, b.move(chess, [0,-1], playerChess, oppoChess))
        chess.set(3,0)
        self.assertEqual(b.Status.INVALID, b.move(chess, [-1,0], playerChess, oppoChess))
        # canter move
        chess.set(3,4)
        self.assertEqual(b.Status.CANTER, b.move(chess, [1,1], playerChess, oppoChess))
        # capture move
        chess.set(8,1)
        self.assertEqual(b.Status.CAPTURE, b.move(chess, [1,1], playerChess, oppoChess))

if __name__ == '__main__':
        unittest.main()
