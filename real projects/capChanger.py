
import pyperclip
# I saw a problem in typing the title and coming back to change the first letter to capital or the whole text.🤓
text = pyperclip.paste()
word = text.split(" ")
changed = []
def change_first():
    for i in word:
        changed.append(i.title())
    pyperclip.copy(" ".join(changed))
    print("it done.😇")
        
def change_all():
    for i in word:
        changed.append(i.upper())
    pyperclip.copy(" ".join(changed))
    print("it done.😇") 
def first_re():
    choices = str(input("""
press (1)to capitalize the first letter
press (2)to capitalize all letters:"""))
    if choices == "1" or choices == "(1)":
        change_first()
    elif choices == "2" or choices == "(2)":
        change_all()
    else:
        print("try again")

first_re()
