import random
import sys
import math

# from board import Board

sys.path.insert(0, '../')
from board import *

class Node(object):
    def __init__(self, board, move, color, cost = 0):
        self.board = board
        self.move = move
        self.color = color
        self.cost = cost
        self.children = []
    
    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def get_move(self):
        return self.move
    
    def get_board(self):
        return self.board

    def get_children(self):
        return self.children

    def get_color(self):
        return self.color

    def add_child(self, new_child):
        self.children.append(new_child)


# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

def disk_square_table(x,y):
    min(x+y, 7 - x+y, x + 7 - y, 7-x + 7-y)

def utility(state_node, p_color):
    acum = 0
    for j in range(8):
        for i in range(8):
            p = str(state_node.get_board())[8*j+i]
            if p_color == p:
                acum += disk_square_table(i,j)
            elif p_color == state_node.get_board().opponent(p):
                acum -= disk_square_table(i,j)
    return acum

def max_value(state_node, alpha, beta):
    board = state_node.get_board()
    
    if board.is_terminal_state():
        return utility(state_node)

    v = -math.inf

    for s in board.legal_moves(state_node.get_color()):
        child = Node(from_string(str(board)).process_move(s), s, board.opponent(state_node.get_color()))
 
        v = max(v, min_value(child, alpha, beta))
        alpha = max(alpha, v)
        if alpha >= beta:
            break

    state_node.set_cost(v)
    return v


def min_value(state_node, color, alpha, beta):
    if state_node.get_board().is_terminal_state():
        return utility(state_node)
        
    v = math.inf
    for s in state_node.get_board().legal_moves(color):
        c = from_string(str(state_node.get_board())).process_move(s)
        v = min(v, max_value(c, alpha, beta))
        beta = min(beta, v)
        if beta >= alpha:
            break
    return v

def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta



    return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])

