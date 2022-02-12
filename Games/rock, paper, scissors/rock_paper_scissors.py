import random
invalid = False
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
should_play = True
while should_play:
    play = 0
    print(rock, paper, scissors)
    options = (rock, paper, scissors)
    human_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    if human_choice == "0":
        human_choice = options[0]
    elif human_choice == "1":
        human_choice = options[1]
    elif human_choice == "2":
        human_choice = options[2]
    else:
        print("Please type a valid option.")
        invalid = True
    if invalid == False:
        print(human_choice)
    computer_choice = random.choice(options)
    if invalid == False:
        invalid = False
        print("Computer chose:",computer_choice)
    if human_choice == computer_choice:
        invalid = False
        print("It's a draw.")
    elif human_choice == options[0] and computer_choice == options[2]:
        invalid = False
        print("You Win!")
    elif human_choice == options[2] and computer_choice == options[1]:
        invalid = False
        print("You win!")
    elif human_choice == options[1] and computer_choice == options[0]:
        invalid = False
        print("You win!")
    else:
        if invalid == False:
            print("You lose!")
    while play != "y" and play != "n":
        play = input("Do you want to play a game of rock, paper, scissors? Type y or n\n")
        if play == "y":
            should_play = True
        elif play == "n":
            should_play = False
