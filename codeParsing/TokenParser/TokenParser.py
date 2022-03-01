# Takes lists of tokens from lexer and parses into tree

class Pattern:
    def match(self, input_list):
        for idx, element in enumerate(self.pattern):
            if isinstance(input_list[idx], tuple):
                if element != input_list[idx][0]:
                    return False
            else:
                if element != input_list[idx]:
                    return False
        return True

    def __init__(self, list_of_types):
        self.pattern = list_of_types

simpleAssignment = Pattern(['VARIABLE', 'VAL_SET', 'NUMBER'])

class TokenParser:

    tree = {"type": "PROGRAM", "body": None}
    current_leaf = tree["body"]

    def __init__(self, input):
        self.code = input


    def parse_next(self):


        if simpleAssignment.match(self.code):

    def parseTokenList(self, input):
        print(simpleAssignment.match(input))
        for i in input:
            print(i)

        pass