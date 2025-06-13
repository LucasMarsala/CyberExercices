#!/usr/bin/env python3.9

import math
from matplotlib import pyplot as plt

def main():
    try:
        print("Please enter the file you want to analyze ", end='')
        file = input()
        user1_1 = open(file)
        times = []
        coordinates_x = []
        coordinates_y = []

        lines = user1_1.readlines()[1:-1]
        length = len(lines)

        for x in range(length):
            values = lines[x].split(' ')
            times.append(values[0])
            coordinates_x.append(values[1])
            coordinates_y.append(values[2])
        velocity = []
        maximum_val = 0
        time_occurrence = 0
        for x in range(0, length - 1, 2):
            r = math.sqrt(((float(coordinates_x[x + 1]) - float(coordinates_x[x]))**2) + ((float(coordinates_y[x + 1]) - float(coordinates_y[x]))**2))
            t = (float(times[x + 1]) - float(times[x]))
            v = r / t
            if v > maximum_val:
                maximum_val = v
                time_occurrence = t
            velocity.append(v)

        average = 0
        for x in range(0, len(velocity)):
            average = average + float(velocity[x])
        average = average / len(velocity)
        print("The average velocity is", average)
        print("The maximum value of the velocity is", maximum_val)
        print("The time of occurrence of the maximum velocity is", time_occurrence)
        plt.plot(velocity)
        plt.title("Velocity of " + file)
        plt.ylim(0, 2.5*10**5)
        plt.xlim(0, length)
        plt.show()
    except Exception:
        raise


if __name__ == "__main__":
    # execute only if run as a script
    main()
