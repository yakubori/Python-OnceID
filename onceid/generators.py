import random

from onceid import ONCEB50, ONCESIZE

def getOnceID():
  """Generate a random 11-character OnceID."""
  return getMyOnceID()

def getShortOnceID():
  """Generate a random 8-character OnceID."""
  return getMyOnceID(8)

def getMyOnceID(l = 11):
  """Generate a random n-character OnceID.

  Keyword arguments:
  l -- the desired character length of the OnceID (default 11).

  """
  if not isinstance(l, (int, long)) or l < 3:
    return None
  once_id = ''
  for i in range(l):
    once_idx = random.randint(0, ONCESIZE-1)
    once_id += ONCEB50[once_idx]
  return once_id
