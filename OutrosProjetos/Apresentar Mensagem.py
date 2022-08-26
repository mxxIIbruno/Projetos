import Ferramentas.Cor as cor


def apresentar(lista, num1=None, num2=None):
    if isinstance(lista, list):
        for ind, fun in enumerate(lista):
            print(fun(f" {ind} "), end="|")
            if (ind + 1) == len(lista) // 2:
                print()
        print()
    if isinstance(lista, str):
        return cor.color(lista, num1, num2)


back = [
    cor.background_red, cor.background_black,
    cor.background_green, cor.backgorund_pink,
    cor.background_blue, cor.background_grey,
    cor.background_black, cor.background_purple,
    cor.background_white, cor.background_yellow
]
fonte = [
    cor.fonte_preto, cor.fonte_rosa,
    cor.fonte_azul_marinho, cor.fonte_roxo,
    cor.fonte_cinza, cor.fonte_amarelo,
    cor.fonte_branco, cor.fonte_verde,
    cor.fonte_vermelho
]
configurar = []

print("\t\tFormatar Cor Da Sua Mensagem\n")

apresentar(fonte)
while not configurar:
    entrada_fonte = input("\nEscolha nº[índice]: ")
    if not entrada_fonte.isdigit():
        print("ERRO:\n\tEscolha Número do índice.")
        continue
    configurar.append(int(entrada_fonte))

apresentar(back)
while len(configurar) < 2:
    entrada_background = input("\nEscolha nº[índice]: ")
    if not entrada_background.isdigit():
        print("ERRO:\n\tEscolha Número do índice.")
        continue
    configurar.append(int(entrada_background))
elemento1, elemento2 = fonte[configurar[0]], back[configurar[1]]

mensagem = input("Digite Uma Mensagem: ")
mensagem = apresentar(mensagem, num1=elemento1, num2=elemento2)

print(f'\nSUA MENSAGEM:\n\t{mensagem}')
