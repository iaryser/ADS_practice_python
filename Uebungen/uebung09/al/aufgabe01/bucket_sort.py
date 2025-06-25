
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung09/al/aufgabe01
# Version: Tue Apr 15 11:57:57 CEST 2025

from collections import deque


def bucket_sort(sequence, n):
  """
  Sorts the sequence.
  
  sequence: Sequence to be sorted.
  n: The upper-bound of all values in sequence: 0..(n-1).
  """
  buckets = [None] * n
  
  # TODO: Implement here Phase 1 ...
  while len(sequence) != 0:
    key = sequence.popleft()
    if buckets[key] == None:
      buckets[key] = [key]
    else:
      buckets[key].append(key)
 
  pretty_print(buckets)
  
  # TODO: Implement here Phase 2 ...
  for i in range(n):
    while not buckets[i] == None and len(buckets[i]) != 0:
        e = buckets[i][0]
        buckets[i].remove(e)
        sequence.append(e) 

def pretty_print(buckets):
  print(str(buckets).replace("deque", "").replace("(", "").replace(")", ""))
  
    
if __name__ == '__main__':
  
  my_list = [7, 1, 3, 7, 3, 7]
  sequence = deque(my_list)
  print(sequence)
  bucket_sort(sequence, 10)
  print(sequence)
  
 
  """ Session-Log:
  
  deque([7, 1, 3, 7, 3, 7])
  [[], [1], [], [3, 3], [], [], [], [7, 7, 7], [], []]
  deque([1, 3, 3, 7, 7, 7])
  
  """  
