import random

from onceid import ONCEB50, ONCESIZE

# Generate a random 11-character OnceID.
def getOnceID(): return getMyOnceID()

# Generate a random 8-character OnceID.
def getShortOnceID(): return getMyOnceID(8)

# Generate a random n-character OnceID.
def getMyOnceID(l = 11):
  if not isinstance(l, (int, long)) or l < 3:
    return None
  once_id = ''
  for i in range(l):
    once_idx = random.randint(0, ONCESIZE-1)
    once_id += ONCEB50[once_idx]
  return once_id
