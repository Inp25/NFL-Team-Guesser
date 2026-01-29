import time

# NFL Team Guesser Game
while True:
    name = input("What is your name? ").strip()
    while name == "":
        name = input("Please enter your name: ").strip()

    print("Hello", name + "!")
    print("Welcome to the NFL Team Guesser!")

    sb = input("How many Super Bowl wins does your team have? ").strip()
    while not sb.isdigit() or int(sb) < 0 or int(sb) > 7:
        sb = input("Please enter a number between 0 and 7: ").strip()
    sb = int(sb)

    found = False

    # Easter egg
    if sb == 7:
        print("Wait... no team has 7! Are you Tom Brady? 🐐")
        found = True

    elif sb == 0:
        conf = input("Is your team in the AFC or NFC? ").strip().upper()
        while conf not in ["AFC", "NFC"]:
            conf = input("Please type AFC or NFC: ").strip().upper()
        if conf == "AFC":
            for team in ["Cleveland Browns", "Houston Texans", "Jacksonville Jaguars"]:
                ans = input(f"Is your team the {team}? (yes/no): ").strip().lower()
                if ans == "yes":
                    print(f"Nice! Your team is the {team}!")
                    found = True
                    break
        else:
            for team in ["Detroit Lions", "Minnesota Vikings", "Carolina Panthers", "Atlanta Falcons"]:
                ans = input(f"Is your team the {team}? (yes/no): ").strip().lower()
                if ans == "yes":
                    print(f"Nice! Your team is the {team}!")
                    found = True
                    break

    elif sb == 1:
        conf = input("Is your team in the AFC or NFC? ").strip().upper()
        while conf not in ["AFC", "NFC"]:
            conf = input("Please type AFC or NFC: ").strip().upper()
        if conf == "AFC":
            for team in ["New York Jets", "Baltimore Ravens"]:
                ans = input(f"Is your team the {team}? (yes/no): ").strip().lower()
                if ans == "yes":
                    print(f"Nice! Your team is the {team}!")
                    found = True
                    break
        else:
            for team in ["Philadelphia Eagles", "Chicago Bears", "Seattle Seahawks", "Tampa Bay Buccaneers", "Los Angeles Rams"]:
                ans = input(f"Is your team the {team}? (yes/no): ").strip().lower()
                if ans == "yes":
                    print(f"Nice! Your team is the {team}!")
                    found = True
                    break

    elif sb == 2:
        conf = input("Is your team in the AFC or NFC? ").strip().upper()
        while conf not in ["AFC", "NFC"]:
            conf = input("Please type AFC or NFC: ").strip().upper()
        if conf == "AFC":
            for team in ["Kansas City Chiefs", "Miami Dolphins"]:
                ans = input(f"Is your team the {team}? (yes/no): ").strip().lower()
                if ans == "yes":
                    print(f"Nice! Your team is the {team}!")
                    found = True
                    break
        else:
            for team in ["Washington Commanders", "Los Angeles Rams"]:
                ans = input(f"Is your team the {team}? (yes/no): ").strip().lower()
                if ans == "yes":
                    print(f"Nice! Your team is the {team}!")
                    found = True
                    break

    elif sb == 3:
        conf = input("Is your team in the AFC or NFC? ").strip().upper()
        while conf not in ["AFC", "NFC"]:
            conf = input("Please type AFC or NFC: ").strip().upper()
        if conf == "AFC":
            for team in ["Denver Broncos", "Las Vegas Raiders"]:
                ans = input(f"Is your team the {team}? (yes/no): ").strip().lower()
                if ans == "yes":
                    print(f"Nice! Your team is the {team}!")
                    found = True
                    break
        else:
            ans = input("Is your team the New York Giants? (yes/no): ").strip().lower()
            if ans == "yes":
                print("Nice! Your team is the New York Giants!")
                found = True

    elif sb == 4:
        conf = input("Is your team in the AFC or NFC? ").strip().upper()
        while conf not in ["AFC", "NFC"]:
            conf = input("Please type AFC or NFC: ").strip().upper()
        if conf == "AFC":
            ans = input("Is your team the Green Bay Packers? (yes/no): ").strip().lower()
            if ans == "yes":
                print("Nice! Your team is the Green Bay Packers!")
                found = True
        else:
            ans = input("Is your team the San Francisco 49ers? (yes/no): ").strip().lower()
            if ans == "yes":
                print("Nice! Your team is the San Francisco 49ers!")
                found = True

    elif sb == 5:
        ans = input("Is your team the Dallas Cowboys? (yes/no): ").strip().lower()
        if ans == "yes":
            print("Nice! Your team is the Dallas Cowboys!")
            found = True
        else:
            ans = input("Is your team the San Francisco 49ers? (yes/no): ").strip().lower()
            if ans == "yes":
                print("Nice! Your team is the San Francisco 49ers!")
                found = True

    elif sb == 6:
        ans = input("Is your team the Pittsburgh Steelers? (yes/no): ").strip().lower()
        if ans == "yes":
            print("Nice! Your team is the Pittsburgh Steelers!")
            found = True
        else:
            ans = input("Is your team the New England Patriots? (yes/no): ").strip().lower()
            if ans == "yes":
                print("Nice! Your team is the New England Patriots!")
                found = True

    if not found:
        print("There are no other teams with that number of Super Bowl wins.")

    again = input("Would you like to play again? (yes/no): ").strip().lower()
    while again not in ["yes", "no"]:
        again = input("Please type yes or no: ").strip().lower()

    if again == "yes":
        continue
    else:
        print("Thanks for playing,", name + "!")
        time.sleep(2)
        break
