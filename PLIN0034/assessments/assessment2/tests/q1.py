from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
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




def test_conllu_reader_basic_desc(line, ret_value, fn_name):
    test_strs = '''
def test_conllu_reader_basic(read_conllu_file):
    sentences = read_conllu_file('data/en_ewt-ud-dev.conllu')
    assert len(sentences) == 2001
    s = sentences[0]
    words = [x[0] for x in s]
    words_expected = ['From', 'the', 'AP', 'comes', 'this', 'story', ':']
    assert words == words_expected
    tags = [x[1] for x in s]
    tags_expected = ['ADP', 'DET', 'PROPN', 'VERB', 'DET', 'NOUN', 'PUNCT']
    assert tags == tags_expected
    s = sentences[-1]
    words = [x[0] for x in s]
    words_expected = ['Also', ',', 'they', 'have', 'great', 'customer', 'service', 'and', 'a', 'very', 'knowledgeable', 'staff']
    assert words == words_expected
    tags = [x[1] for x in s]
    tags_expected = ['ADV', 'PUNCT', 'PRON', 'VERB', 'ADJ', 'NOUN', 'NOUN', 'CCONJ', 'DET', 'ADV', 'ADJ', 'NOUN']
    assert tags == tags_expected
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)


@test_case(points=8, hidden=False)
def test_conllu_reader_basic(read_conllu_file):
    sentences = read_conllu_file('data/en_ewt-ud-dev.conllu')
    assert len(sentences) == 2001, test_conllu_reader_basic_desc(2, len(sentences), "len(sentences)")
    s = sentences[0]
    words = [x[0] for x in s]
    words_expected = ['From', 'the', 'AP', 'comes', 'this', 'story', ':']
    assert words == words_expected, test_conllu_reader_basic_desc(6, words, "words")
    tags = [x[1] for x in s]
    tags_expected = ['ADP', 'DET', 'PROPN', 'VERB', 'DET', 'NOUN', 'PUNCT']
    assert tags == tags_expected, test_conllu_reader_basic_desc(9, tags, "tags")
    s = sentences[-1]
    words = [x[0] for x in s]
    words_expected = ['Also', ',', 'they', 'have', 'great', 'customer', 'service', 'and', 'a', 'very', 'knowledgeable', 'staff']
    assert words == words_expected, test_conllu_reader_basic_desc(13, words, "words")
    tags = [x[1] for x in s]
    tags_expected = ['ADV', 'PUNCT', 'PRON', 'VERB', 'ADJ', 'NOUN', 'NOUN', 'CCONJ', 'DET', 'ADV', 'ADJ', 'NOUN']
    assert tags == tags_expected, test_conllu_reader_basic_desc(16, tags, "tags")

