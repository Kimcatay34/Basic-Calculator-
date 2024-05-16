import tkinter as tk

def calculator():
    calculator_root = tk.Toplevel(root)
    calculator_root.title("Calculator")
    calculator_root.geometry("665x725+150+250")
    calculator_root.configure(bg='#022345')
    

    equation = ""
    def show(value):
        nonlocal equation
        equation += value
        label_result.config(text=equation)

    def clear():
        nonlocal equation
        equation = ""
        label_result.config(text=equation)

    def calculate():
        nonlocal equation
        result = ""
        if equation!= "":
            try:
                result = eval(equation)
            except:
                result = "Error"
                equation = ""
        label_result.config(text=result)

    label_result = tk.Label(calculator_root, width=25, height=2, text="", font=("arial",30,"bold"), justify= tk.RIGHT)
    label_result.pack()

    # Add buttons here
    button1=tk.Button(calculator_root, text="C", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#fa8a20', fg='#00698f',command=lambda: clear())
    button1.place(x=20, y=135)
    button2=tk.Button(calculator_root, text="/", width=3, height=1, font=("arial", 30, "bold"), bd=1,bg='#122534', fg='#00698f', command=lambda: show("/"))
    button2.place(x=200, y=135)
    button3=tk.Button(calculator_root, text="%", width=3, height=1, font=("arial", 30, "bold"), bd=1,bg='#122534', fg='#00698f', command=lambda: show("%"))
    button3.place(x=390, y=135)
    button4=tk.Button(calculator_root, text="*", width=3, height=1, font=("arial", 30, "bold"), bd=1,bg='#122534', fg='#00698f', command=lambda: show("*"))
    button4.place(x=530, y=135)

    button5=tk.Button(calculator_root, text="7", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("7"))
    button5.place(x=20, y=235)
    button6=tk.Button(calculator_root, text="8", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("8"))
    button6.place(x=200, y=235)
    button7=tk.Button(calculator_root, text="9", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("9"))
    button7.place(x=390, y=235)
    button8=tk.Button(calculator_root, text="-", width=3, height=1, font=("arial", 30, "bold"), bd=1,bg='#122534', fg='#00698f', command=lambda: show("-"))
    button8.place(x=530, y=235)

    button9=tk.Button(calculator_root, text="4", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("4"))
    button9.place(x=20, y=335)
    button0=tk.Button(calculator_root, text="5", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("5"))
    button0.place(x=200, y=335)
    button00=tk.Button(calculator_root, text="6", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("6"))
    button00.place(x=390, y=335)
    button11=tk.Button(calculator_root, text="+", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#122534', fg='#00698f', command=lambda: show("+"))
    button11.place(x=530, y=335)

    button12=tk.Button(calculator_root, text="1", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("1"))
    button12.place(x=20, y=435)
    button13=tk.Button(calculator_root, text="2", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("2"))
    button13.place(x=200, y=435)
    button14=tk.Button(calculator_root, text="3", width=3, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("3"))
    button14.place(x=390, y=435)
    button15=tk.Button(calculator_root, text="0", width=8, height=1, font=("arial", 30, "bold"), bd=1, bg='#d6e9ff', fg='#00698f', command=lambda: show("0"))
    button15.place(x=20, y=535)

    button16=tk.Button(calculator_root, text=".", width=3, height=1, font=("arial", 30, "bold"), bd=1,bg='#d6e9ff', fg='#00698f', command=lambda: show("."))
    button16.place(x=350, y=535)
    button17=tk.Button(calculator_root, text="=", width=3, height=2, font=("arial", 30, "bold"), bd=1,bg='#505050', fg='#00698f', command=lambda: calculate())
    button17.place(x=530, y=445)

def discount_calculator():
    calculator_root = tk.Toplevel(root)
    calculator_root.title("Discount Calculator")
    calculator_root.geometry("400x200+150+250")
    calculator_root.configure(bg='#0558ac')

    marked_price_label = tk.Label(calculator_root, text="Marked Price:", bg='#a8c6e0')
    marked_price_label.pack()
    marked_price_entry = tk.Entry(calculator_root)
    marked_price_entry.pack()

    discount_label = tk.Label(calculator_root, text="Discount (%):",bg='#a8c6e0')
    discount_label.pack()
    discount_entry = tk.Entry(calculator_root)
    discount_entry.pack()

    final_price_label = tk.Label(calculator_root, text="Final Price:",bg='#a8c6e0')
    final_price_label.pack()

    def calculate_final_price():
        marked_price = float(marked_price_entry.get())
        discount_percentage = float(discount_entry.get())
        discount = (discount_percentage / 100) * marked_price
        selling_price = marked_price - discount
        final_price_label.config(text=f"Final Price: {selling_price:.2f}")
        discount_label.config(text=f"Discount: {discount_percentage:.2f}%")

    calculate_button = tk.Button(calculator_root, text="Calculate", bg='#d6e9ff',command=calculate_final_price)
    calculate_button.pack()

root = tk.Tk()
root.title("Main Window")
root.geometry("200x200")
root.configure(bg='#0097e8')  # blue background

button2 = tk.Button(root, text="Discount Calculator", command=discount_calculator, bg='#ffcc00', fg='#00698f')  # light orange background and blue text
button2.pack(pady=10)

button = tk.Button(root, text="Calculator", command=calculator, bg='#33cc33', fg='#00698f')  # light green background and blue text
button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit, bg='#ff9999', fg='#00698f')  # light red background and blue text
quit_button.pack(pady=10)

root.mainloop()
