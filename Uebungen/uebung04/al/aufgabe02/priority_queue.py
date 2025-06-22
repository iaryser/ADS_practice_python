
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung04/al/aufgabe02
# Version: Sun Mar  9 19:25:53 CET 2025

import functools
from uebung04.al.aufgabe02.full_priority_queue_exception import FullPriorityQueueException


class PriorityQueue:
  """ A heap-based (array-implementation) Priority-Queue with fixed length. """
  
  @functools.total_ordering
  class _PQEntry:
    
    def __init__(self, key, value):
      self._key = key
      self._value = value

    def get_key(self):
      return self._key

    def get_value(self):
      return self._value

    def __lt__(self, other):
      if other == None:
        return False
      return self._key < other._key 
    
    def __eq__(self, other):
      if other == None:
        return False
      return self._key == other._key
    
    def __str__(self):
      return "(" + str(self._key) + "," + str(self._value) +")"
    
    
  def __init__(self, max_size): 
    self._heap_array = [None] * (max_size+1)
    self._last = 0 # Points to the last element in the heap.

  def insert(self, key, value):
    if self._last == (len(self._heap_array) - 1):
      raise FullPriorityQueueException("Maximum reached: " + str(len(self._heap_array)))
    
    # TODO: Implement here...
    
    self._last += 1
    e = PriorityQueue._PQEntry(key, value)
    self._heap_array[self._last] = e
    
    # TODO: Implement here...
    
    return e
  
  def min(self):
    # TODO: Implement here...
    return None

  def remove_min(self):
    # TODO: Implement here...
    return None
  
  def is_empty(self):
    # TODO: Implement here...
    return True
  
  def size(self):
    # TODO: Implement here...
    return -1
  
  def print(self):
    print(self.__str__())
    
  def __str__(self):
    string = "["
    for i in range(len(self._heap_array)):
      entry= self._heap_array[i]
      if entry != None:
        string += "[" + str(entry) + "," + str(i) + "]"
      else:
        string += "None"
      if i < len(self._heap_array)-1:
        string += ", "
    string += "]"
    return string 

  def _swap(self, parent_index, child_index):
    """ Swaps a child-node with its parent-node.
  
    parentIndex Index of the parent-node.
  
    childIndex Index of the child-node.
    """
    # TODO: Implement here...
    pass

  def _upheap(self, current_index):
    # TODO: Implement here...
    pass

  def _downheap(self, current_index):
    # TODO: Implement here...
    pass
  
  
