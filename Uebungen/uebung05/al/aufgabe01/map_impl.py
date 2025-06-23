
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung05/al/aufgabe01
# Version: Mon Mar 17 10:49:24 CET 2025

import enum
from uebung05.al.aufgabe01.entry import Entry


class MapImpl:
  
  def __init__(self):  
    self._list = []
  
  def size(self):
    # TODO: Implement here...
    return None
  
  def is_empty(self):
    # TODO: Implement here...
    return None
  
  def put(self, key, value):
    # TODO: Implement here...
    return None
      
  def get(self, key):
    # TODO: Implement here...
    return None
  
  def remove(self, key):
    # TODO: Implement here...
    return None
    
  def values(self):
    # TODO: Implement here...
    return None
  
  def key_set(self):
    # TODO: Implement here...
    return None
  
  def entry_set(self):
    # TODO: Implement here...
    return None
  
  def printMap(self, prefix = ""):
    print(prefix + "Printing map (" + str(self.size()) + " Entries): ")
    for e in self._list:
      print(f"  {e.get_key():3d}: {e.get_value()}")
      
