import random
import sys
import math
import time

sys.path.append('..')  # i know this is a dirty hack but, you know, time...
from board import *


class Node(object):
    def __init__(self, board, move, color, cost = None):
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
    
    def get_child_with_value(self, value):
        cs = self.get_children()
        if len(cs) == 0:
            return None
        for c in cs:
            if c.get_cost() == value:
                return c 
        return None
        
    def get_color(self):
        return self.color

    def add_child(self, new_child):
        self.children.append(new_child)


# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

def game_stage(board):
    piece_count = sum([1 for piece in str(board) if piece != '.'])
    if piece_count <= 20:
        return 0 #early game
    if piece_count <= 40:
        return 1 #mid game
    return 2     #late game


def disk_square_table(x,y):
    return 14 - min(x+y, 7 - x+y, x + 7 - y, 7-x + 7-y)


def mobility_strategy(state_node, is_min):
    board = state_node.get_board()

    self_moves = len(board.legal_moves(state_node.get_color()))
    opp_moves = len(board.legal_moves(board.opponent(state_node.get_color())))
    if self_moves == 0:
        return 50 if is_min else -50
    if opp_moves == 0:
        return -50 if is_min else 50

    ratio = self_moves/opp_moves
    return 1/ratio if is_min else ratio


def most_pieces_strategy(state_node, is_min):
    num_self  = sum([1 for piece in str(state_node.get_board()) if piece==state_node.get_color()])
    num_other = sum([1 for piece in str(state_node.get_board()) if piece==state_node.get_board().opponent(state_node.get_color())])
    if num_self  == 0 :
        return math.inf if is_min else -math.inf
    if num_other == 0:
        return  -math.inf if is_min else math.inf
    else:
        return num_other/num_self if is_min else num_self/num_other


def evaluate_terminal_state(state_node, is_min):
    num_self  = sum([1 for piece in str(state_node.get_board()) if piece==state_node.get_color()])
    num_other = sum([1 for piece in str(state_node.get_board()) if piece==state_node.get_board().opponent(state_node.get_color())])
    if num_self > num_other:
        return -math.inf if is_min else  math.inf
    if num_self < num_other:
        return  math.inf if is_min else -math.inf
    else:
        return 0


def utility(state_node, p_color, is_min):
    if state_node.get_board().is_terminal_state():
        evaluate_terminal_state(state_node, is_min)

    stage = game_stage(state_node.get_board())
    
    if stage == 0:
        return most_pieces_strategy(state_node, is_min)
    if stage == 1:
        return mobility_strategy(state_node, is_min)
    if stage == 2:
        return most_pieces_strategy(state_node, is_min)    


def max_value(state_node, alpha, beta, depth, start_time):
    board = state_node.get_board()
    color = state_node.get_color()

    current_time = time.time()

    if board.is_terminal_state() or depth == 0 or (current_time - start_time) > 4.9:
        u = utility(state_node, color, False)
        state_node.set_cost(u)
        return u

    v = -math.inf
    for s in board.legal_moves(color):
        #print (s)
        new_board = from_string(str(board))
        new_board.process_move(s, color)
        child = Node(new_board, s, board.opponent(color))
        state_node.add_child(child)
        v = max(v, min_value(child, alpha, beta, depth-1, start_time))
        alpha = max(alpha, v)
        #print (v)
        if alpha >= beta:
            break

    state_node.set_cost(v)
    return v


def min_value(state_node, alpha, beta, depth, start_time):
    board = state_node.get_board()
    color = state_node.get_color()

    current_time = time.time()

    if board.is_terminal_state() or depth==0 or (current_time - start_time) > 4.9:
        u = utility(state_node, color, True)
        state_node.set_cost(u)
        return u

    v = math.inf

    for s in board.legal_moves(color):
        new_board = from_string(str(board))
        new_board.process_move(s, color)
        child = Node(new_board, s, board.opponent(color))
        state_node.add_child(child)
        v = min(v, max_value(child, alpha, beta, depth-1, start_time))
        beta = min(beta, v)
        if beta >= alpha:
            break

    state_node.set_cost(v)
    return v


def make_move(the_board, color):
    """
    Returns an Othello move
    :param the_board: a board.Board object with the current game state
    :param color: a character indicating the color to make the move ('B' or 'W')
    :return: (int, int) tuple with x, y indexes of the move (remember: 0 is the first row/column)
    """
    root = Node(the_board, None, color)
    value = max_value(root, -math.inf, math.inf, 5, time.time())
    child = root.get_child_with_value(value)
    if child is None:
        return (-1,-1)
    else:
        return child.get_move()


