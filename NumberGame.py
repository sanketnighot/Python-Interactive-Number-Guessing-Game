# -*- coding: utf-8 -*-
"""
Made By :- SANKET ASHOK NIGHOT
Email Id:- sanketnighot25@gmail.com

"""
import random
import time
import sys
from tqdm.auto import tqdm
def rangeSelect(num):
    if num == 1 :   return 10, 4, 1
    elif num == 2 : return 30, 6, 2
    elif num == 3 : return 50, 8, 3
    elif num == 4 : return 100, 10, 4
def setup(playername):  
    print("Hello", playername)
    time.sleep(1.0)
    print("Lets Start 'THE NUMBER GUESSING GAME'")
    time.sleep(0.5)
    time.sleep(0.5)
    print('''
          Select Range of Number:
                  Press (1) for 1-10
                  Press (2) for 1-30
                  Press (3) for 1-50
                  Press (4) for 1-100
                  ''')
    time.sleep(1.0)
    x = 1 
    while x != 0:
        rangeinput = int(input("Enter Range : "))
        if rangeinput in range(1, 5) :
            print("Loading ...")

            print("")
            rangeip, chance, hints = rangeSelect(rangeinput)
        
            x = 0
        else :
            print("Loading ...")
            print("")
            time.sleep(2.0)
            print("Invalid Entry ...")
            time.sleep(1.0)
            print("Please Try Again ...")
            print("Loading ...")
            print("")
            time.sleep(1.5)
    def generateHints(number, rng):
        hintlist = list()
        if number%2 == 0 :
            val = "Number is Even"
            hintlist.append(val)
        elif number%2 != 0:
            val = "Number is Odd"
            hintlist.append(val)
        for i in range(3, number):
            val = number%i
            if val == 0 :
                adon = f"Number is Divisible by {i}"
                hintlist.append(adon)
        return hintlist
    def hintanalyse(num):
        t = 1
        while t != 0 :
            print("Do you want to use Hints?")
            print('''
                      Press (1) for Hints
                      Press (2) to Continue
                
                ''')
            getchoice = int(input("Enter Your Choice : "))
            if getchoice == 1 : 
                sendhint = random.randint(1, num)
                t = 0
                return sendhint
            elif getchoice == 2 :
                t = 0
                return None
            else :
                print("Loading ...")
                print("")
                time.sleep(2.0)
                print("Invalid Entry ...")
                time.sleep(1.0)
                print("Please Try Again ...")
                print("Loading ...")
                print("")
                time.sleep(1.5)
    def Score(hints, hintsused, chance, count, status):
        if hintsused == 0 : h = 4
        elif hintsused == hints : h = 0
        elif hintsused >= hints/2 : h = 2
        elif hintsused < hints/2: h = 3
        if count == 1 : c = 4
        elif count == chance : c = 1
        elif count >= chance/2 : c = 2
        elif count < chance/2 : c = 3
        if status == 1 : s = 2
        score = h + c + s
        return score
    def guessNumber(player, realnum, rangeip, chance, hints, hintlist):
        orghints = hints
        count = 0
        list1 = list()
        hintsused = 0
        time.sleep(1.0)
        for i in range(1, chance + 1):
            print("_____________________________________________________")
            print("")
            count = count + 1
            temp = chance - i + 1
            print(f"{player}, You Have:")
            print("    ", temp, "Chances and")
            print("    ", hints, "Hints left")
            print("")
            time.sleep(0.7)
            numb = len(hintlist)
            if hints != 0 :
                choice = hintanalyse(numb)
                if choice != None :
                    varb = hintlist[choice - 1]
                    del hintlist[choice - 1]
                    
                    print("")
                    print("# HINT :",varb)
                    hints = hints - 1
                    hintsused = hintsused + 1
                else: print("Continue Pressed, No Hints Used")
            time.sleep(1.5)
            if i != 1 : print("Your Previous Attempts :", list1)
            guessednumber = int(input("Guess the Number : "))
            list1.append(guessednumber)
            print("Analyzing ...")
            time.sleep(2.0)
            print("")
            if guessednumber > realnum and guessednumber in range(1, rangeip) :
                print(f"Sorry {player}, Guessed Number {guessednumber} is Bigger than Generated Number")
                print("")
                time.sleep(2.0)
            elif guessednumber < realnum and guessednumber in range(1, rangeip) :
                print(f"Sorry {player}, Guessed Number {guessednumber} is Smaller than Generated Number")
                print("")
                time.sleep(2.0)
            elif guessednumber == realnum :
                print(f"Congratulations {player}, You guessed the Number {guessednumber} in {count} chances ...")
                print("")
                print("")
                print("***** YOU WON THE GAME !!! *****")
                print("")
                print("")
                print("Calculating Your Score of This Game ...")
                for i in tqdm(range(0, 100), desc="Analyzing Your Performance", unit="xsn", leave = False, ascii = False): time.sleep(.0025)
                time.sleep(2.5)
                score = Score(orghints, hintsused, chance, count, 1)
                calc = ""
                for i in range(1, 11):
                    if i <= score :
                        calc = calc + " *"
                    elif i > score or i <= 10 :
                        calc = calc + " -"
                        
                print("")
                print("")
                print(f"Congratulations {player}, Your Score is ...")
        
                print(calc)
                time.sleep(0.5)
                time.sleep(2.0)
                print('''
                      
                
                
*************************************************************
Thank You For Playing "THE INTERACTIVE NUMBER GUESSING GAME"
*************************************************************




''')
                sys.exit(1)
                
                break
            elif guessednumber not in range(1, rangeip):
                print(f"{player}, You are guessing the number which is out of Range You Selected...")
                print(f"Please Select number in range '1 to {rangeip}'")
                
            
        if count == chance :
            print(f"Sorry {player}, You were unable to Guess Number in {count} chances")
            print("")
            print("##### YOU LOST THE GAME !!! #####")
            print("")
            print(f"The Generated Number is {realnum}")
            time.sleep(2.0)
            print('''
                  
            
            
*************************************************************
Thank You For Playing "THE INTERACTIVE NUMBER GUESSING GAME"
*************************************************************



''')
    print("Generating Random Number ...")
    time.sleep(2.5)
    realnumber = random.randint(1 ,rangeip)
    print("**Random Number Generated**")
    print("")
    print("")
    time.sleep(0.5)
    print("Generating Hints ...")
    time.sleep(2.5)
    genhints = generateHints(realnumber, rangeip)
    print("**Hints Generated**")
    print("")
    print("")
    time.sleep(2.0)
    hints2 = len(genhints)
    print(f"{playername},")
    time.sleep(1.35)
    print(f"*  Range to Guess is '1 to {rangeip}'")
    time.sleep(1.0)
    print(f"*  You have to guess Number in '{chance}' Chances")
    time.sleep(1.0)
    if hints <= hints2 : print(f"*  You can use '{hints}' hint/s to guess number if you want")
    elif hints > hints2 : 
        print(f"*  You can use '{hints2}' hint/s to guess number if you want")
        hints = hints2
    print("")
    print("")
    time.sleep(0.5)
    print("Now... Try Guessing the Generated Number >>>")
    print("")
    print("")
    guessNumber(playername, realnumber, rangeip, chance, hints, genhints)
print('''
*****************************************************
  Welcome to "THE INTERACTIVE NUMBER GUESSING GAME"
*****************************************************
''')
time.sleep(1.5)
print(''' ~~ Instructions To Play "THE INTERACTIVE NUMBER GUESSING GAME" ~~
      
          $  Enter Your Name.
          $  Choose the Range of Numbers you would like to Play the Game.
          $  According to your choice Program will generate a Number 
          and some hints to guess it in Limited chances.
          $  Try to guess the number in given chances.
          $  Its totally upto you if you want to use hints or not.
          $  If You are unable toguess the number in given chances 
          then you will loose the game.
          $  On Correctly Guessing the number you will see your performance score.
          $  The Program will calculate the score according to your performance.
          $  Try to guess the number in less attempts and with less use of hints
          to increase your performance score
          $  Appreciate the work if you like.
          $  👍  ALl The Best ... Happy Playing ... Happy Coding ... 😀😀😀
          
          NOTE : The Game will start Soon ...

''')
print("")
for i in tqdm(range(0, 100), desc="Building Your Game", unit="xsn", leave = False, ascii = False):
    int_num = random.choice(range(1, 10))
    x = int_num/70
    time.sleep(x)

playername = input("Please Enter Your Name : ")
time.sleep(1.0)
if __name__ == "__main__" :
    setup(playername)
