def break_words(stuff):
  """This function will break up words for us."""
  words = stuff.split(' ')
  return words

def sort_words(words):
  """Worts the words."""
  return sorted(words)

def print_first_word(words):
  """Prints the first word after popping it off."""
  word = words.pop(0)
  print(word)

def print_last_word(words):
  """Prints the last word after popping if off."""
  word = words.pop(-1)
  print(word)

def sort_sentence(sentence):
  """Takes in a full sentence and returns the sorted words."""
  words = break_words(sentence)
  return sort_words(words)

def print_first_and_last(sentence):
  """Prints the first and last words of the sentence."""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
  """Sorts the words then prints the first and last one."""
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)

#  1    import ex25
#  2    sentence = "All good things come to those who wait."
#  3    words = ex25.break_words(sentence)
#  4    words
#  5    sorted_words = ex25.sort_words(words)
#  6    sorted_words
#  7    ex25.print_first_word(words)
#  8    ex25.print_last_word(words)
#  9    words
# 10    ex25.print_first_word(sorted_words)
# 11    ex25.print_last_word(sorted_words)
# 12    sorted_words
# 13    sorted_words = ex25.sort_sentence(sentence)
# 14    sorted_words
# 15    ex25.print_first_and_last(sentence)
# 16    ex25.print_first_and_last_sorted(sentence)

# STUDY DRILLS
# 1. Take the remaining lines of the What You Should See output and figure out what they are doing. Make sure you understand how you are running your functions in the ex25 module.

# 2. Try doing this: help(ex25) and also help(ex25.break_words). Notice how you get help for your module and how the help is those odd """ strings you put after each function in ex25? Those special strings are called documentation comments, and we’ll be seeing more of them.

# 3. Typing ex25. is annoying. A shortcut is to do your import like this: from ex25 import *. This is like saying, “Import everything from ex25.” Programmers like saying things backward. Start a new session and see how all your functions are right there.

# 4. Try breaking your file and see what it looks like in python when you use it. You will have to quit python with quit() to be able to reload it.