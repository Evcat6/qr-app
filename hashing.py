import random;
import string;


alphabet_string_lower = string.ascii_lowercase
alphabet_string_upper = string.ascii_uppercase

alphabet_list = list(alphabet_string_lower)

alphabet_list_upper = list(alphabet_string_upper)

string_hash = ""
res_hash = ""

def list_to_String(list):
    str = ""
    return str.join(list)

def string_randomizer(array_lower, array_upper):
    result = []
    for i in range(1, 5):
        result += array_lower[random.randint(0, len(array_lower) - 1)]
        result += array_upper[random.randint(0, len(array_upper) - 1)]
    return list_to_String(result)

def hashing():
    return str(random.randint(10000, 99999))