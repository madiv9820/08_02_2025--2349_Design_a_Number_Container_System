from timeout_decorator import timeout
from Solution import NumberContainers
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {
            'default_example': (["NumberContainers","find","change","change","change","change","find","change","find"], 
                                [[],[10],[2,10],[1,10],[3,10],[5,10],[10],[1,20],[10]],
                                [None,-1,None,None,None,None,1,None,2]),
            'number_not_present': (["NumberContainers","find"], [[],[100]], [None,-1]),
            'multiple_numbers_and_indices': (["NumberContainers","change","change","change","change","change","find","find","find"],
                                             [[],[10,100],[5,200],[1,100],[7,300],[3,100],[100],[200],[300]],
                                             [None,None,None,None,None,None,1,5,7]),
            'replacing_numbers': (["NumberContainers","change","change","find","find"],
                                  [[],[1,100],[1,200],[100],[200]],
                                  [None,None,None,-1,1]),
            'large_indexes': (["NumberContainers","change","find"],
                              [[],[1000000000,999999999],[999999999]],
                              [None,None,1000000000]),
            'edge_case_for_maximum_index_and_number': (["NumberContainers","change","find","change","find"],
                                                       [[],[109,109],[109],[109,200],[109]],
                                                       [None,None,109,None,-1]),
            'no_change_in_find_result': (["NumberContainers","change","change","change","find"],
                                         [[],[1,50],[3,50],[5,50],[50]],
                                         [None,None,None,None,1])
        }
        return super().setUp()
    
    @timeout(0.5)
    def test_case_default_example(self):
        input_functions, inputs, expected = self.__testcases['default_example']
        output = []
        for i in range(len(inputs)):
            if input_functions[i] == 'NumberContainers':
                self.__solution = NumberContainers()
                output.append(None)
            elif input_functions[i] == 'change': output.append(self.__solution.change(inputs[i][0], inputs[i][1]))
            else: output.append(self.__solution.find(inputs[i][0]))
        
        self.assertEqual(output, expected)
    @timeout(0.5)
    def test_case_number_not_present(self):
        input_functions, inputs, expected = self.__testcases['number_not_present']
        output = []
        for i in range(len(inputs)):
            if input_functions[i] == 'NumberContainers':
                self.__solution = NumberContainers()
                output.append(None)
            elif input_functions[i] == 'change': output.append(self.__solution.change(inputs[i][0], inputs[i][1]))
            else: output.append(self.__solution.find(inputs[i][0]))
        
        self.assertEqual(output, expected)
    @timeout(0.5)
    def test_case_multiple_numbers_and_indices(self):
        input_functions, inputs, expected = self.__testcases['multiple_numbers_and_indices']
        output = []
        for i in range(len(inputs)):
            if input_functions[i] == 'NumberContainers':
                self.__solution = NumberContainers()
                output.append(None)
            elif input_functions[i] == 'change': output.append(self.__solution.change(inputs[i][0], inputs[i][1]))
            else: output.append(self.__solution.find(inputs[i][0]))
        
        self.assertEqual(output, expected)
    @timeout(0.5)
    def test_case_replacing_numbers(self):
        input_functions, inputs, expected = self.__testcases['replacing_numbers']
        output = []
        for i in range(len(inputs)):
            if input_functions[i] == 'NumberContainers':
                self.__solution = NumberContainers()
                output.append(None)
            elif input_functions[i] == 'change': output.append(self.__solution.change(inputs[i][0], inputs[i][1]))
            else: output.append(self.__solution.find(inputs[i][0]))
        
        self.assertEqual(output, expected)
    @timeout(0.5)
    def test_case_large_indexes(self):
        input_functions, inputs, expected = self.__testcases['large_indexes']
        output = []
        for i in range(len(inputs)):
            if input_functions[i] == 'NumberContainers':
                self.__solution = NumberContainers()
                output.append(None)
            elif input_functions[i] == 'change': output.append(self.__solution.change(inputs[i][0], inputs[i][1]))
            else: output.append(self.__solution.find(inputs[i][0]))
        
        self.assertEqual(output, expected)
    @timeout(0.5)
    def test_case_edge_case_for_maximum_index_and_number(self):
        input_functions, inputs, expected = self.__testcases['edge_case_for_maximum_index_and_number']
        output = []
        for i in range(len(inputs)):
            if input_functions[i] == 'NumberContainers':
                self.__solution = NumberContainers()
                output.append(None)
            elif input_functions[i] == 'change': output.append(self.__solution.change(inputs[i][0], inputs[i][1]))
            else: output.append(self.__solution.find(inputs[i][0]))
        
        self.assertEqual(output, expected)
    @timeout(0.5)
    def test_case_no_change_in_find_result(self):
        input_functions, inputs, expected = self.__testcases['no_change_in_find_result']
        output = []
        for i in range(len(inputs)):
            if input_functions[i] == 'NumberContainers':
                self.__solution = NumberContainers()
                output.append(None)
            elif input_functions[i] == 'change': output.append(self.__solution.change(inputs[i][0], inputs[i][1]))
            else: output.append(self.__solution.find(inputs[i][0]))
        
        self.assertEqual(output, expected)
    
if __name__ == '__main__': unittest.main()