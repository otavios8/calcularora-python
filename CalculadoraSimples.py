def calcular(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return "Operação inválida"


def main():
    try:
        a = float(input("Primeiro número: "))
        op = input("Operação (+ - * /): ")
        b = float(input("Segundo número: "))

        print("Resultado:", calcular(a, b, op))

    except ValueError:
        print("Digite apenas números válidos")


if __name__ == "__main__":
    main()
    