code_0 = {"global_variables": {},
          "functions":
              {"main":
                  {"code": [
                      {"return": {"argument": {'type': 'variable', 'name': 'foo'}}}
                  ],
                      "local_variables":
                          {"foo": {
                              "type": "integer",
                              "initial": {'type': 'integer', 'value': 0}}},
                      "arguments": []
                  }
              }
          }

# def main( void ){
#    def foo = int[2] := [0,1]
#    for( j : foo ){
#        j = j+1
#    }
#    return foo
# }

code_1 = {
    "global_variables": {},
    "functions": {
        "main": {
            "code": [
                {
                    "for": {
                        "loop_variable": "foo",
                        "local_variable": {"j": {"type": "integer"}},
                        "array_index": [0, 1],
                        "code": [
                            {
                                "set": {
                                    "left": {"type": "variable", "name": "j"},
                                    "expression": {
                                        "type": "add",
                                        "arguments": [
                                            {"type": "variable", "name": "j"},
                                            {"type": "integer", "value": 1},
                                        ],
                                    },
                                }
                            }
                        ],
                    }
                },
                {"return": {"argument": {"type": "variable", "name": "foo"}}},
            ],
            "local_variables": {
                "foo": {
                    "type": "integer_array",
                    "length": 2,
                    "initial": {"type": "integer_array", "value": [0, 1]},
                }
            },
            "arguments": [],
        }
    },
}
