"""
You are provided with the following image

:

0000000000
0111111100
0000111100
0000111100
0001111100
0000111100
0001100000
0000000000
0000000000

The structuring element

is given below, and its origin is the middle pixel.

111
111
111

After
is dilated with the structuring element , what is the number of pixels marked obtained in the image? Enter the appropriate integer in the text box below.
Alternatively, you may submit a program which computes and displays the required integer. 
"""

def dilation(b, s):

    row = len(b)
    col = len(b[0])

    result = []
    for i in range(row):
        line = []
        for j in range(col):
            line.append(0)

        result.append(line)

    for i in range(row):
        for j in range(col):
            if b[i][j] == '1':
                
                result[i-1][j-1] = 1
                result[i-1][j] = 1
                result[i-1][j+1] = 1
                result[i][j-1] = 1
                result[i][j] = 1
                result[i][j+1] = 1
                result[i+1][j-1] = 1
                result[i+1][j] = 1
                result[i+1][j+1] = 1

    count = 0

    for i in range(row):
        for j in range(col):
            count += result[i][j]

    return count


b = [
    '0000000000',
    '0111111100',
    '0000111100',
    '0000111100',
    '0001111100',
    '0000111100',
    '0001100000',
    '0000000000',
    '0000000000'
]

s = [
    '111',
    '111',
    '111',
]

print(dilation(b,s))