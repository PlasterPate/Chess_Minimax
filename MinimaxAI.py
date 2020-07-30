import chess
import random
from time import sleep

PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

PAWN_SCORE = 100
KNIGHT_SCORE = 300
BISHOP_SCORE = 300
ROOK_SCORE = 500
QUEEN_SCORE = 1000
KING_SCORE = 400

OPPONENT = False
MINE = True

INF = float("inf")

class MinimaxAI():
    def __init__(self, depth):
        self.depth = depth

    def choose_move(self, board):
        moves = list(board.legal_moves)
        minimaxScores = []
        print(PAWN_TABLE)
        xxx = board.pieces(PAWN, MINE)
        print(list(xxx))
        print(self.psScore(board, PAWN_TABLE, PAWN, OPPONENT))
        for m in moves:
            board.push(m)
            score = self.minimax(board, 1, INF, -INF)
            board.pop()
            minimaxScores.append((score, m))
            # print(str(m) + " : " + str(score))
        bestAction = min(minimaxScores, key=lambda x: x[0])[1]

        # print(self.evalFunc(board))
        return bestAction

    def minimax(self, board, depth, alpha, beta):
        if self.depth == depth or board.is_game_over():
            value = self.evalFunc(board) + self.psEval(board)
            # print(value)
            return value
        moves = list(board.legal_moves)
        if depth % 2 == 0:
            bestVal = INF
            for m in moves:
                board.push(m)
                value = self.minimax(board, depth + 1, alpha, beta)
                # scores.append(value)
                bestVal = min(bestVal, value)
                beta = min(beta, bestVal)
                board.pop()
                if beta <= alpha:
                    break
            return bestVal
        else:
            bestVal = -INF
            for m in moves:
                board.push(m)
                value = self.minimax(board, depth + 1, alpha, beta)
                # scores.append(value)
                bestVal = max(bestVal, value)
                alpha = max(alpha, bestVal)
                board.pop()
                if beta <= alpha:
                    break
            return bestVal

    def evalFunc(self, board):
        pawnScore = self.calculateScore(board, PAWN_SCORE, PAWN)
        knightScore = self.calculateScore(board, KNIGHT_SCORE, KNIGHT)
        bishopScore = self.calculateScore(board, BISHOP_SCORE, BISHOP)
        rookScore = self.calculateScore(board, ROOK_SCORE, ROOK)
        queenScore = self.calculateScore(board, QUEEN_SCORE, QUEEN)

        return pawnScore + knightScore + bishopScore + rookScore + queenScore

    def pieceCount(self, board, piece, side):
        return len(list(board.pieces(piece, side)))

    def calculateScore(self, board, pieceScore, pieceType):
        return pieceScore * (self.pieceCount(board, pieceType, MINE) - self.pieceCount(board, pieceType, OPPONENT))

    def psScore(self, board, pTable, pType, side):
        pieces = list(board.pieces(pType, side))
        if side:
            pTable.reverse()
            s = sum([pTable[x] for x in pieces])
            pTable.reverse()
        else:
            s = sum([pTable[x] for x in pieces])
        return s

    def psEval(self, board):
        p = self.psScore(board, PAWN_TABLE, PAWN, OPPONENT)
        k = self.psScore(board, KNIGHT_TABLE, KNIGHT, OPPONENT)
        b = self.psScore(board, BISHOP_TABLE, BISHOP, OPPONENT)
        r = self.psScore(board, ROOK_TABLE, ROOK, OPPONENT)
        q = self.psScore(board, QUEEN_TABLE, QUEEN, OPPONENT)
        king = self.psScore(board, KING_TABLE, KING, OPPONENT)
        return p + k + b + r + q + king


PAWN_TABLE = [0,  0,  0,  0,  0,  0,  0,  0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0]


KNIGHT_TABLE = [-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50]

BISHOP_TABLE = [-20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-10,-10,-10,-10,-10,-20]

ROOK_TABLE = [0,  0,  0,  0,  0,  0,  0,  0,
  5, 10, 10, 10, 10, 10, 10,  5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  0,  0,  0,  5,  5,  0,  0,  0]

QUEEN_TABLE = [-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
 -5,  0,  5,  5,  5,  5,  0, -5,
  0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20]

KING_TABLE = [-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20]

