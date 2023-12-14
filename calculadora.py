import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.resizable(False, False)
        
        self.resultado_var = tk.StringVar()

        # Pantalla
        pantalla = tk.Entry(self, textvariable=self.resultado_var, font=('Arial', 14),
                            bd=10, insertwidth=4, width=22,justify='right')
        pantalla.grid(row=0, column=0, columnspan=4)

        # Teclas de la calculadora
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        

        for (texto, fila, columna) in botones:
            tk.Button(self, text=texto, padx=16, pady=16, font=('Arial', 14),
                command=lambda t=texto: self.click(t)).grid(row=fila,column=columna, padx=5, pady=5)

        
    def click(self, valor):
        if valor == '=':
            try:
                resultado = str(eval(self.resultado_var.get()))
                self.resultado_var.set(resultado)
            except Exception as e:
                self.resultado_var.set("Error")
        elif valor == 'C':
            self.resultado_var.set("")
        else:
            self.resultado_var.set(self.resultado_var.get() + valor)

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()