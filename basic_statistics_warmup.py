"""
You are given an array of N integers separated by spaces, all in one line.

Display the following:

    Mean (m): The average of all the integers.

    Median of this array: In case, the number of integers is odd, the middle element; else, the average of the middle two elements.

    Mode: The element(s) which occurs most frequently. If multiple elements satisfy this criteria, display the numerically smallest one.

    Standard Deviation (SD).

    SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5

    where xi is the ith element of the array

    Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated by a space. This might be a new term to some. However, it is an important concept with a simple, formulaic solution. Look it up!

Other than the modal values (which should all be integers) the answers should be in decimal form till one place of decimal (0.0 format). An error margin of +/- 0.1 will be tolerated for the standard deviation and the confidence interval boundaries. The mean, mode and median values should match the expected answers exactly.

Assume that these numbers were sampled from a normal distribution; the sample is a reasonable representation of the distribution; a user can approximate that the population standard deviation =~ standard deviation computed for the given points- with the understanding that assumptions of normality are convenient approximations. Some relevant Youtube videos:

Input Format

The first line contains the number of integers.
The second line contains space separated integers for which you need to find the mean, median, mode, standard deviation and confidence interval boundaries.

Constraints

10 <= N <= 2500
0 < xi <= 105

Output Format

A total of five lines are required.

Mean (format:0.0) on the first line
Median (format: 0.0) on the second line
Mode(s) (Numerically smallest Integer in case of multiple integers)
Standard Deviation (format:0.0) 
Lower and Upper Boundary of Confidence Interval (format: 0.0) with a space between them.

Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output

43900.6
44627.5
4978
30466.9
25017.0 62784.2

Note
Use the constant 1.96 while computing the confidence interval.

Scoring

Scoring is proportional to the number of test cases cleared.
"""

# N = int(input())
# X = list(map(int, input().split()))

N = 10
X = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]

X.sort()

sum = 0.0
for i in range(N):
    sum += X[i]

if N%2 == 1:
    median = X[int(N/2)]
else:
    median = (X[int(N/2)-1] + X[int(N/2)]) / 2

mean = sum / N

mode = max(X, key=X.count)

sd = 0.0

for i in range(N):
    sd += (X[i]-mean)**2

sd /= N
sd = sd**0.5

c = 1.96

sd_err = sd / (N**0.5)

low = round(mean - sd_err * c, 1)
up = round(mean + sd_err * c, 1)

print('{0:.1f}'.format(mean))
print('{0:.1f}'.format(median))
print(int(mode))
print('{0:.1f}'.format(sd))
print('{0:.1f}'.format(low), '{0:.1f}'.format(up))