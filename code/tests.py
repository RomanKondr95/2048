from game import get_num_from_ind, get_empty_list,get_ind_from_num
import unittest
class Test_2048(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_num_from_ind(1,2),7)
    def test_2(self):
        self.assertEqual(get_num_from_ind(3,3),16)
    def test_3(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13, 14, 15, 16]
        mas = [[0]* 4 for i in range(4)]
        self.assertEqual(get_empty_list(mas),a)
    def test_4(self):
        a = []
        mas = [[1]* 4 for i in range(4)]
        self.assertEqual(get_empty_list(mas),a)
    def test_5(self):
        a = [5,6,7,8,9,10,11,12,13,14,15,16]
        mas = [[1,1,1,1],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]
        ]
        self.assertEqual(get_empty_list(mas),a)
    def test_6(self):
        self.assertEqual(get_ind_from_num(7),(1,2))
    def test_6(self):
        self.assertEqual(get_ind_from_num(16),(3,3))


if __name__ == '__main__':
    unittest.main()