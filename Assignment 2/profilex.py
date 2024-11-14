from numpy import np
import time
import random
import sort
# SYSC 2100 Winter 2023 Lab 11/Asst 2

# Put import statements here.

__author__ = 'Dania Mahmoud'
__student_number__ = '101218762'


# Your profiling functions can have as many parameters as you want.
# The return type of each function is up to you.

def profile_bubble_sort() -> dict:
    n = 1000
    avg_times = dict()
    avg = 0
    for i in range(10):
        if n <= 3000:
            lst = []
            lst.append(np.random.randint(0, n, n))
            p1 = time.perf_counter()
            sort.bubble_sort(lst[0], n)
            p2 = time.perf_counter()
            avg += (p2 - p1)
            avg_times[n] = avg / 10
            n += 250
    return avg_times


def profile_selection_sort() -> dict:
    n = 1000
    avg_times = dict()
    avg = 0
    for i in range(10):
        if n <= 3000:
            lst = []
            lst.append(np.random.randint(0, n, n))
            p1 = time.perf_counter()
            sort.selection_sort(lst[0], n)
            p2 = time.perf_counter()
            avg += (p2 - p1)
            avg_times[n] = avg / 10
            n += 250
    return avg_times


def profile_insertion_sort() -> dict:
    n = 1000
    avg_times = dict()
    avg = 0
    for i in range(10):
        if n <= 3000:
            lst = []
            lst.append(np.random.randint(0, n, n))
            p1 = time.perf_counter()
            sort.insertion_sort(lst[0], n)
            p2 = time.perf_counter()
            avg += (p2 - p1)
            avg_times[n] = avg / 10
            n += 250
    return avg_times


def profile_heapsort() -> dict:
    n = 1000
    avg_times = dict()
    avg = 0
    for i in range(10):
        if n <= 3000:
            lst = []
            lst.append(np.random.randint(0, n, n))
            p1 = time.perf_counter()
            sort.heapsort(lst[0], n)
            p2 = time.perf_counter()
            avg += (p2 - p1)
            avg_times[n] = avg / 10
            n += 250
    return avg_times
# You are permitted to change this script.


if __name__ == '__main__':
    arr1 = profile_bubble_sort()
    arr2 = profile_selection_sort()
    arr3 = profile_insertion_sort()
    arr4 = profile_heapsort()
    print(arr1)
    print(arr2)
    print(arr3)
    print(arr4)

