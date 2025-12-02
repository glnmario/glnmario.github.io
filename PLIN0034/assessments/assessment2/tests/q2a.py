from otter.test_files import test_case

OK_FORMAT = False

name = "q2a"
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




def test_pen_and_paper_basic_desc(line, ret_value, fn_name):
    test_strs = '''
def test_pen_and_paper_basic(input_initial, input_iteration1, input_iteration2, input_iteration3, input_iteration4, input_iteration5, input_iteration6, dependencies_iteration1, dependencies_iteration2, dependencies_iteration3, dependencies_iteration4, dependencies_iteration5, dependencies_iteration6, stack_intial, stack_iteration1, stack_iteration2, stack_iteration3, stack_iteration4, stack_iteration5, stack_iteration6):
    assert len(input_initial) == 4
    assert len(input_iteration1) == 3
    assert len(input_iteration2) == 2
    assert len(input_iteration3) == 2
    assert len(input_iteration4) == 1
    assert len(input_iteration5) == 1
    assert len(input_iteration6) == 1
    assert type(input_initial[0]) == tuple
    assert len(input_initial[0]) == 2
    assert type(input_initial[0][0]) == int
    assert type(input_initial[0][1]) == str
    assert len(dependencies_iteration1) == 0
    assert len(dependencies_iteration2) == 0
    assert len(dependencies_iteration3) == 1
    assert len(dependencies_iteration4) == 1
    assert len(dependencies_iteration5) == 3
    assert len(dependencies_iteration6) == 4
    assert type(dependencies_iteration4[0]) == tuple
    assert type(dependencies_iteration4[0][0]) == int
    assert type(dependencies_iteration4[0][1]) == int
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=5, hidden=False)
def test_pen_and_paper_basic(input_initial, input_iteration1, input_iteration2, input_iteration3, input_iteration4, input_iteration5, input_iteration6, dependencies_iteration1, dependencies_iteration2, dependencies_iteration3, dependencies_iteration4, dependencies_iteration5, dependencies_iteration6, stack_intial, stack_iteration1, stack_iteration2, stack_iteration3, stack_iteration4, stack_iteration5, stack_iteration6):
    assert len(input_initial) == 4, test_pen_and_paper_basic_desc(1, len(input_initial), "len(input_initial)")
    assert len(input_iteration1) == 3, test_pen_and_paper_basic_desc(2, len(input_iteration1), "len(input_iteration1)")
    assert len(input_iteration2) == 2, test_pen_and_paper_basic_desc(3, len(input_iteration2), "len(input_iteration2)")
    assert len(input_iteration3) == 2, test_pen_and_paper_basic_desc(4, len(input_iteration3), "len(input_iteration3)")
    assert len(input_iteration4) == 1, test_pen_and_paper_basic_desc(5, len(input_iteration4), "len(input_iteration4)")
    assert len(input_iteration5) == 1, test_pen_and_paper_basic_desc(6, len(input_iteration5), "len(input_iteration5)")
    assert len(input_iteration6) == 1, test_pen_and_paper_basic_desc(7, len(input_iteration6), "len(input_iteration6)")
    assert type(input_initial[0]) == tuple, test_pen_and_paper_basic_desc(8, type(input_initial[0]), "type(input_initial[0])")
    assert len(input_initial[0]) == 2, test_pen_and_paper_basic_desc(9, len(input_initial[0]), "len(input_initial[0])")
    assert type(input_initial[0][0]) == int, test_pen_and_paper_basic_desc(10, type(input_initial[0][0]), "type(input_initial[0][0])")
    assert type(input_initial[0][1]) == str, test_pen_and_paper_basic_desc(11, type(input_initial[0][1]), "type(input_initial[0][1])")
    assert len(dependencies_iteration1) == 0, test_pen_and_paper_basic_desc(12, len(dependencies_iteration1), "len(dependencies_iteration1)")
    assert len(dependencies_iteration2) == 0, test_pen_and_paper_basic_desc(13, len(dependencies_iteration2), "len(dependencies_iteration2)")
    assert len(dependencies_iteration3) == 1, test_pen_and_paper_basic_desc(14, len(dependencies_iteration3), "len(dependencies_iteration3)")
    assert len(dependencies_iteration4) == 1, test_pen_and_paper_basic_desc(15, len(dependencies_iteration4), "len(dependencies_iteration4)")
    assert len(dependencies_iteration5) == 3, test_pen_and_paper_basic_desc(16, len(dependencies_iteration5), "len(dependencies_iteration5)")
    assert len(dependencies_iteration6) == 4, test_pen_and_paper_basic_desc(17, len(dependencies_iteration6), "len(dependencies_iteration6)")
    assert type(dependencies_iteration4[0]) == tuple, test_pen_and_paper_basic_desc(18, type(dependencies_iteration4[0]), "type(dependencies_iteration4[0])")
    assert type(dependencies_iteration4[0][0]) == int, test_pen_and_paper_basic_desc(19, type(dependencies_iteration4[0][0]), "type(dependencies_iteration4[0][0])")
    assert type(dependencies_iteration4[0][1]) == int, test_pen_and_paper_basic_desc(20, type(dependencies_iteration4[0][1]), "type(dependencies_iteration4[0][1])")

