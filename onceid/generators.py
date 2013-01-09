import random

from onceid import ONCEB50, ONCESIZE

def getOnceID(): return getMyOnceID()

def getShortOnceID(): return getMyOnceID(8)

def getMyOnceID(l = 11):
  if l is None or not isinstance( l, (int, long) ):
    return None
  once_id = ''
  for i in range(l):
    once_idx = random.randint(0, ONCESIZE-1)
    once_id += ONCEB50[once_idx]
  return once_id
