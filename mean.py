#you are so concentrated in coding, its funny
#orsholya ... I came especially to fix your amazing name

#Print the mean of the data.txt
import sys

summation=0
n=0

#Sum input values
for number in open('data.txt'):
	summation += float(number)
	n += 1

print sum / n
