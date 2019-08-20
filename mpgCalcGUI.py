#Author: Anthony Garza
#Purpose: The purpose of this program is to make a GUI program using tkinter.
#       This program calculates the miles per gallon a vehicle has based off
#       of user input. It has validation code to ensure that user input is both
#       numerical and positive.

import tkinter
import tkinter.messagebox

#define GUI class
class Miles_Per_Gallon:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.disp_msg = tkinter.StringVar()
        msg = "\nMPG ="
        self.disp_msg.set(msg)

        # create frames for GUI
        self.uframe= tkinter.Frame(self.main_window) #upper frame
        self.bframe= tkinter.Frame(self.main_window) #button frame
        self.rframe= tkinter.Frame(self.main_window) #entry frame
        self.msgFrame= tkinter.Frame(self.main_window) #messageframe

        # create label widgets
        self.gallon_amt= tkinter.Label(self.uframe, text= "Enter # of gallons used")
        self.miles_amt= tkinter.Label(self.rframe, text = "Enter # of miles traveled")

        # create entry widgets
        self.ent_gallon_amt= tkinter.Entry(self.uframe, width=10)
        self.ent_miles_amt= tkinter.Entry(self.rframe, width=10)

        #create button widgets
        self.btn_calc= tkinter.Button(self.bframe, \
                                      text = "Calculate MPG", \
                                      command = self.calcMPG)
        self.btn_exit= tkinter.Button(self.bframe, text = "Exit", \
                                      command = self.main_window.destroy)
        
        #create message label
        self.lbl_message= tkinter.Label(self.msgFrame,
                textvariable=self.disp_msg,
                font=('Calibri',16))
        self.lbl_message.pack()

        #pack gallon frame
        self.gallon_amt.pack(side = "left")
        self.ent_gallon_amt.pack(side= "left")
        
        #pack miles frame
        self.miles_amt.pack(side = "left")
        self.ent_miles_amt.pack(side = "left")

        #pack button frame
        self.btn_calc.pack(side = "left")
        self.btn_exit.pack(side = "left")
        
        #pack frames
        self.uframe.pack(side="top")
        self.rframe.pack(side="top")
        self.bframe.pack(side="top")
        self.msgFrame.pack()

        tkinter.mainloop()

    def calcMPG(self):
        msg= ""
        try:
            gallon_amt = float(self.ent_gallon_amt.get())
            miles_amt = float(self.ent_miles_amt.get())
            if gallon_amt <= 0 or miles_amt <= 0:
                msg = "Error! Value cannot be less than or equal to 0."
                self.disp_msg.set(msg)
                return
        except ValueError:
            msg = "Error! Value must be numerical."
            self.disp_msg.set(msg)
        else:
            mpg = miles_amt / gallon_amt
            msg += "\nMPG = " + format(mpg, ".2f")
            self.disp_msg.set(msg)
        
#define main fucntion
def main():
    Miles_Per_Gallon()

#invoke main function
main()
            
