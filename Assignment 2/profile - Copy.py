# SYSC 2100 Winter 2023 Lab 11/Asst 2
from sort import *
from time import perf_counter
import random
__author__ = 'Joseph Marques'
__student_number__ = '101218139'


# Your profiling functions can have as many parameters as you want.
# The return type of each function is up to you.

def profile_bubble_sort(k: int, n: int, num_iter: int)-> dict:
    """
    Returns a dictionary with num_iter keys of the average time it takes for k trials to perform bubble sort.
    Raises ValueError if k is less than 10 or num_iter is less than 1.
    
    >>>profile_bubble_sort(10,1000,15)
    {1000: 0.12152731000000001, 1250: 0.18580924000000004, ..., 
    4500: 1.9446288821741984}
    >>profile_bubble_sort(2,2000,17)
    ValueError: Not enough trials
    
    >>profile_bubble_sort(15,1050,-74)
    ValueError: Number of results cannot be this number
    """
    if k < 10:
        raise ValueError("Not enough trials")
    if num_iter < 1:
        raise ValueError('Number of results cannot be this number')
    if n < 1000:
        raise ValueError('Number is too small')
    #Function can still run if n is greater than 4000 but it takes too long for the computer to run
    if n > 4000:
        raise ValueError('Number is too large') 
    time = 0
    unsorted=[] # Stores an unsorted list of integers
    results = {} # Dictionary used to store the results of each average time as a value and the n-value as a key
    dct = {} # Dictionary using n-values as keys and a list of unsorted integers as values
    # Loops according to the number of results wanted in the list
    for x in range(num_iter):
        #exits loop if n is greater than 6000
        if n > 6000:
            print("n value is too large")
            break
        # Builds the unsorted list
        for i in range(n): 
            unsorted.append(random.randint(0,n))   
        dct[n] = unsorted
        # Loops according to the number of trials wanted
        for j in range(k):  
            to_sort = dct[n]
            time_start = perf_counter()
            # Calls the sorting function
            bubble_sort(to_sort, len(to_sort)) 
            time_end = perf_counter()
            time += (time_end - time_start)
        # Stores the average time as a value with it's respective n-value as the key
        results[n] = time/k
        time = 0
        n += 250 # Increments n by 250 for every n-value iteration until it reaches num_iter
        unsorted.clear() #Clears the unsorted list so that the next n-iteration does not add n elements to the pre-existing list
    return results 

def profile_selection_sort(k: int, n: int, num_iter: int) -> dict:
    '''
    Returns a dictionary with a length of num_iter of the average time it takes for k trials to perform selection sort.
    Raises ValueError if k is less than 10 or num_iter is less than 1.
    
    >>>profile_selection_sort(10,1000,15)
    {1000: 0.049337029999998096, 1250: 0.08004069999999501, ..., 
    4500: 1.0302147799999943} 
    '''
    if k < 10:
        raise ValueError("Not enough trials")
    if num_iter < 1:
        raise ValueError('Number of results cannot be this number')
    if n < 1000:
        raise ValueError('Number is too small')
    #Function can still run if n is greater than 4000 but it takes too long for the computer to run
    if n > 4000:
        raise ValueError('Number is too large') 
    time = 0
    unsorted=[] # Stores an unsorted list of integers
    results = {} # Dictionary used to store the results of each average time as a value and the n-value as a key
    dct = {} # Dictionary using n-values as keys and a list of unsorted integers as values
    # Loops according to the number of results wanted in the list
    for x in range(num_iter):
        #exits loop if n is greater than 6000
        if n > 6000:
            print("n value is too large")
            break
        # Builds the unsorted list
        for i in range(n): 
            unsorted.append(random.randint(0,n))   
        dct[n] = unsorted
        # Loops according to the number of trials wanted
        for j in range(k):  
            to_sort = dct[n]
            time_start = perf_counter()
            # Calls the sorting function
            selection_sort(to_sort, len(to_sort)) 
            time_end = perf_counter()
            time += (time_end - time_start)
        # Stores the average time as a value with it's respective n-value as the key
        results[n] = time/k
        time = 0
        n += 250 # Increments n by 250 for every n-value iteration until it reaches num_iter
        unsorted.clear() #Clears the unsorted list so that the next n-iteration does not add n elements to the pre-existing list
    return results        


def profile_insertion_sort(k: int, n: int, num_iter: int) -> list:
    '''
    Returns a dictionary with a length of num_iter of the average time it takes for k trials to perform insertion sort.
    Raises ValueError if k is less than 10 or num_iter is less than 1.
    
    >>>profile_insertion_sort(10,1000,15)
    {1000: 0.007304150000001642, 1250: 0.01057998000000282, ..., 
    4500: 0.13478457999999877}
    ''' 
    if k < 10:
        raise ValueError("Not enough trials")
    if num_iter < 1:
        raise ValueError('Number of results cannot be this number')
    if n < 1000:
        raise ValueError('Number is too small')
    #Function can still run if n is greater than 4000 but it takes too long for the computer to run
    if n > 4000:
        raise ValueError('Number is too large') 
    time = 0
    unsorted=[] # Stores an unsorted list of integers
    results = {} # Dictionary used to store the results of each average time as a value and the n-value as a key
    dct = {} # Dictionary using n-values as keys and a list of unsorted integers as values
    # Loops according to the number of results wanted in the list
    for x in range(num_iter):
        #exits loop if n is greater than 6000
        if n > 6000:
            print("n value is too large")
            break
        # Builds the unsorted list
        for i in range(n): 
            unsorted.append(random.randint(0,n))   
        dct[n] = unsorted
        # Loops according to the number of trials wanted
        for j in range(k):  
            to_sort = dct[n]
            time_start = perf_counter()
            # Calls the sorting function
            insertion_sort(to_sort, len(to_sort)) 
            time_end = perf_counter()
            time += (time_end - time_start)
        # Stores the average time as a value with it's respective n-value as the key
        results[n] = time/k
        time = 0
        n += 250 # Increments n by 250 for every n-value iteration until it reaches num_iter
        unsorted.clear() #Clears the unsorted list so that the next n-iteration does not add n elements to the pre-existing list
    return results
        

    #Function can still run if n is greater than 4000 but it takes too long for the computer to run
def profile_heapsort() -> dict:
    n = 1000
    avg_times = dict()
    avg = 0
    for i in range(10):
        if n <= 3000:
            lst = []
            for i in range(n):
                lst.append(random.randint(0, n))
            p1 = perf_counter()
            heapsort(lst, n)
            p2 = perf_counter()
            avg += (p2 - p1)
            avg_times[n] = avg
            n += 250
    return avg_times

# You are permitted to change this script.
if __name__ == '__main__':
    #print(profile_bubble_sort(10,1000,15))
   # print(profile_selection_sort(10,1000,15))
   # print(profile_insertion_sort(10,1000,15))
    print(profile_heapsort())

'''
    print(profile_bubble_sort(15,2000, 7))
    print(profile_selection_sort(15,2000, 7))
    print(profile_insertion_sort(15,2000, 7))
    print(profile_heapsort(15,2000, 7))   
    
    print(profile_bubble_sort(11,1750, 9))
    print(profile_selection_sort(11,1750, 9))
    print(profile_insertion_sort(11,1750,9))
    print(profile_heapsort(11,1750, 9))     
'''

