"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    return X if x_count == o_count else O

    


def actions(board):
    possible_move = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_move.append((i,j))
    return possible_move


def result(board, action):
    
    if action not in actions(board):
        raise Exception("Invalid actions")
    
    new_board = copy.deepcopy(board)
    current_player = player(board)

    i,j = action
    new_board[i][j] = current_player

    return new_board




def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
     
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    if winner(board) is not None:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    win = winner(board)

    if win == X:
        return 1
    if win == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X wants to maximize
        value, move = max_value(board)
    else:
        # O wants to minimize
        value, move = min_value(board)
    
    return move

def max_value(board):

    if terminal(board):
        return utility(board), None
    
    v = float('-inf')
    best_action = None
    
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
    
    return v, best_action

def min_value(board):

    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    best_action = None
    
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
    
    return v, best_action

