import unittest
from day1 import count_calories, count_calories_2

class TestCountCalories(unittest.TestCase):
    def test_count_calories(self):
        """
        Test that the count_calories function correctly computes the maximum calorie count.
        """
        self.assertEqual(count_calories(['100','','200','','100','200']), 200)
        self.assertEqual(count_calories(['100','','200','','300','200']), 300)
        self.assertEqual(count_calories(['100','','200','','100','300']), 300)

class TestCountCalories2(unittest.TestCase):
    def test_count_calories_2(self):
        """
        Test that the count_calories_2 function correctly computes the sum of the top three calorie counts.
        """
        self.assertEqual(count_calories_2(['100','','200','','100','200']), 500)
        self.assertEqual(count_calories_2(['100','','200','','300','200']), 600)
        self.assertEqual(count_calories_2(['100','','200','','100','300']), 600)

if __name__ == '__main__':
    unittest.main()
