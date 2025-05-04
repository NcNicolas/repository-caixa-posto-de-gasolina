from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 10
getcontext().rounding = ROUND_HALF_UP

# Nomes das bombas e tanques
nome_bombas = [
    "Gasolina 1",
    "Gasolina 2",
    "Gasolina 3",
    "V-power",
    "S10 1",
    "S10 2",
    "S500 3"
]

nome_tanques = [
    "Gasolina comum",
    "Diesel S10",
    "Diesel S500",
    "V-power"
]

# Preços das bombas
preco_bombas = [
    Decimal('6.69'),    #Bomba de gasolina 1
    Decimal('6.89'),    #Bomba de gasolina 2
    Decimal('6.69'),    #Bomba de gasolina 3
    Decimal('6.99'),    #Bomba de gasolina aditivada
    Decimal('6.99'),    #Bomba de s10 1
    Decimal('6.79'),    #Bomba de s10 2
    Decimal('6.79'),    #Bomba de s500
]

# Listas para armazenar resultados
bomba_litros = []
bomba_reais = []
litros_tanques = []

def coletar_tanques():
    print("ESTOQUE DO DIA".center(30))
    for tanque in nome_tanques:
        litros_tanques.append(Decimal(input(f"Litros no tanque '{tanque}': ")))

    print("Tanques coletados!".center(30))

def registrar_bombas():
    print("REGISTRO DE COMBUSTIVEL VENDIDO".center(30))
    for nome, preco in zip(nome_bombas, preco_bombas):
        print(f"\n{nome}")
        litros = Decimal(input("Numeração DIA: ")) - Decimal(input("Numeração NOITE: "))
        reais = litros * preco

        bomba_litros.append(litros)
        bomba_reais.append(reais)

        print(f"Litros: {litros.quantize(Decimal('0.01'))} | Reais: {reais.quantize(Decimal('0.01'))}\n")

    print("Registro concluido!\n")
diversos = Decimal('0.00')  # valor inicial

def div():
    global diversos
    diversos = Decimal(input("Diversos: "))
def exibir_resumo():
    print("\nVENDAS".center(65))
    print(f"\n{'Bico':<15} | {'Preço':<8} | {'Litros':<10} | {'Reais'}")
    print("-" * 50)
    for nome, preco, litros, reais in zip(nome_bombas, preco_bombas, bomba_litros, bomba_reais):
        print(f"{nome:<15} | {preco:<8} | {litros:<10.2f} | {reais:.2f}")

    print(f"\nDiversos: R$ {diversos.quantize(Decimal('0.01'))}")
    total_geral = sum(bomba_reais) + diversos
    print(f"Total em Reais (com diversos): R$ {total_geral.quantize(Decimal('0.01'))}")
    print(f"Total em Litros: {sum(bomba_litros).quantize(Decimal('0.01'))}\n")

def exibir_tanques_combustivel():
    print("TANQUES".center(60))
    print(f"{'Gasolina':<15} | {'S-10':<15} | {'S-500':<15} | {'V-Power'}")
    print("-" * 65)

    # Estoque  atual dos taques
    print(f"{litros_tanques[0]:<15.2f} | {litros_tanques[1]:<15.2f} | {litros_tanques[2]:<15.2f} | {litros_tanques[3]:.2f}")

    # Quantidade abastecida por tipo de combustivel
    print(f"{sum(bomba_litros[0:3]):<15.2f} | {sum(bomba_litros[4:6]):<15.2f} | {bomba_litros[6]:<15.2f} | {bomba_litros[3]:.2f}")

    # Quantidade restante nos tanques
    print(f"{(litros_tanques[0] - sum(bomba_litros[0:3])):<15.2f} | "
          f"{(litros_tanques[1] - sum(bomba_litros[4:6])):<15.2f} | "
          f"{(litros_tanques[2] - bomba_litros[6]):<15.2f} | "
          f"{(litros_tanques[3] - bomba_litros[3]):.2f}")

# Execução
coletar_tanques()
registrar_bombas()
div()
exibir_resumo()
exibir_tanques_combustivel()

# Laço de encerramento
while True:
    comando = input("Digite 'sair' para encerrar o programa: ")
    if comando.lower() == 'sair':
        break
