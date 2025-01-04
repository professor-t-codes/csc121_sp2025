# Richard Tillies
# January 4, 2025
# GUI Programming
#
import tkinter as tk
import tkinter.messagebox as mb

# Grade weights
TEST_WEIGHT = 0.2
LAB_WEIGHT = 0.3
EXAM_WEIGHT = 0.5


class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Grade Calculator")
        self.main_window.geometry('260x150')

        # Frames
        self.tests_frame = tk.Frame(self.main_window)
        self.labs_frame = tk.Frame(self.main_window)
        self.exams_frame = tk.Frame(self.main_window)
        self.average_frame = tk.Frame(self.main_window)
        self.buttons_frame = tk.Frame(self.main_window)

        # Tests Frame
        self.test_label = tk.Label(self.tests_frame, text='Tests Grade:')
        self.test_entry = tk.Entry(self.tests_frame, width=5)

        self.test_label.pack(side='left')
        self.test_entry.pack(side='left')

        # Labs Frame
        self.lab_label = tk.Label(self.labs_frame, text='Labs Grade:')
        self.lab_entry = tk.Entry(self.labs_frame, width=5)

        self.lab_label.pack(side='left')
        self.lab_entry.pack(side='left')

        # Exams Frame
        self.exam_label = tk.Label(self.exams_frame, text='Exams Grade:')
        self.exam_entry = tk.Entry(self.exams_frame, width=5)

        self.exam_label.pack(side='left')
        self.exam_entry.pack(side='left')

        # Average Frame
        self.result_value = tk.StringVar()
        self.result_value.set('TBD')
        self.avg_label = tk.Label(self.average_frame, text='Grade Average:')
        self.result_label = tk.Label(self.average_frame, textvariable=self.result_value)

        self.avg_label.pack(side='left')
        self.result_label.pack(side='left')

        # Buttons Frame
        self.calc_button = tk.Button(self.buttons_frame, text='Calculate', command=self.calc_grade)
        self.quit_button = tk.Button(self.buttons_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.tests_frame.pack()
        self.labs_frame.pack()
        self.exams_frame.pack()
        self.average_frame.pack()
        self.buttons_frame.pack(side='bottom')

        tk.mainloop()

    def calc_grade(self):
        try:
            tests = float(self.test_entry.get())
            labs = float(self.lab_entry.get())
            exams = float(self.exam_entry.get())

            average = tests * TEST_WEIGHT \
                      + labs * LAB_WEIGHT \
                      + exams * EXAM_WEIGHT

            letter = self.get_letter(average)
            # print(f'{average:.1f} {letter}')
            self.result_value.set(f'{average:.1f} ({letter})')
        except ValueError:
            # mb.showinfo('Invalid entry', 'Please enter numbers only')
            # mb.showerror('Invalid entry', 'Please enter numbers only')
            self.result_value.set(f'*ERROR*')

    def get_letter(self, grade):
        if grade >= 90:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        else:
            return 'F'


my_gui = MyGUI()
