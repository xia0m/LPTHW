from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two no one line, how?

# indata = open(from_file).read()
open(to_file,'w').write(open(from_file).read())

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN  to continue, Ctrl-c to abort")
# input()

# out_file = open(to_file,'w')
# out_file.write(indata)

# print("Alright, all done.")

# out_file.close()

# STUDY DRILLS
# 1. This script is really annoying. There’s no need to ask you before doing the copy, and it prints too much out to the screen. Try to make the script more friendly to use by removing features.

# 2. See how short you can make the script. I could make this one line long.

# 3. Notice at the end of the What You Should See section I used something called cat? It’s an old command that concatenates files together, but mostly it’s just an easy way to print a file to the screen. Type man cat to read about it.

# 4. Find out why you had to write out_file.close() in the code.

# 5. Go read up on Python’s import statement, and start python3.6 to try it out. Try importing some things and see if you can get it right. It’s alright if you do not.
