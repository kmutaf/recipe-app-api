"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """test adding number togetehrs"""

        res = calc.add(5,6)

        self.assertEqual(res,11)