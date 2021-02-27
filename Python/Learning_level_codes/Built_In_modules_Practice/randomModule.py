import random

a=random.random() # random floating value between 0 and 1 (0 and 1 are included)
a=random.uniform(1,2) # random floating value between 1 and 10 (1 and 10 are excluded)
a=random.randint(1,10) #random integer values between 1 and 10 (1 and 10 are included)
l=[1,2,3,4,5]
a=random.choice(l) #picks up a random element from list
a=random.choices(l,k=10) # this will return a list of 10 random picks from input list
a=random.choices(l,weights=[30,30,10,10,5],k=10) # Weights are provided for probability of random choices
print(a)