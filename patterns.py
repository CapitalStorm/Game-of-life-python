#here we can create all the required patterns

import numpy as np

def insert_pattern(board, pattern, i,j):
    shape = np.shape(board)
    a = shape[0]
    b = shape[1]
    h = np.shape(pattern)[0]
    w = np.shape(pattern)[1]
    if i+h <= a and j+w <= b:
        #place pattern
        for x in range(h):
            for y in range(w):
                board[x+i,y+j] = pattern[x,y]
    else:
        raise ValueError
    return board

def rotate_once(pattern):
    shape = np.shape(pattern)
    new_pattern = np.zeros((shape[1],shape[0]))
    #once clockwise turn
    for i in range(shape[0]):
        for j in range(shape[1]):
            new_pattern[j,shape[0]-i-1] = pattern[i,j]
    return new_pattern
    
def rotate_pattern(pattern, turn:int):
    #this function rotates a pattern by specified turns clockwise
    actual = turn % 4
    if actual == 1:
        return rotate_once(pattern)
    elif actual == 0:
        return pattern
    else:
        return rotate_pattern(rotate_once(pattern),actual-1)

glider = np.array([
    [0,1,0],
    [0,0,1],
    [1,1,1]
])

lwss = np.array([
    [0,1,1,1,1],
    [1,0,0,0,1],
    [0,0,0,0,1],
    [1,0,0,1,0]
])

blinker = np.array([
    [1],
    [1],
    [1]
])

toad = np.array([
    [0,0,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,0,0]
])

block = np.array([
    [1,1],
    [1,1]
])

beehive = np.array([
    [0,1,1,0],
    [1,0,0,1],
    [0,1,1,0]
])

