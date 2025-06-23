
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung05/al/aufgabe01
# Version: Mon Mar 17 10:49:24 CET 2025

import enum
from entry import Entry


class MapImpl:
  
  def __init__(self):  
    self._list = []
  
  def size(self):
    # TODO: Implement here...
    return len(self._list)
  
  def is_empty(self):
    # TODO: Implement here...
    return self.size() == 0
  
  def put(self, key, value):
    # TODO: Implement here...
    index = 0
    for entry in self._list:
      if key == entry.get_key():
        old_value = entry.get_value()
        self._list[index] = Entry(key, value)
        return old_value
      index += 1
      
    self._list.append(Entry(key, value))
    return None
      
  def get(self, key):
    # TODO: Implement here...
    for entry in self._list:
      if key == entry.get_key():
        return entry.get_value()
    return None
  
  def remove(self, key):
    # TODO: Implement here...
    for entry in self._list:
      if key == entry.get_key():
        value = entry.get_value()
        self._list.remove(entry)
        return value
    return None
    
  def values(self):
    # TODO: Implement here...
    value_list = []
    if not self.is_empty():
      for entry in self._list:
        value_list.append(entry.get_value())
    return value_list
  
  def key_set(self):
    # TODO: Implement here...
    return {entry.get_key() for entry in self._list}
  
  def entry_set(self):
    # TODO: Implement here...
    entry_set = []
    if not self.is_empty():
      for entry in self._list:
        entry_set.append(entry)
    return entry_set
  
  def printMap(self, prefix = ""):
    print(prefix + "Printing map (" + str(self.size()) + " Entries): ")
    for e in self._list:
      print(f"  {e.get_key():3d}: {e.get_value()}")
      
