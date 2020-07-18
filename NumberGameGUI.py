# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import sleep
import random


class GuessNumber:
    
    
    
    def gameWindow(self):
        def rangeSelect(self):
            if self.num == 10 :   return 4, 1
            elif self.num == 30 : return 6, 2
            elif self.num == 50 : return 8, 3
            elif self.num == 100 : return 10, 4
            
        def generatehints(self):
            self.hintlist = list()
            if self.realnumber%2 == 0 :
                val = "Number is Even"
                self.hintlist.append(val)
            elif self.realnumber%2 != 0:
                val = "Number is Odd"
                self.hintlist.append(val)
            for i in range(3, self.realnumber):
                val = self.realnumber%i
                if val == 0 :
                    adon = f"Number is Divisible by {i}"
                    self.hintlist.append(adon)
            return self.hintlist
        
        def givehints(self):
            if int(self.hints) > 0 :
                self.count = len(self.hintgenerated)
                self.givenum = random.randint(0, self.count - 1)
                self.givehints = self.hintgenerated[self.givenum]
                
                del self.hintgenerated[self.givenum]
                messagebox.showinfo(title = 'Hint', message = self.givehints)
                self.hints = int(self.hints) - 1
                self.numhint = "Get Hints (" + str(self.hints)+ ")"
                self.hintsbutton.config(text = self.numhint)
            if int(self.hints) == 0 : 
                self.hintsbutton.state((['disabled']))
                
        
        def checkNum(self):
            self.countchance = self.countchance+ 1
            if self.guees.get() == '' :
                messagebox.showinfo(title = 'No Number Guessed', message = f"{self.name}, No Number Entered")
                return
            self.guessnum = int(self.guees.get())
            print(self.guessnum)
            
            self.chances = int(self.chances)
            if self.chances >= 1 :
                
                
                
                
                if int(self.guessnum) > int(self.realnumber) :
                    messagebox.showinfo(title = 'Analysis', message = f"{self.name}, Guessed Number {self.guessnum} is BIGGER then Generated Number ... Try Again")
                    self.chances = self.chances - 1
                    self.chancesare.config(text = self.chances)
                elif int(self.guessnum) < int(self.realnumber) :
                    messagebox.showinfo(title = 'Analysis', message = f"{self.name}, Guessed Number {self.guessnum} is SMALLER then Generated Number ... Try Again")
                    self.chances = self.chances - 1
                    self.chancesare.config(text = self.chances)
                elif int(self.guessnum) == int(self.realnumber) :
                    self.guees.delete(0, 'end')
                    self.guessbutton.state((['disabled']))
                    self.hintsbutton.state((['disabled']))
                    self.guees.state((['disabled']))
                    messagebox.showinfo(title = 'Result', message = f"Congratulations {self.name}, You Guessed the Number Correctly in {self.countchance} Chances")
                    
                    self.guees.state((['disabled']))

                    self.game.destroy()
            self.listguess.append(self.guessnum)
            
                    
            if self.chances == 0 :
                self.guees.delete(0, 'end')
                self.guessbutton.state((['disabled']))
                self.hintsbutton.state((['disabled']))
                self.guees.state((['disabled']))
                messagebox.showinfo(title = 'Results', message = f"{self.name}, You Lost the Game ... Try Again")
                messagebox.showinfo(title = 'Actual Number', message = f"{self.name}, The Number was {self.realnumber}")
                
                self.guees.state((['disabled']))

                self.game.destroy()
            if self.chances != 0 or int(self.guessnum) == int(self.realnumber):
                self.guees.delete(0, 'end')
                self.guesslist.config(text = self.listguess)
                    
                
                
        '''------------------\/gui------------ /\ backend ------------------'''

        
        self.name = self.name
        self.hp = "Hello," + self.name
        self.ranges = self.ranges
        self.num = int(self.ranges)
        self.chances, self.hints = rangeSelect(self)
        self.countchance = 0
        self.game = Tk()
        self.game.title("New Window")
        self.game.resizable(False, False)
        self.game.configure(background = '#e1d8b9')
        style = ttk.Style()
        style.configure('TFrame', background = '#e1d8b9')
        style.configure('TButton', background = '#e1d8b9')
        style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 14))

        style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
        ttk.Label(self.game, text = '$$ Interactive Number Guessing Game $$',
                  style = 'Header.TLabel').grid(row = 0, column = 2, columnspan= 3)
        ttk.Label(self.game, text= self.hp, style = 'TLabel').grid(row = 1, column = 2, columnspan = 3)
        self.listguess = list()
        self.rangesip = "1 to " + self.ranges
        ttk.Label(self.game, text= "Previous Guesses :", style = 'TLabel').grid(row = 5, column = 1, sticky = 'e')
        self.guesslist = ttk.Label(self.game, text= self.listguess, style = 'TLabel')
        self.guesslist.grid(row = 5, column = 2, columnspan = 3)
        ttk.Label(self.game, text= "Range is:").grid(row = 4, column = 0)
        ttk.Label(self.game, text= self.rangesip).grid(row = 4, column = 1)
        ttk.Label(self.game, text= "Chances :").grid(row = 4, column = 4, sticky = 'e')
        self.chancesare = ttk.Label(self.game, text= self.chances)
        self.chancesare.grid(row = 4, column = 5)
        # ttk.Label(self.game, text= "    self.hints :").grid(row = 4, column = 6)
        self.instn = ttk.Label(self.game, text = " ")
        self.instn.grid(row = 5, column = 2)
        self.realnumber = random.randint(1, self.num)
        print(self.realnumber)
        # ttk.Label(self.game, text= "Generating self.hints ...").grid(row = 5, column = 2)
        self.hintgenerated = generatehints(self)
        self.hints2 = len(self.hintgenerated)
        print(self.hintgenerated)
        if self.hints <= self.hints2 : self.hints = self.hints
        elif self.hints > self.hints2 : self.hints = self.hints2
        # self.hintsare = ttk.Label(self.game, text= self.hints ).grid(row = 4, column = 7)
        self.guees = ttk.Entry(self.game, width = 25, font = ('Arial', 10))
        self.guees.grid(row = 7, column = 2, padx = 10, columnspan = 2, sticky = 'e')
        self.yourguess = ttk.Label(self.game, text = "Guess the Number")
        self.yourguess.grid(row = 6, column = 2, columnspan = 3)
        self.numhint = "Get Hints (" + str(self.hints)+ ")"
        self.hintsbutton = ttk.Button(self.game, text = self.numhint , command = lambda : givehints(self) )
        self.hintsbutton.grid(row = 4, column = 6, padx = 5, pady = 5, columnspan = 2)
        self.guessbutton = ttk.Button(self.game, text = 'Check',
                   command = lambda : checkNum(self))
        self.guessbutton.grid(row = 7, column = 4, padx = 5, pady = 5, sticky = 'w')
        
    
    '''------------------\/primary------------ /\ new window ------------------'''
    
    def __init__(self, master):
              
        self.master = master
        self.master.title('Number Guessing Game')
        self.master.resizable(False, False)
        self.master.configure(background = '#e1d8b9')
    
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        # self.logo = PhotoImage(file = '.img\\num1.gif')
        
        # ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = '$$ The Number Guessing Game $$', style = 'Header.TLabel').grid(row = 0, column = 1, columnspan= 6)
        ttk.Label(self.frame_header, wraplength = 1000,
                  text = ("Welcome to play the Game")).grid(row = 1, column = 1, columnspan= 6)
        ttk.Label(self.frame_header, wraplength = 1000,
                  text = (''' ~~ Instructions To Play "THE INTERACTIVE NUMBER GUESSING GAME" ~~
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
''')).grid(row = 1, column = 1, columnspan= 4)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        
        ttk.Label(self.frame_content, text = 'Name:').grid(
            row = 0, column = 0, padx = 10, pady = 10, sticky = 'sw')
        self.entry_name = ttk.Entry(self.frame_content, width = 35, font = ('Arial', 10))
        self.entry_name.grid(row = 1, column = 0, padx = 10)
        
    
        self.ranges = StringVar()
        ttk.Label(self.frame_content, text = 'Select Range:').grid(
            row = 4, column = 0, padx = 5, pady = 10, sticky = 'sw')
        ttk.Radiobutton(self.frame_content, text = '1 - 10', variable = self.ranges,
		value = '10').grid(row = 5, column = 0, padx = 10,sticky = 'sw' )
        ttk.Radiobutton(self.frame_content, text = '1 - 30', variable = self.ranges,
		value = '30').grid(row = 6, column = 0, padx = 10, sticky = 'sw')
        ttk.Radiobutton(self.frame_content, text = '1 - 50', variable = self.ranges,
		value = '50').grid(row = 7, column = 0, padx = 10, sticky = 'sw')
        ttk.Radiobutton(self.frame_content, text = '1 - 100', variable = self.ranges,
		value = '100').grid(row = 8, column = 0, padx = 10, sticky = 'sw')
        
        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 13, column = 0, padx = 5, pady = 5, sticky = 'e')
        
        self.progressbar = ttk.Progressbar(self.frame_content, orient="horizontal", length = 300)
        self.progressbar.grid(row = 15, column = 0, columnspan= 5,padx = 5, pady = 5, sticky = 'e')
        self.progressbar.config(mode = 'determinate', maximum= 100.0, value = 0.0)

        
        
    def submit(self):
        global getname, getrange
        
        x = 0
        while x != 100 :
            temp = random.randint(0, 45)
            if temp + x <= 100 :
                self.progressbar['value'] += temp
                self.frame_content.update_idletasks()
                x += temp
                sleep(0.5)
            elif temp + x > 100 and x > 85 :
                g = 100 - temp
                self.progressbar['value'] += g
            else: continue
        self.name = self.entry_name.get()
        self.ranges = self.ranges.get()
        
        if len(self.name) == 0 or len(self.ranges) == 0:
            messagebox.showinfo(title = 'Error', message = 'Name or Range Not Submitted ! ... Please Fill all Fields')
            self.progressbar['value'] = 0
            

        elif len(self.name) != 0 or len(self.ranges) != 0:
            print('Name: {}'.format(self.name))
            print('Range: {}'.format(self.ranges))
            self.master.destroy()
            GuessNumber.gameWindow(self)
            # messagebox.showinfo(title = 'Success', message = 'Name and Range Submitted!')
          

def main():          
    global root
    
    root = Tk()
    guessNumber = GuessNumber(root)    
    root.mainloop()

    
if __name__ == "__main__": main()
