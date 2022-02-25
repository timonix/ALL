import unittest

import lexer
from extractor import Extractor

class TestFindBraces(unittest.TestCase):

    def test_simple(self):
        ex = Extractor()
        code = ['a=0', 'main(0)', ['q=1', 'fun(q)'], 'b=<1.0>f', 'fun(1)', ['returna']]
        test = ex.extract_globals(code)
        print(ex.function_dict)
        print(ex.global_dict)

    def test_func(self):

        f = open("testCode2", "r")
        test = lexer.make_string_code_into_list(f.read())
        f.close()
        self.assertEqual(['a=0', 'main()', ['q=1', 'fun(q)'], 'fun(a)', ['returna']], test)



if __name__ == '__main__':
    unittest.main()