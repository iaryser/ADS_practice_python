
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung02/al/aufgabe02
# Version: Sun Feb 23 20:27:43 CET 2025


class Node: 

  def __init__(self, element = None, previous = None, nxt = None):
    self._element = element
    self._prev = previous
    self._next = nxt
        
  def set_element(self, new_elem):
    self._element = new_elem
  
  def set_next(self, new_next):
    self._next = new_next
    
  def set_prev(self, new_prev):
    self._prev = new_prev
    
  def get_element(self):  
    return self._element
  
  def get_next(self):
    return self._next
  
  def get_prev(self):
    return self._prev
  
  
