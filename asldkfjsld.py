import tkinter
import tkinter.messagebox
# //Author Name: Bijan Amirzadehasl
# //Date: 11/3/2021
# //Program Name: Amirzadehasl_JoeFastFood.py
# //Purpose: Make a GUI of checkboxes for a fast food restaurants that adds up the total of items checked
#   Purpose: Also include a text box that contains special instructions for the cook
#   Purpose: display the total and special instructions in another window

class MyGUI:
    def __init__(self):
        # Modified the check buttons demo in example 13-13
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()

        self.prompt_label = tkinter.Label(self.bottom_frame,
                                          text='Instructions for Kitchen:')
        self.instruct_entry = tkinter.Entry(self.bottom_frame,
                                            width=5)

        self.prompt_label.pack(side='left')
        self.instruct_entry.pack(side='left')

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)

        self.cb1 = tkinter.Checkbutton(self.top_frame, \
                                       text='Hamburger $4', onvalue=4, offvalue=0, variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, \
                                       text='Cheese Burger $5', onvalue=5, offvalue=0, variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, \
                                       text='Large Fries $4', onvalue=4, offvalue=0, variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, \
                                       text='Medium Fries $2', onvalue=2, offvalue=0, variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, \
                                       text='Large Soda $3', onvalue=3, offvalue=0, variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, \
                                       text='Medium Soda $1', onvalue=1, offvalue=0, variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, \
                                       text='Apple Pie $3', onvalue=3, offvalue=0, variable=self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.top_frame, \
                                       text='Ice Cream $4', onvalue=4, offvalue=0, variable=self.cb_var8)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, \
                                        text='OK', command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                                          text='Quit', command=self.main_window.destroy)

        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_choice(self):

        total = self.cb_var1.get() + self.cb_var2.get() + self.cb_var3.get() + self.cb_var4.get() + self.cb_var5.get() + self.cb_var6.get() + self.cb_var7.get() + self.cb_var8.get()
        self.message = 'Total cost of order: $' + str(total) + '\nInstructions for the kitchen: ' + str(self.instruct_entry.get())

        if self.cb_var1.get() == 1:
            self.message = self.message + '\n'
        if self.cb_var2.get() == 1:
            self.message = self.message + '\n'
        if self.cb_var3.get() == 1:
            self.message = self.message + '\n'
        if self.cb_var4.get() == 1:
            self.message = self.message + '\n'
        if self.cb_var5.get() == 1:
            self.message = self.message + '\n'
        if self.cb_var6.get() == 1:
            self.message = self.message + '\n'
        if self.cb_var7.get() == 1:
            self.message = self.message + '\n'
        if self.cb_var8.get() == 1:
            self.message = self.message + '\n'

        tkinter.messagebox.showinfo('Order', self.message)


def main():
    my_gui = MyGUI()


main()
