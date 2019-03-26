#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY s as parameter.
#

def funWithAnagrams(s):
    # Write your code here

    result = []
    result.append(s[0])

    for i in range(1, len(s)):
        
        flag = 0

        for j in range(len(result)):
            if len(s[i]) == len(result[j]):

                temp_s = list(s[i])
                temp_r = list(result[j])

                while len(temp_r) > 0:

                    remove = 0

                    for itr in range(len(temp_s)):
                        if temp_r[0] == temp_s[itr]:
                            temp_r.pop(0)
                            temp_s.pop(itr)
                            remove = 1
                            break

                    if remove == 0:
                        break

                if remove == 1:
                    flag = 1
                    break

        if flag == 0:
            result.append(s[i])

    result.sort()

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s_count = int(input().strip())

    # s = []

    # for _ in range(s_count):
    #     s_item = input()
    #     s.append(s_item)

    # result = funWithAnagrams(s)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()


    s_count = 4

    s = ['code', 'aaagmnrs', 'anagrams', 'doce']

    result = funWithAnagrams(s)

    print('\n'.join(result))
    