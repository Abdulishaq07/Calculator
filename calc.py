from tkinter import *
import re  # Import the re module

def love():
    class Calculator:
        def __init__(self, master):
            self.master = master
            master.title("Python Calculator")
            master.configure(bg='#333333')  # Dark grey background for the window

            # Create screen widget with new colors
            self.screen = Text(master, state='disabled', width=60, height=3, bg="#F5F5F5", fg="#333333", font=("times", 12, "bold"))

            # Position screen in window
            self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
            self.screen.configure(state='normal')

            # Initialize screen value as empty
            self.equation = ''

            # Create buttons with new colors using method createButton
            b1 = self.createButton(7)
            b2 = self.createButton(8)
            b3 = self.createButton(9)
            b4 = self.createButton(u"\u232B", None)
            b5 = self.createButton(4)
            b6 = self.createButton(5)
            b7 = self.createButton(6)
            b8 = self.createButton(u"\u00F7")
            b9 = self.createButton(1)
            b10 = self.createButton(2)
            b11 = self.createButton(3)
            b12 = self.createButton('*')
            b13 = self.createButton('.')
            b14 = self.createButton(0)
            b15 = self.createButton('+')
            b16 = self.createButton('-')
            b17 = self.createButton('=', None, 34)

            # Buttons stored in list
            buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]

            # Initialize counter
            count = 0
            # Arrange buttons with grid manager
            for row in range(1, 5):
                for column in range(4):
                    buttons[count].grid(row=row, column=column)
                    count += 1
            # Arrange last button '=' at the bottom
            buttons[16].grid(row=5, column=0, columnspan=4)

        def createButton(self, val, write=True, width=7):
            # Create a button with new colors
            return Button(self.master, text=val, command=lambda: self.click(val, write), width=width, bg="#D35400", fg="#F5F5F5", font=("times", 20))

        def click(self, text, write):
            # Handle what happens when you click a button
            if write is None:
                # Only evaluate code when there is an equation to be evaluated
                if text == '=' and self.equation:
                    # Replace the unicode value of division ./. with python division symbol / using regex
                    self.equation = re.sub(u"\u00F7", '/', self.equation)
                    answer = str(eval(self.equation))
                    self.clear_screen()
                    self.insert_screen(answer, newline=True)
                elif text == u"\u232B":
                    self.clear_screen()
            else:
                # Add text to screen
                self.insert_screen(text)

        def clear_screen(self):
            # To clear the screen
            self.equation = ''
            self.screen.configure(state='normal')
            self.screen.delete('1.0', END)

        def insert_screen(self, value, newline=False):
            self.screen.configure(state='normal')
            self.screen.insert(END, value)
            # Record every value inserted in the screen
            self.equation += str(value)
            self.screen.configure(state='disabled')

    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()

love()
