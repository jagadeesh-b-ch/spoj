from random import random

p = float(input())
noOfHeads = 0
noOfTails = 0
if 0 <= p <= 1:
    for i in range(0, 100):
        if random() < p:
            noOfHeads = noOfHeads + 1
        else:
            noOfTails = noOfTails + 1
    print("No. of Heads", noOfHeads)
    print("No. of Tails", noOfTails)
else:
    print("Invalid value of p")
