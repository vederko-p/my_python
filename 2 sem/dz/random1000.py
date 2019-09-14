import random

numbers = [random.randint(-500,500) for x in range(1000)]

def negative(l):

    counter = 0
    
    minN = l.index(min(numbers))
    maxN = l.index(max(numbers))

    if minN < maxN:
        
        interval = l[minN:maxN]

        for x in interval:

            if x > 0:
                continue

            if x < 0:
                counter += 1
                

    if minN > maxN:

        interval = l[maxN:minN]

        for x in interval:

            if x > 0:
                continue

            if x < 0:
                counter += 1

    return (counter)

print(negative(numbers))
