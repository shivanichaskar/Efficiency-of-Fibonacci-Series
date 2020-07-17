import time
import unittest
from forth_part_explain.forth_explain import FibonacciSequence

class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._fibonacci_sequence = FibonacciSequence()
        self._efficiency_data = dict()  #empty dictionary

    def test_first_method(self):
        starting_time = time.time() #start timingeg. 1,2,3,... etc

        self._fibonacci_sequence.recursive_method(30) #this will execute

        ending_time = time.time()  #stop timing

        self._efficiency_data['recursive_method'] = ending_time - starting_time  # it will give the time at which 'self._fibonacci_sequence.recursive_method(10)' this line of code executed

        print(self._efficiency_data)

    def test_second_method(self):

        starting_time = time.time()

        self._fibonacci_sequence.math_method(30)

        ending_time = time.time()

        self._efficiency_data['math_method'] = ending_time - starting_time

        print(self._efficiency_data)

    def tearDown(self):
        self._fibonacci_sequence = None
        self._efficiency_data.clear()




if __name__ == '__main__':
    unittest.main()