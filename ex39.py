# create a mapping of state to abbreviation

states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
  'CA':'San Francisco',
  'MI':'Detroit',
  'FL':'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is  ", states['Michigan'])
print("Florida's abbreviation is  ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
  print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
  print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

# STUDY DRILLS
# 1. Do this same kind of mapping with cities and states/regions in your country or some other country.

# 2. Find the Python documentation for dictionaries and try to do even more things to them.

# 3. Find out what you can’t do with dictionaries. A big one is that they do not have order, so try playing with that.