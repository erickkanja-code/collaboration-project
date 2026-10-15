
import random
import time
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def type_text(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def play_game():
    clear_screen()

    secret_code = str(random.randint(1000, 9999))
    attempts = 0
    max_attempts = 7

    print("=" * 40)
    type_text("   C O D E B R E A K E R   v1.0")
    print("=" * 40)

    type_text("\n[ SYSTEM ] Secure terminal accessed...")
    time.sleep(0.5)
    type_text("[ SYSTEM ] Secret code generated.")
    type_text("[ SYSTEM ] You have 7 attempts to crack it.\n")

    print("Guess the 4-digit code.")
    print("HINT: I'll tell you how many digits are correct.\n")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts} >> ")

        if not guess.isdigit() or len(guess) != 4:
            print("[ ERROR ] Enter exactly 4 digits.\n")
            continue

        attempts += 1

        if guess == secret_code:
            type_text("\n[ ACCESS GRANTED ]", 0.08)
            type_text("You cracked the code!")
            print(f"Code: {secret_code}")
            print(f"Attempts used: {attempts}")
            break

        correct_positions = sum(
            guess[i] == secret_code[i] for i in range(4)
        )

        correct_digits = sum(
            min(guess.count(digit), secret_code.count(digit))
            for digit in set(guess)
        )

        print(f"Digits in the correct position: {correct_positions}")
        print(f"Correct digits in any position: {correct_digits}\n")

    else:
        type_text("\n[ ACCESS DENIED ]", 0.08)
        print(f"The secret code was {secret_code}")

    print("\n" + "=" * 40)

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()

        if again != "y":
            print("Disconnecting from terminal...")
            break
