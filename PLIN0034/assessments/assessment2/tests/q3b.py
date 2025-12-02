from otter.test_files import test_case

OK_FORMAT = False

name = "q3b"
points = 10

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




def test_vectoriser_basic_desc(line, ret_value, fn_name):
    test_strs = '''
def test_vectoriser_basic(vectoriser):
    from sklearn.feature_extraction import DictVectorizer
    assert isinstance(vectoriser, DictVectorizer) == True
    assert hasattr(vectoriser, 'feature_names_') == True
    assert len(vectoriser.feature_names_) > 0
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=2.5, hidden=False)
def test_vectoriser_basic(vectoriser):
    from sklearn.feature_extraction import DictVectorizer
    assert isinstance(vectoriser, DictVectorizer) == True, test_vectoriser_basic_desc(2, isinstance(vectoriser, DictVectorizer), "isinstance(vectoriser, DictVectorizer)")
    assert hasattr(vectoriser, 'feature_names_') == True, test_vectoriser_basic_desc(3, hasattr(vectoriser, 'feature_names_'), "hasattr(vectoriser, 'feature_names_')")
    assert len(vectoriser.feature_names_) > 0, test_vectoriser_basic_desc(4, len(vectoriser.feature_names_), "len(vectoriser.feature_names_)")


def test_classifier_basic_desc(line, ret_value, fn_name):
    test_strs = '''
def test_classifier_basic(classifier):
    from sklearn.linear_model import LogisticRegression
    assert isinstance(classifier, LogisticRegression) == True
    assert hasattr(classifier, 'classes_') == True
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=2.5, hidden=False)
def test_classifier_basic(classifier):
    from sklearn.linear_model import LogisticRegression
    assert isinstance(classifier, LogisticRegression) == True, test_classifier_basic_desc(2, isinstance(classifier, LogisticRegression), "isinstance(classifier, LogisticRegression)")
    assert hasattr(classifier, 'classes_') == True, test_classifier_basic_desc(3, hasattr(classifier, 'classes_'), "hasattr(classifier, 'classes_')")

