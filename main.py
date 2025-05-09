from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 10
getcontext().rounding = ROUND_HALF_UP

#Nome dos tanque e litragem de cada um
nome_tanques = [
    "Gasolina comum",
    "Diesel S10",
    "Diesel S500",
    "V-power"
]

# Nomes e Preços das bombas
nomes_precos = {
    "Gasolina 1": Decimal('6.69'),
    "Gasolina 2": Decimal('6.89'),
    "Gasolina 3": Decimal('6.69'),
    "V-power": Decimal('6.99'),
    "S10 1": Decimal('6.99'),
    "S10 2": Decimal('6.79'),
    "S500 3": Decimal('6.79'),
}


# Listas para armazenar resultados
bomba_litros = []
bomba_reais = []
litros_tanques = []
litros_final = []

#Coletor de entradas de combustiveis
def coletar_tanques():
    print("ESTOQUE DO DIA".center(30))
    for tanque in nome_tanques:
        litros_tanques.append(Decimal(input(f"Litros no tanque '{tanque}': \n")))

    print("Tanques coletados!".center(30))

#Registro das numerações das bombas
def registrar_bombas():
    print("REGISTRO DE COMBUSTIVEL VENDIDO".center(30))
    for nome, preco in zip(nomes_precos.keys(), nomes_precos.values()):
        print(f"\n{nome}")
        litros = Decimal(input("Numeração DIA: ")) - Decimal(input("Numeração NOITE: "))
        reais = litros * preco

        bomba_litros.append(litros)
        bomba_reais.append(reais)

        print(f"Litros: {litros.quantize(Decimal('0.01'))} | Reais: {reais.quantize(Decimal('0.01'))}\n")
    global diversos
    diversos = Decimal(input("Diversos: "))

    print("Registro concluido!\n")
diversos = Decimal('0.00')  # valor inicial

#Resumo da venda geral
def exibir_resumo():
    print("\nVENDAS".center(65))
    print(f"\n{'Bico':<15} | {'Preço':<8} | {'Litros':<10} | {'Reais'}")
    print("-" * 50)
    for nome, preco, litros, reais in zip(nomes_precos.keys(), nomes_precos.values(), bomba_litros, bomba_reais):
        print(f"{nome:<15} | {preco:<8} | {litros:<10.2f} | {reais:.2f}")

    print(f"\nDiversos: R$ {diversos.quantize(Decimal('0.01'))}")
    print(f"Total em Reais : R$ {sum(bomba_reais).quantize(Decimal('0.01'))}")
    print(f"Total em Reais (com diversos): R$ {sum(bomba_reais) + diversos.quantize(Decimal('0.01'))}")
    print(f"Total em Litros: {sum(bomba_litros).quantize(Decimal('0.01'))}\n")

#Exibi o total de listros em cada tanque no final
def exibir_tanques_combustivel():
    print("TANQUES".center(60))
    print(f"{'Gasolina':<15} | {'S-10':<15} | {'S-500':<15} | {'V-Power'}")
    print("-" * 65)

    # Estoque  atual dos taques
    print(f"{litros_tanques[0]:<15.2f} | {litros_tanques[1]:<15.2f} | {litros_tanques[2]:<15.2f} | {litros_tanques[3]:.2f}")

    # Quantidade abastecida por tipo de combustivel
    print(f"{sum(bomba_litros[0:3]):<15.2f} | {sum(bomba_litros[4:6]):<15.2f} | {bomba_litros[6]:<15.2f} | {bomba_litros[3]:.2f}")

    # Quantidade restante nos tanques
    litros_final.extend([
        litros_tanques[0] - sum(bomba_litros[0:3]),
        litros_tanques[1] - sum(bomba_litros[4:6]),
        litros_tanques[2] - bomba_litros[6],
        litros_tanques[3] - bomba_litros[3]
        ])

    print(f"{litros_final[0]:<15.2f} | {litros_final[1]:<15.2f} | {litros_final[2]:<15.2f} | {litros_final[3]:.2f}\n")
    
#Pega o resultado mais proximo da altura do tanque
def valor_mais_proximo(dados, alvo):
    chave_mais_proxima = min(dados, key=lambda k: abs(dados[k] - alvo))
    return chave_mais_proxima, dados[chave_mais_proxima]

#Exibi a altura e quantida que sobra em cada tanque
def tanques():
    print("Altura dos tanques:".center(45))
    print(f"{"Tipo":<15} | {f"Altura":<15} | LItros")
    print("=" * 45 )
    from tabelas import tabela
    for nome, tabela, alvo,  in zip(nome_tanques, tabela.values(), litros_final):
        chave, valor = valor_mais_proximo(tabela, alvo)
        print(f"{nome:<15} | {chave:<15} | {valor}")
        print("-" * 45)

# Execução
coletar_tanques()
registrar_bombas()
exibir_resumo()
exibir_tanques_combustivel()
tanques()

# Laço de encerramento
while True:
    comando = input("Digite 'sair' para encerrar o programa: ")
    if comando.lower() == 'sair':
        break
