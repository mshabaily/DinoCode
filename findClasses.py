# Function that finds class definitions within a string of code
# Currently configured to recognise python syntax using regular expressions
# Values returned:
#   - class name
#   - class attributes
#   - init method + parameters
#   - destructor / deinitialiser method
#   - other methods

import re

code = input()
print (findClasses(code))

def findClasses(code : str):

    classes = re.findall("^class.*(?:\n|$)")
   
    return classes