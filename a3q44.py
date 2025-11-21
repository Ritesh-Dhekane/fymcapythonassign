print("Name = Ritesh Dhekane")

import re

print("Name = Ritesh Dhekane")

def is_valid_pibm(identifier):
    pattern = r'^[a-k][0369][a-zA-Z0-9#]*$'

    if re.match(pattern, identifier):
        print("Valid PIBM Identifier")
    else:
        print("Invalid PIBM Identifier")

# Take input from user
inp = input("Enter a PIBM language identifier: ")
is_valid_pibm(inp)
