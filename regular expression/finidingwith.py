import re


phoneNumber = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumber.search("'My number is 415-555-4242.'")
print(f"phone number found {mo.group()}")