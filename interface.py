from tkinter import Tk, ttk, Entry, Button
from ttkbootstrap import Style

def criar_interface(subtracao, divisao, multiplicacao, soma):

    def calcular_resultado():
        try:
            numero1 = float(entrada_numero1.get())
            numero2 = float(entrada_numero2.get())
            operacao = botao_operacao.get()
            
            if operacao == '+':
                resultado = soma(numero1, numero2)
            elif operacao == '-':
                resultado = subtracao(numero1, numero2)
            elif operacao == '*':
                resultado = multiplicacao(numero1, numero2)
            elif operacao == '/':
                resultado = divisao(numero1, numero2)
            else:
                resultado = 'Operação inválida'
            
            resultado_label.config(text=f'Resultado: {resultado}')
        except Exception as e:
            resultado_label.config(text=f'Erro: {e}')

    estilo = Style(theme='superhero')
    janela = estilo.master
    janela.title('Calculadora')

    frame_global = ttk.Frame()

    # Entrada para os números
    entrada_frame = ttk.Frame(frame_global)
    
    label_numero1 = ttk.Label(entrada_frame, text='Número 1:')
    label_numero1.grid(row=0, column=0, padx=5, pady=5)
    entrada_numero1 = Entry(entrada_frame)
    entrada_numero1.grid(row=0, column=1, padx=5, pady=5)

    label_numero2 = ttk.Label(entrada_frame, text='Número 2:')
    label_numero2.grid(row=1, column=0, padx=5, pady=5)
    entrada_numero2 = Entry(entrada_frame)
    entrada_numero2.grid(row=1, column=1, padx=5, pady=5)

    # Seletor de operação
    label_operacao = ttk.Label(entrada_frame, text='Operação:')
    label_operacao.grid(row=2, column=0, padx=5, pady=5)
    botao_operacao = ttk.Combobox(entrada_frame, values=['+', '-', '*', '/'])
    botao_operacao.grid(row=2, column=1, padx=5, pady=5)

    # Botão de calcular
    botao_calcular = Button(entrada_frame, text='Calcular', command=calcular_resultado)
    botao_calcular.grid(row=3, columnspan=2, pady=10)

    # Label para mostrar o resultado
    resultado_label = ttk.Label(entrada_frame, text='Resultado:')
    resultado_label.grid(row=4, columnspan=2, pady=5)

    entrada_frame.pack(padx=10, pady=10)
    frame_global.pack(padx=10, pady=10)

    janela.mainloop()
