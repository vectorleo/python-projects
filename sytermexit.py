import sys

while True:
    print("type 'exit' to exit")
    response = input(">")
    if response == "exit":
        sys.exit()
    print(f"you type {response}.") 