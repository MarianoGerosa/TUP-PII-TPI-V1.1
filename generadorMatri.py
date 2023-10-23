import random
import string

# get random password pf length 8 with letters, digits, and symbols
def generar():
    characters = string.ascii_letters + string.digits
    cod = ''.join(random.choice(characters) for i in range(8))
    return cod