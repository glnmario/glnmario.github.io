from otter.test_files import test_case

OK_FORMAT = False

name = "q3c"
points = 4

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




def test_train_accuracy_basic_desc(line, ret_value, fn_name):
    test_strs = '''
def test_train_accuracy_basic(train_accuracy):
    if train_accuracy < 1:
        train_accuracy *= 100
    assert train_accuracy < 100
    assert train_accuracy > 1
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=2, hidden=False)
def test_train_accuracy_basic(train_accuracy):
    if train_accuracy < 1:
        train_accuracy *= 100
    assert train_accuracy < 100, test_train_accuracy_basic_desc(3, train_accuracy, "train_accuracy")
    assert train_accuracy > 1, test_train_accuracy_basic_desc(4, train_accuracy, "train_accuracy")

