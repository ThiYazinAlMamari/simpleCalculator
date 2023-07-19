import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to delete the last character in the entry field
def delete_character():
    entry.delete(len(entry.get())-1)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define button styling
button_width = 8
button_height = 3
button_padx = 10
button_pady = 10

# Create number buttons
button_one = tk.Button(window, text="1", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                       command=lambda: button_click(1))
button_one.grid(row=3, column=0)

button_two = tk.Button(window, text="2", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                       command=lambda: button_click(2))
button_two.grid(row=3, column=1)

button_three = tk.Button(window, text="3", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                         command=lambda: button_click(3))
button_three.grid(row=3, column=2)

button_four = tk.Button(window, text="4", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                        command=lambda: button_click(4))
button_four.grid(row=2, column=0)

button_five = tk.Button(window, text="5", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                        command=lambda: button_click(5))
button_five.grid(row=2, column=1)

button_six = tk.Button(window, text="6", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                       command=lambda: button_click(6))
button_six.grid(row=2, column=2)

button_seven = tk.Button(window, text="7", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                         command=lambda: button_click(7))
button_seven.grid(row=1, column=0)

button_eight = tk.Button(window, text="8", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                         command=lambda: button_click(8))
button_eight.grid(row=1, column=1)

button_nine = tk.Button(window, text="9", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                        command=lambda: button_click(9))
button_nine.grid(row=1, column=2)

# Create operator buttons
button_plus = tk.Button(window, text="+", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                        command=lambda: button_click("+"))
button_plus.grid(row=3, column=3)

button_minus = tk.Button(window, text="-", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                         command=lambda: button_click("-"))
button_minus.grid(row=3, column=4)

button_multiply = tk.Button(window, text="*", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                            command=lambda: button_click("*"))
button_multiply.grid(row=2, column=3)

button_divide = tk.Button(window, text="/", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                          command=lambda: button_click("/"))
button_divide.grid(row=2, column=4)

# Create other buttons
button_zero = tk.Button(window, text="0", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                        command=lambda: button_click(0))
button_zero.grid(row=4, column=0)

button_all_clear = tk.Button(window, text="AC", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                             command=clear_entry, bg="orange")
button_all_clear.grid(row=1, column=3)

button_delete = tk.Button(window, text="DEL", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                          command=delete_character, bg="orange")
button_delete.grid(row=1, column=4)

button_equal = tk.Button(window, text="=", width=button_width, height=button_height, padx=button_padx, pady=button_pady,
                         command=evaluate_expression)
button_equal.grid(row=4, column=1)

# Start the main event loop
window.mainloop()

