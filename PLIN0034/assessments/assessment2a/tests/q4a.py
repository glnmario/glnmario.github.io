from otter.test_files import test_case

OK_FORMAT = False

name = "q4a"
points = 15

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




def test_read_conllu_file_desc(line, ret_value, fn_name):
    test_strs = '''
def test_read_conllu_file(read_conllu_file):
    d = read_conllu_file('data/en_ewt-ud-dev.conllu')
    assert len(d) == 2001
    assert isinstance(d, list)
    assert isinstance(d[0], list)
    assert len(d[0]) == 7
    assert isinstance(d[0][0], tuple)
    assert d[0][0][-1] == 3
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=0, hidden=False)
def test_read_conllu_file(read_conllu_file):
    d = read_conllu_file('data/en_ewt-ud-dev.conllu')
    assert len(d) == 2001, test_read_conllu_file_desc(2, len(d), "len(d)")
    assert isinstance(d, list)
    assert isinstance(d[0], list)
    assert len(d[0]) == 7, test_read_conllu_file_desc(5, len(d[0]), "len(d[0])")
    assert isinstance(d[0][0], tuple)
    assert d[0][0][-1] == 3, test_read_conllu_file_desc(7, d[0][0][-1], "d[0][0][-1]")


def test_dependency_parse_desc(line, ret_value, fn_name):
    test_strs = '''
def test_dependency_parse(read_conllu_file, dependency_parse):
    d = read_conllu_file('data/en_ewt-ud-dev.conllu')
    deps = dependency_parse(d[0])
    assert len(deps) == 7
    deps = sorted(deps, key=lambda edge: edge[0])
    for i, dep in enumerate(deps):
        assert isinstance(dep, tuple)
        assert len(dep) == 2
        assert dep[0] == i + 1
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=0, hidden=False)
def test_dependency_parse(read_conllu_file, dependency_parse):
    d = read_conllu_file('data/en_ewt-ud-dev.conllu')
    deps = dependency_parse(d[0])
    assert len(deps) == 7, test_dependency_parse_desc(3, len(deps), "len(deps)")
    deps = sorted(deps, key=lambda edge: edge[0])
    for i, dep in enumerate(deps):
        assert isinstance(dep, tuple)
        assert len(dep) == 2, test_dependency_parse_desc(7, len(dep), "len(dep)")
        assert dep[0] == i + 1, test_dependency_parse_desc(8, dep[0], "dep[0]")

