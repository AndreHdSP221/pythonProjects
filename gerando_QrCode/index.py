from qrCode import qrCode

while True:
    try:
        codigo_qrCode = input("Digite o código que o qrCode deverá exibir: ")
        if codigo_qrCode.lower() == "sair":
            break
        nome_Pasta = input("Digite o nome da Subpasta: ")
        qtd_qrCode = int(input("Digite a quantidade de qrCodes (Somente inteiros): "))

        qr = qrCode(codigo_qrCode, nome_Pasta)
        qr.gerarCodigo(qtd_qrCode)

    except ValueError:
        print("Por favor, insira um número inteiro válido.")
    except Exception as error:
        print(f"Ocorreu um erro: {error}")
