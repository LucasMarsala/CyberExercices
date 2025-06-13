#!/usr/bin/env python3.9

def use_extended_euclidean(a, b):
    values = []
    r = b
    r1 = a
    s = 0
    s1 = 1
    t = 1
    t1 = 0
    q = 0
    print("----------------------------------\na = ", a, ", b = ", b, "\nInitialising:\nr1 = ", r1, ", s1 = ", s1, ", t1 = ", t1, "\t\t|\tr1 = s1*a + t1*b = ", s1, "*", a, " + ", t1, "*", b, " = ", ((s1*a) + (t1 * b)), "\nr = ", r, ", s = ", s, ", t = ", t, "\t\t|\tr = s*a + t*b = ", s, "*", a, " + ", t, "*", b, " = ", ((s * a) + (t * b)), sep='')
    while (r != 0):
        values.clear()
        print("----------------------------------")
        print("q = floor(", r1, "/", r, ") = ", int((r1 / r)), sep='')
        q = int(r1 / r)
        temp = (r1 - (q * r))
        print("r = ", temp, " = ", r1, " - ", q, "*", r, sep='')
        r1 = r
        r = temp
        temp = (s1 - (q * s))
        print("s = ", temp, " = ", s1, " - ", q, "*", s, sep='')
        s1 = s
        s = temp
        temp = (t1 - (q * t))
        print("t = ", temp, " = ", t1, " - ", q, "*", t, sep='')
        t1 = t
        t = temp
        print("sa + tb = ", s, "*", a, " + ", t, "*", b, " = ", ((s * a) + (t * b)), sep='')
        values.append(r1)
        values.append(s1)
        values.append(t1)
    print("----------------------------------\nThe GCD of ", a, " and ", b, " is ", ((values[1] * a) + (values[2] * b)), "\n", ((values[1] * a) + (values[2] * b)), " = ", values[1], "*", a, " + ", values[2], "*", b, sep='')


def main():
    try:
        print("Please enter the first integer: ", end='')
        a = int(input())
        print("Please enter the second integer: ", end='')
        b = int(input())

        if (a < 0) or (b < 0):
            print("Numbers should be positive")
            exit(1)
        use_extended_euclidean(a, b)
    except Exception as e:
        raise
        exit(1)

if __name__ == "__main__":
    # execute only if run as a script
    main()
