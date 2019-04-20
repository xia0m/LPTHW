from sys import argv

script, input_file = argv

def print_all(f):
  print(f.read())

def rewind(f):
  f.seek(0)

def print_a_line(line_count,f):
  print(line_count, f.readline())

current_file = open(input_file)

print("First Let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three line:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

# STUDY DRILLS
# 1. Write an English comment for each line to understand what that line does.

# 2. Each time print_a_line is run, you are passing in a variable, current_line. Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.

# 3. Find each place a function is used, and check its def to make sure that you are giving it the right arguments.

# 4. Research online what the seek function for file does. Try pydoc file, and see if you can figure it out from there. Then try pydoc file.seek to see what seek does.

# 5. Research the shorthand notation +=, and rewrite the script to use += instead.