import random
import sys
import math
from queue import Queue

sys.path.insert(0, '../')
from board import *

class Node(object):
    def __init__(self, board, move, color, cost = None):
        self.board = board
        self.move = move
        self.color = color
        self.cost = cost
        self.children = Queue()
    
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
        if cs.qsize() == 0:
            return
        for c in range(cs.qsize()):
            child = cs.get(c)
            if child.get_cost() == value:
                return child 
        
    def get_color(self):
        return self.color

    def add_child(self, new_child):
        self.children.put(new_child)


# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

def disk_square_table(x,y):
    return min(x+y, 7 - x+y, x + 7 - y, 7-x + 7-y)

def utility(state_node, p_color):
    acum = 0
    if state_node.get_board().is_terminal_state():
        num_self  = sum([1 for piece in str(state_node.get_board()) if piece==p_color])
        num_other = sum([1 for piece in str(state_node.get_board()) if piece==state_node.get_board().opponent(p_color)])
        if num_self > num_other:
            return math.inf
        if num_self < num_other:
            return -math.inf
        else:
            return 0

    for j in range(8):
        for i in range(8):
            p = str(state_node.get_board())[8*j+i]
            if p_color == p:
                acum += disk_square_table(i,j)
            elif state_node.get_board().opponent(p_color) == p:
                acum -= disk_square_table(i,j)
    return acum

def max_value(state_node, alpha, beta, depth):
    board = state_node.get_board()
    color = state_node.get_color()

    if board.is_terminal_state() or depth==0:
        return utility(state_node, color)

    v = -math.inf
    for s in board.legal_moves(color):
        new_board = from_string(str(board))
        new_board.process_move(s, color)
        child = Node(new_board, s, board.opponent(color))
        state_node.add_child(child)
        v = max(v, min_value(child, alpha, beta, depth-1))
        alpha = max(alpha, v)
        if alpha >= beta:
            break

    state_node.set_cost(v)
    print(id(state_node))
    return v


def min_value(state_node, alpha, beta, depth):
    board = state_node.get_board()
    color = state_node.get_color()

    if board.is_terminal_state() or depth==0:
        return utility(state_node, color)

    v = math.inf

    for s in board.legal_moves(color):
        new_board = from_string(str(board))
        new_board.process_move(s, color)
        child = Node(new_board, s, board.opponent(color))
        state_node.add_child(child)
        v = min(v, max_value(child, alpha, beta, depth-1))
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
    print(id(root))
    value = max_value(root, -math.inf, math.inf, 2)
    # print(len(root.get_children()))
    move = root.get_child_with_value(value).get_move()
    # print(move)
    return move

