from otter.test_files import test_case

OK_FORMAT = False

name = "q2"
points = None

def format_error(lines, line, ret_value="", fn_name=""):
  return_str = "\n\n"
  return_str += "The last line of the following test program failed.\n"
  return_str += "Make sure that your function returns exactly the same value\n"
  return_str += "as specified in the <b>assert</b> statement.\n\n"
  
  num_spaces = len(lines[2]) - len(lines[2].strip()) 
  return_str += "\n".join([l[num_spaces:] for l in lines[2:line+1]])
  return_str += "\n<b>"
  return_str += lines[line+1][num_spaces:]
  return_str += "</b>\n\n"

  
  return_str += f"{fn_name} returned:\n"
  return_str += str(ret_value)
  return_str += "\n\n"
  
  return return_str  
 


def normalise_negation_v1_test_desc(line, ret_value, fn_name):
    test_strs = '''
def normalise_negation_v1_test(normalise_negation_v1):
  assert normalise_negation_v1("I wouldn't know") == "I would not know"
  assert normalise_negation_v1("I shouldn't know") == "I should not know"
  assert normalise_negation_v1("He isn't tall") == "He is not tall"
  assert normalise_negation_v1("Don't you think?") == "Don't you think?"
  assert normalise_negation_v1("I won't") == "I won't"
  assert normalise_negation_v1("I abcshouldn't know") == "I abcshould not know"



    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def normalise_negation_v1_test(normalise_negation_v1):
  assert normalise_negation_v1("I wouldn't know") == "I would not know", normalise_negation_v1_test_desc(1, normalise_negation_v1("I wouldn't know"), "normalise_negation_v1(\"I wouldn't know\")")
  assert normalise_negation_v1("I shouldn't know") == "I should not know", normalise_negation_v1_test_desc(2, normalise_negation_v1("I shouldn't know"), "normalise_negation_v1(\"I shouldn't know\")")
  assert normalise_negation_v1("He isn't tall") == "He is not tall", normalise_negation_v1_test_desc(3, normalise_negation_v1("He isn't tall"), "normalise_negation_v1(\"He isn't tall\")")
  assert normalise_negation_v1("Don't you think?") == "Don't you think?", normalise_negation_v1_test_desc(4, normalise_negation_v1("Don't you think?"), "normalise_negation_v1(\"Don't you think?\")")
  assert normalise_negation_v1("I won't") == "I won't", normalise_negation_v1_test_desc(5, normalise_negation_v1("I won't"), "normalise_negation_v1(\"I won't\")")
  assert normalise_negation_v1("I abcshouldn't know") == "I abcshould not know", normalise_negation_v1_test_desc(6, normalise_negation_v1("I abcshouldn't know"), "normalise_negation_v1(\"I abcshouldn't know\")")




def normalise_negation_v2_test_desc(line, ret_value, fn_name):
    test_strs = '''
def normalise_negation_v2_test(normalise_negation_v2):
  assert normalise_negation_v2("I wouldn't know") == "I would not know"
  assert normalise_negation_v2("I shouldn't know") == "I should not know"
  assert normalise_negation_v2("He isn't tall") == "He is not tall"
  assert normalise_negation_v2("Don't you think?") == "Do not you think?"
  assert normalise_negation_v2("I won't") == "I won't"
  assert normalise_negation_v2("I SHOULDN'T know") == "I SHOULD not know"
  assert normalise_negation_v2("I ShOULDN'T know") == "I ShOULD not know"
  assert normalise_negation_v2("I ShOULdN'T know") == "I ShOULd not know"
  assert normalise_negation_v2("I abcShOULdN'T know") == "I abcShOULd not know"


    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def normalise_negation_v2_test(normalise_negation_v2):
  assert normalise_negation_v2("I wouldn't know") == "I would not know", normalise_negation_v2_test_desc(1, normalise_negation_v2("I wouldn't know"), "normalise_negation_v2(\"I wouldn't know\")")
  assert normalise_negation_v2("I shouldn't know") == "I should not know", normalise_negation_v2_test_desc(2, normalise_negation_v2("I shouldn't know"), "normalise_negation_v2(\"I shouldn't know\")")
  assert normalise_negation_v2("He isn't tall") == "He is not tall", normalise_negation_v2_test_desc(3, normalise_negation_v2("He isn't tall"), "normalise_negation_v2(\"He isn't tall\")")
  assert normalise_negation_v2("Don't you think?") == "Do not you think?", normalise_negation_v2_test_desc(4, normalise_negation_v2("Don't you think?"), "normalise_negation_v2(\"Don't you think?\")")
  assert normalise_negation_v2("I won't") == "I won't", normalise_negation_v2_test_desc(5, normalise_negation_v2("I won't"), "normalise_negation_v2(\"I won't\")")
  assert normalise_negation_v2("I SHOULDN'T know") == "I SHOULD not know", normalise_negation_v2_test_desc(6, normalise_negation_v2("I SHOULDN'T know"), "normalise_negation_v2(\"I SHOULDN'T know\")")
  assert normalise_negation_v2("I ShOULDN'T know") == "I ShOULD not know", normalise_negation_v2_test_desc(7, normalise_negation_v2("I ShOULDN'T know"), "normalise_negation_v2(\"I ShOULDN'T know\")")
  assert normalise_negation_v2("I ShOULdN'T know") == "I ShOULd not know", normalise_negation_v2_test_desc(8, normalise_negation_v2("I ShOULdN'T know"), "normalise_negation_v2(\"I ShOULdN'T know\")")
  assert normalise_negation_v2("I abcShOULdN'T know") == "I abcShOULd not know", normalise_negation_v2_test_desc(9, normalise_negation_v2("I abcShOULdN'T know"), "normalise_negation_v2(\"I abcShOULdN'T know\")")



def normalise_negation_test_desc(line, ret_value, fn_name):
    test_strs = '''
def normalise_negation_test(normalise_negation):
  assert normalise_negation("I won't.") ==  "I won't."
  assert normalise_negation("Don't you think?") ==  "Do not you think?"
  assert normalise_negation("I WOULDN'T KNOW") ==  "I WOULD not KNOW"
  assert normalise_negation("I sHoUlDn'T!") ==  "I sHoUlD not!"
  assert normalise_negation("He isn't tall.") ==  "He is not tall."
  assert normalise_negation("They aren't in Spain.") ==  "They are not in Spain."
  assert normalise_negation("They weren't in Spain.") ==  "They weren't in Spain."
  assert normalise_negation("I abcshouldn't") ==  "I abcshouldn't"
  assert normalise_negation("I shouldn'tabc") ==  "I shouldn'tabc"
  assert normalise_negation("I shouldn't, though") ==  "I should not, though"
  assert normalise_negation("I shouldn't? Oh!") ==  "I should not? Oh!"
  assert normalise_negation("I shouldn't! Oh!") ==  "I should not! Oh!"




    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def normalise_negation_test(normalise_negation):
  assert normalise_negation("I won't.") ==  "I won't.", normalise_negation_test_desc(1, normalise_negation("I won't."), "normalise_negation(\"I won't.\")")
  assert normalise_negation("Don't you think?") ==  "Do not you think?", normalise_negation_test_desc(2, normalise_negation("Don't you think?"), "normalise_negation(\"Don't you think?\")")
  assert normalise_negation("I WOULDN'T KNOW") ==  "I WOULD not KNOW", normalise_negation_test_desc(3, normalise_negation("I WOULDN'T KNOW"), "normalise_negation(\"I WOULDN'T KNOW\")")
  assert normalise_negation("I sHoUlDn'T!") ==  "I sHoUlD not!", normalise_negation_test_desc(4, normalise_negation("I sHoUlDn'T!"), "normalise_negation(\"I sHoUlDn'T!\")")
  assert normalise_negation("He isn't tall.") ==  "He is not tall.", normalise_negation_test_desc(5, normalise_negation("He isn't tall."), "normalise_negation(\"He isn't tall.\")")
  assert normalise_negation("They aren't in Spain.") ==  "They are not in Spain.", normalise_negation_test_desc(6, normalise_negation("They aren't in Spain."), "normalise_negation(\"They aren't in Spain.\")")
  assert normalise_negation("They weren't in Spain.") ==  "They weren't in Spain.", normalise_negation_test_desc(7, normalise_negation("They weren't in Spain."), "normalise_negation(\"They weren't in Spain.\")")
  assert normalise_negation("I abcshouldn't") ==  "I abcshouldn't", normalise_negation_test_desc(8, normalise_negation("I abcshouldn't"), "normalise_negation(\"I abcshouldn't\")")
  assert normalise_negation("I shouldn'tabc") ==  "I shouldn'tabc", normalise_negation_test_desc(9, normalise_negation("I shouldn'tabc"), "normalise_negation(\"I shouldn'tabc\")")
  assert normalise_negation("I shouldn't, though") ==  "I should not, though", normalise_negation_test_desc(10, normalise_negation("I shouldn't, though"), "normalise_negation(\"I shouldn't, though\")")
  assert normalise_negation("I shouldn't? Oh!") ==  "I should not? Oh!", normalise_negation_test_desc(11, normalise_negation("I shouldn't? Oh!"), "normalise_negation(\"I shouldn't? Oh!\")")
  assert normalise_negation("I shouldn't! Oh!") ==  "I should not! Oh!", normalise_negation_test_desc(12, normalise_negation("I shouldn't! Oh!"), "normalise_negation(\"I shouldn't! Oh!\")")




