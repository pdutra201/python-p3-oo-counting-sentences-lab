#!/usr/bin/env python3
import pdb
import re
class MyString:
  
  def __init__(self, value = ""):
    ##pdb.set_trace()
    self.value = value


  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    if self._value[-1] == ".":
      return True
    else:
      return False
    
  def is_question(self):
    if self._value[-1] == "?":
      return True
    else:
      return False
  
  def is_exclamation(self):
    if self._value[-1] == "!":
      return True
    else:
      return False
    
  def count_sentences(self):
    new_str = re.split(r'[^\w\s,]', self._value)
    new_str = [word for word in new_str if word]
    ##pdb.set_trace()
    return len(new_str)


  value = property(get_value, set_value)