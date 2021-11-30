play_str=input("Would you like to play? (0=no, 1=yes) ")

human = int(0)
computer = int(0)
while int(play_str) != 0:

    pile1 = int(5)
    pile2 = int(5)
    print("Start --> Pile 1:",pile1,"   Pile 2:",pile2)

    while (pile1 > 0) or (pile2 > 0):
        pile = int(input("Choose a pile (1 or 2): "))

        while ((pile == 1)and(pile1 == 0))or((pile == 2)and(pile2 == 0)):

            print("Pile must be 1 or 2 and non-empty. Please try again.")
            pile = int(input("Choose a pile (1 or 2): "))
        else:

            while (pile != 1) and (pile != 2):

                print("Pile must be 1 or 2 and non-empty. Please try again.")
                pile = int(input("Choose a pile (1 or 2): "))
            else:
                stones = int(input("Choose stones to remove from pile: "))

                while (stones > 3) or (stones < 1):

                    print("Invalid number of stones. Please try again.")
                    stones = int(input("Choose stones to remove from pile: "))
                else:
                    print("Player -> ",end='')
                    print("Remove",stones,"stones from pile",pile)

                    if (pile == 1) and (pile1 >= stones):

                        pile1 = pile1 - stones
                        print("Pile 1:",pile1,"   Pile 2:",pile2)

                        if (pile1 <= 0) and (pile2 <= 0):


                            human = human + 1
                            print("\nPlayer wins!")
                            print("Score -> human:",human,"; computer:",computer)
                        else:


                            if (pile2 > 0):

                                pile2 = pile2 - 1
                                print("Computer -> ",end='')
                                print("Remove 1 stones from pile 2")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            else:

                                pile1 = pile1 - 1
                                print("Computer -> ",end='')
                                print("Remove 1 stones from pile 1")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            if (pile1 <= 0) and (pile2 <= 0):

                                computer = computer + 1
                                print("\nComputer wins!")
                                print("Score -> human:",human,"; computer:",computer)

                    if (pile == 2) and (pile2 >= stones):

                        pile2 = pile2 - stones
                        print("Pile 1:",pile1,"   Pile 2:",pile2)

                        if (pile1 <= 0) and (pile2 <= 0):

                            human = human + 1
                            print("\nPlayer wins!")
                            print("Score -> human:",human,"; computer:",computer)

                        else:

                            if (pile1 > 0):

                                pile1 = pile1 - 1
                                print("Computer -> ",end='')
                                print("Remove 1 stones from pile 1")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            else:

                                pile2 = pile2 - 1
                                print("Computer -> ",end='')
                                print("Remove 1 stones from pile 2")
                                print("Pile 1:",pile1,"   Pile 2:",pile2)

                            if (pile1 <= 0) and (pile2 <= 0):

                                computer = computer + 1
                                print("\nComputer wins!")
                                print("Score -> human:",human,"; computer:",computer)

    else:
        play_str = input("\nWould you like to play again? (0=no, 1=yes) ")
else:
   print("\nThanks for playing! See you again soon!")
