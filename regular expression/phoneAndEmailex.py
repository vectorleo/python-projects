import pyperclip , re

phoneNO = re.compile(r'''
(\d{3}|\(\d{3}\)) # area code of phonenumber
(\s|-|\.) #seperator
(\d{3})   #next three digits 
(\s|-|\.) #seperator
(\d{4})   #next 4 number 
(\s*(ext|x|ext.)\s*\d{2,5})? 
''', re.VERBOSE)


email = re.compile(r'''
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
''', re.VERBOSE)




text = str(pyperclip.paste())

matches = []


#todo paste to clipboard