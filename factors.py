#!/usr/bin/python3
from sys import argv
from math import isqrt
import timeit

def main():
    if len(argv) != 2:
        return

    with open(argv[1], "r") as file:
        # Optimize fetching using list comprehension
        numbers = [int(num) for num in file]

    for number in numbers:
        if number % 2 == 0:
            print("{}={}*{}".format(number, number // 2, 2))
            continue

        m = 3
        for n in range(m, (isqrt(number) + 1), 2):
            if number % n == 0:
                print("{}={}*{}".format(number, number // n, n))
                break

        if m == (number // 2) + 1:
            print("{}={}*{}".format(number, 1, number))


if __name__ == "__main__":
    start_time = timeit.default_timer()
    cpu_time = timeit.timeit(main, number=1)
    end_time = timeit.default_timer()

    elapsed_time = end_time - start_time
    system_time = elapsed_time - cpu_time

    print("real 0m0.{0:.0f}s".format(elapsed_time))
    print("user 0m0.{0:.0f}s".format(cpu_time))
    print("sys 0m0.{0:.1f}s".format(system_time))
