import tkinter as tk
from tkinter import messagebox

def calculate_monthly_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 100 / 121
    total_payments = years * 12
    result = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / ((1 + monthly_rate) ** total_payments - 1)
    print(round(result, 2))
    #111
    return round(result, 2)


def calculate_mortgage():
    try:
        principal = float(entry_principal.get())
        annual_rate = float(entry_rate.get()) 
        years = int(entry_years.get())
        
        monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
        
        label_result.config(text=f"Ежемесячный платеж: {monthly_payment} руб.")
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные данные.")



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ипотечный калькулятор")
    
    tk.Label(root, text="Сумма кредита (руб):").grid(row=0, column=0)
    entry_principal = tk.Entry(root)
    entry_principal.grid(row=0, column=1)

    tk.Label(root, text="Процентная ставка (% годовых):").grid(row=1, column=0)
    entry_rate = tk.Entry(root)
    entry_rate.grid(row=1, column=1)

    tk.Label(root, text="Срок (лет):").grid(row=2, column=0)
    entry_years = tk.Entry(root)
    entry_years.grid(row=2, column=1)

    btn_calculate = tk.Button(root, text="Рассчитать", command=calculate_mortgage)
    btn_calculate.grid(row=3, column=0)

    label_result = tk.Label(root, text="Ежемесячный платеж: 0.00 руб.")
    label_result.grid(row=4, column=0)
    
    root.mainloop()