import unittest
from maxcript.greeting import helloworld

class TestPrintHelloWorldTest(unittest.TestCase):
    def test_print_hello_world(self):
        self.assertEqual(helloworld.print_hello_world(), "hello world")
        
if __name__ == '__main__':
    unittest.main()
