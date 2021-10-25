import unittest
from sum1 import sum
class test1(unittest.testcase):
  def test_sum(self):
    data = [4,5,6]
    res = sum(data)
    self.equal(res,15)
if __name__ == '__main__':
  unittest.main()
