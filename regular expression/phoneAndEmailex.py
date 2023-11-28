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

for group in phoneNO.findall(text):
    phonenumber = "-".join([group[1],group[3],group[5]])
    if group[6] != " ":
        phonenumber += " x" + group[6]
    matches.append(phonenumber)
for groups in email.findall(text):
    matches.append(group[0])

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("copied to clipboard: ")
    print("\n".join(matches))
else:
    print('No phone numbers or email addresses found.')



#todo paste to clipboard