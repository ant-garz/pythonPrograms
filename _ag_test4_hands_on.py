#Script Name: ag_test4_hands_on.py
#Author: Anthony Garza
#Purpose: the purpose of this program is to utilize GUI programming to
#        display a dialoge box showing that I have completed the
#       final exam. 





import tkinter
import tkinter.messagebox

class CIS115_FinalExam:
    def __init__(self):
        self.mywin = tkinter.Tk()

        self.lbl_event = tkinter.Label(self.mywin,text="CIS115-Final Exam")
        self.btn_dispMsg= tkinter.Button(self.mywin,text="Display Message",\
                                         command = self.DispFunct)
        self.btn_quit= tkinter.Button(self.mywin, text="Quit",\
                                      command = self.mywin.destroy)

        self.lbl_event.pack()
        self.btn_dispMsg.pack()
        self.btn_quit.pack()

        tkinter.mainloop()
    #function to display the tkinter dialog box
    def DispFunct(self):
        tkinter.messagebox.showinfo("CIS 115","Final Exam Completed!")


def main():
    exam = CIS115_FinalExam()

main()
