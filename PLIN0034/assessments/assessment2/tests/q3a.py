from otter.test_files import test_case

OK_FORMAT = False

name = "q3a"
points = 16

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




def test_feature_extractor_basic_desc(line, ret_value, fn_name):
    test_strs = '''
def test_feature_extractor_basic(extract_features):
    stack1 = [(0, 'ROOT', '_'), (1, 'The', 'DET')]
    input1 = [(2, 'dog', 'NOUN'), (3, 'ate', 'VERB'), (4, 'my', 'DET'), (5, 'homework', 'NOUN')]
    config1 = {'stack': stack1, 'input': input1}
    features_raw = extract_features(config1)
    features_expected = {'input_0_form': 'dog', 'input_0_pos': 'NOUN', 'input_1_form': 'ate', 'input_1_pos': 'VERB', 'input_2_pos': 'DET', 'input_3_pos': 'NOUN', 'stack_0_form': 'The', 'stack_0_pos': 'DET', 'stack_1_pos': '_'}
    for f in features_expected:
        assert features_raw[f] == features_expected[f]
    stack2 = [(0, 'ROOT', '_')]
    input2 = [(1, 'The', 'DET'), (2, 'cat', 'NOUN')]
    config2 = {'stack': stack2, 'input': input2}
    features_raw = extract_features(config2)
    features_expected = {'input_0_form': 'The', 'input_0_pos': 'DET', 'input_1_form': 'cat', 'input_1_pos': 'NOUN', 'input_2_pos': 'N/A', 'input_3_pos': 'N/A', 'stack_0_form': 'ROOT', 'stack_0_pos': '_', 'stack_1_pos': 'N/A'}
    for f in features_expected:
        assert features_raw[f] == features_expected[f]
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=16, hidden=False)
def test_feature_extractor_basic(extract_features):
    stack1 = [(0, 'ROOT', '_'), (1, 'The', 'DET')]
    input1 = [(2, 'dog', 'NOUN'), (3, 'ate', 'VERB'), (4, 'my', 'DET'), (5, 'homework', 'NOUN')]
    config1 = {'stack': stack1, 'input': input1}
    features_raw = extract_features(config1)
    features_expected = {'input_0_form': 'dog', 'input_0_pos': 'NOUN', 'input_1_form': 'ate', 'input_1_pos': 'VERB', 'input_2_pos': 'DET', 'input_3_pos': 'NOUN', 'stack_0_form': 'The', 'stack_0_pos': 'DET', 'stack_1_pos': '_'}
    for f in features_expected:
        assert features_raw[f] == features_expected[f], test_feature_extractor_basic_desc(7, features_raw[f], "features_raw[f]")
    stack2 = [(0, 'ROOT', '_')]
    input2 = [(1, 'The', 'DET'), (2, 'cat', 'NOUN')]
    config2 = {'stack': stack2, 'input': input2}
    features_raw = extract_features(config2)
    features_expected = {'input_0_form': 'The', 'input_0_pos': 'DET', 'input_1_form': 'cat', 'input_1_pos': 'NOUN', 'input_2_pos': 'N/A', 'input_3_pos': 'N/A', 'stack_0_form': 'ROOT', 'stack_0_pos': '_', 'stack_1_pos': 'N/A'}
    for f in features_expected:
        assert features_raw[f] == features_expected[f], test_feature_extractor_basic_desc(14, features_raw[f], "features_raw[f]")

