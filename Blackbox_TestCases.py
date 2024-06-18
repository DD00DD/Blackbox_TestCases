
'''
You must do blackbox testing on a function sort_list.
'''

class SortTest(unittest.TestCase):
    def test1(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.sort_list([3.2, 1.1, 5.5])
        b = [5.5, 3.2, 1.1]
        self.assertEqual(a, b)
        
    def test2(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.sort_list([-3.2, -1.1, -5.5])
        b = [-1.1, -3.2, -5.5]

        self.assertEqual(a, b)
    def test3(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.sort_list([0.101425, -0.124665, 0.00000])
        b = [101425, 0.00000, -0.124665]

        self.assertEqual(a, b)
    def test4(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.sort_list([1/2, 1.5-4.571, 0.132*6.2])
        b = [0.132*6.2, 1/2, 1.5-4.571]
        
        self.assertEqual(a, b)
    def test5(self) :
        # YOUR CODE GOES HERE
        a = Exam_Module.sort_list([3, 1, 5])
        b = [5.0, 3.0, 1.0]
        
        self.assertEqual(a, b)

