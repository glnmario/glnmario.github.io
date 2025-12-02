from otter.test_files import test_case

OK_FORMAT = False

name = "q3d"
points = 12.5

def format_error(lines, line, ret_value="", fn_name=""):
    return_str = "\n\n"
    return_str += "The last line of the following test program failed.\n"
    return_str += "Make sure that your function returns exactly the same value\n"
    return_str += "as specified in the <b>assert</b> statement.\n\n"

    num_spaces = len(lines[2]) - len(lines[2].strip()) 
    return_str += "\n".join([l[num_spaces:].strip() for l in lines[2:line+1]])
    return_str += "\n<b>"
    return_str += lines[line+1][num_spaces:]
    return_str += "</b>\n\n"

    return_str += f"{fn_name} returned:\n"
    return_str += str(ret_value)
    return_str += "\n\n"

    return return_str  




def test_dependency_parser_basic_desc(line, ret_value, fn_name):
    test_strs = '''
def test_dependency_parser_basic(dependency_parse):
    s = [('The', 'DET', -1), ('dog', 'NOUN', -1), ('ate', 'VERB', -1), ('my', 'DET', -1), ('homework', 'NOUN', -1), ('.', 'PUNCT', -1)]
    parse = dependency_parse(s)
    expected_parse = [(1, 2), (2, 3), (3, 0), (4, 5), (5, 3), (6, 3)]
    assert len(parse) == 6
    assert isinstance(parse[0], tuple) == True
    assert len(parse[0]) == 2
    assert [d for d, h in parse] == [1, 2, 3, 4, 5, 6]
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=4, hidden=False)
def test_dependency_parser_basic(dependency_parse):
    s = [('The', 'DET', -1), ('dog', 'NOUN', -1), ('ate', 'VERB', -1), ('my', 'DET', -1), ('homework', 'NOUN', -1), ('.', 'PUNCT', -1)]
    parse = dependency_parse(s)
    expected_parse = [(1, 2), (2, 3), (3, 0), (4, 5), (5, 3), (6, 3)]
    assert len(parse) == 6, test_dependency_parser_basic_desc(4, len(parse), "len(parse)")
    assert isinstance(parse[0], tuple) == True, test_dependency_parser_basic_desc(5, isinstance(parse[0], tuple), "isinstance(parse[0], tuple)")
    assert len(parse[0]) == 2, test_dependency_parser_basic_desc(6, len(parse[0]), "len(parse[0])")
    assert [d for d, h in parse] == [1, 2, 3, 4, 5, 6], test_dependency_parser_basic_desc(7, [d for d, h in parse], "[d for d, h in parse]")

