# 1. Guess The Number Game:
# -we will generate a random number with the help of randint() function from 1 to 100 and ask the user to guess it.
# -After every guess, the user will be told if the number is above or below the randomly generated number.
# -The user will win if they guess the number maximum five attempts.
# -Ask the user to stop or continue playing again.
# ***
# Add another situations like:
# level of game (hard (guess 3 times), medium (6 times), easy (10 times)
# assume that you have 100$, each game you spent 5$. Play game until you choose stop, report the game you win/lost and amount you have.
import random
money = 100
win = 0
loose = 0
while True: #Chơi nhiều ván cho đến khi stop
    money -= 5
    if money <= 0:
        print("You have no money. It isn't able to continue playing")
        break
    com_num = random.randint(1,100)
    print(com_num)
    for i in range (1,6): #Tùy mức độ mà tăng vòng lặp lên tiếp: hard: (1,4); medium (1,7); easy (1,11)
        your_num = int(input("Question 1 - Please type the number that you guess: "))
        if com_num == your_num:
            print("You've guessed correctly")
            win += 1 #Đoán trúng --> Thắng --> + 1 ván thắng
            break
        elif your_num < com_num:
            print(f"The number {your_num} that you've guessed is below the randomly generated number")
        else:
            print(f"The number {your_num} that you've guessed is above the randomly generated number")
    else:
        print(f"Sorry. You've reached 5 times of trials. The correct number is {com_num}")
        loose += 1
    print("---------------YOUR RESULT OF THE GAME---------------")
    print(f"Games won: {win}")
    print(f"Games lost: {loose}")
    print(f"Money left: {money} $")
    response = input("Do you want to play again? (Please type [Y/N] or [y/n]: ")
    if response == "N" or response == "n":
        break

