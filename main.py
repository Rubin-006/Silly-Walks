import matplotlib.pyplot as plt
import random

last_item = lambda lst: lst[len(lst)-1] # Gives last value of a list

x, y= [random.randint(0,10)], [random.randint(0,10)] # Establishes a random starting point
directions = ["u","d","l","r"] # Choices of direction

length_of_step = 1 # adjust this to adjust length of step

for i in range(20): # adjust this range to adjust number of steps taken
    direction = random.choice(directions)
    match direction:
        case "u":
            y.append(last_item(y)+length_of_step)
            x.append(last_item(x))
        case "d":
            y.append(last_item(y)-length_of_step)
            x.append(last_item(x))
        case "r":
            x.append(last_item(x)+length_of_step)
            y.append(last_item(y))
        case "l":
            x.append(last_item(x)-length_of_step)
            y.append(last_item(y))

plt.plot(x,y)
plt.show()