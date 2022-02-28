import unittest
from TokenParser import TokenParser, Pattern



class TestTokenParser(unittest.TestCase):

    def test_pattern_matching(self):
        pat = Pattern(['VARIABLE', 'VAL_SET', 'NUMBER'])
        self.assertTrue(pat.match([('VARIABLE', 'b'), 'VAL_SET', ('NUMBER', 4)]))
        self.assertTrue(pat.match([('VARIABLE', 'a'), 'VAL_SET', ('NUMBER', 1)]))

    def test_simple(self):
        i = [('VARIABLE', 'a'), 'VAL_SET', ('NUMBER', 1)]
        par = TokenParser()
        tree = par.parseTokenList(i)
        self.assertEqual({"type": "OP", "operator": "SET", "left": {"type": "VAR_INT", "name": "A"},
                          "right": {"type": "NUMBER", "value": 1}}, tree)
