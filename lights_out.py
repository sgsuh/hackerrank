"""
Lights Out is a game of cellular automaton where a cell and all its defined neighbors changes states on firing it.
In this version of Lights Out, 2 players compete against each other by firing the cells on an 8x8 grid. Each cell has 2 states.

    ON indicated by the number 1
    OFF indicated by the number 0

A cell at (r,c) on firing changes its state and 2 of its neighbors, the one towards its right (r,c+1) and the one below (r+1,c).

You are allowed only to fire at cells that are ON.

Input Format

Top left cell of the grid is indexed as (0,0) and the bottom right of the grid is indexed at (7,7). The 1st player is represented by the number 1 and the 2nd player is represented by the number 2.

The first line of input contains the number of the current player.
8 lines follow, each line containing 8 integers without any space between them. Each integer can be either 0 or 1 representing the 2 states of the cell.

Output Format

You are required to output two single spaced integers that is the position of the cell you wish to fire.

Sample Input

1
01101100
01010101
10111100
00001111
10101010
00000001
11100011
00101000

Sample Output

0 1

The output results in the following grid configuration.

00001100
00010101
10111100
00001111
10101010
00000001
11100011
00101000

The cells (0,1) and (0,2) and (1,1) all change their states from ON to OFF.

Game Play

A random generated grid is given as the initial input. First player goes first. The first player able to get all the cells' state to OFF wins. If no player wins for the first 100 moves, then the game is considered a DRAW. 
"""

def solution(grid):

    for i in range(8):
        for j in range(8):
            if grid[i][j] == '1':
                print(i, j)

                return 0

    return 0

n = 1

grid = ['01101100',
        '01010101',
        '10111100',
        '00001111',
        '10101010',
        '00000001',
        '11100011',
        '00101000']


# n = int(input())

# grid = []
# for i in range(0, 8):
#     grid.append(input())

grid = solution(grid)
