from tkinter import Tk, ttk, Text, Button


def criar_interface():

    def adicionar_numero(numero):
        conta.config(state='normal')
        conta.insert('end', numero)
        conta.config(state='disabled')

    def get_resultado_e_operacao():
        resultado = float(conta.get('1.0', 'end'))
        operacao = botao_operacao.get()
        return [resultado, operacao]
    
    janela = Tk()
    janela.title('Calculadora')

    frame_global = ttk.Frame()

    # Tela para ver conta
    conta_frame = ttk.Frame(frame_global)
    conta = Text(
        conta_frame,
        state='disabled',
        width=40,
    )
    conta.pack(fill='both', expand='yes')

    # Teclado numérico
    teclado_numero = ttk.Frame(frame_global)

    label_operacao = ttk.Label(
        teclado_numero,
        text='Operação:',
        font=(None, 12)
    )
    label_operacao.grid(row=0, column=0, pady=10)

    botao_operacao = ttk.Combobox(
        teclado_numero,
        values=['+', '-', '*', '/'],
    )
    botao_operacao.grid(row=0, column=1, pady=10)

    botao0 = Button(
        teclado_numero,
        text='0',
        width=7,
        height=1,
        command=lambda: adicionar_numero('0')
    )
    botao0.grid(row=4, column=1)

    botao1 = Button(
        teclado_numero,
        text='1',
        width=7,
        height=1,
        command=lambda: adicionar_numero('1')
    )
    botao1.grid(row=1, column=0)

    botao2 = Button(
        teclado_numero,
        text='2',
        width=7,
        height=1,
        command=lambda: adicionar_numero('2')
    )
    botao2.grid(row=1, column=1)

    botao3 = Button(
        teclado_numero,
        text='3',
        width=7,
        height=1,
        command=lambda: adicionar_numero('3')
    )
    botao3.grid(row=1, column=2)

    botao4 = Button(
        teclado_numero,
        text='4',
        width=7,
        height=1,
        command=lambda: adicionar_numero('4')
    )
    botao4.grid(row=2, column=0)

    botao5 = Button(
        teclado_numero,
        text='5',
        width=7,
        height=1,
        command=lambda: adicionar_numero('5')
    )
    botao5.grid(row=2, column=1)

    botao6 = Button(
        teclado_numero,
        text='6',
        width=7,
        height=1,
        command=lambda: adicionar_numero('6')
    )
    botao6.grid(row=2, column=2)

    botao7 = Button(
        teclado_numero,
        text='7',
        width=7,
        height=1,
        command=lambda: adicionar_numero('7')
    )
    botao7.grid(row=3, column=0)

    botao8 = Button(
        teclado_numero,
        text='8',
        width=7,
        height=1,
        command=lambda: adicionar_numero('8')
    )
    botao8.grid(row=3, column=1)

    botao9 = Button(
        teclado_numero,
        text='9',
        width=7,
        height=1,
        command=lambda: adicionar_numero('9')
    )
    botao9.grid(row=3, column=2)

    # Botão de calcular
    botao_calcular = Button(
        text='Calcular',
        command=get_resultado_e_operacao
    )

    conta_frame.pack()
    teclado_numero.pack()
    frame_global.pack()
    botao_calcular.pack(fill='both')

    janela.mainloop()
