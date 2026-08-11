import numpy as np
import time
import os
import subprocess
from patterns import insert_pattern as ip
from patterns import glider, lwss, blinker, beehive

def create_board(shape):
    #creates a board of size (a,b)
    board = np.zeros(shape,int)
    return board

def display_board(board):
    for row in board:
        disp = ''
        for cell in row:
            if cell==0:
                disp += '_ '
            else:
                disp += '# '
        print(disp)
    return

def count_neighbors(board,i,j):
    #Takes a board function with all the weights and returns the number of nearest neighbours for a_ij
    shape = np.shape(board) #this returns (a,b)
    a = shape[0]
    b = shape[1]
    value = 0
    for x in [i-1,i,i+1]:
    #x is contained within (0,a) by this condition
        if x>=0 and x<a:
            for y in [j-1,j,j+1]:
                #y is contained within (0,b)
                if y>=0 and y<b:
                        #since board values are 0 and 1, the board cell value can add to the neigbor count
                        value += board[x,y]
    return value

def game_rule(state:int,n:int):
    #this function takes in the value of a cell, state, and neighbors, n, and returns the new state
    value = 0
    if state==1:
        if n<2:
            value=0
        elif n==2 or n==3:
            value=1
        elif n>3 and n<9:
            value=0
        else:
            print('Neigbour value exceeds 8. Error')
    elif state==0:
        if n==3:
            value=1
        else:
            value=0
    else:
        print('Value Error for cell')
    
    return value

def update_board(board):
    #this function takes in the value of current cell and applies rules to it and updates its state returning the new board.
    shape = np.shape(board) 
    newboard = create_board(shape) #zero board for next state
    for i in range(shape[0]):
        for j in range(shape[1]):
            old_state = board[i,j]
            #if the cell is alive N will be reduced by a number since it has been counted in nearest neighbor algo
            N = count_neighbors(board,i,j) - old_state
            #apply rule
            newboard[i,j] = game_rule(old_state,N)
    return newboard

#start
#initialize a random board
#blinker board generation 1
board = create_board((30,30))
ip(board,glider,3,5)
ip(board,blinker,20,24)
ip(board,beehive,25,13)
ip(board,lwss,15,2)
display_board(board)
time.sleep(1)
subprocess.run('cls', shell=True)
#gen 2 and later

for gen in range(100):
    print(f"Generation {gen}")
    display_board(board)
    board = update_board(board)
    time.sleep(0.2)
    subprocess.run('cls', shell=True)



