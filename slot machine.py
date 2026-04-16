import math
import random
import os
from time import sleep

balance = 100     # set the default value of balance when starting
is_running = True # makes app run


def main_game_menu():
    global balance
    global choice
    sleep(.3)
    print("loding...")  # a good stylish for solt game menu
    sleep(.5)
    print("       ------------ welcome to Slot ------------")
    sleep(.2)
    print("       -            ***************            -")
    sleep(.2)
    print("       -            * 🥭🍎🍉🍒🍍 *            -")
    sleep(.2)
    print(f"       -            ***************            -            balance:{balance:.2f}$")
    sleep(.2)
    print("       -                                       -")
    sleep(.2)
    print("       -    **** what are you here for ? ****  -")
    sleep(.2)
    print("       -    *  1-play the slot machine🎰    *  -")
    sleep(.2)
    print("       -    *2-recover your saved balance???*  -")
    sleep(.2)
    print("       -    *    3- Exit solt game🚪        *  -")
    print("       -     **********--(1-3)--************   -")
    print()
    sleep(.5)
    choice = input(" enter your choice: ")

def print_row():  # this fun is for animations and row print
    global is_running
    symbols = ["🥭", "🍎", "🍉", "🍒", "🍍"]
    animations = 5  #The times of animation before showing the final result
    rows = []

    for animation in range(animations):   # create rows list with random symbols for animation
        row = [random.choice(symbols) for _ in range(3)]
        rows.append(row)

    for row in rows: # print the rows in same row
         output = "\r " + " | ".join(row) + " "
         print(output,end="",flush=True)
         sleep(.3)


    last_row  = rows[-1] #saves the values of last row in rows
    return last_row




def get_payout(balance,amount,row): # this fun is for calculating the payout of the game
    balance = balance - amount
    if row[0] == row[1] == row[2]:
        amount = amount * 5
        print("u got triple!🎉")
        balance = balance + amount
        print(f"ur balance is: {balance:.2f}$💸")
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        amount = amount * 2                                          # cheaking random result and editing balance
        print("u got double!??🥳")
        balance = balance + amount
        print(f"ur balance is: {balance:.2f}$")
    else:
     print("u lost😫😭")
     balance = balance + amount/2
     print(f"ur balance is: {balance:.2f}$")
    return balance





def recovery(): #account loging in system
    global balance
    account_name = input("enter your account name: ")
    account_password = input("enter your password: ")
    file_path = f"saves/{account_name}.txt"
    if os.path.exists(f"{file_path}"):
        with open(file_path, "r") as f:
            lines = f.readlines()
        if len(lines) >= 2 and lines[0].strip() == account_password:
            balance = float(lines[1].strip())
            print("Balance recovered!")
        else:
            print("Incorrect password or corrupted save file.")
    else:
        print("No saved balance found.")



def exit_game(balance): # the exit and saves account system
    global is_running
    saving_choice = input(f"thanks for playing solt,yor current balance is: " + str(
        balance) + "$\ndo you want to save it? (y/n): ").lower()
    running3 = True
    while running3:
        if saving_choice == "y":
            new_account_password = ""
            while not new_account_password:
                new_account_name = input("enter your new account name: ")
                new_account_password = input("enter your new password: ")
                file_path = f"saves/{new_account_name}.txt"
                if not new_account_name:
                    print("account name field is required!")  # making sure that user entered the account name
                    continue

                if not new_account_password:
                    print("password field is required!") #making sure that user entered the account password
                    continue


                if os.path.exists(file_path):
                    print("account name already exists, please choose a different name.")
                else:
                  try:
                      os.makedirs("saves", exist_ok=True)
                      with open(file_path, "w") as f:
                         f.write(f"{new_account_password}\n{balance}")
                      print("Balance saved!")
                      running3 = False
                      print("goodbye")
                      is_running = False
                      break
                  except:
                     print("Error saving file, please try again!")
                     continue

        else:
            print("Invalid choice, please enter 'y' or 'n'.")
            saving_choice = input("Do you want to save your balance? (y/n): ").lower()
            if saving_choice == "y":
                print("Balance saved!")
                break
            elif saving_choice == "n":
                print("goodbye")
                is_running = False
                break
            else:
                continue



def main(): # the fun of running programme
  global balance, is_running

  while is_running :
    main_game_menu()

    if choice == "1":
        is_running2 = True
        while is_running2:
         print(f"yor current balance is : {balance:.2f}$")
         try:
             amount = int(input("enter the amount to play💸: "))
             # cheaking user money amount
             if amount > balance:
                 print("You don't have enough balance! ❌")   #making sure that user have enough balance to play
                 continue
             if amount <= 0:
                 print("Please enter a positive amount! 🚫")
             last_row = print_row()
             balance = get_payout(balance, amount,last_row)
             while True:
              play_again_chioce = input("do you want to play again? (y/n): ").lower()
              if play_again_chioce == "y":
               break
              elif play_again_chioce == "n":
                  is_running2 = False
                  break
         except ValueError:
             print("Error: please enter a valid number!")
             continue

    elif choice == "2":   #cheaking user choice
        recovery()

    elif choice == "3":
        exit_game(balance)
    else:
        pass




if __name__ == "__main__": #making sure that is the main file
    main()
