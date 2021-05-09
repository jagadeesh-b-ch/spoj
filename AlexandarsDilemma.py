from random import randint

# Probability of drawing
no_of_times_lucky = 0
for i in range(0, 1000):
    probability_of_110 = randint(1, 5)
    if probability_of_110 == 1:
        no_of_times_lucky = no_of_times_lucky + 1
print("Alexandar got $110 " + str(no_of_times_lucky) + " times out of 1000 times")

