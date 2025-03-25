# goal is to check if an input is a valid mobile number...
# the verification is not that strict but it's good enough for now...
# in mowt cases people will use regex for this depending on CONTEXT



def mobile(num):
    num = str(num)
    config = "789"
    
    if len(num) != 10 or not num.isdigit():
        return "NO"
    
    return "YES" if num[0] in config else "NO"


# for example in the US a valid regex to check if a number is valid is this:
import re

def is_valid_format(phone):
    pattern = re.compile(r"^\+?[1-9]\d{1,14}$")  # Supports E.164 format
    return bool(pattern.match(phone))

print(is_valid_format("+14155552671"))  # ✅ True (Valid)
print(is_valid_format("12345"))         # ❌ False (Too short)
# cheerrrrs