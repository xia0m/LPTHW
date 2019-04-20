def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")

print("We can just give the function name directly")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("WE can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the tow, variables and math")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers + 1000)

# STUDY DRILLS
# 1. Go back through the script and type a comment above each line explaining in English what it does.

# 2. Start at the bottom and read each line backward, saying all the important characters.

# 3. Write at least one more function of your own design, and run it 10 different ways.