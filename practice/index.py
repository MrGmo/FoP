import re

some_string = 'Hello@12345@####'
matches = re.split('@', some_string)

print(matches)