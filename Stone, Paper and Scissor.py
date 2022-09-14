import random

print("Welcome to the Stone, Paper, Scissor Game")

# User choise
while True:
    wincom = 0
    winuser = 0
    for i in range(1, 6):
        print("\nRound", i, "Start")
        user = input("1) Stone\n2) Paper\n3) Scissor\nChoose one option: ").title()
        if user == "stone":
            print("You selected Stone")
        elif user == "paper":
            print("You selected Paper")
        elif user == "scissor":
            print("You selected Scissor")
        else:
            exit("Program Failed")
            break

        # Computer choise
        computer = random.choice(["Stone", "Paper", "Scissor"])
        print("Computer selected", computer)
        if (user == "stone" and computer =="Paper") or (user == "paper" and computer == "Scissor") or (user == "scissor" and computer == "Stone"):
            print("Computer won!")
            wincom += 1
        elif (user == "stone" and computer =="Scissor") or (user == "paper" and computer == "Stone") or (user == "scissor" and computer == "Paper"):
            print("You won!")
            winuser += 1
        elif (user == "stone" and computer =="Stone") or (user == "paper" and computer == "Paper") or (user == "scissor" and computer == "Scissor"):
            print("It's a draw!")
        else:
            print("Program Failed")

    if wincom > winuser:
        print(f"\nMatch Over\nYou Lose!\nScores: Computer {wincom} Your {winuser}")
    elif wincom < winuser:
        print(f"\nMatch Over\nYou won!\nScores: Computer {wincom} Your {winuser}")
    elif wincom == winuser:
        print(f"\nMatch Over\nIt's a draw!\nScores: Computer: {wincom}, You: {winuser}")
    user_choise = input("\nPlay Again? (Yes/Exit): ")
    if user_choise == 'yes':
        continue
    else:
        break
