#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'largestMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def largestMatrix(arr):
    # Write your code here
    R = len(arr) # no. of rows in M[][]
    C = len(arr[0]) # no. of columns in M[][]
 
    S = [[0 for k in range(C+1)] for l in range(R+1)]
    # here we have set the first row and column of S[][]
 
    # Construct other entries
    for i in range(1, R+1):
        for j in range(1, C+1):
            if (arr[i-1][j-1] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                            S[i-1][j-1]) + 1
            else:
                S[i][j] = 0
     
    # Find the maximum entry and
    # indices of maximum entry in S[][]
    max_of_s = S[0][0]
    
    for i in range(R+1):
        for j in range(C+1):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                
    return max_of_s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_rows = int(input().strip())
    arr_columns = int(input().strip())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    result = largestMatrix(arr)

    fptr.write(str(result) + '\n')

    fptr.close()