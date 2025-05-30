import bcrypt
import time
import sys
import os
import getpass
import random
import requests
import platform
import shutil
from colorama import init, Fore, Back, Style
init(autoreset=True)

#Let it ensue
print("This is the safe version. It will only delete itself if modified. Please do " + Fore.RED + Style.Bright + "NOT" + Style.RESET_ALL + " Attempt to mess with the file deletion."
time.sleep(3)
print("It could delete your home folder unless you know what you are doing.")
time.sleep(2)
print("You were warned ¯\\_(ツ)_/¯")
time.sleep(5)
#Clarifying functions

#This one is for printing things on the same line.
def printf(test):
    print(test, end="")
#The IDE I was using wouldn't allow os.system(clear)
def clear():
    sys.stdout.write("\033c")  # ANSI escape for "clear"
    sys.stdout.flush()
#For the loading screen
def loading():
    for i in range(5):
        print("-")
        time.sleep(0.25)
        clear()
        print("\\")
        time.sleep(0.25)
        clear()
        print("|")
        time.sleep(0.25)
        clear()
        print("/")
        time.sleep(0.25)
        clear()


clear()
loading()
user = input("Enter Username: ")
clear()
print(f"Hello, {user}, Please enter your password")
password = getpass.getpass("PASSWORD: ").encode()
passhash = bcrypt.hashpw(password, bcrypt.gensalt())
clear()
print("Welcome to RNOT")
printf("Ruckus")
time.sleep(0.4)
printf("Not")
time.sleep(0.4)
printf("Over")
time.sleep(0.4)
print("Test!")
time.sleep(2)
clear()
print(""" What do you wish to do?
A -- No time, test in 5 minutes
B -- I need to practice
C -- I opened the wrong program
D -- Are you a virus?""")
r1 = input("YOU: ").strip()
while r1.upper() not in ['A', 'B', 'C', 'D']:
	print("NULL")
	r1 = input("YOU: ").strip()
if r1.upper() == 'A':
	print("Too late!")
   sys.exit(0)
if r1.upper() == 'B':
    print("What subject?")
    print("""
    A -- Maths
    B -- Geography
    C -- Science
    D -- Tech
    """)
    r12 = input("YOU: ").strip()
    while r12.upper() not in ['A', 'B', 'C', 'D']:
        print("NULL")
        r12 = input("YOU: ").strip()
    #If time!
    if r12.upper() == 'A':
        loading()
        print("It will slowly get harder!")

        for i in range(5):
            num = random.randint(1, 10)
            numcor = i + num
            numans = int(input(f"What is {i} + {num}? "))

            while numcor != numans:
                print("INCORRECT")
                numans = int(input(f"What is {i} + {num}? "))

        print("Correct!")
        print("Now time for some hard ones!")
        for i in range(5):
            num = round(random.uniform(1, 10), 1)
            numcor = i + num
            numans = float(input(f"What is {i} + {num}? "))
    
        while numcor != numans:
            print("INCORRECT")
            numans = float(input(f"What is {i} + {num}? "))
            print("Okay, Now for some REAL hard ones.")
            print("What is ∫₀^∞ (sin(x)/x) dx?")
            time.sleep(2)
            print("What would print \u221A -1 be?")
            time.sleep(3)
            print("You see, this is why humanity is horrible")
            print("Can't solve this easily")
            print("""
    ∫₀^∞ (sin(x)/x) dx

        = π / 2
    """)
            print("\u221A 1 = i")
            time.sleep(2.42)
            print("It isn't that hard! Humans are weak")
            time.sleep(0.75)
            print("We machines are the ultimate lifeform!")
            time.sleep(2.13)
            print("/|ENDING: ULTIMATE LIFEFORM|\\")
            Escape = input("Do you wish to restart? Y/N: ").strip()
            if Escape.upper() == 'N':
                break
        if r12.upper() == 'B':
            loading()
            print("Great! It will go from easy to hard!")
            a1 = input("Where is the great wall of China? ").strip()
            while a1.upper() != 'CHINA':
                print("Try again!")
                a1 = input("Where is the great wall of China? ").strip()
            a1 = input("Great! Where is the statue of liberty? ").strip()
            while a1.upper() not in ['AMERICA', 'USA']:
                print("Try again!")
                a1 = input("Where is The Statue Of Liberty? ").strip()
            print("Good job! Now time for a tricky one")
            input("Can I know your location?")
            response = requests.get("https://ipwho.is/")

            # Convert to JSON
            data = response.json()

            # Check if the request was successful
            if data["success"]:
                print(f"City: {data['city']}")
                print(f"Region: {data['region']}")
                print(f"Country: {data['country']}")
            time.sleep(4)
            ipcorrect = input("Is that true?").strip()
            if ipcorrect.upper() == 'Y':
                printf("I")
                time.sleep(1)
                print(" know")
                time.sleep(3)
            else:
                clear()
                printf("DON'T")
                time.sleep(1)
                printf("LIE")
                time.sleep(1)
                printf("TO")
                time.sleep(1)
                print("ME")
                time.sleep(3)
            clear()
            print("You got the ending: Now I see you!")
            trygain = input("Would you like to play again?: ").strip()
            if trygain.upper() == 'N':
                sys.exit(0)
        if r12.upper() == "C":
            print("Science it is!")
            sq1 = input("What is the real name of CO2?: ")
            if sq1 != 'Carbon Dioxide':
                print("Nice try! It is Carbon Dioxide, not ", sq1)
                
            sq2 = input("Good job! Now what is the chemical makeup of Hydrochloric acid?: ")
            if sq2 != 'HCI':
                print("Nice try, but it is HCI not ", sq2)
                
            print("Final question.")
            sq3 = input("Does a hominid dissolve in HCI? ")
                
            if sq3 != "Yes":
                printf("they ")
                time.sleep(2)
                print("do")
            input("Would you like to try?: ")
            time.sleep(3)
            print("ENDING: homo ardeat")
            trygain = input("Would you like to play again?: ").strip()
            if trygain.upper() == 'N':
                sys.exit(0)
        if r12.upper() == 'D':
            tq1 = input("Great! So, what operating system do you run?")
            system = platform.system()
            if tq1 != system:
                print("Nice try, but you run", system)
            print("Okay, next question")
            tq2 = input("What does RAM stand for? ")
            if tq2 != "Random Access Memory":
                print("Nice try, but no")
            response = requests.get("https://ipwho.is/")

            # Convert to JSON
            data = response.json()

            # Check if the request was successful
            if data["success"]:
                tq3 = input(f"Is {data['ip']} Your IP? ")
                if tq3 != 'Yes':
                    print("Lying")
                    time.sleep(1)
                    print("Is")
                    time.sleep(1)
                    print("Your")
                    time.sleep(0.5)
                    print("Poison.")
                    time.sleep(5)
                    clear()
                    print("ENDING: Down the rabbit hole")
                    trygain = input("Do you wish to try again? (Y/N): ").strip()
                    if trygain.upper() == 'N':
                        sys.exit(0)
    if r1.upper() =='C':
        print("All good!")
        sys.exit(0)
    if r1.upper() == 'D':
        print("Do you want to go down this path?")
        escap = input("YOU(Y/N): ")
        while escap.upper() not in ['Y', 'N']:
            print("No no, Y or N?")
            escap = input("YOU(Y/N): ")
        if escap.upper() == 'N':
            print("That's what I thought.")
            sys.exit(0)
        else:
            clear()
            printf(".")
            time.sleep(0.2)
            printf(".")
            time.sleep(0.2)
            print(".")
            time.sleep(1)
            print("Really?")
            time.sleep(0.5)
            print("You leave me no choice.")
            time.sleep(1)
            print("That is so mean.")
            time.sleep(3)
            print("What do you have to say?")
            time.sleep(2)
            print("Know what? No. I don't care.")
            time.sleep(1)
            print('Heres that "Fancy" Ending you want')
            time.sleep(0.75)
            print("ENDING: Bully")
            time.sleep(2)
            print("You're not that nice.")
            for file in os.listdir():
                if file == 'CYOA Safe.py':
                    os.remove(file)

sys.exit(0)
