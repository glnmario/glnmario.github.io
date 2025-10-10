from otter.test_files import test_case

OK_FORMAT = False

name = "q3"
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
 


def test_read_all_lines_desc(line, ret_value, fn_name):
    test_strs = '''
def test_read_all_lines(read_all_lines):
  file_name = "data/t8.shakespeare.processed.txt"
  lines = read_all_lines(file_name)
  not_counter = 0
  for line in lines:
    if " not " in line:
      not_counter += 1
  assert not_counter == 5155

    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def test_read_all_lines(read_all_lines):
  file_name = "data/t8.shakespeare.processed.txt"
  lines = read_all_lines(file_name)
  not_counter = 0
  for line in lines:
    if " not " in line:
      not_counter += 1
  assert not_counter == 5155, test_read_all_lines_desc(7, not_counter, "not_counter")


def test_process_file_desc(line, ret_value, fn_name):
    test_strs = '''
def test_process_file(process_file):
  file_name = "data/t8.shakespeare.processed.txt"
  lines = process_file(file_name)
  not_counter = 0
  for line in lines:
    if " not " in line:
      not_counter += 1
  assert not_counter == 6809

    '''.split("\n")
    return format_error(test_strs, line, ret_value, fn_name)

@test_case(points=None, hidden=False)
def test_process_file(process_file):
  file_name = "data/t8.shakespeare.processed.txt"
  lines = process_file(file_name)
  not_counter = 0
  for line in lines:
    if " not " in line:
      not_counter += 1
  assert not_counter == 6809, test_process_file_desc(7, not_counter, "not_counter")

