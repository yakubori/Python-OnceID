import unittest
import random

from onceid import *

class TestOnceIDFunctions(unittest.TestCase):

  # Generator tests.
  def test_generators(self):
    once_id = generators.getOnceID()
    short_once_id = generators.getShortOnceID()
    
    self.assertTrue(len(once_id) == 11)
    self.assertTrue(len(short_once_id) == 8)
    
    for i in range(0, 2):
      once_id = generators.getMyOnceID(i)
      self.assertEqual(once_id, None)
    for i in range(3, 256):
      once_id = generators.getMyOnceID(i)
      self.assertTrue(len(once_id) == i, 'Failed on: '+str(i))

  # Encoding tests.
  def test_encoding(self):
    for j in range(0, 1000000):
      i = random.randint(0, 5000000)
      once_id = encoding.toOnceID(i)
      decoded = encoding.fromOnceID(once_id)
      self.assertEqual(i, decoded, "Failed on decode %s, expecting %d" % (once_id, i))
    r_test = 12342345234523122413
    once_id = encoding.toOnceID(r_test)
    decoded = encoding.fromOnceID(once_id)
    self.assertEqual(r_test, decoded, "Failed on decode %s, expecting %d" % (once_id, r_test))

if __name__ == '__main__':
  unittest.main(verbosity=2)
