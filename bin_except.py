#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 01/30/23
#Modify the binary search function from the exploration so that,
# instead of returning -1 when the target value is not in the list,
# raises a TargetNotFound exception (you'll need to define this exception class).
# Otherwise it should function normally. Name this function bin_except.

class TargetNotFound(Exception):
  """Exception class for a binary search algorithm. It will be raised when the target value it is not present in list"""
  pass

def bin_except(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns -1, indicating the target value isn't in the list
  """
  first = 0
  last = len(a_list) - 1
  while first <= last:
    middle = (first + last) // 2 #splits list in half and checks midpoint first
    if a_list[middle] == target: #if target found, location returned
      return middle
    if a_list[middle] > target: #continues splitting list in half and checking for value until found
      last = middle - 1
    else:
      first = middle + 1
  raise TargetNotFound














