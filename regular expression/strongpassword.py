import re

passwordcheck1 = re.compile('''
([a-zA-Z0-9]{8,20})
''')
#user_passw = input('enter a password that has at least\nOne capital letter, small letter ,and one number : ')
print(re.__doc__)