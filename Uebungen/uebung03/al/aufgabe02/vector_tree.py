# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung03/al/aufgabe02
# Version: Sun Mar  2 12:51:33 CET 2025

import enum
from no_such_node_exception import NoSuchNodeException

ROOT_INDEX = 1

class VectorTree:

  class _child_side(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()

  def __init__(self):
    self._binary_tree = [None, None]  # index 0 unused, root at index 1
    self._size = 0

  def root(self):
    # TODO: Implement here...
    return self._binary_tree[ROOT_INDEX]

  def set_root(self, root):
    # TODO: Implement here...
    self._remove(ROOT_INDEX)
    self._assure_size(ROOT_INDEX)
    self._binary_tree[ROOT_INDEX] = root
    self._size = 1

  def parent(self, child):
    # TODO: Implement here...
    if self.is_root(child):
      return None
    return self._binary_tree[self._get_position(child) // 2]

  def left_child(self, parent):
    # TODO: Implement here...
    return self._get_child(parent, VectorTree._child_side.LEFT)

  def right_child(self, parent):
    # TODO: Implement here...
    return self._get_child(parent, VectorTree._child_side.RIGHT)

  def is_internal(self, node):
    # TODO: Implement here...
    return not self.is_external(node)

  def is_external(self, node):
    # TODO: Implement here...
    pos = self._get_position(node)
    left = self._child_pos_by_index(pos, VectorTree._child_side.LEFT)
    right = self._child_pos_by_index(pos, VectorTree._child_side.RIGHT)
    return not (self._has_node_at_position(left) or self._has_node_at_position(right))

  def is_root(self, node):
    # TODO: Implement here...
    return node == self._binary_tree[ROOT_INDEX]

  def set_right_child(self, parent, child):
    # TODO: Implement here...
    self._set_child(parent, child, VectorTree._child_side.RIGHT)

  def set_left_child(self, parent, child):
    # TODO: Implement here...
    self._set_child(parent, child, VectorTree._child_side.LEFT)

  def remove_right_child(self, parent):
    # TODO: Implement here...
    self._remove_child(parent, VectorTree._child_side.RIGHT)

  def remove_left_child(self, parent):
    # TODO: Implement here...
    self._remove_child(parent, VectorTree._child_side.LEFT)

  def size(self):
    # TODO: Implement here...
    return self._size

  def print_vector(self, message):
    print("\n" + message)
    print(self._binary_tree)

  # --- helper methods ---

  def _get_position(self, node):
    try:
      position = self._binary_tree.index(node)
    except ValueError:
      raise NoSuchNodeException(f'There is no node: {node}')
    return position

  def _child_pos_by_index(self, parent_pos, side):
    return parent_pos * 2 + (0 if side == VectorTree._child_side.LEFT else 1)

  def _child_pos_by_value(self, parent, side):
    return self._child_pos_by_index(self._get_position(parent), side)

  def _has_node_at_position(self, pos):
    return pos < len(self._binary_tree) and self._binary_tree[pos] is not None

  def _get_child(self, parent, side):
    pos = self._child_pos_by_value(parent, side)
    if not self._has_node_at_position(pos):
      return None
    return self._binary_tree[pos]

  def _set_child(self, parent, child, side):
    self._remove_child(parent, side)
    pos = self._child_pos_by_value(parent, side)
    self._assure_size(pos)
    if self._binary_tree[pos] is None:
      self._size += 1
    self._binary_tree[pos] = child

  def _remove_child(self, parent, side):
    pos = self._child_pos_by_value(parent, side)
    if self._has_node_at_position(pos):
      self._remove(pos)

  def _remove(self, pos):
    for side in VectorTree._child_side:
      child_pos = self._child_pos_by_index(pos, side)
      if self._has_node_at_position(child_pos):
        self._remove(child_pos)
    self._binary_tree[pos] = None
    self._size -= 1

  def _assure_size(self, pos):
    while pos >= len(self._binary_tree):
      self._binary_tree.append(None)
