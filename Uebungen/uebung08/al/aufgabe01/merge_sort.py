
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung08/al/aufgabe01
# Version: Tue Apr  8 12:39:58 CEST 2025

import random
import sys
from time import time


def merge_sort(s):
  """
  Sorts a list with the merge-sort algorithm.
  
  Precondition: Length must be 2^x.
  s: Sequence to be sorted.
  Returns the sorted sequence.
  """
  n = len(s)
  if n > 1:
    s1, s2 = partition(s, n//2)
    
    # TODO: Implement here...
    
  return s


def partition(s, n):
  
  # TODO: Implement here...
  
  return None
  
  
def merge(a, b):
  n = len(a) * 2
  s = [None] * n
  ai = 0  # First element in 'sequence' A
  bi = 0  # First element in 'sequence' B
  si = 0  # Last element in 'sequence' S
  
  # TODO: Implement here...
  
  return s 


def verify(orginalData, sortedData):
  correctSorted = orginalData.copy()
  correctSorted.sort()
  for i in range(len(orginalData)):
    if(correctSorted[i] != sortedData[i]):
      print("ERROR: wrong sorted!")
      print("Orginal : ", orginalData)
      print("Sorted  : ", sortedData)
      print(f"index[{i}]: should be: {correctSorted[i]}, but is: {sortedData[i]}")
      sys.exit(1)
  
  
if __name__ == '__main__':
  
  my_list = [7, 2, 9, 4, 3, 8, 6, 1]
  orginal_list = my_list.copy()
  print(my_list)

  my_list = merge_sort(my_list)
  
  print(my_list)
  verify(orginal_list, my_list)
        
  # Makeing some test to measure the time needed of merge_sort().
  # Creating int-lists, beginning with length of 2^min_exponent
  # until the last array with length of 2^max_exponent.
  min_exponent = 13
  max_exponent = 18
  last_time = sys.float_info.max
  for exp in range(min_exponent, max_exponent + 1):
    length = pow(2, exp)
    MEASUREMENTS = 10
    min_time = sys.float_info.max
    for i in range(MEASUREMENTS):
      data = list(range(length))
      random.shuffle(data)
      #list.reverse(data)
      start = time()
      merge_sort(data)
      end = time()
      time_spent = end - start
      if(time_spent < min_time):
        min_time = time_spent
    print(f"List-Size: {length:7,d}         Time: {min_time*1e3:7.1f} ms          Ratio to last: {min_time / last_time:.1f}")
    last_time = min_time


  """ Session-Log:
  
  [7, 2, 9, 4, 3, 8, 6, 1]
  [1, 2, 3, 4, 6, 7, 8, 9]
  List-Size:   8,192         Time:   ???.? ms          Ratio to last: 0.0
  List-Size:  16,384         Time:   ???.? ms          Ratio to last: ?.?
  List-Size:  32,768         Time:   ???.? ms          Ratio to last: ?.?
  List-Size:  65,536         Time:   ???.? ms          Ratio to last: ?.?
  List-Size: 131,072         Time:   ???.? ms          Ratio to last: ?.?
  List-Size: 262,144         Time:   ???.? ms          Ratio to last: ?.?

  """  
