import tkinter as tk
from tkinter import messagebox

class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de Caracteres Especiais")
        self.geometry("450x400")

        self.codigo_peca_entry = tk.Entry(self)
        self.codigo_original_entry = tk.Entry(self)
        self.tipo_peca_entry = tk.Entry(self)
        self.linhas_entry = tk.Entry(self)

        self.codigo_peca_entry.place(x=10, y=10, width=200, height=20)
        self.codigo_original_entry.place(x=10, y=40, width=200, height=20)
        self.tipo_peca_entry.place(x=10, y=70, width=200, height=20)
        self.linhas_entry.place(x=10, y=100, width=200, height=20)

        self.converter_button = tk.Button(self, text="Converter", command=self.converter_button_click)
        self.converter_button.place(x=10, y=130, width=100, height=30)

        self.resultado_textbox = tk.Text(self, width=55, height=13)
        self.resultado_textbox.place(x=10, y=170)

    def converter_button_click(self):
        codigo_peca = self.codigo_peca_entry.get()
        codigo_original = self.codigo_original_entry.get()
        tipo_peca = self.tipo_peca_entry.get()
        linhas = int(self.linhas_entry.get())

        self.resultado_textbox.delete(1.0, tk.END)

        for _ in range(linhas):
            texto = messagebox.askstring("Texto", "Digite um texto:")
            texto_convertido = self.converter_seta_e_barra(texto)
            self.resultado_textbox.insert(tk.END, texto_convertido + "\n")

        self.resultado_textbox.insert(tk.END, "Texto convertido:\n")
        self.resultado_textbox.insert(tk.END, tipo_peca + "\n\n")
        self.resultado_textbox.insert(tk.END, "Código da Peça:\n")
        self.resultado_textbox.insert(tk.END, codigo_peca + "\n\n")
        self.resultado_textbox.insert(tk.END, "Código Original:\n")
        self.resultado_textbox.insert(tk.END, codigo_original + "\n\n")
        self.resultado_textbox.insert(tk.END, "Intercambialidade:")

    def converter_seta_e_barra(self, texto):
        texto_convertido = texto.replace("->", "→").replace("|", "│")
        return texto_convertido

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
