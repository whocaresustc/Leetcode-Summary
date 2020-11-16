import unittest


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fun(3), 4)

    def test2(self):
        self.assertEqual(fun(4), 5)


if __name__ == '__main__':
    unittest.main()