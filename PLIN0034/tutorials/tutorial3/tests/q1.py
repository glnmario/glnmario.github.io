from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
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
 


def find_all_pets_test_desc(line, ret_value, fn_name):
    test_strs = '''
def find_all_pets_test(find_all_pets):
  assert find_all_pets("Judith has a dog and 12 cats") == ['dog', 'cat']
  assert find_all_pets("Cats are fluffier than dogs") == ['Cat', 'dog']
  assert find_all_pets("catcatcatcatcat") == ['cat', 'cat', 'cat', 'cat', 'cat']
  assert find_all_pets("The hungry caterpillar") == ['cat']
  assert find_all_pets("Of Mice and Men") == []
  assert find_all_pets("Dognition") == ['Dog']

    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def find_all_pets_test(find_all_pets):
  assert find_all_pets("Judith has a dog and 12 cats") == ['dog', 'cat'], find_all_pets_test_desc(1, find_all_pets("Judith has a dog and 12 cats"), "find_all_pets(\"Judith has a dog and 12 cats\")")
  assert find_all_pets("Cats are fluffier than dogs") == ['Cat', 'dog'], find_all_pets_test_desc(2, find_all_pets("Cats are fluffier than dogs"), "find_all_pets(\"Cats are fluffier than dogs\")")
  assert find_all_pets("catcatcatcatcat") == ['cat', 'cat', 'cat', 'cat', 'cat'], find_all_pets_test_desc(3, find_all_pets("catcatcatcatcat"), "find_all_pets(\"catcatcatcatcat\")")
  assert find_all_pets("The hungry caterpillar") == ['cat'], find_all_pets_test_desc(4, find_all_pets("The hungry caterpillar"), "find_all_pets(\"The hungry caterpillar\")")
  assert find_all_pets("Of Mice and Men") == [], find_all_pets_test_desc(5, find_all_pets("Of Mice and Men"), "find_all_pets(\"Of Mice and Men\")")
  assert find_all_pets("Dognition") == ['Dog'], find_all_pets_test_desc(6, find_all_pets("Dognition"), "find_all_pets(\"Dognition\")")


def find_all_pets_with_spaces_test_desc(line, ret_value, fn_name):
    test_strs = '''
def find_all_pets_with_spaces_test(find_all_pets_with_spaces):
  assert find_all_pets_with_spaces("Judith has a dog and 12 cats and a rooster.") == ['dog']
  assert find_all_pets_with_spaces("Judith has a dog and a cat and a rooster.") == ['dog', 'cat']
  assert find_all_pets_with_spaces("Judith has a dog and a cat.") == ['dog']
  assert find_all_pets_with_spaces("Cat is a type of animal.") == []
  assert find_all_pets_with_spaces("Cats are fluffier than dogs") == []
  assert find_all_pets_with_spaces("catcatcatcatcat") == []
  assert find_all_pets_with_spaces("The hungry caterpillar") == []
  assert find_all_pets_with_spaces("Of Mice and Men") == []
  assert find_all_pets_with_spaces("Dognition") == []


    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def find_all_pets_with_spaces_test(find_all_pets_with_spaces):
  assert find_all_pets_with_spaces("Judith has a dog and 12 cats and a rooster.") == ['dog'], find_all_pets_with_spaces_test_desc(1, find_all_pets_with_spaces("Judith has a dog and 12 cats and a rooster."), "find_all_pets_with_spaces(\"Judith has a dog and 12 cats and a rooster.\")")
  assert find_all_pets_with_spaces("Judith has a dog and a cat and a rooster.") == ['dog', 'cat'], find_all_pets_with_spaces_test_desc(2, find_all_pets_with_spaces("Judith has a dog and a cat and a rooster."), "find_all_pets_with_spaces(\"Judith has a dog and a cat and a rooster.\")")
  assert find_all_pets_with_spaces("Judith has a dog and a cat.") == ['dog'], find_all_pets_with_spaces_test_desc(3, find_all_pets_with_spaces("Judith has a dog and a cat."), "find_all_pets_with_spaces(\"Judith has a dog and a cat.\")")
  assert find_all_pets_with_spaces("Cat is a type of animal.") == [], find_all_pets_with_spaces_test_desc(4, find_all_pets_with_spaces("Cat is a type of animal."), "find_all_pets_with_spaces(\"Cat is a type of animal.\")")
  assert find_all_pets_with_spaces("Cats are fluffier than dogs") == [], find_all_pets_with_spaces_test_desc(5, find_all_pets_with_spaces("Cats are fluffier than dogs"), "find_all_pets_with_spaces(\"Cats are fluffier than dogs\")")
  assert find_all_pets_with_spaces("catcatcatcatcat") == [], find_all_pets_with_spaces_test_desc(6, find_all_pets_with_spaces("catcatcatcatcat"), "find_all_pets_with_spaces(\"catcatcatcatcat\")")
  assert find_all_pets_with_spaces("The hungry caterpillar") == [], find_all_pets_with_spaces_test_desc(7, find_all_pets_with_spaces("The hungry caterpillar"), "find_all_pets_with_spaces(\"The hungry caterpillar\")")
  assert find_all_pets_with_spaces("Of Mice and Men") == [], find_all_pets_with_spaces_test_desc(8, find_all_pets_with_spaces("Of Mice and Men"), "find_all_pets_with_spaces(\"Of Mice and Men\")")
  assert find_all_pets_with_spaces("Dognition") == [], find_all_pets_with_spaces_test_desc(9, find_all_pets_with_spaces("Dognition"), "find_all_pets_with_spaces(\"Dognition\")")



def find_actually_all_pets_test_desc(line, ret_value, fn_name):
    test_strs = '''
def find_actually_all_pets_test(find_actually_all_pets):
  assert find_actually_all_pets("Judith has a dog, a Cat, and a rooster.") == ['dog', 'Cat']
  assert find_actually_all_pets("Judith has a dog and 12 cats.") == ['dog', 'cat']
  assert find_actually_all_pets("Judith has a dog and a cat.") == ['dog', 'cat']
  assert find_actually_all_pets("Cat is a type of animal.") == ['Cat']
  assert find_actually_all_pets("Cats are fluffier than dogs") == ['Cat', 'dog']
  assert find_actually_all_pets("catcatcatcatcat") == []
  assert find_actually_all_pets("The hungry caterpillar") == []
  assert find_actually_all_pets("Of Mice and Men") == []
  assert find_actually_all_pets("Dognition") == []


    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def find_actually_all_pets_test(find_actually_all_pets):
  assert find_actually_all_pets("Judith has a dog, a Cat, and a rooster.") == ['dog', 'Cat'], find_actually_all_pets_test_desc(1, find_actually_all_pets("Judith has a dog, a Cat, and a rooster."), "find_actually_all_pets(\"Judith has a dog, a Cat, and a rooster.\")")
  assert find_actually_all_pets("Judith has a dog and 12 cats.") == ['dog', 'cat'], find_actually_all_pets_test_desc(2, find_actually_all_pets("Judith has a dog and 12 cats."), "find_actually_all_pets(\"Judith has a dog and 12 cats.\")")
  assert find_actually_all_pets("Judith has a dog and a cat.") == ['dog', 'cat'], find_actually_all_pets_test_desc(3, find_actually_all_pets("Judith has a dog and a cat."), "find_actually_all_pets(\"Judith has a dog and a cat.\")")
  assert find_actually_all_pets("Cat is a type of animal.") == ['Cat'], find_actually_all_pets_test_desc(4, find_actually_all_pets("Cat is a type of animal."), "find_actually_all_pets(\"Cat is a type of animal.\")")
  assert find_actually_all_pets("Cats are fluffier than dogs") == ['Cat', 'dog'], find_actually_all_pets_test_desc(5, find_actually_all_pets("Cats are fluffier than dogs"), "find_actually_all_pets(\"Cats are fluffier than dogs\")")
  assert find_actually_all_pets("catcatcatcatcat") == [], find_actually_all_pets_test_desc(6, find_actually_all_pets("catcatcatcatcat"), "find_actually_all_pets(\"catcatcatcatcat\")")
  assert find_actually_all_pets("The hungry caterpillar") == [], find_actually_all_pets_test_desc(7, find_actually_all_pets("The hungry caterpillar"), "find_actually_all_pets(\"The hungry caterpillar\")")
  assert find_actually_all_pets("Of Mice and Men") == [], find_actually_all_pets_test_desc(8, find_actually_all_pets("Of Mice and Men"), "find_actually_all_pets(\"Of Mice and Men\")")
  assert find_actually_all_pets("Dognition") == [], find_actually_all_pets_test_desc(9, find_actually_all_pets("Dognition"), "find_actually_all_pets(\"Dognition\")")



def find_all_hashtags_test_desc(line, ret_value, fn_name):
    test_strs = '''
def find_all_hashtags_test(find_all_hashtags):
  assert find_all_hashtags("#Olympics2024 in France") == ['#Olympics2024']
  assert find_all_hashtags("The#Olympics2024 in France") == []
  assert find_all_hashtags("The #Olympics2024 in France") == ['#Olympics2024']
  assert find_all_hashtags("#Olympics2024 in #France") == ['#Olympics2024', '#France']
  assert find_all_hashtags("The #Olympics_2024 were in #France.") == ['#Olympics_2024', '#France']
    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def find_all_hashtags_test(find_all_hashtags):
  assert find_all_hashtags("#Olympics2024 in France") == ['#Olympics2024'], find_all_hashtags_test_desc(1, find_all_hashtags("#Olympics2024 in France"), "find_all_hashtags(\"#Olympics2024 in France\")")
  assert find_all_hashtags("The#Olympics2024 in France") == [], find_all_hashtags_test_desc(2, find_all_hashtags("The#Olympics2024 in France"), "find_all_hashtags(\"The#Olympics2024 in France\")")
  assert find_all_hashtags("The #Olympics2024 in France") == ['#Olympics2024'], find_all_hashtags_test_desc(3, find_all_hashtags("The #Olympics2024 in France"), "find_all_hashtags(\"The #Olympics2024 in France\")")
  assert find_all_hashtags("#Olympics2024 in #France") == ['#Olympics2024', '#France'], find_all_hashtags_test_desc(4, find_all_hashtags("#Olympics2024 in #France"), "find_all_hashtags(\"#Olympics2024 in #France\")")
  assert find_all_hashtags("The #Olympics_2024 were in #France.") == ['#Olympics_2024', '#France'], find_all_hashtags_test_desc(5, find_all_hashtags("The #Olympics_2024 were in #France."), "find_all_hashtags(\"The #Olympics_2024 were in #France.\")")
