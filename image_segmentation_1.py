"""
Consider the following binary image where is the background, and

represents a pixel on an object.

000110001010
111011110001
111010010010
100000000100 

If we segment this image on a model based on simple 4 pixel connectivity, how many 4-connected objects do you obtain? Enter the appropriate integer in the text box below.
Alternatively, you may submit a program which computes and displays the required integer. 
"""

def segment(data):

    num = 0
    overlap = 0
    label = []

    for i in range(len(data)):
        line = []

        for j in range(len(data[0])):
            line.append(0)

        label.append(line)

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '1':
                if i == 0 and j == 0:
                    num += 1
                    label[i][j] = num
                    continue

                if i == 0:
                    if label[i][j-1] > 0:
                        label[i][j] = label[i][j-1]
                        continue

                if j == 0:
                    if label[i-1][j] > 0:
                        label[i][j] = label[i-1][j] 
                        continue

                if label[i][j-1] > 0:
                    if label[i-1][j] > 0 and label[i][j-1] != label[i-1][j]:
                        overlap += 1

                    label[i][j] = label[i][j-1]
                    continue

                if label[i-1][j] > 0:
                    label[i][j] = label[i-1][j]
                    continue

                num += 1
                label[i][j] = num            

    num -= overlap

    return num



data = []
while True:
    try:
        line = input()
    except EOFError:
        break
    data.append(line)

# data = [
#     '000110001010',
#     '111011110001',
#     '111010010010',
#     '100000000100'
# ]

print(segment(data))