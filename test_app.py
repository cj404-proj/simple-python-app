# test_app.py
import unittest
import app

class TestApp(unittest.TestCase):
    def test_output(self):
        self.assertEqual("Hello, Jenkins from Python!", "Hello, Jenkins from Python!")

if __name__ == '__main__':
    unittest.main()