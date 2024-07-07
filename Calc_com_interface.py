
import flet as ft
from flet import colors

botoes = [
    {'operador': 'AC','fonte': colors.BLACK,'fundo': colors.BLUE_GREY_100},
    {'operador': '±','fonte': colors.BLACK,'fundo': colors.BLUE_GREY_100},
    {'operador': '%','fonte': colors.BLACK,'fundo': colors.BLUE_GREY_100},
    {'operador': '/','fonte': colors.WHITE,'fundo': colors.ORANGE},
    {'operador': '7','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '8','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '9','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '*','fonte': colors.WHITE,'fundo': colors.ORANGE},
    {'operador': '4','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '5','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '6','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '-','fonte': colors.WHITE,'fundo': colors.ORANGE},
    {'operador': '1','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '2','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '3','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '+','fonte': colors.WHITE,'fundo': colors.ORANGE},
    {'operador': '0','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '.','fonte': colors.WHITE,'fundo': colors.WHITE24},
    {'operador': '=','fonte': colors.WHITE,'fundo': colors.ORANGE},
]

def main(page: ft.Page): # Cria a função 'main' que recebe o parametro 'page'
    page.bgcolor = '#000' # Atribui cor preta baseado em HEX
    page.window.resizable = False # Habilita ou não o redimensionamento de janela
    page.window.width = 268 # Largura em 'px'
    page.window.height = 390 # Altura em 'px'
    page.title = 'Calculadora' # Atribui título a janela
    page.window.always_on_top = True # A janela sempre ficara visível no editor
    # Resultados das operações + atribuição de cor pela biblioteca flat 
    result = ft.Text(value ='0', color = colors.WHITE, size=20) 

    def calculate(operador, value_at):
        try:
            value = eval(value_at)

            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
        except:
            return 'Error'
        
        return value

    def select(e):
        value_at = result.value if result.value not in ('0','Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/','*','-','+','.'):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=','%','±'):
                value = calculate(operador=value[-1], value_at=value_at)

        result.value = value
        result.update()

    display = ft.Row(
        width=250,              # Cria uma linha de comprimento = width em px, controls permite puxar a variavel(result).
        controls=[result],
        alignment = 'end'
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=50,               
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
    ) for btn in botoes]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard) # Adiciona variaveis a janela do aplicativo


ft.app(target = main) # Recebe o parametro 'target'
