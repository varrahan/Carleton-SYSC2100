# SYSC 2100 Winter 2023 Lab 11/Asst 2

from sort import *
from time import perf_counter
import random
__author__ = 'Varrahan Uthayan'
__student_number__ = '101229572'


# Your profiling functions can have as many parameters as you want.
# The return type of each function is up to you.

def profile_bubble_sort(k: int, n: int, num_results: int)-> list:
    """
    Returns a list with a length of num_results of the average time it takes for k trials to perform bubble sort.
    Raises ValueError if k is less than 10 or num_results is less than 1.
    
    >>>profile_bubble_sort(11,1000,20)
    ['average time for n = 1000: 0.0595651454545454', 
    'average time for n = 1200: 0.0910319272727272', ..., 
    'average time for n = 4800: 1.57964346363635']
    >>profile_bubble_sort(9,2000,12)
    ValueError: Not enough trials. Minimum is 10.
    
    >>profile_bubble_sort(12,1000,-2)
    ValueError: Number of results is too low. Minimum is 1.
    """
    if k < 10:
        raise ValueError("Not enough trials. Minimum is 10.")
    if num_results < 1:
        raise ValueError('Number of results is too low. Minimum is 1')
    if n < 1000:
        raise ValueError('n - value is too small. Minimum is 1000')
    # Function can still run if n is greater than 5000 however it takes too long for the function to run
    if n > 5000:
        raise ValueError('n - value is too large. Max is 5000.') 
    unsorted_list=[] # List that will contain the values that need to be sorted
    results = [] # List used to store the results of each average time for the num_results iteration
    stored_dict = {} # Dictionary using n-values as keys and a list of unsorted integers as values
    # Loops according to the number of results wanted in the list
    for x in range(num_results):
        time = 0
        # Exits loop if n is greater than 7000 since it will take too long to sort.
        if n > 7000:
            print("n value is too large. Maximum is 7000")
            return results
        for i in range(n): 
            unsorted_list.append(random.randint(0,n))   
        stored_dict[n] = unsorted_list
        # Loops according to the number of trials wanted, which is parameter k
        for j in range(k):  
            lst = stored_dict[n]
            time_start = perf_counter()
            # The only line that changes in the other functions 
            # Calls the sorting function that the profile function is timing
            bubble_sort(lst, len(lst)) 
            time_end = perf_counter()
            time += (time_end - time_start)
        # Adds the average time as a string to a list that stores the results
        results.append('average time for n = ' + str(n) + ': ' + str(time/k))
        n += 200 # Increments n by 200 for every iteration of 'for j in range(num_results)'
        unsorted_list.clear()
    return results 

def profile_selection_sort(k: int, n: int, num_results: int) -> list:
    '''
    Returns a list with a length of num_results of the average time it takes for k trials to perform selection sort.
    Raises ValueError if k is less than 10 or num_results is less than 1.
    
    >>>profile_selection_sort(11,1000,20)
    ['average time for n = 1000: 0.04902582727273015', 
    'average time for n = 1200: 0.0680043454545424', ..., 
    'average time for n = 4800: 1.144400318181818']  
    '''
    if k < 10:
        raise ValueError("Not enough trials. Minimum is 10.")
    if num_results < 1:
        raise ValueError('Number of results is too low. Minimum is 1')
    if n < 1000:
        raise ValueError('n - value is too small. Minimum is 1000')
    # Function can still run if n is greater than 5000 however it takes too long for the function to run
    if n > 5000:
        raise ValueError('n - value is too large. Max is 5000.') 
    unsorted_list=[] # List that will contain the values that need to be sorted
    results = [] # List used to store the results of each average time for the num_results iteration
    stored_dict = {} # Dictionary using n-values as keys and a list of unsorted integers as values
    # Loops according to the number of results wanted in the list
    for x in range(num_results):
        time = 0
        # Exits loop if n is greater than 7000 since it will take too long to sort.
        if n > 7000:
            print("n value is too large. Maximum is 7000")
            return results
        for i in range(n): 
            unsorted_list.append(random.randint(0,n))   
        stored_dict[n] = unsorted_list
        # Loops according to the number of trials wanted, which is parameter k
        for j in range(k):  
            lst = stored_dict[n]
            time_start = perf_counter()
            # The only line that changes in the other functions 
            # Calls the sorting function that the profile function is timing
            sort.selection_sort(lst, len(lst)) 
            time_end = perf_counter()
            time += (time_end - time_start)
        # Adds the average time as a string to a list that stores the results
        results.append('average time for n = ' + str(n) + ': ' + str(time/k))
        n += 200 # Increments n by 200 for every iteration of 'for j in range(num_results)'
        unsorted_list.clear()
    return results       


def profile_insertion_sort(k: int, n: int, num_results: int) -> list:
    '''
    Returns a list with a length of num_results of the average time it takes for k trials to perform insertion sort.
    Raises ValueError if k is less than 10 or num_results is less than 1.
    
    >>>profile_insertion_sort(11,1000,20)
    ['average time for n = 1000: 0.06788624545454719', 
    'average time for n = 1200: 0.09940692727272901', ..., 
    'average time for n = 4800: 0.3332155454545468'] 
    ''' 
    if k < 10:
        raise ValueError("Not enough trials. Minimum is 10.")
    if num_results < 1:
        raise ValueError('Number of results is too low. Minimum is 1')
    if n < 1000:
        raise ValueError('n - value is too small. Minimum is 1000')
    # Function can still run if n is greater than 5000 however it takes too long for the function to run
    if n > 5000:
        raise ValueError('n - value is too large. Max is 5000.') 
    unsorted_list=[] # List that will contain the values that need to be sorted
    results = [] # List used to store the results of each average time for the num_results iteration
    stored_dict = {} # Dictionary using n-values as keys and a list of unsorted integers as values
    # Loops according to the number of results wanted in the list
    for x in range(num_results):
        time = 0
        # Exits loop if n is greater than 7000 since it will take too long to sort.
        if n > 7000:
            print("n value is too large. Maximum is 7000")
            return results
        for i in range(n): 
            unsorted_list.append(random.randint(0,n))   
        stored_dict[n] = unsorted_list
        # Loops according to the number of trials wanted, which is parameter k
        for j in range(k):  
            lst = stored_dict[n]
            time_start = perf_counter()
            # The only line that changes in the other functions 
            # Calls the sorting function that the profile function is timing
            insertion_sort(lst, len(lst)) 
            time_end = perf_counter()
            time += (time_end - time_start)
        # Adds the average time as a string to a list that stores the results
        results.append('average time for n = ' + str(n) + ': ' + str(time/k))
        n += 200 # Increments n by 200 for every iteration of 'for j in range(num_results)'
        unsorted_list.clear()
    return results
        
def profile_heapsort(k: int, n: int, num_results: int) -> list:
    '''
    Returns a list with a length of num_results of the average time it takes for k trials to perform heapsort.
    Raises ValueError if k is less than 10 or num_results is less than 1.
    
    >>>profile_heapsort(11,1000,20)
    ['average time for n = 1000: 0.01738963636364071', 
    'average time for n = 1200: 0.020800954545450168', ..., 
    'average time for n = 4800: 0.10495118181818373'] 
    '''     
    if k < 10:
        raise ValueError("Not enough trials. Minimum is 10.")
    if num_results < 1:
        raise ValueError('Number of results is too low. Minimum is 1')
    if n < 1000:
        raise ValueError('n - value is too small. Minimum is 1000')
    # Function can still run if n is greater than 5000 however it takes too long for the function to run
    if n > 5000:
        raise ValueError('n - value is too large. Max is 5000.') 
    unsorted_list=[] # List that will contain the values that need to be sorted
    results = [] # List used to store the results of each average time for the num_results iteration
    stored_dict = {} # Dictionary using n-values as keys and a list of unsorted integers as values
    # Loops according to the number of results wanted in the list
    for x in range(num_results):
        time = 0
        # Exits loop if n is greater than 7000 since it will take too long to sort.
        if n > 7000:
            print("n value is too large. Maximum is 7000")
            return results
        for i in range(n): 
            unsorted_list.append(random.randint(0,n))   
        stored_dict[n] = unsorted_list
        # Loops according to the number of trials wanted, which is parameter k
        for j in range(k):  
            lst = stored_dict[n]
            time_start = perf_counter()
            # The only line that changes in the other functions 
            # Calls the sorting function that the profile function is timing
            heapsort(lst, len(lst)) 
            time_end = perf_counter()
            time += (time_end - time_start)
        # Adds the average time as a string to a list that stores the results
        results.append('average time for n = ' + str(n) + ': ' + str(time/k))
        n += 200 # Increments n by 200 for every iteration of 'for j in range(num_results)'
        unsorted_list.clear()
    return results
# You are permitted to change this script.
if __name__ == '__main__':
    print(profile_bubble_sort(11,1000,20))
    print(profile_selection_sort(11,1000,20))
    print(profile_insertion_sort(11,1000,20))
    print(profile_heapsort(11,1000,20))


    print(profile_bubble_sort(15,3000, 4))
    print(profile_selection_sort(15, 3000, 4))
    print(profile_insertion_sort(15,3000, 4))
    print(profile_heapsort(15,3000, 4))   
    
    print(profile_bubble_sort(10,5000, 7))
    print(profile_selection_sort(10,5000, 7))
    print(profile_insertion_sort(10,5000,7))
    print(profile_heapsort(10,5000, 7))     

