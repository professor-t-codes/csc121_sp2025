# Richard Tillies
# January 4, 2025
# GUI Programming
#
import tkinter as tk
import tkinter.messagebox as mb

# Prices and Discount
WORKBOOK_PRICE = 8.5
TEXTBOOK_PRICE = 24.0
MAGAZINE_PRICE = 5.95
DISCOUNT = 0.25


class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Cash Register")
        self.main_window.geometry('260x200')

        # Frames
        self.workbooks_frame = tk.Frame(self.main_window)
        self.textbooks_frame = tk.Frame(self.main_window)
        self.magazines_frame = tk.Frame(self.main_window)
        self.discount_frame = tk.Frame(self.main_window)
        self.total_frame = tk.Frame(self.main_window)
        self.buttons_frame = tk.Frame(self.main_window)

        # Workbooks Frame
        self.workbook_label = tk.Label(self.workbooks_frame, text='Workbooks:')
        self.workbook_entry = tk.Entry(self.workbooks_frame, width=5)
        self.workbook_label.pack(side='left')
        self.workbook_entry.pack(side='left')

        # Textbooks Frame
        self.textbook_label = tk.Label(self.textbooks_frame, text='Textbooks:')
        self.textbook_entry = tk.Entry(self.textbooks_frame, width=5)
        self.textbook_label.pack(side='left')
        self.textbook_entry.pack(side='left')

        # Magazines Frame
        self.magazine_label = tk.Label(self.magazines_frame, text='Magazines:')
        self.magazine_entry = tk.Entry(self.magazines_frame, width=5)
        self.magazine_label.pack(side='left')
        self.magazine_entry.pack(side='left')

        # Discount Frame
        self.is_checked = tk.IntVar()

        self.discount_checkbox = tk.Checkbutton(self.discount_frame, text="25% Discount", variable=self.is_checked)
        self.discount_checkbox.pack(side='left')

        # Total Frame
        self.result_value = tk.StringVar()
        self.result_value.set('$0.00')

        self.total_label = tk.Label(self.total_frame, text='Total:')
        self.result_label = tk.Label(self.total_frame, textvariable=self.result_value)
        self.total_label.pack(side='left')
        self.result_label.pack(side='left')

        # Buttons Frame
        self.calc_button = tk.Button(self.buttons_frame, text='Calculate', command=self.calc_total)
        self.quit_button = tk.Button(self.buttons_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames on window
        self.workbooks_frame.pack()
        self.textbooks_frame.pack()
        self.magazines_frame.pack()
        self.discount_frame.pack()
        self.total_frame.pack()
        self.buttons_frame.pack(side='bottom')

        tk.mainloop()

    def calc_total(self):
        try:
            workbooks = float(self.workbook_entry.get())
            textbooks = float(self.textbook_entry.get())
            magazines = float(self.magazine_entry.get())
            is_discount = self.is_checked.get()

            total = workbooks * WORKBOOK_PRICE \
                    + textbooks * TEXTBOOK_PRICE \
                    + magazines * MAGAZINE_PRICE

            if is_discount:
                total *= (1 - DISCOUNT)

            self.result_value.set(f'${total:.2f}')
        except ValueError:
            # mb.showinfo('Invalid entry', 'Please enter numbers only')
            # mb.showerror('Invalid entry', 'Please enter numbers only')
            self.result_value.set(f'*ERROR*')


my_gui = MyGUI()
