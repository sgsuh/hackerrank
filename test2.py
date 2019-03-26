#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'betterCompression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def betterCompression(s):
    # Write your code here

    array = []

    temp = ''

    temp += s[0]

    for i in range(1, len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            array.append(temp)
            temp = s[i]

        else:
            temp += s[i]

    array.append(temp)
    array.sort()

    result = ''
    temp = array[0]
    new_str = ''

    while len(array) > 0:
        
        flag = 0

        for i in range(1, len(array)):
            if i >= len(array):
                break
                
            if temp[0] == array[i][0]:
                flag = 1
                new_str = temp[0]
                new_str += str(int(temp[1:]) + int(array[i][1:]))
                temp = new_str
                array.pop(i)
            else:
                break

        if flag == 0:
            result += temp
            array.pop(0)

            if len(array) > 0:
                temp = array[0]
                new_str = ''

    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = betterCompression(s)

    # fptr.write(result + '\n')

    # fptr.close()

    s = 'a12c56a12c5a2b4a7'

    result = betterCompression(s)

    print(result + '\n')