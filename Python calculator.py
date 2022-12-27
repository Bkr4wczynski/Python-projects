import tkinter as tk
from math import *
from random import random

Button_Signs = {0: ('%', '00', 'RAND', 'AC', '\u21BA'),
                1: ('1/x', 'abs', 'ln', 'log(b,a)', 'n!'),
                2: ('pi', 'e', 'fi', '(', ')'),
                3: ('√', 'ʸ√', 'x²', 'xʸ', ','),
                4: ('+', '-', '*', '/', '.'),
                5: ('5', '6', '7', '8', '9'),
                6: ('0', '1', '2', '3', '4')}

Last_Calculations = {1: "",
                     2: "",
                     3: "",
                     4: "",
                     5: ""}

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

font = "Impact"

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("690x441")
root.resizable(False, False)
answer_to_the_equation = ''

zero_error = "Zero division error!"
syntax_error = "Syntax error!"
value_error = "Value error!"
type_error = "Type error!"
name_error = "Name error!"
error = False


def remove_spaces_from_entry():
    to_calc = ""
    for i in Entry.get():
        if i == " ":
            i = ""
        to_calc += i
    Entry.delete(0, tk.END)
    Entry.insert(tk.END, to_calc)


def check_if_user_entered_wrong_math_operation():
    global error
    if Entry.get() != zero_error and Entry.get() != "":
        try:
            round(eval(Entry.get()), 1)
        except SyntaxError:
            Entry.delete(0, tk.END)
            Entry.insert(tk.END, syntax_error)
            error = True
        except ValueError:
            Entry.delete(0, tk.END)
            Entry.insert(tk.END, value_error)
            error = True
        except ZeroDivisionError:
            Entry.delete(0, tk.END)
            Entry.insert(tk.END, zero_error)
            error = True
        except TypeError:
            Entry.delete(0, tk.END)
            Entry.insert(tk.END, type_error)
            error = True
        except NameError:
            Entry.delete(0, tk.END)
            Entry.insert(tk.END, name_error)
            error = True


def calculate_equation_and_show_answer():
    global answer_to_the_equation, error
    remove_spaces_from_entry()
    check_if_user_entered_wrong_math_operation()
    if not error:
        answer_to_the_equation = round(eval(str(Entry.get())), 12)
        Answer_Label.config(text=f"Answer: {answer_to_the_equation}")
        add_result_to_calculations_history()
    error = False


def return_factorial():
    if Entry.get()[-2:] == "n!":
        Entry.delete(len(Entry.get()) - 2, tk.END)
        Entry.insert(tk.END, "factorial(")


def return_square_root():
    if Entry.get()[-1:] == "√" and Entry.get()[-2:] != "ʸ√":
        Entry.delete(len(Entry.get()) - 1, tk.END)
        Entry.insert(tk.END, "**(1/2)")


def return_root():
    if Entry.get()[-2:] == "ʸ√":
        Entry.delete(len(Entry.get()) - 2, tk.END)
        Entry.insert(tk.END, "**(1/")


def return_square():
    if Entry.get()[-2:] == "x²":
        Entry.delete(len(Entry.get()) - 2, tk.END)
        Entry.insert(tk.END, "**2")


def return_power():
    if Entry.get()[-2:] == "xʸ":
        Entry.delete(len(Entry.get()) - 2, tk.END)
        Entry.insert(tk.END, "**")


def return_natural_logarithm():
    if Entry.get()[-2:] == "ln":
        Entry.delete(len(Entry.get()) - 2, tk.END)
        Entry.insert(tk.END, "log(")


def return_logarithm():
    if Entry.get()[-8:] == "log(b,a)":
        Entry.delete(len(Entry.get()) - 8, tk.END)
        Entry.insert(tk.END, "log(")


def return_absolute_value():
    if Entry.get()[-3:] == "abs":
        Entry.delete(len(Entry.get()) - 3, tk.END)
        Entry.insert(tk.END, "abs(")


def return_reciprocal_of_a_number():
    if Entry.get()[-3:] == "1/x":
        Entry.delete(len(Entry.get()) - 3, tk.END)
        Entry.insert(0, "1/")


def return_percent():
    if Entry.get()[-1:] == "%":
        Entry.delete(len(Entry.get()) - 1, tk.END)
        Entry.insert(tk.END, "*0.01")


def return_random_number():
    if Entry.get()[-4:] == "RAND":
        Entry.delete(len(Entry.get()) - 4, tk.END)
        Entry.insert(tk.END, f"{random()}")


def return_fi():
    if Entry.get()[-2:] == "fi":
        Entry.delete(len(Entry.get()) - 2, tk.END)
        Entry.insert(tk.END, f"{(1 + sqrt(5)) / 2}")


def clear_screen():
    if Entry.get()[-2:] == "AC":
        Entry.delete(0, tk.END)


def clear_last_screen_digit():
    if Entry.get()[-1:] == "\u21BA":
        Entry.delete(len(Entry.get()) - 2, tk.END)


def copy_answer_to_clipboard():
    if Answer_Label.cget("text") != "Answer: waiting... ":
        root.clipboard_clear()
        root.clipboard_append(Answer_Label.cget("text")[8:])


Entry = tk.Entry(root, width=23, font="Impact 17", fg="#C6CECE", bg="#36454F")
Entry.place(x=410, y=0)
Calculate_Button = tk.Button(root, width=34, height=2, text="Calculate", font=font, fg="#36454F", bg="#C6CECE")
Calculate_Button.config(command=calculate_equation_and_show_answer)
Calculate_Button.place(x=410, y=32)
Answer_Label = tk.Label(root, width=35, height=4, fg="#C6CECE", bg="#36454F", font=font, text="Answer: waiting... ")
Answer_Label.place(x=410, y=87)
Calculations_History_Label = tk.Label(root, width=28, height=11, fg="#C6CECE", bg="gray4")
Calculations_History_Label.config(font=f"{font} 15")
Calculations_History_Label.place(x=410, y=173)
Copy_Button = tk.Button(root, width=34, height=2, text="Copy answer", font=font, fg="#36454F", bg="#C6CECE")
Copy_Button.config(command=copy_answer_to_clipboard)
Copy_Button.place(x=410, y=174)

index = 1


def add_result_to_calculations_history():
    global index
    if index > 5:
        index = 1
    Last_Calculations[index] = f"{answer_to_the_equation}"
    index += 1
    initialize_calculation_history_label()


def initialize_calculation_history_label():
    x = '\n'. join(f'{key}: {value}' if value else f"{key}: waiting..." for key, value in Last_Calculations.items())
    Calculations_History_Label.config(text=f"\nCalculations history: \n{x}")


def call_needed_functions():
    return_factorial()
    return_square_root()
    return_square()
    return_power()
    return_root()
    return_natural_logarithm()
    return_logarithm()
    return_absolute_value()
    return_reciprocal_of_a_number()
    return_percent()
    return_random_number()
    return_fi()
    clear_screen()
    clear_last_screen_digit()


def insert_button_sign_chosen_by_user(mouse):
    Entry.insert(tk.END, mouse.widget.cget('text'))
    call_needed_functions()


def build_ui_and_bind_buttons():
    for y in range(7):
        for x in range(5):
            button = tk.Button(Frame)
            button.config(text=Button_Signs[y][x], height=2, width=8, font=f"{font} 14", fg="#C6CECE", bg="#36454F")
            button.grid(row=y, column=x)
            button.bind('<Button-1>', insert_button_sign_chosen_by_user)


if __name__ == "__main__":
    Frame = tk.Frame(root)
    Frame.place(x=0, y=0)
    build_ui_and_bind_buttons()
    initialize_calculation_history_label()
    root.mainloop()

# Podziękowania dla lukasa i binq za pomoc w tworzeniu kodu
# Kod tego programu NIE JEST zastrzeżony, można korzystać z niego oraz go modyfikować bez żadnych opłat.
