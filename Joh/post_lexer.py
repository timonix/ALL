code_0 = [
    {"type": "define"},
    {"type": "function", "name": "main"},
    {"type": "("},
    {"type": "keyword_void"},
    {"type": ")"},
    {"type": "{"},
    {"type": "newLine"},
    {"type": "define"},
    {"type": "variable", "name": "foo"},
    {"type": "set"},
    {"type": "keyword_int"},
    {"type": "set_initial"},
    {"type": "integer", "value": 0},
    {"type": "newLine"},
    {"type": "keyword_return"},
    {"type": "variable", "name": "foo"},
    {"type": "newLine"},
    {"type": "}"}
]

code_1 = [
    {"type": "define"},
    {"type": "function", "name": "main"},
    {"type": "("},
    {"type": "keyword_void"},
    {"type": ")"},
    {"type": "{"},
    {"type": "newLine"},
    {"type": "define"},
    {"type": "variable", "name": "foo"},
    {"type": "set"},
    {"type": "keyword_int"},
    {"type": "single_index", "value": 2},
    {"type": "set_initial"},
    {"type": "array_index", "indices": [0, 1]},
    {"type": "newLine"},
    {"type": "keyword_for"},
    {"type": "("},
    {"type": "variable", "name": "j"},
    {"type": ":"},
    {"type": "variable", "name": "foo"},
    {"type": ")"},
    {"type": "{"},
    {"type": "newLine"},
    {"type": "variable", "name": "j"},
    {"type": "set"},
    {"type": "variable", "name": "j"},
    {"type": "operation_add"},
    {"type": "integer", "value": 1},
    {"type": "newLine"},
    {"type": "}"},
    {"type": "newLine"},
    {"type": "keyword_return"},
    {"type": "variable", "name": "foo"},
    {"type": "newLine"},
    {"type": "}"}
]

code_2 = [
    {"type": "define"},
    {"type": "function", "name": "fun_1"},
    {"type": "("},
    {"type": "variable", "name": "foo"},
    {"type": ")"},
    {"type": "{"},
    {"type": "newLine"},
    {"type": "variable", "name": "foo"},
    {"type": "array_index", "indices": [0, 1]},
    {"type": "set"},
    {"type": "array_index", "indices": [4, 5]},
    {"type": "newLine"},
    {"type": "keyword_return"},
    {"type": "integer", "value": 0},
    {"type": "newLine"},
    {"type": "}"},
    {"type": "newLine"},
    {"type": "newLine"},
    {"type": "define"},
    {"type": "function", "name": "main"},
    {"type": "("},
    {"type": "keyword_void"},
    {"type": ")"},
    {"type": "{"},
    {"type": "newLine"},
    {"type": "define"},
    {"type": "variable", "name": "foo"},
    {"type": "set"},
    {"type": "keyword_int"},
    {"type": "single_index", "value": 2},
    {"type": "set_initial"},
    {"type": "array_index", "indices": [0, 1]},
    {"type": "newLine"},
    {"type": "keyword_return"},
    {"type": "integer", "value": 0},
    {"type": "newLine"},
    {"type": "}"}
]
