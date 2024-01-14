import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Currency Converter")

        # Set window size and default currency values
        self.root.geometry("800x600")
        self.from_currency_var = tk.StringVar(value="INR")
        self.to_currency_var = tk.StringVar(value="USD")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Styling
        style = ThemedStyle(self.root)
        style.set_theme("equilux")

        # Customize the style for Label and Button widgets
        style.configure('White.TLabel', foreground='white', font=('Helvetica', 18, 'bold'))
        style.configure('White.TButton', foreground='white', font=('Helvetica', 14, 'bold'))
        style.configure('MadeBy.TLabel', foreground='white', font=('Helvetica', 12))

        # Main Frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Title Label
        title_label = ttk.Label(main_frame, text="Currency Converter", style='White.TLabel')
        title_label.pack(pady=20)

        # Amount Entry
        amount_label = ttk.Label(main_frame, text="Amount:", style='White.TLabel')
        amount_label.pack(pady=10)
        self.amount_entry = ttk.Entry(main_frame, font=("Helvetica", 14))
        self.amount_entry.pack(pady=10)

        # From Currency
        from_currency_label = ttk.Label(main_frame, text="From Currency:", style='White.TLabel')
        from_currency_label.pack(pady=10)
        self.from_currency_combobox = ttk.Combobox(main_frame, textvariable=self.from_currency_var, values=self.get_currency_list(),
                                                   font=("Helvetica", 14))
        self.from_currency_combobox.pack(pady=10)

        # To Currency
        to_currency_label = ttk.Label(main_frame, text="To Currency:", style='White.TLabel')
        to_currency_label.pack(pady=10)
        self.to_currency_combobox = ttk.Combobox(main_frame, textvariable=self.to_currency_var, values=self.get_currency_list(),
                                                 font=("Helvetica", 14))
        self.to_currency_combobox.pack(pady=10)

        # Convert Button
        convert_button = ttk.Button(main_frame, text="Convert", style="TButton.Convert.TButton", command=self.convert_currency)
        convert_button.pack(pady=20)

        # Result Label
        self.result_var = tk.StringVar()
        result_label = ttk.Label(main_frame, textvariable=self.result_var, style='White.TLabel', wraplength=600)
        result_label.pack(pady=20)

        # Made by Label
        made_by_label = ttk.Label(main_frame, text="Made by Jude Felix, Rahul D, and Jai Surya of class 12 B", style='MadeBy.TLabel')
        made_by_label.pack(pady=20)

    def get_currency_list(self):
        # Add more currencies as needed
        return ["USD", "EUR", "GBP", "INR", "JPY"]

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            c = CurrencyRates()
            rate = c.get_rate(from_currency, to_currency)
            result = amount * rate

            self.result_var.set(f"{amount:.2f} {self.get_currency_symbol(from_currency)} = {result:.2f} {self.get_currency_symbol(to_currency)}")

        except Exception as e:
            self.result_var.set(f"Error: {e}")

    def get_currency_symbol(self, currency_code):
        # Add more currency symbols as needed
        symbols = {"USD": "$", "EUR": "€", "GBP": "£", "INR": "₹", "JPY": "¥"}
        return symbols.get(currency_code, currency_code)

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()


