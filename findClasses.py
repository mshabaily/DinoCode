# Function that finds class definitions within a string of code
# Currently configured to recognise python syntax using regular expressions
# Values returned:
#   - class name
#   - class attributes
#   - init method + parameters
#   - destructor / deinitialiser method
#   - other methods

import re

def findClasses(code : str):
    pattern = re.compile("""put magic regex here""")
    classes = pattern.finditer(code)

    return classes