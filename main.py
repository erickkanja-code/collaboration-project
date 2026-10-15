    print("=" * 40)


def play_game(stats):
    clear_screen()
    difficulty, code_length, max_attempts = choose_difficulty()
    secret_code = "".join(
        str(random.randint(0, 9)) for _ in range(code_length)
    )
    attempts = 0
    won = False
    started_at = time.time()

    print("\n" + "=" * 40)
    type_text("   C O D E B R E A K E R   v2.0")
    print("=" * 40)
    type_text("\n[ SYSTEM ] Secure terminal accessed...")
    type_text(f"[ SYSTEM ] Difficulty: {difficulty}")
    type_text(f"[ SYSTEM ] Code length: {code_length} digits")
    type_text(f"[ SYSTEM ] You have {max_attempts} attempts.")
    print("\nType 'hint' for a hint, or 'quit' to end the round.")
    print("Leading zeroes are allowed.\n")

    while attempts < max_attempts:
        guess = input(
            f"Attempt {attempts + 1}/{max_attempts} >> "
        ).strip().lower()

        if guess == "quit":
            print(f"Round ended. The code was {secret_code}.")
            break

        if guess == "hint":
            # A hint reveals one digit and its position without changing attempts.
            position = random.randrange(code_length)
            print(
                f"[ HINT ] Position {position + 1} contains "
                f"the digit {secret_code[position]}.\n"
            )
            continue

        if not guess.isdigit() or len(guess) != code_length:
            print(f"[ ERROR ] Enter exactly {code_length} digits.\n")
            continue

        attempts += 1

        if guess == secret_code:
            won = True
            type_text("\n[ ACCESS GRANTED ]", 0.04)
            type_text("You cracked the code!")
            print(f"Code: {secret_code}")
            print(f"Attempts used: {attempts}")
            print(f"Time taken: {int(time.time() - started_at)} seconds")
            break

        correct_positions = sum(
            guess[i] == secret_code[i] for i in range(code_length)
        )
        correct_digits = sum(
            min(guess.count(digit), secret_code.count(digit))
            for digit in set(guess)
        )

        print(f"Correct position(s): {correct_positions}")
        print(f"Correct digit(s), any position: {correct_digits}\n")

    else:
        type_text("\n[ ACCESS DENIED ]", 0.04)
        print(f"The secret code was {secret_code}")

    stats["games_played"] += 1
    if won:
        stats["games_won"] += 1
        if (
            stats["best_attempts"] is None
            or attempts < stats["best_attempts"]
        ):
            stats["best_attempts"] = attempts

    stats["history"].append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "won": won,
        "difficulty": difficulty,
        "attempts": attempts,
    })
    stats["history"] = stats["history"][-20:]
    save_stats(stats)


def main():
    stats = load_stats()

    while True:
        print("\n" + "=" * 40)
        print("       C O D E B R E A K E R")
        print("=" * 40)
        print("1. Play")
        print("2. View statistics")
        print("3. Exit")

        choice = input("Select an option >> ").strip()

        if choice == "1":
            play_game(stats)
        elif choice == "2":
            show_stats(stats)
        elif choice == "3":
            print("Disconnecting from terminal...")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
