# Symbol Review

# and #
tf = (True and False)
print(tf)

# as #

# assert #
assert 3%2==1,"condition is false"

# break # # continue #
for val in "string":
  if val == "i":
      continue # break
      # with break, output is s t r the end
      # with continue, output is s t r n g end
  print(val)
print("The end")

# class #

# del #
x = ["apple", "banana", "cherry"]
del x[0]
print(x)

#elif else #

# except # 
try:
  print(y)
except:
  print("An exception occurred")

#  finally # 
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
# raise #  Raise an exception when things go wrong

# exec #
exec 'print("hello")'

# for #
for x in range(1,6):
  print(x)
