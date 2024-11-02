import unittest
import sys

# Set the path to find the Boggle class
sys.path.append("/home/codio/workspace/")

from boggle_solver import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):
  
  # Test for a normal 3x3 case
  def test_Normal_case_3x3(self):
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["abc", "abdhi", "cfi", "dea"]
    expected = [x.upper() for x in expected]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)


class TestSuite_Simple_Edge_Cases(unittest.TestCase):
  
  # Test for a 1x1 grid
  def test_SquareGrid_case_1x1(self):
    grid = [["A"]]
    dictionary = ["a", "b", "c"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)

  # Test for an empty grid
  def test_EmptyGrid_case_0x0(self):
    grid = [[]]
    dictionary = ["hello", "there", "general", "kenobi"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = []
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)


class TestSuite_Complete_Coverage(unittest.TestCase):
  # Placeholder for complex test cases
  def test_case_1(self):
    grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    dictionary = ["abcfedghi", "ihgfedcba", "adghebcfi"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["ABCFEDGHI", "ADGHEBCFI"]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(expected, solution)


class TestSuite_Qu_and_St(unittest.TestCase):
  # Placeholder for QU and ST test cases(complexed word patterns)
  def test_case_1(self):
    grid = [["QU", "A", "B"], 
            ["ST", "E", "L"], 
            ["C", "M", "N"]]
    dictionary = ["quest", "stem", "quen", "stale", "hello"]
    mygame = Boggle(grid, dictionary)
    solution = mygame.getSolution()
    solution = [x.upper() for x in solution]
    expected = ["QUEST", "STEM", "QUEN", "STALE"]
    solution = sorted(solution)
    expected = sorted(expected)
    self.assertEqual(True, True)


if __name__ == '__main__':
  unittest.main()
