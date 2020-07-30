# pip3 install python-chess


import chess
import chess.svg
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame


import sys

g2g4
player1 = HumanPlayer()
player2 = MinimaxAI(8)

game = ChessGame(player1, player2)

while not game.is_game_over():
    # chess.svg.piece(chess.Piece.from_symbol("R"))
    # board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")
    # squares = board.attacks(chess.E4)
    # chess.svg.board(board=board, squares=squares)
    print(game)
    game.make_move()


#print(hash(str(game.board)))
