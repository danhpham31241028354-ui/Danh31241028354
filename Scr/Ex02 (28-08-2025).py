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
# Write a game that simulate rolling a pair of dice.
# -If the sum of two faces is greater than 5 à “Tài”
# -Otherwise  à “Xỉu”
# -User ask for guessing “Tài” or “Xỉu”
# -Match the results
# -After one turn, ask user for continue playing game.
# -**** Extend the game by asking the user to enter an amount of money, then continue playing until the user runs out of money or the user stops playing. Statistics of results.
print("---------------------CÂU 2---------------------")
import random
money = int(input("Hãy nhập số tiền bắt đầu: "))
win = lose = 0
while money > 0:
    print(f"You have {money} $")
    bet = int(input("Nhập số tiền bạn cược: "))
    if bet > money:
        print("Không đủ tiền để chơi")
        continue
    doan = input("Hãy đoán 'Tài' hay 'Xỉu: ")
    total = random.randint(1,6) + random.randint(1,6)
    ket_qua = "Tài" if total > 5 else "Xỉu"
    print(f"Tổng của xúc sắc là {total}. Kết quả là {ket_qua}")
    if doan == ket_qua:
        money += bet
        win += 1
        print("Bạn đã thắng")
    else:
        money -= bet
        lose += 1
        print("Bạn đã thua")
    if money <= 0 or input("Play again?(Y/N)"):
        break
print("-----------RESULT-----------")
print(f"Thắng: {win}, Thua: {lose}, Tiền còn lại: {money} $)")
