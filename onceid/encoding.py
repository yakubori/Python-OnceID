from onceid import ONCEB50, ONCESIZE

# Convert a numeric ID to a OnceID.
def toOnceID(dividend):
  if not isinstance(dividend, (int, long)) or dividend < 0:
    return None
  if dividend == 0: return ONCEB50[0]
  once_id = ''
  # The math is done from right-to-left, so we're prepending to the OnceID.
  while dividend >= ONCESIZE:
    remainder = dividend % ONCESIZE
    dividend = dividend // ONCESIZE # floor it.
    once_id = ONCEB50[remainder] + once_id
  once_id = ONCEB50[dividend] + once_id
  return once_id

# Convert a OnceID back to an numeric ID.
def fromOnceID(once_id):
  if not isinstance( once_id, (str) ) or once_id == '':
    return None
  id_split = list(once_id)
  val = 0
  while(len(id_split) > 0):
    char_val = ONCEB50.index( id_split.pop(0) )
    val += char_val * (ONCESIZE ** len(id_split))
  return val
