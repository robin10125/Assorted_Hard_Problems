import numpy as np
import math

'''
This program finds the median of two sorted arrays in logarithmic time
Algorithm:
For sorted arrays n and m
take median of n and m, compare
if n_m > m_m, take first half of n and second of m (including median), else opposite.  If they are equal, then answer is equal to them
return average of n_s and m_s if n_s and m_s length = 1 if sum is even, else if sum is odd, return middle value when n+m=3 
otherwise repeat
 
'''


def generate_sorted_random_list(size):
    """
    Generate a sorted list of random integers.
    """
    random_list = np.random.randint(low=1, high=1000, size=size)  # Generates random integers between 1 and 1000.
    sorted_list = np.sort(random_list) 
    return sorted_list

def merge(array1,array2):
    """
    Merges and sorts two arrays
    """
    merged = np.concatenate((array1,array2))
    merged = np.sort(merged)
    return merged

def fast_find_median(array_n, array_m, union_even):
    """
    Finds median of two sorted arrays in log time.  
    Parameter union even is a boolean that is true if the union has an even number of elements, and false if odd.
    """

    median_n = np.median(array_n)
    median_m = np.median(array_m)

    #if median of n is greater than m, then the median lies within the range of values between:
    # the first element and median element of n 
    # and the median and last element of m
    if median_n > median_m:
        new_n=array_n[:math.ceil(array_n.size/2)]
        new_m=array_m[math.floor(array_m.size/2):]

    #if median of m is greater than n, then the median lies within the range of values between:
    # the first element and median element of m 
    # and the median and last element of n
    elif median_n < median_m:
        new_n=array_n[math.floor(array_n.size/2):]
        new_m=array_m[:math.ceil(array_m.size/2)]
    
    #if both medians are the same, then the median of the union is likewise the same
    else: return median_n

    #check if subarrays are down to median element(s)
    if union_even:
        if new_n.size == 1 and new_m.size == 1:
            return (new_n+new_m)/2
    else:
        if ( new_n.size + new_m.size )==3:
            #sort
            union=np.concatenate((new_n,new_m))
            union = np.sort(union)
            return union[1]
    #if subarrays are not down to median elements, recursively call function until they are
    #TODO To make faster, calculate the number of rucursions based off the log_2(max(m,n)), accounting for rounding, and then do iteration instead of recursion
    median = fast_find_median(new_n,new_m,union_even)
    return median
print("Begin Test")
array_n = generate_sorted_random_list(100)
array_m = generate_sorted_random_list(90)
merged_array=merge(array_n,array_m)
median_val = np.median(merged_array)
union_even = ( array_n.size+array_m.size ) % 2 == 0
median_test = fast_find_median(array_n,array_m, union_even)

print(median_val)
print(median_test)