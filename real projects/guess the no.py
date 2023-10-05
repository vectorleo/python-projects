import random

# for secret no
secret_no = random.randint(1,20)
print("am thinking of a number form 1 to 20....")

#for no of guesses
for guess_taken in range(1,7):
    print("take a guess.")
    guess = int(input())


    if guess < secret_no:
        print("your guess to low.")
    elif guess > secret_no:
        print("your guess to high")
    else:
        break
if guess == secret_no:
    print(f"Good job you have guess my number in {guess_taken} guesses.")
else:
    print(f"Nope,the number i was thinking of was {str(secret_no)} ")

